# time.sleep(random.randint(5,10))
#
# driver.find_element(By.ID, "login").send_keys(username)
# time.sleep(random.randint(2,6))
#
# driver.find_element(By.ID, "password").send_keys(password)
# time.sleep(random.randint(2,4))
#
# driver.find_element(By.CLASS_NAME, "butred").click()
# time.sleep(random.randint(2,15))
#
# driver.find_element(By.HREF, "/authors.asp").click()

# el1 = driver.find_element(By.NAME, "a-1oggnlvchg6q")
# ActionChains(driver).move_to_element(el1).perform()
# time.sleep(2)
# el2 =
# ActionChains(driver).move_to_element(el2).perform()
# el2.click()
# time.sleep(3)
# wait = WebDriverWait(driver, 20)
# wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='reCAPTCHA']")))
# below line will click on the checkbox next to 'I'm not a robot'
# wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
# driver.find_element(By.ID, "recaptcha-demo-submit").click()
# time.sleep(50)
#
# driver.find_element(By.XPATH, "//input[@id='recaptcha-demo-submit']").click()
# el2 = driver.find_element(By.ID, "a636222")
# ActionChains(driver).move_to_element(el2).perform()
#
# time.sleep(20)


# driver.find_element("name", "username").send_keys(username)
# driver.find_element("name", "password").send_keys(password)
#
# driver.find_element(By.CSS_SELECTOR, "input[type=\"submit\" i]").click()
# time.sleep(20)