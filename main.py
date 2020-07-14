from selenium import webdriver
import time

xmu_id = "id"
xmu_pwd = "password"

driver = webdriver.Chrome()

driver.get("https://ids.xmu.edu.cn/authserver/login?service=https://xmuxg.xmu.edu.cn/login/cas/xmu")
driver.find_element_by_xpath('//input[@id="username"]').send_keys(xmu_id)
driver.find_element_by_xpath('//input[@id="password"]').send_keys(xmu_pwd)
driver.find_element_by_xpath('//button[@class="auth_login_btn primary full_width"]').click()

driver.get("https://xmuxg.xmu.edu.cn/app/214")
time.sleep(5)

driver.find_element_by_xpath('//div[@title="我的表单"]').click()
time.sleep(5)

driver.find_element_by_xpath('//div[@id="select_1582538939790"]/div').click()
driver.find_element_by_xpath('//label[@title="是 Yes"]/span[2]').click()
driver.find_element_by_xpath('//div[@id="pdfDomContent"]/following-sibling::span[1]/span').click()
