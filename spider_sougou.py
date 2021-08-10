import requests
if __name__ ==  "__main__":
    url = "https://www.sogou.com/"
    re = requests.get(url=url)
    page_text = re.text
    print(page_text)
    with open("./sougou.html","w",encoding="utf-8") as fp:
        fp.write(page_text)
    


