from src.app import build_status_message, render_homepage


def test_status_message_mentions_pipeline_stages() -> None:
    message = build_status_message("Demo App", "2.0.0")

    assert "Demo App" in message
    assert "2.0.0" in message
    assert "build, test, and deploy" in message


def test_homepage_contains_pipeline_stages() -> None:
    html = render_homepage()

    assert "<!doctype html>" in html
    assert "Build:" in html
    assert "Test:" in html
    assert "Deploy:" in html


def test_homepage_escapes_user_controlled_text() -> None:
    html = render_homepage("<script>alert('bad')</script>", "1.0.0")

    assert "<script>" not in html
    assert "&lt;script&gt;" in html
