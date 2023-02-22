import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


# ............color...
N = '\033[0m'
W = '\033[1;37m' 
B = '\033[1;34m' 
M = '\033[1;35m' 
R = '\033[1;31m' 
G = '\033[1;32m' 
Y = '\033[1;33m' 
C = '\033[1;36m'
# .........................
url = input("Enter the URL: ")
visited = set()
def geturls(baseUrl):
    lst = []
    if baseUrl in visited:
        return lst
    r = requests.get(baseUrl)
    content = r.text
    soup = BeautifulSoup(content, "html.parser")
    for i in soup.findAll("a", href=True):
        u = i.get('href')
        if "http" == u[:4]:
            continue
        if "javascript" in u:
            lst.append('''[javacript] '''+u)
        else:
            lst.append(urljoin(baseUrl,u))
    visited.add(baseUrl)
    return lst

def printurl(lst):
    warnings = [url for url in lst if '=' in url]
    for url in lst:
        if url in warnings:
            print(" ["+Y+"injectable"+N+"]: "+ url)
        else:
            print(" ["+G+"info"+N+"]: "+ url)

def crawl(base):
    lst = geturls(base)
    visited.add(base)
    printurl(lst)
    while lst:
        new_lst = []
        for url in lst:
            if url not in visited:
                new_lst.extend(geturls(url))
                visited.add(url)
        printurl(new_lst)
        lst = new_lst

crawl('https://www.google.com/')  
