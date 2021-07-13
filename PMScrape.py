from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time
import json
driver = webdriver.Firefox()
AllPMs = []
FullPMs = []
def removedeletelinks(d):
    if "delete" in d:
        return False
    else:
        return True
def PMscrape():
    username = input("Input your username: ")
    password = input("Input your password: ")
    driver.get("https://deskthority.net")
    login = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/ul/li[1]/a")
    login.click()
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    time.sleep(.8)
    loginbutton = driver.find_element_by_xpath("/html/body/div[1]/div[2]/form/div[1]/div/div/fieldset/dl[4]/dd/input[3]")
    loginbutton.click()
    PMbutton = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/ul/li[2]/a")
    PMbutton.click()
    pagecount = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[2]/form/div[1]/div/div[2]/div[2]/ul/li[8]/a").text
    for i in range(1,int(pagecount)): 
        Messages = driver.find_elements_by_class_name('topictitle')
        for Message in Messages:
            AllPMs.append(Message.get_attribute("href"))
        driver.find_element_by_xpath("//a[contains(@rel,'next')]").click()
AllPMs = list(filter(removedeletelinks, AllPMs))
AllMessages = {}
def MessageGrab():
    for i in AllPMs:
        driver.get(i)
        try:
            PMTitle = driver.find_element_by_css_selector(".first").text
        except:
            continue
        PMInfo = driver.find_element_by_css_selector("div.postbody:nth-child(2) > p:nth-child(3)").text
        PMBody = driver.find_element_by_css_selector("div.postbody:nth-child(2) > div:nth-child(4)").text
        PMTitle = PMTitle.replace("Re:","")
        PMInfo = PMInfo.replace("From:","")
        PMInfo = PMInfo.replace("Sent:","")
        PMInfo = PMInfo.split("\n")
        PMInfo.pop()
        if len(PMInfo) < 2:
            PMInfo2 = driver.find_element_by_css_selector("a.username:nth-child(4)").text
            PMInfo.append(PMInfo2)
        AllMessages[i] = {}
        AllMessages[i]["Title"] = PMTitle
        AllMessages[i]["Date"] = PMInfo[0]
        AllMessages[i]["Sender"] = PMInfo[1]
        AllMessages[i]["Message"] = PMBody
    PM_database = json.dumps(AllMessages)
    f = open("Messages.json", "w")
    f.write(PM_database)
    f.close()
        
PMscrape()
MessageGrab()


