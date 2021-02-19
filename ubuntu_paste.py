import requests
from lxml import etree

class ubuntuPaste(object):
    def __init__(self):
        self.url = 'https://paste.ubuntu.com'
        self.headers = {
            "Host": "paste.ubuntu.com",
            "Connection": "keep-alive",
            "Origin": "https://paste.ubuntu.com",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Referer": "https://paste.ubuntu.com/",
            "Accept-Encoding": "gzip,deflate,br",
            "Accept-Language": "zh-CN,zh;q=0.9",
        }

    def attack_up(self, code):
        data = {
            "poster": "posterName",
            "syntax": "python3",
            "expiration": "day",
            "content": code,
        }

        res = requests.post(url=self.url, data=data, headers=self.headers)
        html = etree.HTML(res.text)
        pasteUrl = html.xpath('//@href')
        addUrl = pasteUrl[1][:-6]
        targetUrl = self.url + addUrl
        print(targetUrl)


    def main(self):
        code = input('Please enter the code:')
        self.attack_up(code)


if __name__ == '__main__':
    paste = ubuntuPaste()
    paste.main()
