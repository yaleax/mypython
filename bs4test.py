from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook
hearders = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
                 "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
wb = Workbook()
ws = wb.active

for startNume in range(0,250,25):
    content = requests.get(f"https://movie.douban.com/top250?start={startNume}&filter=",headers= hearders).text
    soup = BeautifulSoup(content,"html.parser")
    allName = soup.find_all("span",class_="title")
    allRate = soup.find_all("span",attrs= {"class": "rating_num"})

    for name, rate in zip(allName, allRate):
        title = name.get_text()
        #print(title, rate.get_text())
        if "/" not in title:
            print(title, rate.get_text())
            formatted_string = f"{title} {rate.get_text()}"
            print(formatted_string)
            ws.append([title, rate.get_text()])
            wb.save("豆瓣电影.xlsx")



