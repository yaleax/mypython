import requests
headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                 "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
respons =  requests.get("https://movie.douban.com/top250",headers=headers)
if respons.status_code == 200:
    print("请求成功")
    print(respons.text)
else:
    print("请求失败")

