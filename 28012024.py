
from selenium import webdriver
from time import sleep
dr = webdriver.Chrome()
dr.get("file:///C:/DevOps/tip_calc/index.html")
# for i in range(5):
#     dr.refresh()
#     sleep(2)
billamt = dr.find_element(by="id", value="billamt")
billamt.send_keys("100")
dr.find_element(by="xpath", value="//*[@id=\"serviceQual\"]/option[3]").click()
dr.find_element(by="id", value="peopleamt").send_keys("5")
dr.find_element(by="id", value="musicQual").send_keys("5")
dr.find_element(by="id", value="calculate").click()
actual = dr.find_element(by="id", value="tip").text
expected = 9
# if expected == actual:
#     print("all cool")
# else:
#     print("you have ruined the tip")
#sleep(1000)
assert expected == actual