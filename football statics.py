from selenium.webdriver.common.by import By
from utils import start_driver
from selenium.webdriver.support.ui import Select
import time
import pandas as pd 

driver = start_driver()
driver.get('https://www.adamchoi.co.uk/teamgoals/detailed')
element = driver.find_element(By.XPATH, "//label[contains(text(), 'All matches')]")
element.click()
dropdown=Select(driver.find_element(By.ID,'country'))
dropdown.select_by_visible_text('Spain')
time.sleep(5)


matches_table=driver.find_elements(By.TAG_NAME,'tr')

date=[]
home_team=[]
score=[]
away_team=[]

for match in matches_table :
    date.append(match.find_element(By.XPATH,'./td[1]').text)
    home=match.find_element(By.XPATH,'./td[3]').text
    home_team.append(home)
    print(home)
    score.append(match.find_element(By.XPATH,'./td[4]').text)
    away_team.append(match.find_element(By.XPATH,'./td[5]').text)


time.sleep(5)
driver.quit()

df=pd.DataFrame({'Date':date,'Home Team':home_team,'Score':score,'Away Team':away_team})
df.to_excel('football_data.xlsx',index=False)
print(df)