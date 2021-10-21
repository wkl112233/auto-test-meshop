import time

import allure

import pages
from pages.pagebase import PageBase


class PageFreightMinix:
    """
    运费页面
    """
    def freight(self):
        if not getattr(self, '_freight', None):
            self._freight = PageFreight(self.driver)
        return self._freight


class PageFreight(PageBase):
    @allure.step("操作:点击选择 免运费 ")
    def click_free(self):
        """
        点击选择免费
        """
        self.driver.execute_script("$('div[data-id=\"3\"]>div>div>input').click()")

    @allure.step("操作:点击选择 小包 ")
    def click_small_package(self):
        self.driver.execute_script("$('div[data-id=\"1\"]>div>div>input').click()")

    @allure.step("操作:点击选择 大包 ")
    def click_huge_package(self):
        """
        点击选择大包
        """
        self.click(pages.shop.huge_package)

    @allure.step("点击去支付页 ")
    def click_goto_payment(self):
        self.driver.execute_script("$('#continue_button').click()")

    def get_shipping(self):
        """
        获取运费金额
        :return:text
        """
        return self.text(pages.shop.shipping)

    def get_contacts(self):
        """
        获取付款用户邮箱
        :return:email
        """
        return self.text(pages.shop.sure_email)

    def get_contacts_address(self):
        """
        获取用户地址
        :return:text
        """
        return self.text(pages.shop.sure_address)

    def select_freight(self):
        """
        选择运费业务
        """
        # self.click_huge_package()
        # time.sleep(2)
        self.click_free()
        time.sleep(2)
        self.click_goto_payment()
