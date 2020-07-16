from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# id && pwd
xmu_id = "id"
xmu_pwd = "pwd"

# some chrome options
chrome_options = Options()
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument('--no-sandbox')  # 让Chrome在root权限运行
chrome_options.add_argument('--disable-dev-shm-usage')  # 不打开图形界面
chrome_options.add_argument('window-size=1920x3000')
chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面
chrome_options.add_argument('--hide-scrollbars')
chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/opt/google/chrome/chromedriver')

# delete all cookies
driver.delete_all_cookies()

# login with id and pwd
driver.get("https://ids.xmu.edu.cn/authserver/login?service=https://xmuxg.xmu.edu.cn/login/cas/xmu")
time.sleep(1)
# try:
#     driver.find_element_by_xpath('//input[@id="username"]').send_keys(xmu_id)
# except:
#     driver.find_element_by_xpath('//ul[@class="dropdown-menu"]/li[4]/a').click()
#     driver.get("https://ids.xmu.edu.cn/authserver/login?service=https://xmuxg.xmu.edu.cn/login/cas/xmu")
#     driver.find_element_by_xpath('//input[@id="username"]').send_keys(xmu_id)

driver.find_element_by_xpath('//input[@id="username"]').send_keys(xmu_id)
driver.find_element_by_xpath('//input[@id="password"]').send_keys(xmu_pwd)
driver.find_element_by_xpath('//button[@class="auth_login_btn primary full_width"]').click()

driver.get("https://xmuxg.xmu.edu.cn/app/214")
time.sleep(3)

# 模拟点击，“我的表单” → “请选择” → “是” → “保存”
driver.find_element_by_xpath('//div[@title="我的表单"]').click()
time.sleep(3)

if driver.find_element_by_xpath('//div[@id="select_1582538939790"]/div/div/span').text != "是 Yes":
    driver.find_element_by_xpath('//div[@id="select_1582538939790"]/div').click()
    driver.find_element_by_xpath('//label[@title="是 Yes"]/span[2]').click()

driver.find_element_by_xpath('//div[@id="pdfDomContent"]/following-sibling::span[1]/span').click()
time.sleep(1)

# 处理弹窗
alert = driver.switch_to.alert
alert.accept()

# 退出浏览器
driver.quit()
