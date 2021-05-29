from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import pytchat

braveLocation = 'C:\Program Files\BraveSoftware\Brave-Browser\Application\Brave.exe'
driverPath = 'C:\Program Files (x86)\webDriver\chromedriver.exe' #path location of webDriver
webName = 'http://www.higherlowergame.com/'
#Xpath of different buttons
startClassic = '//*[@id="root"]/div/span/section/div[2]/div/button[1]'
higher = '//*[@id="root"]/div/span/span/div/div[2]/div[2]/button[1]'
lower = '//*[@id="root"]/div/span/span/div/div[2]/div[2]/button[2]'
playAgain = '//*[@id="game-over-btn"]'
videoURL = 'LS8kdhLxew0' #live Video URL

# For brave browser
# options = Options()
# options.binary_location = braveLocation
# driver = webdriver.Chrome(options=options, executable_path=driverPath)
# driver.get(webName)
# time.sleep(10)

# For chrome browser
# driver = webdriver.Chrome(driverPath)
# driver.get(webName)
# time.sleep(10)


def startPress():
    startButton = driver.find_element_by_xpath(startClassic)
    startButton.click()


def highPress():
    highButton = driver.find_element_by_xpath(higher)
    highButton.click()


def lowPress():
    lowButton = driver.find_element_by_xpath(lower)
    lowButton.click()


def againPress():
    playAgainButton = driver.find_element_by_xpath(playAgain)
    playAgainButton.click()


def getVote():
    high, low = 0, 0
    lastVote = ''
    chat = pytchat.create(video_id=videoURL)
    t_end = time.time() + 30
    while time.time() < t_end:
        for c in chat.get().sync_items():
            message = (c.message).casefold()
            print(message)
            if message == 'high' or message == 'higher':
                high += 1
                lastVote = 'H'
            elif message == 'low' or message == 'lower':
                low += 1
                lastVote = 'L'
            else:
                continue
    return high, low, lastVote


startPress()
while True:
    try:
        try:
            tempButton = driver.find_element_by_xpath(higher)
            voteH, voteL, lastV = getVote()
            if voteH > voteL:
                highPress()
            elif voteL > voteH:
                lowPress()
            else:
                if lastV == 'H':
                    highPress()
                else:
                    lowPress()
        except:
            againPress()
    except:
        continue

