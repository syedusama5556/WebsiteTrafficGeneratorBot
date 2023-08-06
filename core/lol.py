import random
from selenium.webdriver.common.keys import Keys
import time
import os 
import undetected_chromedriver as UndetectedChromeDriver
import undetected_chromedriver as UndetectedChromeDriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By

cwd = os.getcwd()
driver = ''

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



def req( target_url, timeo, stay_time):
        try:

            chromedriver_autoinstaller.install()

            chrome_options = UndetectedChromeDriver.ChromeOptions()
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            # chrome_options.add_argument("--headless=new")
            chrome_options.add_argument('--disable-gpu')
            # if useproxy:
            #     chrome_options.add_argument(f'--proxy-server=http://scrapeops.headless_browser_mode=false:{SCRAPEOPS_API_KEY}@proxy.scrapeops.io:5353')

            chrome_options.add_argument(f'--proxy-server=socks5://localhost:5566')
            chrome_options.add_argument("--disable-extensions")
            driver = UndetectedChromeDriver.Chrome(options=chrome_options,version_main=115)
            driver.maximize_window()
            driver.get('http://httpbin.org/ip')
            print("\033[1;32;40mTrying From "+color()+str(driver.find_element(By.TAG_NAME, "body").text))

            # driver = Firefox(s,options=options, executable_path=GeckoDriverManager().install())
     
            # driver = webdriver.Firefox()
            driver.set_page_load_timeout(timeo)
            driver.get(target_url)
            time.sleep(5)
            height = int(driver.execute_script("return document.documentElement.scrollHeight"))

            while True:
                driver.execute_script('window.scrollBy(0,10)')
                time.sleep(0.10)
                totalScrolledHeight = driver.execute_script("return window.pageYOffset + window.innerHeight")
                
                if totalScrolledHeight == height:
                    body = driver.find_element("tag name", "body")
                    body.send_keys(Keys.CONTROL + Keys.HOME)
                    driver.switch_to.window(driver.window_handles[0])
                    break
            print('***Web Page Visited***')
            time.sleep(stay_time)
            driver.close()
        except Exception as e:
            print(e)
            driver.close()


banner()
target = "https://rembg.co/"
target = "https://icgpt.app/"
# target = "https://blog.hubspot.com/marketing/how-to-use-medium"
# target = "https://www.whatsmyip.org/"
timeout = int(100)
stay = int(30)
urllist = ["https://www.sslproxies.org", "https://us-proxy.org", "https://free-proxy-list.net/uk-proxy.html",
           "https://free-proxy-list.net/anonymous-proxy.html", "https://free-proxy-list.net", "https://www.socks-proxy.net"]
for purl in urllist:
    # banner()
    req(target, timeout, stay)
    print("\033[1;32;40mSleeping For 10 Seconds")
    time.sleep(10)
