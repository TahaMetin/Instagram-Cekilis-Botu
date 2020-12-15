from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import InstagramBot

bot = InstagramBot.InstagramBot('yildiznisaaa', 'instagramçekiliş')
bot.signIn()

bot.browser.get('https://www.instagram.com/cagritaner/')
max = 1000
followingsLink = bot.browser.find_elements_by_css_selector('ul li a')[0]
followingsLink.click()
time.sleep(2)
followingsList = bot.browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
numberOfFollowingsInList = len(followingsList.find_elements_by_css_selector('li'))
followingsList.click()
time.sleep(2)
actionChain = webdriver.ActionChains(bot.browser)
while numberOfFollowingsInList < max:
    bot.browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]').click()
    actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
    numberOfFollowingsInList = len(followingsList.find_elements_by_css_selector('li'))
    time.sleep(2)
    print(numberOfFollowingsInList)

followings = []
for user in followingsList.find_elements_by_css_selector('li'):
    userLink = user.find_element_by_css_selector('a').get_attribute('href')
    print(userLink)
    followings.append(userLink)
    if len(followings) == max:
        break

for follower in followings:
    follower = follower.split('/')
    print('"' + follower[3], end='", ')
