# CI/CD Pipeline Demo

A small project for learning how a GitHub Actions pipeline builds, tests, and deploys an app.

The app is intentionally simple: Python generates a static HTML page into `dist/index.html`. The pipeline runs tests, builds the page, uploads the build artifact, and deploys it to GitHub Pages when changes are pushed to `main`.

## What You Will Learn

- How a CI job runs tests before code is merged or deployed
- How a build job creates a deployable artifact
- How a deploy job publishes that artifact after the build passes
- How jobs depend on each other with `needs`

## Project Structure

```text
ci-cd-pipeline-demo/
├── .github/workflows/pipeline.yml
├── src/
│   ├── app.py
│   └── build.py
├── tests/
│   └── test_app.py
├── requirements-dev.txt
└── README.md
```

## Run It Locally

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install test dependencies:

```powershell
pip install -r requirements-dev.txt
```

Run tests:

```powershell
pytest
```

Build the static site:

```powershell
python -m src.build
```

Open `dist/index.html` in your browser.

## Use the Pipeline

1. Create a new GitHub repository.
2. Push this folder to GitHub.
3. In the repository, go to **Settings > Pages**.
4. Set **Build and deployment** to **GitHub Actions**.
5. Push to `main`.

The pipeline will:

1. Run tests.
2. Build `dist/index.html`.
3. Upload the build output.
4. Deploy the site to GitHub Pages.

Pull requests run the test and build jobs, but deployment only happens from `main`.

