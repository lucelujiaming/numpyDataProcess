import os
import urllib.request
 
'''
雅虎历史数据请求
 
    请求地址：http://ichart.yahoo.com/table.csv?s=string&a=int&b=int&c=int&d=int&e=int&f=int&g=d&ignore=.csv
        或者：http://table.finance.yahoo.com/table.csv?a=%d&b=%d&c=%d&d=%d&e=%d&f=%d&s=%s&y=0&g=%s&ignore=.csv
        两者参数有点不一样
 
    说明：
        s — 股票名称
        a — 起始时间，月
        b — 起始时间，日
        c — 起始时间，年
        d — 结束时间，月
        e — 结束时间，日
        f — 结束时间，年
        g — 时间周期。
 
    Ø  参数g的取值范围：d->‘日’(day), w->‘周’(week)，m->‘月’(mouth)，v->‘dividends only’
 
    Ø  月份是从0开始的，如9月数据，则写为08。  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
 
示例
 
    查询浦发银行2010.09.25 – 2010.10.8之间日线数据
 
    http://ichart.yahoo.com/table.csv?s=600000.SS&a=08&b=25&c=2010&d=09&e=8&f=2010&g=d
 
    查看国内沪深股市的股票，规则是：沪股代码末尾加.ss，深股代码末尾加.sz。如浦发银行的代号是：600000.SS
'''
 
ticker = '' # 600028 是"中国石化"的股票代码
ticker += '.ss'   # .ss 表示上证 .sz表示深证
 
date1 = ( 2015, 1, 1 ) #begining time
date2 = ( 2016, 1, 1 ) #ending time  
 
d1 = (date1[1]-1, date1[2], date1[0])
d2 = (date2[1]-1, date2[2], date2[0])  
 
g='d'  
 
urlFmt = 'http://table.finance.yahoo.com/table.csv?a=%d&b=%d&c=%d&d=%d&e=%d&f=%d&s=%s&y=0&g=%s&ignore=.csv'
url =  urlFmt % (d1[0], d1[1], d1[2], d2[0], d2[1], d2[2], ticker, g)  #the url of historical data  
 
filename = 'data.csv'                #file name
filename = os.path.join(os.path.dirname(__file__), filename)   #located file  
urllib.request.urlretrieve(url, filename)        #下载，保存


