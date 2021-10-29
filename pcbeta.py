import requests 
from bs4 import BeautifulSoup
import time
import re
import rsa
import base64
import hashlib
import os
import sys

sys.path.append('.')
requests.packages.urllib3.disable_warnings()
try:
    from pusher import pusher
except:
    pass
from urllib import parse

result = '🏆pcbeta签到姬🏆\n'

cookie = os.environ.get("pcbeta_cookie")
TOKEN = os.environ.get("PUSH_PLUS_TOKEN")

def pushtg(data):
     global TGBOTAPI
     global TGID
     requests.get(
         'http://www.pushplus.plus/send?token='+TOKEN+'&content='+data)



def main():
    global result
    headers={
        'Cookie': cookie,
        'ContentType':'text/html;charset=gbk'
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    requests.session().get('https://i.pcbeta.com/home.php?mod=task&do=apply&id=149',headers=headers)
    fa=requests.session().get('https://i.pcbeta.com/home.php?mod=task&do=draw&id=149',headers=headers)
    fb=BeautifulSoup(fa.text,'html.parser')         
    fc=fb.find('div',id='messagetext').find('p').text
    print("🏆pcbeta签到姬🏆\n")
    print("返回内容")
    print(fc)
    if  "您需要先登录才能继续本操作"  in fc:
        result += "Cookie失效"
    elif "恭喜"  in fc:
        result += "签到成功"
    elif "不是进行中的任务"  in fc:
        result += "不是进行中的任务"
    else:
        result += "签到成功失败"
    
    print(result)
    pushtg(result)
    
def main_handler(event, context):
    main()


if __name__ == '__main__':
    main()
