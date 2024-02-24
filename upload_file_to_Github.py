import requests
import base64

def upload_file_to_github(file_path, repo_name, github_username, github_token):
    url = f"https://api.github.com/repos/{github_username}/{repo_name}/contents/{file_path}"
    
    with open(file_path, "rb") as file:
        content = file.read()
        
    content_encoded = base64.b64encode(content).decode()
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'token {github_token}'
    }
    
    data = {
        'message': 'Upload file via script',
        'content': content_encoded
    }
    
    response = requests.put(url, headers=headers, json=data)
    
    if response.status_code == 201:
        print("Upload ok")
    else:
        print("Error:", response.status_code)
        print(response.text)

if __name__ == "__main__":
    file_path = input("Full path of file: ")
    repo_name = input("Repo name: ")
    github_username = input("GitHub user name: ")
    github_token = input("GitHub token: ")
    
    upload_file_to_github(file_path, repo_name, github_username, github_token)
