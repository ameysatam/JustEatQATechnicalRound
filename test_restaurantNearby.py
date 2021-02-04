from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
import re
import time


driver = webdriver.Chrome("chromedriver.exe")
base_url = "https://www.just-eat.co.uk/"

#The user maximizes the window
driver.maximize_window()

#The user inputs the url above into Chrome web browser
driver.get(base_url)

postalCode = "AR51 1AA"
searchBox = driver.find_element_by_xpath("//input[@name='postcode']")

#The user inputs the postal code AR51 1AA in the search box
searchBox.send_keys(postalCode)
searchButton = driver.find_element_by_xpath("//span[contains(text(),'Search')]")

#The user clicks on the Search Button
searchButton.click()

sortedByHover = driver.find_element_by_xpath("//span[contains(text(),'Sorted by')]")
actions = ActionChains(driver)
actions.move_to_element(sortedByHover).perform()
sortByDistance = driver.find_element_by_xpath("//input[@id='Distance']")

#The user wants to sort the restaurant by distance, hence he selects Distance after hovering the mouse
#over the sorting option
driver.execute_script("arguments[0].click();", sortByDistance)

#Here, the browser is waiting for the page to reload
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Filters')]")))

#Here, for the purpose of looping through each and every result for postal code,
#The total number of search results are found
searchCountText = driver.find_element_by_xpath("//span[@data-search-count='openrestaurants']").text
temp = re.findall(r'\d+', searchCountText)
res = list(map(int, temp))
searchCount = res[0]
print("Search count = " + str(searchCount))

#This is done for my curosity and if I were to loop over all the results in the page,
#I am finding out total number of results after sorting by default
allResultsInThePage = driver.find_elements_by_xpath("//div[@data-search-container='openrestaurants']/div")
print("Search result in the page = " + str(len(allResultsInThePage)))

#Here I initiated the total number of postal code matches as zero
countPostalCodeMatch = 0

#I wanted to perform the test for all the search results, but the number of
#search results is too large and thus would have taken time
# for i in range(searchCount)

#I chose 5 for demonstration purpose
for i in range(5):
#Here, the user tries to find all the restaurant matching their postal code
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Filters')]")))
    ithResult = driver.find_element_by_xpath("//div[@data-search-container='openrestaurants']/div[" +str(i+1) +"]//h3")
    driver.execute_script("arguments[0].scrollIntoView();", ithResult)
    ithResult.click()
    ithResultAddress = driver.find_element_by_xpath("//span[@data-test-id='header-restaurantAddress']").text
    if postalCode in str(ithResultAddress):
        print("The area code MATCHES with the area code searched for!")
        countPostalCodeMatch = countPostalCodeMatch + 1
    else:
        print("The area code DOES NOT MATCH with the area code searched for!")
    driver.back()


#Here, the total number of search result restaurant matching the users postal code are found from
#the above for loop
print("Total restaurant addresses matching with user postal code out of 5 = "+ str(countPostalCodeMatch))
driver.quit()





