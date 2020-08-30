from selenium import webdriver
driver= webdriver.Chrome('C:/Users/Karthik Naidu/Downloads/chromedriver')
driver.get("https://web.whatsapp.com/")
driver.maximize_window()
name= input("contact").split()
msg=input("message to be sent")
input("enter anything after scan QR code")
for i in name:
    user= driver.find_element_by_xpath("//span[@title='{}']".format(i))
    user.click()
    message_box=driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
    message_box.send_keys(msg)
    driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()
'''//span[@title="test"]
//*[@id="main"]/footer/div[1]/div[2]/div/div[2]
//*[@id="main"]/footer/div[1]/div[1]/div[3]/button
//*[@id="main"]/footer/div[1]/div[3]/button
//*[@id="main"]/footer/div[1]/div[3]/button'''
