import time
from selenium.webdriver.common.by import By
from pages.pagebase import PageBase


class PageApplicationManageMinix:
    def application_manage(self):
        if not getattr(self, '_add_product', None):
            self._application_manage = PageApplicationManage(self.driver)
        return self._application_manage


class PageApplicationManage(PageBase):
    """
    应用管理页
    """

    # 获取应用名称
    def get_application_name(self):
        return self.text((By.CSS_SELECTOR, 'div[class="title"]>div>span'))

    # 安装色卡应用
    def add_application(self):
        self.click((By.XPATH, '//*[text()="应用市场"]'))
        time.sleep(2)
        self.click_find_element((By.CSS_SELECTOR, '#pane-1>div>div:nth-child(2)>div>div>div>div>div>div:nth-child(1)'))
        time.sleep(2)
        self.click_find_element((By.XPATH, '//*[text()="安装"]'))
        time.sleep(2)
        self.click((By.XPATH, '//*[text()="同意"]'))

    # 卸载色卡应用
    def uninstall_application(self):
        self.click((By.CSS_SELECTOR, 'button[class="el-button el-button--text delete"]'))
        time.sleep(2)
        self.click((By.CSS_SELECTOR, 'button[class="el-button el-button--danger"]'))
        time.sleep(2)
        return self.base_if_text_exists_element('色卡')
