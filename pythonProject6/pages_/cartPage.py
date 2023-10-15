from selenium.webdriver.common.by import By
class CartPage():
    def __init__(self, driver):
        self.driver = driver

    def delete_firtsProdoct_from_cart(self):
        firstProductDelectButtonElement = self.driver.find_element(By.XPATH, "(\\input[@value='Delete'])[1]")
        firstProductDelectButtonElement.click()