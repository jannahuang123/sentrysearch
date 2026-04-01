from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
LANDING_HTML = REPO_ROOT / "landing" / "index.html"


def read_html() -> str:
    return LANDING_HTML.read_text(encoding="utf-8")


def test_landing_page_has_required_seo_shell():
    html = read_html()
    assert "<title>SentrySearch:" in html
    assert 'name="description"' in html
    assert 'rel="canonical"' in html
    assert 'property="og:title"' in html
    assert "<h1>SentrySearch:" in html


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
