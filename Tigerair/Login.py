from selenium import webdriver
from selenium.webdriver.support import wait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

base_url = 'https://booking.tigerairtw.com/?lang=zh-TW'
qi_element = '//*[@id="root"]/div/div[2]/div[2]/div/div[1]/div/div/div/div/div/div/div[2]/div[1]/div/div/button'
dao_element = '//*[@id="root"]/div/div[2]/div[2]/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/button'
Airport_fromCity = 'KHH'
input_airport_fromCity = '//*[@id="root"]/div/div[2]/div[2]/div/div[1]/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div/input'
Airport_toCity = 'MFM'
input_airport_toCity = '//*[@id="root"]/div/div[2]/div[2]/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/input'
country = '日本'
people_id_number = 'E12345678'

"""
进入网站主页
"""
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(base_url)
wait_appear = WebDriverWait(driver, 10)

driver.implicitly_wait(60)
flight = driver.find_element(By.ID, 'checkbox-one-way').click()
input_date_element_id = 'date-input'

"""
fromCity
"""
fromCity = driver.find_element(By.XPATH, qi_element)
ActionChains(driver).click(fromCity).perform()
driver.implicitly_wait(5)
form_control_s = driver.find_element_by_xpath(input_airport_fromCity).send_keys(Airport_fromCity)
que_ren_fromCity = driver.find_element_by_xpath(input_airport_fromCity).send_keys(Keys.ENTER)
"""
toCity
"""
toCity = driver.find_element(By.XPATH, dao_element)
ActionChains(driver).click(toCity).perform()
driver.implicitly_wait(5)
to_control_s = driver.find_element_by_xpath(input_airport_toCity).send_keys(Airport_toCity)
que_ren_toCity = driver.find_element_by_xpath(input_airport_toCity).send_keys(Keys.ENTER)
"""
输入日期
"""
fromCity_day = driver.find_element_by_id(input_date_element_id).clear()
fromCity_day = driver.find_element_by_id(input_date_element_id).send_keys('2018/7月/25')
"""
搜索航班
"""
driver.find_element_by_xpath('//*[@id="search-form"]/div/div/div[2]/button').click()
driver.implicitly_wait(60)

tiger = driver.find_element_by_xpath(
    '//*[@id="root"]/div/div[2]/div/div[3]/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div').click()

time.sleep(10)
"""
继续   到旅客资料
"""
js = 'var q=document.documentElement.scrollTop=10000'
driver.execute_script(js)

passenger_information = driver.find_element_by_css_selector(
    '#root > div > div.container-fluid > div > div.col-xs-12.col-md-9 > div:nth-child(2) > div.module.module-navigation > div > div.btn-nav.pull-right')
ActionChains(driver).click(passenger_information).perform()

"""
旅客资料填写
"""
sex_choice = driver.find_element_by_xpath('//*[@id="adult-1"]/div/div[1]/div/div[2]/div/div[1]/div[1]/div/div/button')
ActionChains(driver).click(sex_choice).perform()
driver.implicitly_wait(3)
# 性别
sex = 1  # 1为 先生
sex_is = None
if sex == 1:
    sex_is = driver.find_element_by_xpath(
        '//*[@id="adult-1"]/div/div[1]/div/div[2]/div/div[1]/div[1]/div/div/div/ul/li[1]/a')
else:
    sex_is = driver.find_element_by_xpath(
        '//*[@id="adult-1"]/div/div[1]/div/div[2]/div/div[1]/div[1]/div/div/div/ul/li[2]/a')
sex_is.click()
# 姓名
first_name = 'fang'
second_name = 'fang'
input_second_name = driver.find_element_by_xpath(
    '//*[@id="adult-1"]/div/div[1]/div/div[2]/div/div[1]/div[2]/div/input').send_keys(second_name)
input_first_name = driver.find_element_by_xpath(
    '//*[@id="adult-1"]/div/div[1]/div/div[2]/div/div[1]/div[3]/div/input').send_keys(first_name)
# 国家
country_button = driver.find_element_by_xpath(
    '//*[@id="adult-1"]/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div/button')
ActionChains(driver).click(country_button).perform()
country_choice = driver.find_element_by_xpath(
    '//*[@id="adult-1"]/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div/div/div/input').send_keys(country)
country_choice_1 = driver.find_element_by_xpath(
    '//*[@id="adult-1"]/div/div[1]/div/div[2]/div/div[2]/div[2]/div/div/div/div/input').send_keys(Keys.ENTER)

"""
出生日期
"""
# 年
s_year = driver.find_element_by_xpath(
    '//*[@id="adult-1"]/div/div[1]/div/div[2]/div/div[1]/div[4]/div/div[1]/div/select')
Select(s_year).select_by_value('1998')
# 月
s_month = driver.find_element_by_xpath(
    '//*[@id="adult-1"]/div/div[1]/div/div[2]/div/div[1]/div[4]/div/div[2]/div/select')
Select(s_month).select_by_value('10')
# 日
s_day = driver.find_element_by_xpath('//*[@id="adult-1"]/div/div[1]/div/div[2]/div/div[1]/div[4]/div/div[3]/div/select')
Select(s_day).select_by_value('23')
"""
到期日
"""
# 年
d_year = driver.find_element_by_xpath(
    '//*[@id="adult-1"]/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div[1]/div/select')
Select(d_year).select_by_value('2019')
# 月
d_month = driver.find_element_by_xpath(
    '//*[@id="adult-1"]/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div[2]/div/select')
Select(d_month).select_by_value('08')
# 日
d_day = driver.find_element_by_xpath(
    '//*[@id="adult-1"]/div/div[1]/div/div[2]/div/div[2]/div[4]/div/div[3]/div/select')
Select(d_day).select_by_value('26')

# 护照
id_number = driver.find_element_by_xpath(
    '//*[@id="adult-1"]/div/div[1]/div/div[2]/div/div[2]/div[3]/div/input').send_keys(people_id_number)
driver.implicitly_wait(30)

# 行李
xing_li = driver.find_element_by_xpath('//*[@id="baggage-segment-1-adult-1-BG00"]').click()
time.sleep(15)

# 保险框
js = 'var q=document.documentElement.scrollTop=10000'
driver.execute_script(js)

baoxian = driver.find_element_by_xpath('//*[@id="checkbox-insurance-no"]').click()
to_select_chair = driver.find_element_by_xpath(
    '//*[@id="root"]/div/div[2]/div/div[3]/div[2]/div[2]/div/div[2]/a').click()

div_tanchuang = driver.find_element_by_xpath(
    '//*[@id="root"]/div/div[2]/div/div[3]/div[2]/div[1]/div/div[1]/div/div[1]/div/div/div[3]/a[2]').click()

time.sleep(40)
