from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)#this will keep the tab open
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/instant_pot/")

# driver.close()#thhis closes the single tab

price=driver.find_element(By.CLASS_NAME,"a-price-whole").text
price_fraction=driver.find_element(By.CLASS_NAME,"a-price-fraction").text
print(f"price of your product is ${price}.{price_fraction}")
driver.quit()#this closes the entire programe