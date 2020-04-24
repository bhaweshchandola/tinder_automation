from selenium import webdriver  # automation tool
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup  # extraction tool
import csv  # formatting tool
import re  # regular expressions for finding text
import os, time
from selenium.webdriver.common.keys import Keys

URL = "https://www.tinder.com"

chrome_options = Options()
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--log-lecel=3")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

time.sleep(10)
main_page = driver.current_window_handle

try:
    close_modal = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
    close_modal.click()
except:
    pass

try:
    close_modal1 = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/button')
    close_modal1.click()
except:
    pass
login = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
login.click()

try:
    more_options_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button')
    more_options_button.click()
except:
    pass

facebook_login_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
facebook_login_button.click()
time.sleep(5)
for handle in driver.window_handles: 
    if handle != main_page: 
        login_page = handle
driver.switch_to.window(login_page)
soup = BeautifulSoup(driver.page_source, 'lxml')
print(soup)
email_text = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
email_text.send_keys("email/username")

password_text = driver.find_element_by_xpath('//*[@id="pass"]')
password_text.send_keys('password')


submit_cred = driver.find_element_by_xpath('//*[@id="u_0_0"]')
submit_cred.click()

time.sleep(10)
driver.switch_to.window(main_page) 
location_accept = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
location_accept.click()

not_interested = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
not_interested.click()

try:
    close_modal = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
    close_modal.click()
except:
    pass
time.sleep(5)
location_accept1 = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button')
location_accept1.click()

while True:
    try:
        close1 = drive.find_element_by_xpath('<button type="button" class="button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Ell Bdrs(100px) Px(24px) Px(20px)--s Py(0) Mih(42px)--s Mih(50px)--ml Fw($semibold) focus-button-style D(b) Mx(a) C($c-secondary) C($c-base):h" draggable="false"><span class="Pos(r) Z(1)">Not interested</span></button>')
        close1.click()
    except:
        pass
    try:
        close_modal = driver.find_element_by_xpath('''<button type="button" class="button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Ell Bdrs(100px) Px(24px) Px(20px)--s Py(0) Mih(40px) button--outline Bdw(2px) Bds(s) Trsdu($fast) Bdc($c-secondary) C($c-secondary) Bdc($c-base):h C($c-base):h Bdc($c-base):f C($c-base):f Bdc($c-base):a C($c-base):a Fw($semibold) focus-button-style W(100%)--s" draggable="false"><span class="Pos(r) Z(1)">I Accept</span></button>''')
        close_modal.click()
    except:
        pass
    driver.find_element_by_css_selector('body').send_keys(Keys.RIGHT)
    time.sleep(2)