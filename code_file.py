from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pandas as pd

# imported required libraries

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opstra.definedge.com/")
login = driver.find_element(By.XPATH, '//div/button[@class="v-btn v-btn--flat theme--dark"]')
login.click()

# opened the opstra website
# clicked on login button

email = driver.find_element(By.ID, value="username")
email.send_keys('priyanshukamde22@gmail.com')
password = driver.find_element(By.ID, value="password")
password.send_keys('unacademy22')

# send login keys

login = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.ID, "kc-login")))
login.click()

# login into website

el = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//div[@class="v-menu v-menu--inline"][3]')))
el.click()
element1 = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//div[@style="height: 40px;"][9]')))
element1.click()

# clicked on open interest and then on option chain

dropdown1 = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//div[@class="flex xs12 md4 ml-3"][2]')))
dropdown1.click()
dropdown = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//div/div[@role="listitem"][1]')))
dropdown.click()

# selected the date for nifty

time.sleep(5)
data1 = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, '//table[@id="grid_2033181033_0_content_table"]/tbody/tr')))

# made an element storage data1 to store tr element

OIChangeC = []
OIC = []
VolumeC = []
ITMProbC = []
IVC = []
LTPC = []
CHANGEC = []
STRIKE = []
CHANGEP = []
LTPP = []
IVP = []
ITMProbP = []
VolumeP = []
OIP = []
OIChangeP = []

# made lists for the dataframe df

time.sleep(5)

for data in data1:
    OIChangeC.append(data.find_element(By.XPATH, './td[1]').text)
    OIC.append(data.find_element(By.XPATH, './td[2]').text)
    VolumeC.append(data.find_element(By.XPATH, './td[3]').text)
    ITMProbC.append(data.find_element(By.XPATH, './td[4]').text)
    IVC.append(data.find_element(By.XPATH, './td[5]').text)
    LTPC.append(data.find_element(By.XPATH, './td[6]').text)
    CHANGEC.append(data.find_element(By.XPATH, './td[7]').text)
    STRIKE.append(data.find_element(By.XPATH, './td[8]').text)
    CHANGEP.append(data.find_element(By.XPATH, './td[9]').text)
    LTPP.append(data.find_element(By.XPATH, './td[10]').text)
    IVP.append(data.find_element(By.XPATH, './td[11]').text)
    ITMProbP.append(data.find_element(By.XPATH, './td[12]').text)
    VolumeP.append(data.find_element(By.XPATH, './td[13]').text)
    OIP.append(data.find_element(By.XPATH, './td[14]').text)
    OIChangeP.append(data.find_element(By.XPATH, './td[15]').text)

# iterated along data1 to store specific td element along specific list

df = pd.DataFrame({'OI_Change_C': OIChangeC, 'OI_C': OIC, 'Volume_C': VolumeC,
                   'ITM_Prob_C': ITMProbC, 'IV_C': IVC, 'LTP_C': LTPC, 'CHANGE_C': CHANGEC, 'STRIKE': STRIKE,
                   'CHANGE_P': CHANGEP, 'LTP_P': LTPP, 'IV_P': IVP, 'ITM_Prob_P': ITMProbP, 'Volume_P': VolumeP,
                   'OI_P': OIP, 'OI_Change_P': OIChangeP, })

# made a dataframe to store the scrapped data

df.to_csv('option_change.csv', index=False)
# converted the dataframe to a csv file named option_change

