import time

import allure
from selenium.webdriver import ActionChains

import pages
from pages.pagebase import PageBase
from selenium.webdriver.common.by import By


class PagePaymentMinix:
    def payment(self):
        if not getattr(self, '_payment', None):
            self._payment = PagePayment(self.driver)
        return self._payment


class PagePayment(PageBase):
    @allure.step("操作：选择首信易 直连 支付方式，打开输入框 ")
    def click_pay_ease_direct(self):
        self.click(pages.shop.pay_ease_direct)

    @allure.step("操作：选择 pacy_pay 支付方式 ")
    def click_pacy_pay(self):
        self.click(pages.shop.pacy_pay)

    @allure.step("操作：选择 unlimint 支付方式，打开输入框")
    def click_unlimint_pay(self):
        self.click(pages.shop.unlimint_pay)

    @allure.step("操作：选择 adyen支付 方式，打开输入框 ")
    def click_adyen(self):
        element = self.find_element_func(pages.shop.adyen)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        self.click(pages.shop.adyen)

    @allure.step("操作：选择 Stripe支付 方式，打开输入框 ")
    def click_stripe(self):
        self.click(pages.shop.stripe)

    @allure.step("操作：选择 Checkout支付 方式，打开输入框 ")
    def click_checkout(self):
        self.click(pages.shop.checkout)

    @allure.step("输入首信易 直连支付方式的卡号用户名 ")
    def input_pay_ease_direct_card_name(self, pay_ease_direct_card_name):
        self.click(pages.shop.pay_ease_direct_card_name)
        self.input(pages.shop.pay_ease_direct_card_name, pay_ease_direct_card_name)

    @allure.step("输入首信易 直连支付方式的卡号 ")
    def input_pay_ease_direct_card(self, pay_ease_direct_card):
        self.click(pages.shop.pay_ease_direct_card)
        self.input(pages.shop.pay_ease_direct_card, pay_ease_direct_card)

    @allure.step("输入首信易 直连支付方式的卡号有效期月份 ")
    def input_pay_ease_direct_date(self, pay_ease_direct_date):
        """
        输首信易 直连卡号有效期月份
        """
        self.click(pages.shop.pay_ease_direct_date)
        self.input(pages.shop.pay_ease_direct_date, pay_ease_direct_date)

    @allure.step("输入首信易 直连支付方式的卡号CVC ")
    def input_pay_ease_direct_cvc(self, pay_ease_direct_cvc):
        """
        输首信易 直连卡号cvc
        """
        self.click(pages.shop.pay_ease_direct_cvc)
        self.input(pages.shop.pay_ease_direct_cvc, pay_ease_direct_cvc)

    @allure.step("输入unlimint支付方式的卡号用户名 ")
    def input_unlimint_card_name(self, unlimint_card_name):
        self.click(pages.shop.unlimint_card_name)
        self.input(pages.shop.unlimint_card_name, unlimint_card_name)

    @allure.step("输入unlimint支付方式的卡号 ")
    def input_unlimint_card(self, unlimint_card):
        """
        输unlimint卡号
        """
        self.click(pages.shop.unlimint_card)
        self.input(pages.shop.unlimint_card, unlimint_card)

    @allure.step("输入unlimint支付方式的卡号日期")
    def input_unlimint_date(self, unlimint_date):
        """
        输unlimint卡号日期
        """
        self.click(pages.shop.unlimint_date)
        self.input(pages.shop.unlimint_date, unlimint_date)

    @allure.step("输入unlimint支付方式的卡号用户名")
    def input_unlimint_cvc(self, unlimint_cvc):
        """
        输unlimint卡号用户名
        """
        self.click(pages.shop.unlimint_cvc)
        self.input(pages.shop.unlimint_cvc, unlimint_cvc)

    @allure.step("输入pacy_pay支付方式的卡号")
    def input_pacy_pay_card(self, pacy_pay_card):
        """
        输pacy_pay卡号
        """
        self.click(pages.shop.pacy_pay_card)
        self.input(pages.shop.pacy_pay_card, pacy_pay_card)

    @allure.step("输入stripe支付方式的卡号")
    def input_stripe_card(self, stripe_card):
        self.input(pages.shop.stripe_card, stripe_card)

    @allure.step("输入stripe支付方式的卡号年月")
    def input_stripe_year(self, stripe_year):
        self.input(pages.shop.stripe_year, stripe_year)

    @allure.step("输入pacy_pay支付方式的卡号年月")
    def input_pacy_pay_date(self, pacy_pay_date):
        self.click(pages.shop.pacy_pay_date)
        self.input(pages.shop.pacy_pay_date, pacy_pay_date)

    @allure.step("输入pacy_pay支付方式的信用卡cvc")
    def input_pacy_pay_cvc(self, pacy_pay_cvc):
        """
        输pacy_pay,cvc
        """
        self.click(pages.shop.pacy_pay_cvc)
        self.input(pages.shop.pacy_pay_cvc, pacy_pay_cvc)

    @allure.step("输入stripe支付方式的信用卡cvc")
    def input_stripe_cvc(self, stripe_cvc):
        self.input(pages.shop.stripe_cvc, stripe_cvc)

    @allure.step("输入checkout支付方式的信用卡卡号")
    def input_checkout_card(self, checkout_card):
        self.input(pages.shop.checkout_card, checkout_card)

    @allure.step("输入checkout支付方式的信用卡有效期月份")
    def input_checkout_mm(self, checkout_mm):
        self.input(pages.shop.checkout_mm, checkout_mm)

    @allure.step("输入checkout支付方式的信用卡有效期年份")
    def input_checkout_yy(self, checkout_yy):
        self.input(pages.shop.checkout_yy, checkout_yy)

    @allure.step("输入checkout支付方式的信用卡CVC")
    def input_checkout_cvc(self, checkout_cvc):
        self.input(pages.shop.checkout_cvc, checkout_cvc)

    @allure.step("输入adyen支付方式的信用卡卡号")
    def input_adyen_card(self, adyen_card):
        iframe = self.find_element_func(pages.shop.iframe)
        self.driver.switch_to.frame(iframe)
        time.sleep(1)
        self.input(pages.shop.adyen_card, adyen_card)
        self.driver.switch_to.default_content()

    @allure.step("输入adyen支付方式的信用卡日期年份")
    def input_adyen_year(self, adyen_year):
        iframe1 = self.find_element_func(pages.shop.iframe1)
        self.driver.switch_to.frame(iframe1)
        time.sleep(1)
        self.input(pages.shop.adyen_year, adyen_year)
        self.driver.switch_to.default_content()

    @allure.step("输入adyen支付方式的信用卡CVC")
    def input_adyen_cvc(self, adyen_cvc):
        iframe2 = self.find_element_func(pages.shop.iframe2)
        self.driver.switch_to.frame(iframe2)
        time.sleep(1)
        self.input(pages.shop.adyen_cvc, adyen_cvc)
        self.driver.switch_to.default_content()

    @allure.step("返回首页")
    def click_go_shopping(self):
        """
        点击支付成功页的去购物按钮
        """
        self.driver.execute_script("$('p:nth-child(5)>span>a').click()")

    @allure.step("支付失败，点击重新选择支付方式")
    def click_try_again_btn(self):
        self.driver.execute_script("$('span>a').click()")

    @allure.step("购物车页，点击去购买按钮，回到首页")
    def click_shop_our_products_btn(self):
        # 购物车为空，点击去购买按钮
        self.driver.execute_script("$('div[class=\"EmptyContainer\"]>a').click()")

    @allure.step("操作，点击支付按钮")
    def click_adyen_pay_btn(self):
        """
        点击adyen支付购买按钮
        """
        element = self.find_element_func((By.CSS_SELECTOR, 'button[datapaychannelid="31"]'))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        self.driver.execute_script("$('button[datapaychannelid=\"31\"]').click()")

    @allure.step("操作，点击支付按钮")
    def click_st_pay_btn(self):
        """
        点击st支付购买按钮
        """
        self.driver.execute_script("$('button[datapaychannelid=\"41\"]').click()")

    @allure.step("操作，点击支付按钮")
    def click_pacy_pay_btn(self):
        """
        点击pacy_pay支付购买按钮
        """
        self.driver.execute_script("$('button[datapaychannelid=\"61\"]').click()")

    @allure.step("操作，点击支付按钮")
    def click_unlimint_btn(self):
        """
        点击unlimint支付购买按钮
        """
        self.driver.execute_script("$('button[datapaychannelid=\"121\"]').click()")

    @allure.step("操作，点击支付按钮")
    def click_pay_ease_direct_btn(self):
        """
        点击首信易直连支付购买按钮
        """
        self.driver.execute_script("$('button[datapaychannelid=\"76\"]').click()")

    @allure.step("操作，点击支付按钮")
    def click_ck_pay_btn(self):
        """
        点击ck支付购买按钮
        """
        self.driver.execute_script("$('button[datapaychannelid=\"51\"]').click()")

    @allure.step("操作，选择PayPal支付方式")
    def click_pp_pay(self):
        """
        选择pp支付
        """
        element = self.find_element_func(pages.shop.pp_pay_btn)
        self.driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            element,
            "border: 2px solid red;")
        time.sleep(2)
        ActionChains(self.driver).move_to_element(element).perform()
        time.sleep(2)
        element.click()

    def click_pp_pay_btn(self, pp_email, pp_psd):
        """
        点击paypal支付按钮业务
        """
        pp_iframe = self.find_element_func(pages.shop.pp_iframe)
        pp_iframe_two = self.find_element_func(pages.shop.pp_iframe_two)
        self.driver.switch_to.frame(pp_iframe)
        time.sleep(1)
        self.driver.switch_to.frame(pp_iframe_two)
        self.click(pages.shop.pp_but)
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # self.click(pages.shop.pp_button)
        self.input(pages.shop.pp_email, pp_email)
        time.sleep(1)
        self.click(pages.shop.pp_next)
        time.sleep(1)
        self.input(pages.shop.pp_psd, pp_psd)
        time.sleep(1)
        self.click(pages.shop.pp_login)
        time.sleep(2)

    @allure.step("操作，输入checkout支付 3ds验证码并确认")
    def input_mv_code(self, mv_code):
        """
        输入checkout结算验证码
        """
        ck_code_iframe = self.find_element_func(pages.shop.ck_code_iframe)
        self.driver.switch_to.frame(ck_code_iframe)
        time.sleep(1)
        self.click(pages.shop.mv_code)
        time.sleep(1)
        self.input(pages.shop.mv_code, mv_code)
        time.sleep(1)
        self.click(pages.shop.sure_code)
        self.driver.switch_to.default_content()

    @allure.step("操作，点击确认Pacy_pay支付的3ds验证")
    def click_pacy_pay_code(self):
        """
        输入Pacy_pay结算验证码
        """
        self.click(pages.shop.pacy_pay_code)

    def get_pacy_pay_element(self, ele_id):
        flag = self.base_if_exists_element(ele_id)
        return flag

    @allure.step("操作，点击确认unlimint_pay支付的3ds验证")
    def click_unlimint_pay_code(self):
        """
        输入unlimint_pay结算验证码
        """
        self.click(pages.shop.unlimint_code)

    def get_unlimint_element(self, ele_id):
        flag = self.base_if_exists_element(ele_id)
        return flag

    """
    点击ST支付后,支付页logo
    """

    def click_pay_page_logo(self):
        element = self.find_element_func(pages.shop.st_zf_logo)
        self.driver.execute_script("arguments[0].click();", element)

    """
    获取 stripe支付结果
    """

    def get_stripe_msg(self):
        return self.find_element_func(pages.shop.get_success_msg).get_attribute('textContent')

    """
    获取 checkout 支付结果
    """

    def get_checkout_msg(self):
        return self.find_element_func(pages.shop.get_success_msg).get_attribute('textContent')

    """
    获取 adyen 支付结果
    """

    def get_adyen_msg(self):
        return self.find_element_func(pages.shop.get_success_msg).get_attribute('textContent')

    """
    鼠标悬停在logo图片
    """

    def pay_page_logo_hover(self):
        element = self.find_element_func(pages.shop.st_zf_logo)
        ActionChains(self.driver).move_to_element(element).perform()

    """
    组合业务方法（adyen支付）
    """

    def pay_with_adyen(self, adyen_card, adyen_year, adyen_cvc):
        self.logger.info("正在调用stripe支付方法，卡号：{} 月年: {} cvc:{}".format(adyen_card, adyen_year, adyen_cvc))
        self.click_adyen()
        time.sleep(10)
        self.input_adyen_card(adyen_card)
        time.sleep(1)
        self.input_adyen_year(adyen_year)
        time.sleep(1)
        self.input_adyen_cvc(adyen_cvc)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)
        self.click_adyen_pay_btn()

    """
    组合业务方法（stripe支付）
    """

    def pay_with_stripe(self, stripe_card, stripe_year, stripe_cvc):
        self.logger.info("正在调用stripe支付方法，卡号：{} 月年: {} cvc:{}".format(stripe_card, stripe_year, stripe_cvc))
        self.click_stripe()
        time.sleep(10)
        st_iframe = self.find_element_func(pages.shop.st_iframe)
        self.driver.switch_to.frame(st_iframe)
        self.input_stripe_card(stripe_card)
        time.sleep(1)
        self.input_stripe_year(stripe_year)
        time.sleep(1)
        self.input_stripe_cvc(stripe_cvc)
        time.sleep(1)
        self.driver.switch_to.default_content()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        self.click_st_pay_btn()
        js = "var q=document.documentElement.scrollTop=0"
        self.driver.execute_script(js)

    """
    组合业务方法（checkout支付）
    """

    def pay_with_checkout(self, checkout_card, checkout_mm, checkout_yy, checkout_cvc, mv_code):
        self.logger.info(
            "正在调用checkout支付方法，卡号：{} 月：{} 年: {} cvc:{}".format(checkout_card, checkout_mm, checkout_yy, checkout_cvc,
                                                              mv_code))
        self.click_checkout()
        time.sleep(10)
        ck_iframe = self.find_element_func(pages.shop.ck_iframe)
        self.driver.switch_to.frame(ck_iframe)
        self.input_checkout_card(checkout_card)
        time.sleep(1)
        self.input_checkout_mm(checkout_mm)
        time.sleep(1)
        self.input_checkout_yy(checkout_yy)
        time.sleep(1)
        self.input_checkout_cvc(checkout_cvc)
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        self.click_ck_pay_btn()
        time.sleep(3)
        self.input_mv_code(mv_code)

    def pay_with_paypal(self, pp_email, pp_psd):
        """
        组合业务方法（paypal支付）
        """
        self.logger.info(
            "正在调用paypal支付方法，邮箱：{} 密码：{} ".format(pp_email, pp_psd))
        self.click_pp_pay()
        time.sleep(2)
        self.click_pp_pay_btn(pp_email, pp_psd)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)
        self.click(pages.shop.pp_pay_now)
        time.sleep(2)
        self.driver.switch_to.default_content()
        time.sleep(2)
        self.driver.switch_to.default_content()

    """
    组合业务方法（pacy_pay支付）
    """

    def pay_with_pacy_pay(self, pacy_pay_card, pacy_pay_date, pacy_pay_cvc):
        self.logger.info("正在调用pacy_pay支付方法，卡号：{} 月年: {} cvc:{}".format(pacy_pay_card, pacy_pay_date, pacy_pay_cvc))
        self.click_pacy_pay()
        time.sleep(3)
        # pacy_pay_iframe = self.find_element_func(pages.shop.pacy_pay_iframe)
        # self.driver.switch_to.frame(pacy_pay_iframe)
        self.input_pacy_pay_card(pacy_pay_card)
        time.sleep(1)
        self.input_pacy_pay_date(pacy_pay_date)
        time.sleep(1)
        self.input_pacy_pay_cvc(pacy_pay_cvc)
        time.sleep(1)
        # self.driver.switch_to.default_content()
        # time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        self.click_pacy_pay_btn()
        js = "var q=document.documentElement.scrollTop=0"
        self.driver.execute_script(js)

    """
    组合业务方法（unlimint支付）
    """

    def pay_with_unlimint(self, unlimint_card_name, unlimint_card, unlimint_date, unlimint_cvc):
        self.logger.info(
            "正在调用unlimint支付方法，用户名 {} 卡号：{} 月年: {} cvc:{}".format(unlimint_card_name, unlimint_card, unlimint_date,
                                                                 unlimint_cvc))
        self.click_unlimint_pay()
        time.sleep(3)
        unlimint_iframe = self.find_element_func(pages.shop.unlimint_iframe)
        self.driver.switch_to.frame(unlimint_iframe)
        self.input_unlimint_card_name(unlimint_card_name)
        time.sleep(1)
        self.input_unlimint_card(unlimint_card)
        time.sleep(1)
        self.input_unlimint_date(unlimint_date)
        time.sleep(1)
        self.input_unlimint_cvc(unlimint_cvc)
        time.sleep(1)
        self.driver.switch_to.default_content()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        self.click_unlimint_btn()
        js = "var q=document.documentElement.scrollTop=0"
        self.driver.execute_script(js)

    """
    组合业务方法（pay_ease_direct支付）
    """

    def pay_with_pay_ease_direct(self, pay_ease_direct_card_name, pay_ease_direct_card, pay_ease_direct_date,
                                 pay_ease_direct_cvc):
        self.logger.info(
            "正在调用pay_ease_direct支付方法，用户名 {} 卡号：{} 月年: {} cvc:{}".format(pay_ease_direct_card_name, pay_ease_direct_card,
                                                                        pay_ease_direct_date, pay_ease_direct_cvc))
        self.click_pay_ease_direct()
        time.sleep(3)
        pay_ease_direct_iframe = self.find_element_func(pages.shop.pay_ease_direct_iframe)
        self.driver.switch_to.frame(pay_ease_direct_iframe)
        self.input_pay_ease_direct_card_name(pay_ease_direct_card_name)
        time.sleep(1)
        self.input_pay_ease_direct_card(pay_ease_direct_card)
        time.sleep(1)
        self.input_pay_ease_direct_date(pay_ease_direct_date)
        time.sleep(1)
        self.input_pay_ease_direct_cvc(pay_ease_direct_cvc)
        time.sleep(1)
        self.driver.switch_to.default_content()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        self.click_pay_ease_direct_btn()
        js = "var q=document.documentElement.scrollTop=0"
        self.driver.execute_script(js)
