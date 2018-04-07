# -- coding: utf-8 --
import urllib.request
import execjs

class Stock(object):
    def __init__(self, url):
        self.url = url

    def _request_data(self, url):
        response = urllib.request.urlopen(url)
        data = response.read()
        data = str(data, encoding='utf-8')
        return data

    def get_all_list(self):
        info = []
        data = self._request_data(self.url)
        ctx = execjs.compile(data)
        stock_items = ctx.call("get_data")
        for stock in stock_items:
            info.append(stock['val'])
        return info

#test
stock = Stock('http://www.sse.com.cn/js/common/ssesuggestdata.js')
data = stock.get_all_list()
pass
