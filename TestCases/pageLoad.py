from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

logging.basicConfig(filename='../Logs/PageLoadTime.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info("Loading page on #CHROME Browser")
url = "https://ibpodev.home.tatamotors/edukaan_ui/#/"

start_time = time.time()

driver = webdriver.Chrome()

driver.get(url)

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
logging.info("Locating BODY of the page")

logging.info("Calculating Page Load Time\n")
end_time = time.time()
load_time = end_time - start_time
logging.info(f'Page load time {load_time} seconds\n')

logging.info("Scrolling through page height\n")
page_size = driver.execute_script("return document.body.scrollHeight")
speed = page_size / load_time
logging.info(f'Page speed: {speed} bytes/second\n')

driver.quit()


print("TC1 EXECUTION COMPLETE")


browser = webdriver.Chrome()
logging.info("Executing tests to check performance time\n")
browser.get('https://ibpodev.home.tatamotors/edukaan_ui/#/')


start_time = time.time()

browser.execute_script('return window.performance.timing.loadEventEnd;')

end_time = time.time()

load_time = (end_time - start_time) * 1000

logging.info(f'Page loaded in {load_time} ms')

speed = (len(browser.page_source.encode('utf-8')) / load_time) / 1024

logging.info(f'Page load speed: {speed} KB/s\n')

browser.quit() 

print("TC2 EXECUTION COMPLETE")

'''RUNNING REGRESSION TESTS TO DETERMINE AVERAGE LOAD TIME'''


num_requests = 10
logging.info(f'Running regression tests for {num_requests} repetition\n')

start_time = time.time()

driver = webdriver.Chrome()

for i in range(num_requests):

    driver.get(url)

    time.sleep(1)


end_time = time.time()

average_load_time = (end_time - start_time) / num_requests

logging.info(f'Number of requests: {num_requests}')
logging.info(f'Total load time:  {end_time - start_time}  seconds')
logging.info(f'Average load time per request: {average_load_time}  seconds')

driver.quit()

print("TC3 EXECUTION COMPLETE")