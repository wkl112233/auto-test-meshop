import time

import allure

import pages
from pages.pagebase import PageBase


class ShopMyCenterMinix:
    """
    前台个人中心页
    """

    def my_center(self):
        if not getattr(self, '_my_center', None):
            self._my_center = ShopMyCenter(self.driver)
        return self._my_center


class ShopMyCenter(PageBase):
    def input_email(self, email):
        with allure.step("操作：输入登录邮箱"):
            allure.attach('{}'.format(email), name="输入 {}".format(email))
        self.input(pages.shop.email, email)

    def input_password(self, password):
        with allure.step("操作：输入登录密码"):
            allure.attach('{}'.format(password), name="输入 {}".format(password))
        self.input(pages.shop.password, password)

    @allure.step("操作:登录")
    def click_login_btn(self):
        self.click(pages.shop.login_btn)

    def get_nickname(self):
        """
        获取用户昵称
        """
        return self.text(pages.shop.nickname)

    @allure.step("操作:点击个人中心注册按钮")
    def click_register_page(self):
        self.click(pages.shop.register_page)

    def get_prompt_message(self):
        """
        获取提示信息
        """
        return self.text(pages.shop.tips)

    def input_first_name(self, first_name):
        with allure.step("操作：输入注册人fist name"):
            allure.attach('{}'.format(first_name), name="输入 {}".format(first_name))
        self.input(pages.shop.first_name, first_name)

    def input_last_name(self, last_name):
        with allure.step("操作：输入注册人last_name"):
            allure.attach('{}'.format(last_name), name="输入 {}".format(last_name))
        self.input(pages.shop.last_name, last_name)

    @allure.step("操作:点击注册")
    def click_login_register(self):
        self.click(pages.shop.register_btn)

    @allure.step("操作:退出当前登录账号")
    def click_logout(self):
        self.click(pages.shop.logout)

    """
    组合业务方法（前台用户登录）
    """

    def login(self, email, password):
        self.logger.info("正在调用登录组合业务方法，邮箱：{} 密码：{}".format(email, password))
        self.input_email(email)
        time.sleep(1)
        self.input_password(password)
        time.sleep(1)
        self.click_login_btn()

    """
    组合业务方法（前台用户登录成功）
    """

    def login_success(self, email="jinpeng@meshop.com", password="123456"):
        self.logger.info("正在调用登录组合业务方法，邮箱：{} 密码：{}".format(email, password))
        self.input_email(email)
        time.sleep(1)
        self.input_password(password)
        time.sleep(1)
        self.click_login_btn()

    """
    组合业务方法（前台用户注册）
    """

    def logon_register(self, first_name, last_name, email, password):
        self.logger.info("正在调用注册组合业务方法，名：{} 姓：{} 邮箱：{} 密码：{}".format(first_name, last_name, email, password))
        self.input_first_name(first_name)
        time.sleep(1)
        self.input_last_name(last_name)
        time.sleep(1)
        self.input_email(email)
        time.sleep(1)
        self.input_password(password)
        time.sleep(1)
        self.click_login_register()
