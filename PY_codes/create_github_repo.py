import requests
import json

def create_github_repo(repo_name, description, private=False):
    
    username = 'tarikalim'
    api_key = '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'

    url = 'https://api.github.com/user/repos'
    payload = {
        'name': repo_name,
        'description': description,
        'private': private
    }
    headers = {
        'Authorization': 'token %s' % api_key,
        'Content-Type': 'application/json'
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 201:
        print("Repo created!")
    else:
        print("Error creating repo:", response.status_code)

if __name__ == "__main__":
    repo_name = input("Give a name to your repo: ")
    description = input("Repo description: ")
    private = input("Private repo? ( 'True' 'False'): ")
    
    create_github_repo(repo_name, description, private=bool(private))
