import requests
import re
from urllib.parse import urljoin

# Define the paths and patterns from the YAML file
PATHS = [
    "/.git/",
    "/.git/HEAD",
    "/.git/config",
    "/.git/index",
    "/.git/logs/HEAD",
    "/.git/refs/heads/master",
    "/.git/refs/heads/main",
]

# Regex patterns to match in the response
REGEX_PATTERNS = {
    "HEAD": r"ref: refs/heads/([\w-]+)",  # Extract branch name
    "config": r"\[core\]",  # Match [core] in .git/config
}

# User-Agent to mimic a browser
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

def check_git_exposure(url):
    """
    Check for exposed .git files and directories on the target URL.
    """
    results = {}

    for path in PATHS:
        full_url = urljoin(url, path)
        try:
            response = requests.get(full_url, headers=HEADERS, timeout=10)
            if response.status_code == 200:
                results[path] = {"status": "exposed", "content": response.text}

                # Check for regex matches
                if path.endswith("HEAD"):
                    branch_match = re.search(REGEX_PATTERNS["HEAD"], response.text)
                    if branch_match:
                        results[path]["branch"] = branch_match.group(1)
                elif path.endswith("config"):
                    config_match = re.search(REGEX_PATTERNS["config"], response.text)
                    if config_match:
                        results[path]["config"] = "Git config exposed"
        except requests.RequestException as e:
            results[path] = {"status": "error", "error": str(e)}

    return results

def print_results(results):
    """
    Print the results in a readable format.
    """
    for path, data in results.items():
        print(f"Path: {path}")
        print(f"Status: {data['status']}")
        if "branch" in data:
            print(f"Branch: {data['branch']}")
        if "config" in data:
            print(f"Config: {data['config']}")
        if "error" in data:
            print(f"Error: {data['error']}")
        print("-" * 40)

def main():
    """
    Main function to run the tool.
    """
    print("Git Repository Exposure Scanner")
    target_url = input("Enter the target URL (e.g., http://example.com): ").strip()

    if not target_url.startswith(("http://", "https://")):
        print("Invalid URL. Please include http:// or https://")
        return

    print(f"Scanning {target_url}...")
    results = check_git_exposure(target_url)
    print_results(results)

if __name__ == "__main__":
    main()
