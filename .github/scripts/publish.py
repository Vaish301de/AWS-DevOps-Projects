import os
import markdown
import requests
from pathlib import Path

wp_url = os.environ["WP_URL"]
username = os.environ["WP_USERNAME"]
password = os.environ["WP_APP_PASSWORD"]
repo_name = os.environ["REPO_NAME"]

readme = Path("README.md").read_text()
html_content = markdown.markdown(readme, extensions=['fenced_code', 'tables'])

response = requests.post(
    f"{wp_url}/wp-json/wp/v2/posts",
    auth=(username, password),
    json={
        "title": repo_name,
        "content": html_content,
        "status": "publish"
    }
)

if response.status_code == 201:
    print(f"✅ Published! Post URL: {response.json()['link']}")
else:
    print(f"❌ Failed: {response.status_code} - {response.text}")
    exit(1)
