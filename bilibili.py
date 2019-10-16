import re

import requests

from pymongo import MongoClient


class Bilibili:
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}
        self.url_temp = "https://www.bilibili.com/ranking/all/0/0/1"

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_content_list(self, html_str):
        json_ret = re.findall("<script>window.__INITIAL_STATE__=(.*?)</script>", html_str)[0]
        return json_ret

    def save_data(self, data):
        with open("bilibili.json", "w", encoding="utf-8") as f:
            f.write(data)

    def run(self):
        # 1.url获取
        # 2.请求数据
        html_str = self.parse_url(self.url_temp)
        # 3.提取数据
        json_ret = self.get_content_list(html_str)
        # 4.保存
        self.save_data(json_ret)




if __name__ == '__main__':
    bilibili = Bilibili()
    bilibili.run()