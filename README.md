1. Install Python 3.x

2. Install Flask and requests:
      pip install flask requests

3. Create a GitHub Personal Access Token with repo scope

4. Create mcp server file. [mcp_github_server.py]

5. Set your GitHub token securely (in terminal):
   set GITHUB_TOKEN=ghp_YourTokenHere  # on Windows

6. Run it:
    python mcp_github_server.py

How to Use It
Send a POST request to http://localhost:5001/command with JSON like:
{
  "name": "create-repo",
  "input": {
    "repo_name": "mcp-python-test",
    "private": true,
    "description": "Repository created via custom MCP Python server"
  }
}


