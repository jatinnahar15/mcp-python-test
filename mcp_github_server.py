#git_token = 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

from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Load GitHub token from environment or set manually
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "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")

GITHUB_API_URL = "https://api.github.com"

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}


@app.route("/command", methods=["POST"])
def handle_command():
    data = request.json
    command_name = data.get("name")
    input_data = data.get("input", {})

    if command_name == "create-repo":
        return create_repo(input_data)

    return jsonify({"error": "Unsupported command"}), 400


def create_repo(input_data):
    repo_name = input_data.get("repo_name", "claude-mcp-repo")
    private = input_data.get("private", True)
    description = input_data.get("description", "Created via MCP Python Server")

    payload = {
        "name": repo_name,
        "private": private,
        "description": description,
        "auto_init": True
    }

    response = requests.post(f"{GITHUB_API_URL}/user/repos", headers=HEADERS, json=payload)

    if response.status_code == 201:
        return jsonify({
            "status": "success",
            "html_url": response.json().get("html_url")
        }), 201
    else:
        return jsonify({
            "status": "error",
            "details": response.json()
        }), response.status_code


if __name__ == "__main__":
    app.run(debug=True, port=5001)
    