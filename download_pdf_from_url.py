from urllib.request import urlopen, urlretrieve, Request
import re

"""
Example:
url_web = "https://www.birs.ca/workshops/2019/19w5035/files/"

"""
url_web = "your:url"

# get full html code from a website
response = Request(url=url_web, headers={'User-Agent':      'Mozilla/5.0'})

webpage = urlopen(response)
print(webpage.read())

#urllist = re.findall("href=[\"\'](.*?)[\"\']", urlopen(response).read().decode('utf-8'))
urllist = re.findall(".*href=\"([^\"]+\.pdf)\".*", urlopen(response).read().decode('utf-8'))
print(urllist)
        
for url in urllist:
    print(url)
    """
    Example:
    url_base = "https://www.birs.ca"
    """
    url_base = "from your url"
    url_pdf = f"{url_base}{url}"
    with urlopen(Request(url=url_pdf, headers={'User-Agent':      'Mozilla/5.0'})) as file:
        content = file.read()
    name = url.split('/')[-1]
    print(name)
    with open(name, 'wb') as file:
        file.write(content)
