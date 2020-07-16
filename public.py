import requests
import json
import subprocess


# create github hook
def create_hook():
    create_hook_url = "https://api.github.com/repos/:owner/:repo/hooks"
    header = {
        'Accept': 'application/vnd.github.v3+json',
        'Authorization': 'token TOKEN'
    }
    data = json.dumps({"config": {"url": "http://www.xxx.com", "content_type": "content_type", "secret": "secret",
                                  "insecure_ssl": "insecure_ssl"}
                       })

    resp = requests.post(create_hook_url, data=data, headers=header)
    print(json.loads(resp.text))


# import github repository(--mirror )
def import_github():
    subprocess.run('git clone --mirror https://github.com/:owner/:repo', shell=True)


# mock hook
def fetch_github():
    subprocess.run('git fetch', shell=True)


import_github()
create_hook()
fetch_github()
