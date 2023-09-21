from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12 * math.sin(int(x)))))

try:
  
  link = "http://suninjuly.github.io/explicit_wait2.html"
  browser = webdriver.Chrome()
  browser.get(link)

  # das Warten, sobald der Preis auf $100 sinkt (das Warten soll mindestens 12 Sekunden sein)
  WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))

  # Tippen auf den Button "Book"
  button_book = browser.find_element(By.ID, "book")
  button_book.click()

  x_element = browser.find_element(By.ID, 'input_value')
  x = x_element.text  # Lesen den Wert für die Variable "x" ab
  y = calc(x)  # Berechnen die mathematische Funktion von "x"

  # Das Ergebnis der Funktion in das Data Input Field eintragen
  result = browser.find_element(By.ID, "answer")
  result.send_keys(y)

  # Tippen auf den Button "Submit"
  button = browser.find_element(By.ID, "solve")
  button.click()

finally:
  time.sleep(5)
  browser.quit()