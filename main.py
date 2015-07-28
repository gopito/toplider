# -*- coding: utf-8 -*-
from time import sleep
import urllib2
from splinter import Browser
from antigate import AntiGate
#from PIL import Image

with Browser(driver_name='chrome') as browser:
    # # Visit URL
    url = "https://oauth.vk.com/authorize?client_id=4759951&display=popup&redirect_uri=close.html&response_type=token&scope=2"
    browser.visit(url)


    browser.fill('email', '+79117919519')
    browser.fill('pass', '_apps')
    enterVK=browser.find_by_id("install_allow")
    enterVK.click()
    sleep(3)
    url="http://topliders.ru"
    browser.visit(url)

    sleep(2)
    browser.find_by_css("#dev_page_wrap > div:nth-child(1) > div.dev_page_block.main_desc.fl_l > div > div.dev_main_buttons.clear_fix > div > center > button").click()
    sleep(10)
    links=browser.find_link_by_text("Добавить в друзья")
    for link in links:
        browser.click_link_by_href(link['href'])
        sleep(3)
        browser.windows.current=browser.windows[1]
        friend=browser.find_by_text(u'Добавить в друзья')
        while (browser.is_text_present(u'Добавить в друзья', wait_time=5)):
            friend.click()
            sleep(1)
            browser.find_by_id("validation_skip").click()
            sleep(1)
            try:
                img=browser.find_by_css("div.captcha").find_by_tag("img")
                with open('captcha.jpeg', 'wb') as outfile:
                    outfile.write(urllib2.urlopen(img['src']).read())
                outfile.close()
                sleep(0.1)

                gate = AntiGate('ff3944c2490ee6dcf8872ee03d2a94f6', 'captcha.jpeg')

                input1=browser.find_by_css("input.big_text")
                input1[2].fill(gate.captcha_key)
                browser.find_by_text(u"Отправить").click()
                sleep(0.5)
            except:
                pass
        browser.windows.current.close()
        browser.windows.current=browser.windows[0]
        #http://topliders.ru/?page=office

        #link.click()



    # # Find and click the 'search' button
    # button = browser.find_by_name('btnG')
    # # Interact with elements
    # button.click()
    # if browser.is_text_present('splinter.readthedocs.org'):
    #     print("Yes, the official website was found!")
    # else:
    #     print("No, it wasn't found... We need to improve our SEO techniques")