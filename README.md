<h1 align="center">Website Traffic Generator Bot

</h1>
<p align="center">An open-source Unlimited Website Traffic Generator And YouTube View Generator.</p><br>


###############  Coded by      : syedusama5556 ##############<br>


#### By Changing the name, You won't be a script developer...

## Note:

- The script requires working network connection to work.
- The script requires Geckodriver.
- Good For CPV/CPM Ads.(Only if it can't identify the bot.)
- Good For YouTube View Increaser.(Only if it can't be identified.)
- This script is only for educational purposes.
- **Developer is not responsible for the misuse of Bot.**
<br>

## Features:

- Uses Geckodriver
- Uses Selenium
- Uses More Than 20,000 Proxies
- Running Only One Session At A Time. So No Question Of Hang
- You Can Set The TimeOut and Stay Time 
- Easy to use.

## Usage:

**Notice:** 

To use the Bot type the following commands in Terminal:
```
git clone https://github.com/syedusama5556/WebsiteTrafficGeneratorBot.git
cd Bot
python Bot.py
```

## Run the Proxy Server with tor and docker

So now we gonna create a proxy server

```bash
# build docker container
docker build -t zeta0/alpine-tor:latest .

# ... or pull docker container
docker pull zeta0/alpine-tor:latest

# start docker container
docker run -d -p 5566:5566 -p 2090:2090 -e tors=25 zeta0/alpine-tor

# start docker with privoxy enabled and exposed
docker run -d -p 8118:8118 -p 2090:2090 -e tors=25 -e privoxy=1 zeta0/alpine-tor

# test with ...
curl --socks5 localhost:5566 http://httpbin.org/ip

# or if privoxy enabled ...
curl --proxy localhost:8118 http://httpbin.org/ip

# or to run chromium with your new found proxy
chromium --proxy-server="http://localhost:8118" \
    --host-resolver-rules="MAP * 0.0.0.0 , EXCLUDE localhost"

# monitor
# auth login:admin
# auth pass:admin
http://localhost:2090 or http://admin:admin@localhost:2090

# start docket container with new auth
docker run -d -p 5566:5566 -p 2090:2090 -e haproxy_login=MySecureLogin \
    -e haproxy_pass=MySecurePassword zeta0/alpine-tor
```


# CONTACT ME:

Feel Free To Open An Issue...

```



