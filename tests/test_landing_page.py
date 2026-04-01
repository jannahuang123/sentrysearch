import json
from pathlib import Path
import re


REPO_ROOT = Path(__file__).resolve().parents[1]
LANDING_HTML = REPO_ROOT / "landing" / "index.html"
LANDING_DEMO_DATA = REPO_ROOT / "landing" / "demo-data.json"


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
    assert "SentrySearch: Search Dashcam and Security Video with Natural Language" in html


def test_landing_page_has_core_sections():
    html = read_html()
    for marker in [
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
    ]:
        assert marker in html

    css = (REPO_ROOT / "landing" / "styles.css").read_text(encoding="utf-8")
    assert "#sample-presets button" in css


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
        "View on GitHub",
        "Run locally today",
        "Request hosted demo",
        "What is SentrySearch?",
        "Find the moment a car cut in front of me",
        "Find when someone approached the driveway",
        "Find the clip with a red truck near the stop sign",
        "Does SentrySearch upload my videos?",
        "Can I run SentrySearch locally?",
        "Is this a Tesla Sentry Mode tool only?",
    ]:
        assert phrase in html


def test_landing_page_cta_links_point_to_expected_destinations():
    html = re.sub(r"\s+", " ", read_html())
    repo_url = "https://github.com/jannahuang123/sentrysearch"

    assert f'<a href="#sample-search">Try the sample search</a>' in html
    assert re.search(
        rf'<a href="{re.escape(repo_url)}" rel="noopener noreferrer"\s*>View on GitHub</a\s*>',
        html,
    )
    assert "bundled example data" in html
    assert "does not process live user footage or backend inference" in html

    final_cta = re.search(r'<section id="final-cta".*?</section>', html)
    assert final_cta is not None
    final_cta_html = final_cta.group(0)

    assert f'<a href="{repo_url}">Run locally today</a>' in final_cta_html
    assert '<a href="mailto:demo@sentrysearch.com">Request hosted demo</a>' in final_cta_html
    assert "Try the sample search" not in final_cta_html
    assert "View on GitHub" not in final_cta_html


def test_sample_search_is_wired_to_bundled_demo_data():
    app_js = (REPO_ROOT / "landing" / "app.js").read_text(encoding="utf-8")
    assert 'const DEMO_DATA_URL = "./demo-data.json";' in app_js
    assert "fetch(DEMO_DATA_URL)" in app_js
    assert "Loading bundled demo clips..." in app_js
    assert "Bundled sample search data could not be loaded." in app_js
    assert "return timestamp;" in app_js
    assert "new Date(timestamp)" not in app_js
    assert "toLocaleString" not in app_js
