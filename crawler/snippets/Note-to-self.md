Stuff that i vaguely remember doing while setting the server up
=============
Links
----------
`http://pkmishra.github.io/blog/2013/03/18/how-to-run-scrapy-with-TOR-and-multiple-browser-agents-part-1-mac/`
`https://groups.google.com/forum/#!topic/scrapy-users/WqMLnKbA43I`


History
---------
```sudo apt-get install tor```
```sudo apt-get install polipo```
```sudo vim /etc/polipo/config
    >logSyslog = true
    >logFile = /var/log/polipo/polipo.log
    >proxyAddress = "127.0.0.1"
    >proxyName = "localhost"
    >socksParentProxy = "localhost:9050"
    >diskCacheRoot = ""
    >localDocumentRoot = ""
    >disableLocalInterface=true
```sudo apt-get install privoxy```

