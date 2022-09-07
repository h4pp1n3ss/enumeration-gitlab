import os, sys,json
import requests
from threading import Thread

"""
    GITLAB ACCOUNT ENUMERATION  
    Resource: https://docs.gitlab.com/ee/api/projects.html
"""

url = 'https://gitlab.com/api/v4'
headers = {'PRIVATE-TOKEN': ''}

def print_banner():
    banner = """
            .__  __  .__        ___.                                                      __  .__               
    ____ |__|/  |_|  | _____ \_ |__     ____   ____  __ __  _____   ________________ _/  |_|__| ____   ____  
    / ___\|  \   __\  | \__  \ | __ \  _/ __ \ /    \|  |  \/     \_/ __ \_  __ \__   \   __\  |/  _ \ /    \ 
    / /_/  >  ||  | |  |__/ __ \| \_\ \ \  ___/|   |  \  |  /  Y Y  \  ___/|  | \// __ \|  | |  (  <_> )   |  \\
    \___  /|__||__| |____(____  /___  /  \___  >___|  /____/|__|_|  /\___  >__|  (____  /__| |__|\____/|___|  /
    /_____/                    \/    \/       \/     \/            \/     \/           \/                    \/ 
    
    @Author: h4pp1n3s
    @Description: gitlab enumeration tool
    @Version: 0.1 
    
    """

    print(banner)

def clone_repo(id):
    """
        Function used to clone a repository
    """

    url_clone = url + "/projects/%i/repository/archive" % int(id)
    try:
        resp = requests.get(url_clone, headers=headers)
        open(str(id),"wb").write(resp.content)

    except Exception as err:
        print(f"Unexpected {err=}")

def describe_token():
    """
        Function to fetch permission from specific PERSONAL_TOKEN
    """

    scopes = []
    endpoint_token = url + "/personal_access_tokens"
    url_request = endpoint_token
    print("\n[+] Attempting to obtain scopes...\r\n")
    try:
        resp = requests.get(url_request, headers=headers)
        data = resp.json()
        for dd in data:
            # print("= Id: " + str(dd["id"]) + " | Name: " + str(dd["name"]))
            if scopes.count(dd["scopes"]) == 0:
                scopes.append(list(dd["scopes"]))
    except Exception as err:
        print(f"Unexpected {err=}")
    
    return scopes

def get_project():
    """
        Function useful to get all projects associated.
    """

    endpoint_project = url + '/projects?&private=true&visibility=private&per_page=100&page='

    pids = []
    cont = 0
    for page in range (1,10):
        url_request = endpoint_project + str(page)
        try:
            resp = requests.get(url_request, headers=headers)
            data = resp.json()
            for dd in data:
                cont = cont + 1
                name = str(dd['name'])
                pid = str(dd['id'])
                print("Project Name: " +  name)
                print("Project Web Url: " +  str(dd['web_url']))
                print("Project Id: " +  pid + "\r\n")
                nExist = pids.count(pid)
                if nExist == 0:
                    pids.append(pid)
        except:
            print("[-] Failed to fetch all projects")

    return pids

def get_namespaces():
    """
        Function useful to obtain all namespaces.
    """

    endpoint_project = url + '/projects?&private=true&visibility=private&per_page=100&page='

    nNamespaces = []
    cont = 0
    for page in range (1,10):
        url_request = endpoint_project + str(page)
        try:
            resp = requests.get(url_request, headers=headers)
            data = resp.json()
            for dd in data:
                cont = cont + 1
                nName = str(dd['namespace']['name'])
                nExist = nNamespaces.count(nName)
                if nExist == 0:
                    nNamespaces.append(nName)
        except:
            print("[-] Failed to fetch all namespaces")
    return nNamespaces
    
def gitlab_enumeration(token):

    global headers 
    headers = {'PRIVATE-TOKEN': str(token)}

    print_banner()

    scopes = describe_token()

    if len(scopes) == 0:
        print("\n[-] No items found in the scope")
        sys.exit(1)
    else:
        for scope in scopes:
            for i in scope:
                if i == "api":
                    print("= api scope enabled")
                elif i == "read_user":
                    print("= read_user scoce enabled")
                elif i == "read_api":
                    print("= read_api scope enabled")
                elif i == "read_repository":
                    print("= read_repository scope enabled")
                elif i == "write_repository":
                    print("= write_repository scope enabled")
                elif i == "read_registry":
                    print("= read_registry scope enabled")
                elif i == "write_registry":
                    print("= write_registry scope enabled")
                elif i == "sudo":
                    print(" = sudo scope enabled")
    print("\n[+] For more information visit -> https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#personal-access-token-scopes")

    print("\n[+] Trying to fetch all namespaces ... \r\n")
    nNamespaces = get_namespaces()
    
    for i in nNamespaces:
        print("= Namespace: " + i)        
    print("\n[+] Number of namespaces: " + str(len(nNamespaces)))
    
    print("\n[+] Trying to fetch all projects ... \r\n")
    project_ids = get_project()
    
    for pid in project_ids:
        print("Clonning repo: " + str(pid))
        try:
            clone_thread = Thread(target=clone_repo, args=(pid,))

            clone_thread.start()
            clone_thread.join()

        except Exception as err:
            print(f"Unexpected f{err=}")