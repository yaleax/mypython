from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook

hearders = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": 'll="118200"; bid=if7o-u5rpLw; _vwo_uuid_v2=D42BF118CA0CFBF33DE8D94435B90D555|8925bd17a31f8b7058e92337ffcb5018; __gads=ID=4dc7fd39de72a642-22ad1e0315d700a5:T=1666015161:RT=1666015161:S=ALNI_MYaFQPlEV9oanRAwTzfwojslL387A; dbcl2="263719242:cdu+tcWOYSA"; __utmz=30149280.1666020617.4.3.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmz=223695111.1666020617.3.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; push_noty_num=0; push_doumail_num=0; ct=y; __yadk_uid=YjGciSzXayZFWFJ5s9NkPcW5sv8CoJWw; ck=c-17; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1666700334%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; __utma=30149280.1094459905.1662650904.1666623522.1666700335.9; __utmc=30149280; __utma=223695111.1141913362.1662650905.1666623522.1666700335.8; __utmc=223695111; __gpi=UID=00000b6478645c88:T=1666015161:RT=1666700335:S=ALNI_MarpFDTt2lvlUo2-EkBJy3V-uPMsA; _pk_id.100001.4cf6=6be088305e22e180.1662650904.8.1666700967.1666625362.',
    "Host": "movie.douban.com",
    "sec-ch-ua": "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"106\", \"Not;A=Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}

allName = []
allRate = []
allDirection = []
allComment = []

for num in range(10):
    content = requests.get(f"https://movie.douban.com/top250?start={num * 25}&filter=",headers= hearders).text
    soup = BeautifulSoup(content,"html.parser")
    allNameList = soup.find_all("span",class_="title")
    allRateList = soup.find_all("span",attrs= {"class": "rating_num"})
    allDirectionList = soup.find_all("p",attrs= {"class": ""})
    allCommentList = soup.find_all("span",attrs= {"class": "inq"})
    for name in allNameList:
        if name.text.startswith("\xa0/\xa0"):
            pass
        else:
            allName.append(name.text)
    for rate in allRateList:
        allRate.append(rate.text)
    for direction in allDirectionList:
        if direction:
            myDirection = direction.get_text().strip().split(" ")[1]
            allDirection.append(myDirection)
    for comment in allCommentList:
        allComment.append(comment.text)
#保存到excel
wb = Workbook()
sh = wb.active
try:
    worksheet = wb.create_sheet("豆瓣电影TOP250")
except:
    worksheet = wb["豆瓣电影TOP250"]
myTitle = ['电影名称', '导演', '评分', '评论']
sh.append(myTitle)
print(allName)
print(allRate)
print(allDirection)
print(allComment)

#把 allName,allRate,allDirection,allComment 里的数据写入到excel
for i in range(4):
    if i == 0:
        for j ,name in enumerate(allName):
            sh.cell(row=j+2,column=i+1,value=name)
    if i == 1:
        for j ,rate in enumerate(allRate):
            sh.cell(row=j+2,column=i+1,value=rate)
    if i == 2:
        for j ,direction in enumerate(allDirection):
            sh.cell(row=j+2,column=i+1,value=direction)
    if i == 3:
        for j ,comment in enumerate(allComment):
            sh.cell(row=j+2,column=i+1,value=comment)

wb.save("豆瓣电影TOP250.xlsx")
wb.close()




