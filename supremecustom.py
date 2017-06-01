from selenium import webdriver
import time
import pickle
import datetime
def getCurrentTime():
    return time.strftime("%H:%M:%S")
print ("{} Starting Supreme Script".format(getCurrentTime()))
#########################################
IP         = ''#IP:PORT
url        = 'http://www.supremenewyork.com/shop/new'
Fullname   = ''
email      = ''
phone      = ''
address    = ''
zipcode    = ''
city       = ''
cardtype   = 'Visa'#Ex Visa,AmericanExpress,Mastercard
creditcard = ''
ExpMonth   = ''#Ex 01,02,03,04,05
ExpYear    = ''#Ex 2017, 2018,2019
cvv        = ''
###########################################
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server='+IP)
driver = webdriver.Chrome(chrome_options=chrome_options)
print("{} Using Proxy".format(getCurrentTime()),IP)
driver.get(url)
#Size Selection 
while True:
    try:
        try:
            driver.find_element_by_xpath("""//*[@id="size"]/option[3]""").click()#small
            print ("{} Size Large Selected!!".format(getCurrentTime()))
            break
        except Exception:
            driver.find_element_by_xpath("""//*[@id="size"]/option[2]""").click()#medium
            print ("{} Size Medium Selected!!".format(getCurrentTime()))
            break
        except Exception:
            driver.find_element_by_xpath("""//*[@id="size"]/option[1]""").click()#large
            print ("{} Size Small Selected!!".format(getCurrentTime()))
            break
        except Exception:
            driver.find_element_by_id("""//*[@id="add-remove-buttons"]/input""").click()
            print ("{} ONESIZE Selected!!".format(getCurrentTime()))
            break
    except Exception as E:
        ''
time.sleep(.001)        
driver.find_element_by_xpath("""//*[@id="add-remove-buttons"]/input""").click()    
print("{} Added To Cart".format(getCurrentTime()))    
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
time.sleep(1)
driver.get("https://www.supremenewyork.com/checkout")
print ("{} Submitting Info...".format(getCurrentTime()))
#Info
driver.find_element_by_xpath("""//*[@id="order_billing_name"]""").send_keys(Fullname)#FULL NAME
driver.find_element_by_xpath("""//*[@id="order_email"]""").send_keys(email)#EMAIL
driver.find_element_by_xpath("""//*[@id="order_tel"]""").send_keys("       "+phone)#PHONE
driver.find_element_by_xpath("""//*[@id="bo"]""").send_keys(address)#ADDRESS
driver.find_element_by_xpath("""//*[@id="order_billing_zip"]""").send_keys(zipcode)#ZIP CODE
driver.find_element_by_xpath("""//*[@id="order_billing_city"]""").send_keys(city)#CITY
time.sleep(.2)
#cardtype
if cardtype == 'Visa':
	driver.find_element_by_xpath("""//*[@id="credit_card_type"]/option[1]""").click()
elif cardtype == 'AmericanExpress':
	driver.find_element_by_xpath("""//*[@id="credit_card_type"]/option[2]""").click()
elif cardtype == 'Mastercard':
	driver.find_element_by_xpath("""//*[@id="credit_card_type"]/option[3]""").click()
driver.find_element_by_xpath("""//*[@id="cnb"]""").send_keys("        "+creditcard)
print ("{} Transaction Process With".format(getCurrentTime()),cardtype)
#cardmonth
if ExpMonth ==   '01':
	driver.find_element_by_xpath("""//*[@id="credit_card_month"]/option[1]""").click()
elif ExpMonth == '02':
	driver.find_element_by_xpath("""//*[@id="credit_card_month"]/option[2]""").click()
elif ExpMonth == '03':
	driver.find_element_by_xpath("""//*[@id="credit_card_month"]/option[3]""").click()
elif ExpMonth == '04':
	driver.find_element_by_xpath("""//*[@id="credit_card_month"]/option[4]""").click()
elif ExpMonth == '05':
	driver.find_element_by_xpath("""//*[@id="credit_card_month"]/option[5]""").click()
elif ExpMonth == '06':
	driver.find_element_by_xpath("""//*[@id="credit_card_month"]/option[6]""").click()
elif ExpMonth == '07':
	driver.find_element_by_xpath("""//*[@id="credit_card_month"]/option[7]""").click()
elif ExpMonth == '08':
	driver.find_element_by_xpath("""//*[@id="credit_card_month"]/option[8]""").click()
elif ExpMonth == '09':
	driver.find_element_by_xpath("""//*[@id="credit_card_month"]/option[9]""").click()
elif ExpMonth == '10':
	driver.find_element_by_xpath("""//*[@id="credit_card_month"]/option[10]""").click()
elif ExpMonth == '11':
	driver.find_element_by_xpath("""//*[@id="credit_card_month"]/option[11]""").click()
elif ExpMonth == '12':
	driver.find_element_by_xpath("""//*[@id="credit_card_month"]/option[12]""").click()

#ExYear
if ExpYear ==   '2017':
	driver.find_element_by_xpath("""//*[@id="credit_card_year"]/option[1]""").click()
elif ExpYear == '2018':
	driver.find_element_by_xpath("""//*[@id="credit_card_year"]/option[2]""").click()
elif ExpYear == '2019':
	driver.find_element_by_xpath("""//*[@id="credit_card_year"]/option[3]""").click()
elif ExpYear == '2020':
	driver.find_element_by_xpath("""//*[@id="credit_card_year"]/option[4]""").click()
elif ExpYear == '2021':
	driver.find_element_by_xpath("""//*[@id="credit_card_year"]/option[5]""").click()
elif ExpYear == '2022':
	driver.find_element_by_xpath("""//*[@id="credit_card_year"]/option[6]""").click()
elif ExpYear == '2023':
	driver.find_element_by_xpath("""//*[@id="credit_card_year"]/option[7]""").click()
elif ExpYear == '2024':
	driver.find_element_by_xpath("""//*[@id="credit_card_year"]/option[8]""").click()
elif ExpYear == '2025':
	driver.find_element_by_xpath("""//*[@id="credit_card_year"]/option[9]""").click()

while True:
    try:
        try:
            driver.find_element_by_xpath("""//*[@id="vval"]""").send_keys(cvv)#CVV
            break 
        except Exception:
            driver.find_element_by_xpath("""//*[@id="cvw"]""").send_keys(cvv)
            break 
    except Exception as E:
        ''
driver.find_element_by_xpath("""//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins""").click()
driver.find_element_by_xpath("""//*[@id="pay"]/input""").click()
print ("{} Info Submited, Solve Captcha!".format(getCurrentTime()))   
time.sleep(120)    
driver.quit()
