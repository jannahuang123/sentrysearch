import json
from pathlib import Path
import re


REPO_ROOT = Path(__file__).resolve().parents[1]
LANDING_HTML = REPO_ROOT / "landing" / "index.html"
LANDING_DEMO_DATA = REPO_ROOT / "landing" / "demo-data.json"
ABOUT_HTML = REPO_ROOT / "landing" / "about.html"
PRIVACY_HTML = REPO_ROOT / "landing" / "privacy.html"
TERMS_HTML = REPO_ROOT / "landing" / "terms.html"
ROBOTS_TXT = REPO_ROOT / "landing" / "robots.txt"
SITEMAP_XML = REPO_ROOT / "landing" / "sitemap.xml"


def read_html() -> str:
    return LANDING_HTML.read_text(encoding="utf-8")


def read_demo_data() -> list[dict]:
    return json.loads(LANDING_DEMO_DATA.read_text(encoding="utf-8"))


def test_landing_page_has_required_seo_shell():
    html = re.sub(r"\s+", " ", read_html())
    assert "<title>SentrySearch:" in html
    assert 'content="SentrySearch searches dashcam and security footage in natural language and automatically trims the matching clip."' in html
    assert 'rel="canonical"' in html
    assert 'property="og:title"' in html
    assert "SentrySearch: Smart Video Search for Dashcams" in html


def test_landing_page_has_core_sections():
    html = read_html()
    for marker in [
        'class="site-header"',
        'class="brand-mark"',
        'class="site-footer"',
        'id="hero"',
        'id="definition"',
        'id="use-cases"',
        'id="sample-search"',
        'id="how-it-works"',
        'id="faq"',
        'id="final-cta"',
        'id="sample-search-form"',
        'id="sample-query-input"',
        'id="sample-presets"',
        'id="sample-results"',
    ]:
        assert marker in html


def test_landing_page_has_layout_wrapper_classes():
    html = read_html()
    for marker in [
        'class="hero-actions"',
        'class="query-list"',
        'class="demo-shell"',
        'class="cta-band"',
        'class="hero-grid"',
        'class="hero-stage"',
        'class="hero-showcase"',
        'class="hero-visual"',
        'class="hero-panel"',
        'class="proof-grid"',
        'class="scene-card"',
        'class="seo-section"',
    ]:
        assert marker in html

    css = (REPO_ROOT / "landing" / "styles.css").read_text(encoding="utf-8")
    assert "#sample-presets button" in css
    normalized_css = css.replace(" ", "").lower()
    for marker in [
        "--bg:#0b1326",
        "--panel:#131b2e",
        "--panel-high:#222a3d",
        ".hero-panel",
        ".scene-card",
    ]:
        assert marker in normalized_css


def test_landing_page_has_expanded_heading_hierarchy():
    html = read_html()
    for text in [
        "What Is SentrySearch?",
        "Why Teams Use SentrySearch",
        "SentrySearch For Dashcam Footage",
        "SentrySearch For Security Footage",
        "How SentrySearch Works",
        "SentrySearch FAQ",
    ]:
        assert text in html


def test_landing_page_has_sample_search_demo_data():
    assert LANDING_DEMO_DATA.exists()
    demo_data = read_demo_data()
    assert len(demo_data) >= 3

    for query in demo_data:
        for field in ["label", "prompt", "results"]:
            assert field in query
        assert query["results"], "Each sample query should include at least one result"
        for result in query["results"]:
            for field in ["camera", "timestamp", "score", "clip_label"]:
                assert field in result
            assert re.fullmatch(r"\d{2}:\d{2}-\d{2}:\d{2}", result["timestamp"])


def test_landing_page_has_product_copy_and_ctas():
    html = re.sub(r"\s+", " ", read_html())

    for phrase in [
        "Search dashcam and security footage in natural language",
        "automatically trims the matching clip",
        "Try the sample search",
        "bundled example data",
        "demo-only",
        "does not process live user footage or backend inference",
        "Reserve early access",
        "Request hosted demo",
        "What is SentrySearch?",
        "Find the moment a car cut in front of me",
        "Find when someone approached the driveway",
        "Find the clip with a red truck near the stop sign",
        "Does SentrySearch upload my videos?",
        "Can I reserve early access today?",
        "Is this a Tesla Sentry Mode tool only?",
    ]:
        assert phrase in html


def test_landing_page_targets_single_page_seo_depth():
    html = re.sub(r"\s+", " ", read_html())
    body = re.sub(r"<[^>]+>", " ", html)
    body = re.sub(r"\s+", " ", body).strip()
    word_count = len([word for word in body.split() if word.strip()])
    sentrysearch_count = body.lower().count("sentrysearch")

    assert 1500 <= word_count <= 2200
    density = sentrysearch_count / word_count
    assert 0.03 <= density <= 0.05

    for phrase in [
        "dashcam footage",
        "security footage",
        "driving incidents",
        "parking lot incident",
        "driveway camera",
        "incident review",
        "clip extraction",
        "matched clip",
        "video incident search",
    ]:
        assert phrase in body.lower()


def test_landing_page_cta_links_point_to_expected_destinations():
    html = re.sub(r"\s+", " ", read_html())
    assert f'<a href="#sample-search">Try the sample search</a>' in html
    assert (
        '<a href="mailto:demo@sentrysearch.my?subject=SentrySearch%20early%20access&body=Hi%20SentrySearch%2C%20I%20want%20to%20reserve%20early%20access%20for%20SentrySearch.">Request a hosted demo</a>'
        in html
    )
    assert "bundled example data" in html
    assert "does not process live user footage or backend inference" in html

    final_cta = re.search(r'<section id="final-cta".*?</section>', html)
    assert final_cta is not None
    final_cta_html = final_cta.group(0)

    assert '<a href="mailto:demo@sentrysearch.my?subject=SentrySearch%20early%20access&body=Hi%20SentrySearch%2C%20I%20want%20to%20reserve%20early%20access%20for%20SentrySearch.">Reserve early access</a>' in final_cta_html
    assert '<a href="mailto:demo@sentrysearch.my?subject=SentrySearch%20hosted%20demo&body=Hi%20SentrySearch%2C%20I%20want%20to%20request%20a%20hosted%20demo.">Request hosted demo</a>' in final_cta_html
    assert "Try the sample search" not in final_cta_html
    assert "GitHub" not in final_cta_html


def test_sample_search_is_wired_to_bundled_demo_data():
    app_js = (REPO_ROOT / "landing" / "app.js").read_text(encoding="utf-8")
    assert 'const DEMO_DATA_URL = "./demo-data.json";' in app_js
    assert "fetch(DEMO_DATA_URL)" in app_js
    assert "Loading bundled demo clips..." in app_js
    assert "Bundled sample search data could not be loaded." in app_js
    assert "return timestamp;" in app_js
    assert "new Date(timestamp)" not in app_js
    assert "toLocaleString" not in app_js


def test_readme_mentions_landing_page_preview():
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    assert "Landing page" in readme
    assert "python -m http.server" in readme
    assert "landing/" in readme


def test_landing_page_has_rewritten_meta_copy():
    html = re.sub(r"\s+", " ", read_html())
    title_match = re.search(r"<title>(.*?)</title>", html)
    assert title_match is not None
    title = title_match.group(1).strip()
    assert "SentrySearch: Smart Video Search for Dashcams" == title
    assert 40 <= len(title) <= 60
    assert "SentrySearch introduces a new way to search dashcam footage and security footage in natural language" in html
    assert 'property="og:description"' in html


def test_supporting_pages_exist_with_professional_footer_links():
    landing_html = read_html()

    for file_path in [ABOUT_HTML, PRIVACY_HTML, TERMS_HTML]:
      assert file_path.exists()
      page_html = file_path.read_text(encoding="utf-8")
      assert "SentrySearch" in page_html
      assert 'class="site-header"' in page_html
      assert 'class="site-footer"' in page_html

    for phrase in [
        'href="./about.html"',
        'href="./privacy.html"',
        'href="./terms.html"',
        "About",
        "Privacy",
        "Terms",
    ]:
        assert phrase in landing_html


def test_privacy_and_terms_pages_cover_expected_sections():
    privacy_html = PRIVACY_HTML.read_text(encoding="utf-8")
    terms_html = TERMS_HTML.read_text(encoding="utf-8")
    about_html = ABOUT_HTML.read_text(encoding="utf-8")

    for phrase in [
        "Privacy Policy",
        "Information We Collect",
        "How We Use Information",
        "Data Retention",
        "Contact",
    ]:
        assert phrase in privacy_html

    for phrase in [
        "Terms of Use",
        "Acceptable Use",
        "Disclaimers",
        "Limitation of Liability",
        "Contact",
    ]:
        assert phrase in terms_html

    for phrase in [
        "About SentrySearch",
        "Why we built SentrySearch",
        "Who SentrySearch is for",
    ]:
        assert phrase in about_html


def test_robots_and_sitemap_exist_for_crawlers():
    assert ROBOTS_TXT.exists()
    assert SITEMAP_XML.exists()

    robots = ROBOTS_TXT.read_text(encoding="utf-8")
    sitemap = SITEMAP_XML.read_text(encoding="utf-8")

    assert "User-agent: *" in robots
    assert "Allow: /" in robots
    assert "Sitemap: https://sentrysearch.my/sitemap.xml" in robots

    for url in [
        "https://sentrysearch.my/",
        "https://sentrysearch.my/about.html",
        "https://sentrysearch.my/privacy.html",
        "https://sentrysearch.my/terms.html",
    ]:
        assert url in sitemap


def test_landing_page_has_seo_sections_and_ctas():
    html = read_html()
    for text in [
        "Why Teams Use SentrySearch",
        "SentrySearch For Dashcam Footage",
        "SentrySearch For Security Footage",
        "How SentrySearch Works",
        "SentrySearch FAQ",
        "Reserve early access",
        "Request hosted demo",
    ]:
        assert text in html


def test_sample_search_demo_matches_incident_review_language():
    html = read_html().lower()
    app_js = (REPO_ROOT / "landing" / "app.js").read_text(encoding="utf-8").lower()
    demo_data = read_demo_data()

    assert "bundled example data" in html
    assert "incident" in app_js
    assert any("parking" in item["prompt"].lower() for item in demo_data)
