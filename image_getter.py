import requests
from bs4 import BeautifulSoup
import urlparse

url = "https://www.walmart.com/ip/54649026"
result = requests.get(url)

def image():
    urls=[]
    soup = BeautifulSoup(result.text, "html.parser")
    
    # This will look for a meta tag with the og:image property
    og_image = (soup.find('meta', property='og:image') or
                        soup.find('meta', attrs={'name': 'og:image'}))
    if og_image and og_image['content']:
        print og_image['content']
        print ''
        urls.append(og_image['content'])
    
    # This will look for a link tag with a rel attribute set to 'image_src'
    thumbnail_spec = soup.find('link', rel='image_src')
    if thumbnail_spec and thumbnail_spec['href']:
        print thumbnail_spec['href']
        print ''
        urls.append(thumbnail_spec['href'])
    
    image = """<img src="%s"><br />"""
    for img in soup.findAll("img", src=True):
       print image % urlparse.urljoin(url, img["src"])
       print ''
       if img["src"] not in urls:
            urls.append(img['src'])
            
    return urls