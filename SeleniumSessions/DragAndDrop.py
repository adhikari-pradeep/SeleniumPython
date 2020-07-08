from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('https://jqueryui.com/resources/demos/droppable/default.html')
time.sleep(3)

source = driver.find_element(By.ID,'draggable')
target = driver.find_element(By.ID,'droppable')

act_chains = ActionChains(driver)
# act_chains.drag_and_drop(source, target).perform()
act_chains.click_and_hold(source).move_to_element(target).release().perform()


time.sleep(3)
driver.close()