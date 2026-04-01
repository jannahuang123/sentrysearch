from pathlib import Path
import re


REPO_ROOT = Path(__file__).resolve().parents[1]
LANDING_HTML = REPO_ROOT / "landing" / "index.html"


def read_html() -> str:
    return LANDING_HTML.read_text(encoding="utf-8")


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
    ]:
        assert marker in html


def test_landing_page_has_product_copy_and_ctas():
    html = re.sub(r"\s+", " ", read_html())

    for phrase in [
        "Search dashcam and security footage in natural language",
        "automatically trims the matching clip",
        "Try the sample search",
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

    final_cta = re.search(r'<section id="final-cta".*?</section>', html)
    assert final_cta is not None
    final_cta_html = final_cta.group(0)

    assert f'<a href="{repo_url}">Run locally today</a>' in final_cta_html
    assert '<a href="mailto:demo@sentrysearch.com">Request hosted demo</a>' in final_cta_html
    assert "Try the sample search" not in final_cta_html
    assert "View on GitHub" not in final_cta_html
