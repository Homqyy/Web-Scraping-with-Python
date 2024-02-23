# 《Web Scraping with Python》读书笔记

## 介绍

这是《Web Scraping with Python》一书的读书笔记，主要是为了记录一些重要的知识点和代码示例。`ex-*`文件是书中的示例代码。`pythonScraping`是可复用的代码库。

运行示例代码前，需要创建密码文件`screts.json`，内容如下：

```json
{
    "twitter": {
        "bearer_token": "your bearer token",
        "access_token": "your access token",
        "access_token_secret": "your access token secret",
        "api_key": "your api key",
        "api_key_secret": "your api key secret"
    },
    "google": {
        "api_key": "your api key",
    },
    "ipstack": {
        "api_key": "your api key"
    }
}
```

将上述值替换为自己账号的值即可。

## 引用

- source code of the book: <https://github.com/REMitchell/python-scraping>
- google cloud: <https://console.cloud.google.com/apis/credentials?project=logical-pathway-413902>
- ipstack: <https://ipstack.com/>
- twitter develop: <https://developer.twitter.com/en/portal>

### Python库

- bs4: <https://beautiful-soup-4.readthedocs.io/en/latest/>
- urllib.parse: <https://docs.python.org/3/library/urllib.parse.html>
- urllib.request: <https://docs.python.org/3/library/urllib.request.html>
- html.parser: <https://docs.python.org/3/library/html.parser.html>
- csv: <https://docs.python.org/3/library/csv.html>