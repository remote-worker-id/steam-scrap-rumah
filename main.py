import bs4
from bs4 import BeautifulSoup
import requests

headers = {
'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
}
url = 'https://www.detik.com/terpopuler?tag_from=wp_cb_mostPopular_more'
contents = requests.get(url)
# print(contents)

response = bs4.BeautifulSoup(contents.text, "html.parser")
berita_terpopuler = response.find(attrs={'class':'grid-row list-content'})
media_titles = berita_terpopuler.findAll(attrs={'class':'media__text'})
images = berita_terpopuler.findAll(attrs={'class':'media__image'})
dates = berita_terpopuler.findAll(attrs={'class':'media__date'})

# Title
# for media_title in media_titles:
#     # print(media_title.find('a',attrs={'class':'media__link'}).text)

# Image
# for image in images:
#     print(image.find('a', attrs={'class':'media__link'}).find('img')['src'])

# Date
for date in dates:
    print(date.text)

