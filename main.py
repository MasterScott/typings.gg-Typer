from time import time, sleep
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging']) # Disables printing to console.
driver = webdriver.Chrome(options = options)

driver.get('https://typings.gg/')
sleep(0.3)
words = driver.find_element_by_id('text-display').text

start = time()
for word in words:
    driver.find_element_by_id('input-field').send_keys(word)
stop = time()

elapsed = stop - start
results = driver.find_element_by_id('right-wing').text
print('> Finished.\n\n%s\nELAPSED TIME: %s s' % (results.replace(' / ', '\n'), round(elapsed, 2)))
