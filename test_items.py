from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_page_contains_add_to_basket_button(browser):
    browser.get(link)
    add_to_basket_button = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
    assert EC.presence_of_element_located(add_to_basket_button), 'add to basket button is not on the page'
