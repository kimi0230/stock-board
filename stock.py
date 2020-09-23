
'''

[ 台股即時行情 ]

即時從 Yahoo 股市抓上市/櫃成量排行

'''

import requests
from bs4 import BeautifulSoup
import datetime
import time
import prettytable as pt
import os

def stock(choose = '1'):

    try:
        market = {
            'code': 'tse',
            'title': '上市'
        }

        if choose == '2':
            market['code'] = 'otc'
            market['title'] = '上櫃'

        # Yahoo 網址
        url = 'https://tw.stock.yahoo.com/d/i/rank.php?t=vol&e=' + market['code']

        while 1 == 1:

            # 取得網頁內容
            rs = requests.get(url)

            # 解析網頁內容
            soup = BeautifulSoup(rs.text, 'html.parser')

            # 找出所有放在 table 元素中的資料
            result = soup.find_all('table')

            # 取資料格式檢查用
            i = 0

            # 表單初始化
            tb = pt.PrettyTable()
            tb.field_names = ['排名', '名稱', '成交價', '漲跌', '漲跌幅', '成交量(張)']

            # 只抓有股價資料的 table
            for item in result[2].find_all('tr'):

                # 只取需要的部分
                if i > 2:
                    tmp = item.find_all('td')
                    index = tmp[0].text
                    title = tmp[1].text
                    price = tmp[2].text
                    updown = tmp[3].text
                    updown_percent = tmp[4].text
                    volume = tmp[8].text

                    # 把資料塞進表單
                    tb.add_row([index, title, price, updown, updown_percent, volume])

                # 取資料格式檢查用
                i += 1

            # 清空畫面
            os.system('clear')

            # 輸出表單
            print('\n', market['title'], '成交量排行: ', datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
            print(tb)
            print('[離開] Ctrl + C')

            # 睡一秒
            time.sleep(1)

    except:
        pass

# 執行
choose = input('\n請選擇: [1]上市成交量排行 | [2]上櫃成交量排行\n')
stock(choose)
