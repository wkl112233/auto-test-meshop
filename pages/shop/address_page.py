import time

import allure
from selenium.webdriver.support.select import Select

import pages
from pages.pagebase import PageBase


class PageAddressMinix:
    """
    地址页
    """

    def address(self):
        if not getattr(self, '_address', None):
            self._address = PageAddress(self.driver)
        return self._address


class PageAddress(PageBase):
    @allure.step("操作：点击地址页登录按钮")
    def click_address_login(self):
        self.click(pages.shop.address_login)

    @allure.step("操作:点击地址页推荐按钮")
    def click_recommend_btn(self):
        self.click(pages.shop.recommend_btn)

    def input_address_email(self, email):
        with allure.step("输入地址邮箱"):
            allure.attach('{}'.format(email), name="输入 {}".format(email))
        self.input(pages.shop.address_email, email)

    def input_address_first_name(self, first_name):
        with allure.step("输入收件人名字"):
            allure.attach('{}'.format(first_name), name="输入 {}".format(first_name))
        self.input(pages.shop.address_first_name, first_name)

    def input_address_last_name(self, last_name):
        with allure.step("输入收件人姓"):
            allure.attach('{}'.format(last_name), name="输入 {}".format(last_name))
        self.input(pages.shop.address_last_name, last_name)

    def input_address(self, address):
        with allure.step("输入收件地址"):
            allure.attach('{}'.format(address), name="输入 {}".format(address))
        self.input(pages.shop.address, address)

    def input_address_city(self, city):
        with allure.step("输入收件城市"):
            allure.attach('{}'.format(city), name="输入 {}".format(city))
        self.input(pages.shop.add_city, city)

    def select_country(self, country):
        with allure.step("选择收件国家"):
            allure.attach('{}'.format(country), name="选择 {}".format(country))
        slt = Select(self.find_element_func(pages.shop.select_country))
        slt.select_by_value(country)

    def select_province(self, province):
        with allure.step("选择收件国家省、洲"):
            allure.attach('{}'.format(province), name="选择 {}".format(province))
        alt = Select(self.find_element_func(pages.shop.select_province))
        alt.select_by_value(province)

    def input_address_postal(self, postal):
        with allure.step("输入收件地址邮编"):
            allure.attach('{}'.format(postal), name="输入邮编 {}".format(postal))
        self.input(pages.shop.add_postal, postal)

    def input_address_phone(self, phone):
        with allure.step("输入收件地址手机号"):
            allure.attach('{}'.format(phone), name="输入手机号 {}".format(phone))
        self.input(pages.shop.add_phone, phone)

    def input_discount_code(self, code_value):
        with allure.step("操作：输入折扣蚂"):
            allure.attach('{}'.format(code_value), name="输入 {}".format(code_value))
        self.input(pages.shop.code_value, code_value)

    @allure.step("操作:点击使用折扣吗按钮")
    def click_apply_code(self):
        self.driver.execute_script("$('#btnUseCoupon').click()")

    @allure.step("操作:点击去 shipping页")
    def click_address_to_shipping(self):
        self.driver.execute_script("$('#continue_button').click()")

    @allure.step("操作:进入 购物车页")
    def click_address_to_cart(self):
        self.driver.execute_script("$('span[class=\"step__footer__previous-link-content\"]').click()")

    """
    组合业务方法（填写地址）
    """

    def edit_address(self, email, first_name, last_name, address, city, country, province, postal, phone):
        self.logger.info("正在调用填写地址组合业务方法，邮箱:{} 名：{} 姓：{} 地址: {} 城市: {} 国家 :{} 省份:{} 邮编:{} 手机号:{} ".
                         format(email, first_name,
                                last_name, address,
                                city, country,
                                province, postal,
                                phone))
        self.input_address_email(email)
        time.sleep(1)
        self.input_address_first_name(first_name)
        time.sleep(1)
        self.input_address_last_name(last_name)
        time.sleep(1)
        self.input_address(address)
        time.sleep(1)
        self.input_address_city(city)
        time.sleep(1)
        self.select_country(country)
        time.sleep(2)
        self.select_province(province)
        time.sleep(2)
        self.input_address_postal(postal)
        time.sleep(2)
        self.input_address_phone(phone)
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        self.click_address_to_shipping()

    """
    组合业务方法（填写地址使用折扣码）
    """

    def edit_address_use_discount(self, email, first_name, last_name, address, city, code_value, country, province,
                                  postal, phone,
                                  ):
        self.logger.info("正在调用填写地址组合业务方法，邮箱:{} 名：{} 姓：{} 地址: {} 城市: {} 国家 :{} 省份:{} 邮编:{} 手机号:{} ".
                         format(email, first_name,
                                last_name, address,
                                city, code_value, country,
                                province, postal,
                                phone))
        self.input_address_email(email)
        time.sleep(2)
        # self.click_recommend_btn()
        # time.sleep(2)
        self.input_address_first_name(first_name)
        time.sleep(2)
        self.input_address_last_name(last_name)
        time.sleep(2)
        self.input_address(address)
        time.sleep(2)
        self.input_address_city(city)
        time.sleep(2)
        self.input_discount_code(code_value)
        time.sleep(2)
        self.click_apply_code()
        time.sleep(2)
        self.select_country(country)
        time.sleep(2)
        self.select_province(province)
        time.sleep(2)
        self.input_address_postal(postal)
        time.sleep(2)
        self.input_address_phone(phone)
        time.sleep(1)
        # self.click(pages.shop.recommend_btn_two)
        # time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        self.click_address_to_shipping()
