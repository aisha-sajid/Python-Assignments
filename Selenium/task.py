from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert as alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://margaret:hamilton@studio.stage.edx.org/")
wait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "li.nav-item:nth-child(3)")))

#go to sign in page
sign_in = driver.find_element_by_css_selector("li.nav-item:nth-child(3)")
builder = ActionChains(driver)
builder.click(sign_in).perform()


wait(driver, 20).until(EC.presence_of_element_located((By.ID, "email")))

#go to course list page
username = driver.find_element_by_id('email')
password = driver.find_element_by_id('password')
button = driver.find_element_by_css_selector("#submit")

builder = ActionChains(driver)
builder.send_keys_to_element(username,'rchachar@edx.org')
builder.send_keys_to_element(password,'raees')
builder.click(button)
builder.perform()

course = wait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//li[@data-course-key='course-v1:ColumbiaX+AP123+2017_T2']")))
course.click();

#go to course page
wait(driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.outline-content.course-content")))

#add section
new_section_button = driver.find_element_by_xpath("//li[@class='nav-item'][1]/a[@class='button button-new']")

builder = ActionChains(driver)
builder.move_to_element(new_section_button)
builder.double_click(new_section_button)
builder.perform()
wait(driver,50)

course_content = driver.find_element_by_css_selector("ol.list-sections")

sections = course_content.find_elements_by_class_name('outline-section')
no_of_sections = len(sections)

section_name = sections[no_of_sections-1]
section_name.find_element_by_css_selector('a.action-edit.action-inline.xblock-field-value-edit.incontext-editor-open-action')
wait(driver,30)

builder = ActionChains(driver)
builder.click(section_name)
builder.perform()

driver.close()
