import os
import configparser
from selenium import webdriver
from selenium.webdriver import ChromeOptions


def get_url():
    config = configparser.ConfigParser()
    config.read('config.properties')
    url = (config.get('Application', 'url'))
    return url


def initialize_webdriver():
    path_parent = os.path.dirname(os.getcwd())
    os.chdir(path_parent)
    current_directory = os.getcwd()
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option("detach", True)
    print(current_directory+'\\Drivers\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, executable_path=current_directory + '\\Drivers\\chromedriver.exe')
    return driver
