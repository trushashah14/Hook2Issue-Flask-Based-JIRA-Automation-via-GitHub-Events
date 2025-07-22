from flask import Flask , request #importing module flask from the whole package
import requests
from requests.auth import HTTPBasicAuth
import json

#Creating Flask app instance
app = Flask(__name__)


@app.route("/createJIRA", methods=['POST'])  #decretor : perform an action before a particular function
def createJIRA():

    data = request.get_json()
    print("\n📦 Received GitHub webhook payload:")
    
    action = data.get("action", "")
    if action != "created":
      print(f"🚫 Ignoring action: {action}")
      return json.dumps({"message": f"Ignored action '{action}'."}), 200


    # Extract comment body from GitHub webhook payload
    comment_body = data.get("comment", {}).get("body", "")
    print(f"\n💬 Comment body: '{comment_body}'")

    # Only proceed if the comment is exactly "/jira"
    if comment_body.strip().lower() != "/jira":
        print(f"🧭 Ignored comment: '{comment_body}' — Does not match /jira trigger.")
        return json.dumps({"message": "Comment does not trigger JIRA creation."}), 200


# Extract GitHub issue data
    issue = data.get("issue", {})
    issue_title = issue.get("title", "GitHub Issue")
    issue_body = issue.get("body", "No description provided.")
    issue_url = issue.get("html_url", "")

    print("\n📄 Extracted Issue Details:")
    print(f"🔸 Title: {issue_title}")
    print(f"🔸 Body: {issue_body}")
    print(f"🔸 URL: {issue_url}")


    url = "https://trushashah1402.atlassian.net/rest/api/3/issue"

    API_TOKEN = "****"
    auth = HTTPBasicAuth("trushashah1402@gmail.com", API_TOKEN)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
    "fields": {

        "description": {
        "content": [
            {
            "content": [
                {
                "text": f"{issue_body}\n\nGitHub link: {issue_url}",
                "type": "text"
                }
            ],
            "type": "paragraph"
            }
        ],
        "type": "doc",
        "version": 1
        },

        "issuetype": {
        "id": "10011"
        },

        "project": {
        "key": "TS"
        },
        "summary": issue_title,
    },
    "update": {}
    } )


    print("\n📤 Sending payload to JIRA:")
    print(json.dumps(json.loads(payload), indent=4))

    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )

    print("\n🎯 JIRA API Response:")
    print(f"🔹 Status Code: {response.status_code}")
    print(f"🔹 Response Text: {response.text}")


    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

app.run('0.0.0.0', port=5000)
