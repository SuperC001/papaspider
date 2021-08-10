import requests

if __name__ == "__main__":
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"
    }
    url = "https://www.sogou.com/web"
    kw=input("请输入要搜索的词:")
    param={ 
        "query":kw
    }
    re = requests.get(url=url,params=param,headers=headers)
    page_text = re.text
    filename = kw+".html"
    with open((".\%s" % filename),"w",encoding="utf-8") as fp:
        fp.write(page_text)
