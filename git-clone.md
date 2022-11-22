```
arvindlavania@Arvinds-iMac Documents % gh auth login
? What account do you want to log into? GitHub.com
? What is your preferred protocol for Git operations? HTTPS
? Authenticate Git with your GitHub credentials? Yes
? How would you like to authenticate GitHub CLI? Login with a web browser

! First copy your one-time code: AB12-AB12
Press Enter to open github.com in your browser...
✓ Authentication complete.
- gh config set -h github.com git_protocol https
✓ Configured git protocol
✓ Logged in as Arvindlavania
```

```
arvindlavania@Arvinds-iMac Documents % gh repo clone Arvindlavania/search-replacer
Cloning into 'search-replacer'...
remote: Enumerating objects: 44, done.
remote: Counting objects: 100% (44/44), done.
remote: Compressing objects: 100% (34/34), done.
remote: Total 44 (delta 8), reused 36 (delta 3), pack-reused 0
Receiving objects: 100% (44/44), 159.60 KiB | 387.00 KiB/s, done.
Resolving deltas: 100% (8/8), done.
```

```
arvindlavania@Arvinds-iMac Documents % cd search-replacer
```

````
arvindlavania@Arvinds-iMac search-replacer % ls -l
total 496
-rw-r--r--  1 arvindlavania  staff       0 Nov 22 23:37 Advance-AWS-search.drawio
-rw-r--r--  1 arvindlavania  staff    2284 Nov 22 23:37 README.md
-rw-r--r--  1 arvindlavania  staff   32702 Nov 22 23:37 SearchReplaceArchitecture.drawio.png
-rw-r--r--  1 arvindlavania  staff   12773 Nov 22 23:37 commands.txt
drwxr-xr-x  5 arvindlavania  staff     160 Nov 22 23:37 events
drwxr-xr-x  3 arvindlavania  staff      96 Nov 22 23:37 frontend
-rw-r--r--  1 arvindlavania  staff     305 Nov 22 23:37 samconfig.toml
-rw-r--r--  1 arvindlavania  staff  192177 Nov 22 23:37 search-replace-web.png
drwxr-xr-x  4 arvindlavania  staff     128 Nov 22 23:37 search_replacer
-rw-r--r--  1 arvindlavania  staff    1044 Nov 22 23:37 template.yaml
```
