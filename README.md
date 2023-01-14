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