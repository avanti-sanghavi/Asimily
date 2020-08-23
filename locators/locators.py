from selenium.webdriver.common.by import By


class FilterLocators(object):
    type_filter = (By.XPATH, '//*[@id="typeFilter"]/select')
    manufacturer_filter = (By.XPATH, '//*[@id="manufacturerFilter"]/select')
    os_filter = (By.XPATH, '//*[@id="osFilter"]/select')
    department_filter = (By.XPATH, '//*[@id="osFilter"]/select')
    device_map = (By.CSS_SELECTOR, '#mapContainer > g:nth-child(3)')
    manufacturer = (By.XPATH, '//*[@id="manufacturerFilter"]/select')
