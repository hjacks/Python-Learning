import re
import requests
from bs4 import BeautifulSoup

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0'
}
urls = ['https://www.pexels.com/?page={}'.format(str(i)) for i in range (1,21)]
photos = []

for url in urls:
    wb_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    imgs = soup.select('article.photo-item > a > img')
    for img in imgs:
        photo = img.get('src')
        photos.append(photo)

path = 'F://yibu/'
for item in photos:
    data = requests.get(item,headers=headers)
    photo_name = re.findall('\d\/(.*?)\?a',item)
    
    if photo_name:
        fp = open(path+photo_name[0],'wb')
        print(path+photo_name[0])
        fp.write(data.content)
        fp.close
