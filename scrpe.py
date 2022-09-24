import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
csv_file = open('file.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Product image link',' Product name','Product number/SKU','Product description','All Classifications'])
dic ={}
path = "/usr/bin/geckodriver"
browser = webdriver.Firefox(executable_path=path)
browser.get("https://www.phoenixcontact.com/en-pc/products#pr-cat-id-325")
browser.delete_all_cookies()
browser.find_element(By.CSS_SELECTOR,"#pr-cat-id-325 > ul:nth-child(2) > li:nth-child(1)").click()
browser.implicitly_wait(20)
browser.find_element(By.CSS_SELECTOR,"li.pr-category-card:nth-child(1)").click()
browser.implicitly_wait(20)
number_products = browser.find_element(By.CSS_SELECTOR,".se-result-total-results-count").text
number_pages = browser.find_elements(By.CLASS_NAME,"se-page-link")
number_pages = number_pages[-1].text
number_products = int(number_products.split(" ")[0])
# WebDriverWait(browser,50).until(EC.presence_of_element_located((By.CSS_SELECTOR,f'article.se-result-pos:nth-child({3}) > div:nth-child(1) > section:nth-child(2) > a:nth-child(1) > div:nth-child(1)'))).click()
# try:
#     x = browser.find_element(By.ID,"pr-section-classifications-submenu") 
#     soup = BeautifulSoup(x.get_attribute('innerHTML'),'html.parser')
#     x = soup.find_all('span')
#     for i in range(len(x)):
#         lol = "".join(x[i].contents).strip()20)
#         if lol.isnumeric():
#             dic.update({"".join(x[i-1].contents).strip():lol})
#     print(dic)
# except:
#     pass

# WebDriverWait(browser,50).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[1]/div[3]/div/div/div/div[2]/div/div/div[3]/nav[1]/div[4]/div/div/div/div[1]/div[1]"))).click()
# WebDriverWait(browser,50).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[1]/div[3]/div/div/div/div[2]/div/div/div[3]/nav[1]/div[4]/div/div/div/div[2]/div[1]/div/div[5]"))).click()
# for page in range(1,int(number_pages)+1):
for i in range(1,number_products+1):
    browser.implicitly_wait(20)
    WebDriverWait(browser,50).until(EC.presence_of_element_located((By.CSS_SELECTOR,f'article.se-result-pos:nth-child({i}) > div:nth-child(1) > section:nth-child(2) > a:nth-child(1) > div:nth-child(1)'))).click()                       
    sku=browser.find_element(By.CSS_SELECTOR,"#pr-subheadline > span:nth-child(1)").text
    try:
        x = browser.find_element(By.ID,"pr-section-classifications-submenu")
        browser.implicitly_wait(200)
        soup = BeautifulSoup(x.get_attribute('innerHTML'),'html.parser')
        x = soup.find_all('span')
        for i in range(len(x)):
            lol = "".join(x[i].contents).strip()
            if lol.isnumeric():
                dic.update({"".join(x[i-1].contents).strip():lol})
    except:
        continue
    product_name=browser.find_element(By.ID,"pr-headline").text.split("\n")[0]
    product_image=browser.find_element(By.CSS_SELECTOR,".pr-pictures__main > img:nth-child(1)").get_attribute('src')
    Product_description=browser.find_element(By.CSS_SELECTOR,"#pr-short-description").text
    csv_writer.writerow([product_image,product_name,sku,Product_description,dic])
    dic.clear()                                            
    browser.back()
    # browser.implicitly_wait(200)
    # browser.find_element(By.CSS_SELECTOR,f"nav.se-result-list-navigation:nth-child(2) > div:nth-child(2) > ul:nth-child(2) > li:nth-child({page}) > span:nth-child(1) > a:nth-child(1)").click()
    
    



    


