from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")
search_bar=driver.find_element(By.XPATH,value='//*[@id="id-search-field"]')
print(search_bar.get_attribute("id"))
a=driver.find_element(By.XPATH,value='//*[@id="content"]/div/section/div[1]/div[3]/h2')
print(a.text)
driver.quit()