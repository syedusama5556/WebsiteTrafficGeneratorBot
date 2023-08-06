import random
from typing import KeysView
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Firefox, FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
import threading
import time
from selenium import webdriver

from selenium.webdriver.common.proxy import *
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


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
            random_index = random.randint(0, len(iplist) - 1)

            PROXY = iplist[index]+":"+portlist[index]
            print("\033[1;32;40mTrying From IP " + color() + str(PROXY))
            print("\033[1;32;40mTrying From URL " + color() + str(proxy_url))
            chrome_options = webdriver.ChromeOptions()
            # chrome_options.add_argument('--headless')
            # chrome_options.add_argument('--no-sandbox')
            # chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--proxy-server={}'.format(PROXY))

            driver = webdriver.Chrome(options=chrome_options,executable_path=ChromeDriverManager().install())
            # driver.implicitly_wait(3)
            driver.set_page_load_timeout(timeo)
            driver.get(target_url)
            # Find the element to scroll
            element = driver.find_element_by_css_selector("a[class='textcolor']")

            # Create an instance of the ActionChains class
            actions = ActionChains(driver)

            # Move the mouse to the element
            actions.move_to_element(element)

            # Scroll down by sending the "SPACE" key to the element
            for i in range(10):
                time.sleep(1)
                actions.send_keys(KeysView.SPACE)

            # Perform the actions
            actions.perform()
            time.sleep(stay_time)
            driver.close()
        except Exception as e:
           print("failed")


def run_threads(target, timeout, stay, urllist, num_threads):
    threads = []
    for i in range(num_threads):
        purl = random.choice(urllist)
        t = threading.Thread(target=req, args=(
            purl, target, timeout, stay))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()


if __name__ == '__main__':
    banner()
    target = "https://rembg.co/"
    # target = "https://rembg.co/blogdetailpage.php?id=1"
    timeout = int(100)
    stay = int(20)
    urllist = ["https://www.sslproxies.org", "https://us-proxy.org", "https://free-proxy-list.net/uk-proxy.html",
               "https://free-proxy-list.net/anonymous-proxy.html", "https://free-proxy-list.net", "https://www.socks-proxy.net"]
    
    # urllist = [ "https://free-proxy-list.net"]
    num_threads = 20
    run_threads(target, timeout, stay, urllist, num_threads)
    print("\033[1;32;40mSleeping For 10 Seconds")
    time.sleep(10)
