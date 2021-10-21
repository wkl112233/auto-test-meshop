import os

from selenium import webdriver

from config import BASE_DIR


class GetDriver:
    __web_driver = None

    """
    获取web driver 
    """

    @classmethod
    def get_web_driver(cls, url):
        if cls.__web_driver is None:
            # 获取浏览器对象
            options = webdriver.ChromeOptions()
            # options.add_argument('headless')
            # options.add_argument('window-size=1200x600')
            cls.__web_driver = webdriver.Chrome(os.path.join(BASE_DIR, 'chromedriver'), chrome_options=options)
            # 最大化
            cls.__web_driver.maximize_window()
            # 打开url
            cls.__web_driver.get(url)
        # 返drive
        return cls.__web_driver

    """
    关闭web driver
    """

    @classmethod
    def close_web_driver(cls):
        if cls.__web_driver:
            cls.__web_driver.quit()
            # 置空操作
            cls.__web_driver = None
