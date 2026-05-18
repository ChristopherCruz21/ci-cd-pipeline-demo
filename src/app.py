from html import escape


def build_status_message(app_name: str, version: str) -> str:
    return f"{app_name} version {version} passed build, test, and deploy checks."


def render_homepage(app_name: str = "CI/CD Pipeline Demo", version: str = "1.0.0") -> str:
    safe_app_name = escape(app_name)
    safe_version = escape(version)
    message = escape(build_status_message(app_name, version))

    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{safe_app_name}</title>
    <style>
      body {{
        margin: 0;
        font-family: Arial, sans-serif;
        background: #f6f8fa;
        color: #24292f;
      }}

      main {{
        max-width: 760px;
        margin: 64px auto;
        padding: 32px;
        background: white;
        border: 1px solid #d0d7de;
        border-radius: 8px;
      }}

      h1 {{
        margin-top: 0;
      }}

      .pipeline {{
        display: grid;
        gap: 12px;
        margin-top: 24px;
      }}

      .stage {{
        padding: 16px;
        border: 1px solid #d0d7de;
        border-radius: 6px;
      }}
    </style>
  </head>
  <body>
    <main>
      <h1>{safe_app_name}</h1>
      <p>{message}</p>
      <p>Current demo version: <strong>{safe_version}</strong></p>

      <section class="pipeline" aria-label="Pipeline stages">
        <div class="stage"><strong>Build:</strong> generate the static site files.</div>
        <div class="stage"><strong>Test:</strong> run automated checks with pytest.</div>
        <div class="stage"><strong>Deploy:</strong> publish the built site to GitHub Pages.</div>
      </section>
    </main>
  </body>
</html>
"""
