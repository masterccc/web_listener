# fakeweb

Listen incoming web requests and save them into mongo database :

```
result = {
    "http":http,
    "request": f"{request.method} {url}",
    "ip": request.headers.get('X-Real-IP'),
    "headers": request.headers,
    "content": posst_content,
}
   
    fakeweb_db.requests.insert_one(result)

``` 

# Output sample

```
_id: ObjectId("63c29653bf6c5802ccb48d0e"),
    http: "http 10",
    request: "POST /cgi-bin/ViewLog.asp",
    ip: "172.xx.xx.43",
    headers: {
        "X-Real-IP": "172.xx.xx.43",
        Host: "127.0.0.1:7000",
        Connection: "close",
        "Content-Length": "176",
        "Accept-Encoding": "gzip, deflate",
        Accept: "*/*",
        "User-Agent": "r00ts3c-owned-you",
        "Content-Type": "application/x-www-form-urlencoded"
    },
    content: "remotesubmitFlag1remotesyslogFlag1RemoteSyslogSupportec="
    ```
