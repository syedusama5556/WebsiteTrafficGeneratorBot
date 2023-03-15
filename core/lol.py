import random
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import requests
from selenium.webdriver import Firefox, FirefoxOptions
from bs4 import BeautifulSoup
import time
import os 

cwd = os.getcwd()

count = 1200
color1 = ["\033[1;31;40m", "\033[1;32;40m", "\033[1;33;40m",
          "\033[1;34;40m", "\033[1;35;40m", "\033[1;36;40m"]
def color():
    return str(random.choice(color1))
def banner():
    print("    \033[1;36;40m Code made by: \033[1;32;40m syedusama5556")
    print("        \033[1;31;40mSome Proxies May Be Dead. :(")
    print(
        "        \033[1;31;40mRemember:The Website In Which You Are Testing May Identify This Bot.")
    print("\n\n")
def req(proxy_url, target_url, timeo, stay_time):
    r = requests.get(proxy_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    list = soup.find(class_='table table-striped table-bordered')
    list1 = list.findAll('td')
    iplist = []
    portlist = []
    j = 0
    while (j < (8*count)):
        try:
            a = str(list1[j].contents[0])
            iplist.append(a)
            j = j+8
        except:
            break
    j = 1
    while (j < (8*count)):
        try:
            a = str(list1[j].contents[0])
            portlist.append(a)
            j = j+8
        except:
            break
    for index in range(0, (len(iplist)-1)):
        try:
            PROXY = iplist[index]+":"+portlist[index]
            print("\033[1;32;40mTrying From "+color()+str(PROXY))
            webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
                            "httpProxy": PROXY, "sslProxy": PROXY, "proxyType": "MANUAL"}
            options = FirefoxOptions()
            options.add_argument('--proxy-server={}'.format(PROXY))
            driver = Firefox(options=options, executable_path=GeckoDriverManager().install())
            # driver = webdriver.Firefox()
            driver.set_page_load_timeout(timeo)
            driver.get(target_url)
            time.sleep(stay_time)
            driver.close()
        except Exception as e:
            driver.close()
banner()
target = "https://rembg.co/"
# target = "https://www.instagram.com/reel/CZqStUxqPZ5/"
timeout = int(100)
stay = int(50)
urllist = ["https://www.sslproxies.org", "https://us-proxy.org", "https://free-proxy-list.net/uk-proxy.html",
           "https://free-proxy-list.net/anonymous-proxy.html", "https://free-proxy-list.net", "https://www.socks-proxy.net"]
for purl in urllist:
    banner()
    req(purl, target, timeout, stay)
    print("\033[1;32;40mSleeping For 10 Seconds")
    time.sleep(10)
