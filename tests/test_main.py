"""
Delawere 2023
"""

from selenium.webdriver.common.by import By

URL = "https://test.qa.studio"
def test_smoke(browser):
    """
    SMK-1 smoke test
    """

    browser.get(URL)

    element = browser.find_element(by=By.CSS_SELECTOR, value="[class='tab-featured ']")
    element.click()

    

    x_path_table = '//*[@id="rz-shop-content"]/ul/li[1]/div/div[2]/h2/a'
    element = browser.find_element(By.XPATH, value=x_path_table)
    element.click()

    sku = browser.find_element(By.CLASS_NAME, value="sku")
    assert sku.text == 'C0MSSDSUM7', "Unexpected sku"
    
    print('OK') 