# enumeration-gitlab

This tool help to obtain scopes, namespaces, projects from gitlab account.

Usage:

```
$ python enumeration-gitlab.py --token TOKEN

            .__  __  .__        ___.                                                      __  .__               
    ____ |__|/  |_|  | _____ \_ |__     ____   ____  __ __  _____   ________________ _/  |_|__| ____   ____  
    / ___\|  \   __\  | \__  \ | __ \  _/ __ \ /    \|  |  \/     \_/ __ \_  __ \__   \   __\  |/  _ \ /    \ 
    / /_/  >  ||  | |  |__/ __ \| \_\ \ \  ___/|   |  \  |  /  Y Y  \  ___/|  | \// __ \|  | |  (  <_> )   |  \
    \___  /|__||__| |____(____  /___  /  \___  >___|  /____/|__|_|  /\___  >__|  (____  /__| |__|\____/|___|  /
    /_____/                    \/    \/       \/     \/            \/     \/           \/                    \/ 
    
    @Author: h4pp1n3ss
    @Description: gitlab enumeration tool
    @Version: 0.1 
    
    

[+] Attempting to obtain scopes...

= api scope enabled
= read_user scoce enabled
= read_api scope enabled
= read_repository scope enabled
= write_repository scope enabled
= read_registry scope enabled
= write_registry scope enabled

[+] For more information visit -> https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#personal-access-token-scopes

[+] Trying to fetch all namespaces ...

....
```