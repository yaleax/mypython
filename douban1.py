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

movieName = []
movieDirector = []
movieScore = []
movieComment = []

for i in range(10):
    url = f'https://movie.douban.com/top250?start={i*25}&filter='
    response = requests.get(url, headers=hearders)
    soup = BeautifulSoup(response.text, 'html.parser')
    movieNameList = soup.find_all('span', class_='title')
    movieDirectorList = soup.find('p', attrs={"class": ""})
    movieScoreList = soup.find_all('span', class_="rating_num")
    for name in movieNameList:
        if name.text.startswith('\xa0/\xa0'):
            pass
        else:
            movieName.append(name.string)
    for movie in soup.select('.item'):
        directorList = movie.find('p', attrs={"class": ""})
        if directorList:
            myDirector = directorList.get_text().strip().split(' ')[1]
            movieDirector.append(myDirector)
    for score in movieScoreList:
        movieScore.append(score.text)
    for movie in soup.select('.item'):
        if movie.select('.bd .quote') == []:
            movieComment.append('空')
        else:
            comment = movie.select('.bd .quote')[0].text  # 影评
            movieComment.append(comment.strip())

print(movieName)