import json
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep as t

f = open("c:/showdown/data.json")
data = json.load(f)

driver = webdriver.Chrome()
driver.get(data['siteData'][0]['url'])

elem = WebDriverWait(driver, 200).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, data['siteData'][0]['nameBtn'])) #This is a dummy element
)

elem = WebDriverWait(driver, 200).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, data['siteData'][0]['nameBtn']))
)

elem = driver.find_element(By.CSS_SELECTOR, data['siteData'][0]['nameBtn']).click()
elem = WebDriverWait(driver, 100).until(
EC.presence_of_element_located((By.CSS_SELECTOR, data['siteData'][0]['nameInput'])) #This is a dummy element
)
elem = driver.find_element(By.CSS_SELECTOR, data['siteData'][0]['nameInput']).send_keys(data['siteData'][0]['name'])
elem = driver.find_element(By.CSS_SELECTOR, data['siteData'][0]['chooseBtn']).click()

elem = driver.find_element(By.CSS_SELECTOR, data['siteData'][0]['teamBtn']).click()
elem = driver.find_element(By.CSS_SELECTOR, data['siteData'][0]['newTeamBtn']).click()
elem = driver.find_element(By.CSS_SELECTOR, data['siteData'][0]['formatBtn']).click()
elem = driver.find_element(By.CSS_SELECTOR, data['siteData'][0]['Gen7OUBtn']).click()
elem = driver.find_element(By.CSS_SELECTOR, data['siteData'][0]['addPokemonBtn']).click()

for pokemonIndex in range(1,7):
    enter = Keys.ENTER
    elem = driver.find_element(By.CSS_SELECTOR, data['siteData'][0]['pokeInput']).send_keys(data['siteData'][pokemonIndex]['name'],enter,data['siteData'][pokemonIndex]['item'],enter,data['siteData'][pokemonIndex]['ability'],enter,data['siteData'][pokemonIndex]['move01'],enter,data['siteData'][pokemonIndex]['move02'],enter,data['siteData'][pokemonIndex]['move03'],enter,data['siteData'][1]['move04'],enter)
    enter = Keys.TAB
    elem = driver.find_element(By.CSS_SELECTOR, data['siteData'][0]['HPInput']).send_keys(data['siteData'][pokemonIndex]['HP'],enter,data['siteData'][pokemonIndex]['atk'],enter,data['siteData'][pokemonIndex]['def'],enter,data['siteData'][pokemonIndex]['spAtk'],enter,data['siteData'][pokemonIndex]['spDef'],enter,data['siteData'][pokemonIndex]['spd'])
    match(pokemonIndex):
        case 1:
            elem = driver.find_element(By.CSS_SELECTOR, data['siteData'][0]['nextBtn']).click()
        case 2:
            elem = driver.find_element(By.CSS_SELECTOR, data['siteData'][0]['nextBtn2']).click()
        case 3:
            elem = driver.find_element(By.CSS_SELECTOR, data['siteData'][0]['nextBtn3']).click()
        case 4:
            elem = driver.find_element(By.CSS_SELECTOR, data['siteData'][0]['nextBtn4']).click()
        case 5:
            elem = driver.find_element(By.CSS_SELECTOR, data['siteData'][0]['nextBtn5']).click()



elem = driver.find_element(By.CSS_SELECTOR, data['siteData'][0]['backBtn']).click()
elem = driver.find_element(By.CSS_SELECTOR, data['siteData'][0]['backBtn']).click()





t(10)


