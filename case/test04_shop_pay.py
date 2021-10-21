import time

import allure
import pytest
from case import TestBase
from pages.shop.home import ShopHomePageMinix
from pages.shop.my_center import ShopMyCenterMinix
from pages.shop.address_page import PageAddressMinix
from pages.shop.goods_terminal_page import PageGoodsInfoMinix
from pages.shop.shipping_page import PageFreightMinix
from pages.shop.payment_page import PagePaymentMinix
from pages.admin.home import PageAdminHomeMinix


@allure.severity(allure.severity_level.CRITICAL)  # 阻塞
@allure.epic("前台：购物流程")
@allure.issue("https://template001.meshopstore.com")  # 前台地址
class TestShopPayment(TestBase, ShopHomePageMinix, ShopMyCenterMinix, PageAddressMinix, PageGoodsInfoMinix,
                      PageAdminHomeMinix,
                      PageFreightMinix, PagePaymentMinix):
    url = 'https://template001.meshopstore.com'

    @allure.story("测试单件商品adyen支付，购买时使用折扣码的购物流程")
    @allure.title("测试adyen支付的用例")
    @pytest.mark.parametrize(
        "index, text, e_index, k_text,email, first_name, last_name, address,"
        "city,code_value,country, province, postal,"
        "phone,adyen_card, adyen_year, adyen_cvc,expect",
        [(
                '0', '1.0 Meter', '1', 'Apple', 'wangjinpeng@meshop.net', 'liu', 'bei',
                'red barracks South Rade 14 #',
                'Ottawa', 'adyen', '1220', 'California', 'M2j 4A677', '16478366006', '4444333322221111', '0330', '737',
                'Your order')]
    )
    def test_adyen_pay(self, index, text, e_index, k_text, email, first_name, last_name, address, city,
                       code_value, country,
                       province, postal, phone,
                       adyen_card, adyen_year, adyen_cvc, expect):
        try:
            time.sleep(5)
            self.driver.get('https://template001.meshopstore.com/collections/auto/')
            time.sleep(3)
            self.shop_home().click_test_goods_name()
            self.driver.switch_to.window(self.driver.window_handles[-1])
            time.sleep(2)
            self.goods_info().select_test_goods_cart_buy(index, text, e_index, k_text)
            time.sleep(2)
            self.shop_home().click_mini_checkout()
            # 调用地址页编辑业务
            self.address().edit_address_use_discount(email, first_name, last_name, address, city, code_value, country,
                                                     province,
                                                     postal, phone)
            time.sleep(1)
            # 调用选择运费方式业务
            self.freight().select_freight()
            # 调取adyen支付业务
            self.payment().pay_with_adyen(adyen_card, adyen_year, adyen_cvc)
            time.sleep(8)
            # 断言
            msage = self.payment().get_adyen_msg()
            self.logger.info("获取的支付信息为：")
            self.logger.info(msage)
            time.sleep(3)
            assert expect in msage, "断言出错，获取的支付信息为：{}, 预期结果为：{}".format(msage, expect)
            with allure.step('断言支付结果，并截图'):
                self.screenshot()
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.story("测试单件商品stripe支付，购买时不使用折扣码的购物流程")
    @allure.title('测试stripe支付的用例')
    @pytest.mark.parametrize(
        "e_index, k_text, email, first_name, last_name, address, city,"
        "country, province, postal,"
        " phone,stripe_card, stripe_year, stripe_cvc,expect",
        [('0', 'iPhone 11pro max', 'jinpeng@meshop.net', 'liu', 'bei', 'red barracks South Rade 14 #',
          'Ottawa', '1220', 'California', 'M2j 4A677', '16478366006', '4242424242424242', '0424', '100',
          'Your order')]
    )
    def test_stripe_pay(self, e_index, k_text, email, first_name, last_name, address,
                        city, country,
                        province, postal, phone,
                        stripe_card, stripe_year, stripe_cvc, expect):
        try:
            with allure.step('首页打开系列列表页'):
                self.driver.get('https://template001.meshopstore.com/collections/auto/')
            time.sleep(3)
            self.shop_home().click_test_goods_name_two()
            self.driver.switch_to.window(self.driver.window_handles[-1])
            time.sleep(2)
            self.goods_info().select_goods_sku(e_index, k_text)
            time.sleep(3)
            self.goods_info().click_add_cart()
            time.sleep(3)
            self.shop_home().click_mini_checkout()
            time.sleep(2)
            self.address().edit_address(email, first_name, last_name, address, city, country, province, postal, phone)
            # 调用选择运费方式业务
            self.freight().select_freight()
            time.sleep(3)
            # 选卡支付
            self.payment().pay_with_stripe(stripe_card, stripe_year, stripe_cvc)
            time.sleep(8)
            # 断言
            msage = self.payment().get_stripe_msg()
            self.logger.info("获取的支付信息为：")
            time.sleep(3)
            self.logger.info(msage)
            assert expect in msage, "断言出错，获取的支付信息为：{}, 预期结果为：{}".format(msage, expect)
            time.sleep(2)
            with allure.step('断言支付结果，并截图'):
                self.screenshot()
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.story("测试前台用户登录后，商品终端页点击立即购买使用checkout支付方式购买的购物流程业务")
    @allure.title('测试checkout支付的用例')
    @pytest.mark.parametrize(
        "checkout_card, checkout_mm, checkout_yy, checkout_cvc,mv_code,expect",
        [('4242424242424242', '03', '30', '100', 'Checkout1!', 'Your order')])
    def test_checkout_pay(self, checkout_card, checkout_mm, checkout_yy, checkout_cvc, mv_code, expect):
        try:
            with allure.step('打开首页个人中心登录账户'):
                self.driver.get('https://template001.meshopstore.com')
                time.sleep(2)
                # 调用登录业务方法
                self.shop_home().click_icon()
                self.my_center().login_success()
            time.sleep(2)
            with allure.step('登录成功后打开系列列表页，并选择产品进入商品终端页'):
                self.driver.get('https://template001.meshopstore.com/collections/auto/')
                time.sleep(2)
                self.driver.get('https://template001.meshopstore.com/collections/auto/product/price-100125/')
            time.sleep(3)
            self.goods_info().click_buy_now()
            time.sleep(2)
            self.address().click_address_to_shipping()
            time.sleep(3)
            self.freight().select_freight()
            time.sleep(3)
            # 选卡支付
            self.payment().pay_with_checkout(checkout_card, checkout_mm, checkout_yy, checkout_cvc, mv_code)
            time.sleep(4)
            # 断言
            msage = self.payment().get_checkout_msg()
            self.logger.info("获取的支付信息为：")
            self.logger.info(msage)
            assert expect in msage, "断言出错，获取的支付信息为：{}, 预期结果为：{}".format(msage, expect)
            time.sleep(2)
            with allure.step('断言支付结果，并截图'):
                self.screenshot()
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.story("测试多件商品使用unlimint支付方式购买的购物流程业务")
    @allure.title('测试用户unlimint支付的用例')
    @pytest.mark.parametrize(
        "count, e_index, k_text,email, first_name, last_name, address, city, country, "
        "province, postal, phone,unlimint_card_name, unlimint_card, unlimint_date, unlimint_cvc,expect",
        [('iphone', '0', "iPhone 12", 'jinpeng@meshop.net', 'liu', 'bei', 'red barracks South Rade 14 #',
          'Ottawa', '1220', 'California', 'M2j 4A677', '16478366006', 'Test', '4000000000000002', '0330', '737',
          'Your order')])
    def test_unlimint_pay(self, count, e_index, k_text, email, first_name, last_name, address, city, country, province,
                          postal, phone, unlimint_card_name, unlimint_card, unlimint_date, unlimint_cvc,
                          expect):
        try:
            with allure.step('返回首页个人中心退出用户登录'):
                self.driver.get('https://template001.meshopstore.com/')
                time.sleep(2)
                self.shop_home().click_icon()
                time.sleep(2)
                self.my_center().click_logout()
                time.sleep(2)
            with allure.step('选择第一件产品加入购物车'):
                self.driver.get('https://template001.meshopstore.com/')
                time.sleep(2)
                self.shop_home().goto_shop_search_page(count)
                time.sleep(2)
                self.driver.get('https://template001.meshopstore.com/product/apple-iphones-'
                                'hinterdeckel-stil-silizium-%E4%BF%9D%E6%8A%A4%E5%A5%97-%E5%A3%B3-1136529/')
                time.sleep(2)
                self.goods_info().select_goods_sku(e_index, k_text)
                time.sleep(2)
                self.goods_info().click_add_cart()
            time.sleep(3)
            with allure.step('选择第二件产品加入购物车'):
                self.driver.get('https://template001.meshopstore.com/collections/auto/')
                time.sleep(1)
                self.driver.get('https://template001.meshopstore.com/collections/auto/product/price-100125/')
                self.goods_info().click_add_cart()
                time.sleep(3)
            self.shop_home().click_mini_checkout()
            time.sleep(2)
            self.address().edit_address(email, first_name, last_name, address, city, country, province, postal, phone)
            # 调用选择运费方式业务
            self.freight().select_freight()
            time.sleep(3)
            self.payment().pay_with_unlimint(unlimint_card_name, unlimint_card, unlimint_date, unlimint_cvc)
            time.sleep(6)
            element = self.payment().base_if_exists_element(ele_id="success")
            if element is True:
                self.payment().click_unlimint_pay_code()
            else:
                self.driver.switch_to.window(self.driver.window_handles[-1])
            time.sleep(5)
            # 断言
            msage = self.payment().get_checkout_msg()
            self.logger.info("获取的支付信息为：")
            self.logger.info(msage)
            assert expect in msage, "断言出错，获取的支付信息为：{}, 预期结果为：{}".format(msage, expect)
            with allure.step('断言支付结果，并截图'):
                self.screenshot()
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.story("测试无必选区商品使用首信易_直连支付方式购买的业务")
    @allure.title('测试首信易 直连支付的用例')
    @pytest.mark.parametrize(
        "email, first_name, last_name, address, city, country, province, postal, phone,pay_ease_direct_card_name, "
        "pay_ease_direct_card, pay_ease_direct_date,pay_ease_direct_cvc, expect",
        [('jinpeng@meshop.net', 'liu', 'bei', 'red barracks South Rade 14 #',
          'Ottawa', '1220', 'California', 'M2j 4A677', '16478366006', 'Test', '4100000000000001', '0325', '123',
          'Your order')])
    def test_pay_ease_direct(self, email, first_name, last_name, address, city, country, province, postal, phone,
                             pay_ease_direct_card_name, pay_ease_direct_card, pay_ease_direct_date,
                             pay_ease_direct_cvc, expect, ):
        try:
            with allure.step('前台系列列表页打开无必选区商品终端页'):
                self.driver.get('https://template001.meshopstore.com/')
                time.sleep(3)
                self.driver.get('https://template001.meshopstore.com/collections/auto/')
                time.sleep(2)
                self.driver.get('https://template001.meshopstore.com/collections/auto/product/price-100125/')
                time.sleep(3)
            self.goods_info().click_add_cart()
            time.sleep(3)
            self.shop_home().click_mini_checkout()
            time.sleep(2)
            self.address().edit_address(email, first_name, last_name, address, city, country, province, postal, phone)
            # 调用选择运费方式业务
            self.freight().select_freight()
            time.sleep(3)
            self.payment().pay_with_pay_ease_direct(pay_ease_direct_card_name, pay_ease_direct_card,
                                                    pay_ease_direct_date,
                                                    pay_ease_direct_cvc)
            time.sleep(5)
            # 断言
            msage = self.payment().get_checkout_msg()
            self.logger.info("获取的支付信息为：")
            self.logger.info(msage)
            assert expect in msage, "断言出错，获取的支付信息为：{}, 预期结果为：{}".format(msage, expect)
            with allure.step('断言支付结果，并截图'):
                self.screenshot()
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.story("测试编辑和修改多件商品必选区内容并加入购物车后，使用Pacy_pay支付方式支付的购物流程业务")
    @allure.title('测试用户Pacy_pay支付的用例')
    @pytest.mark.parametrize(
        "count, e_index, k_text,pacy_pay_card, pacy_pay_date, pacy_pay_cvc,expect",
        [('iphone', '0', "iPhone 11pro", '4711100000000000', '0323', '123', 'Your order')])
    def test_pacy_pay_pay(self, count, e_index, k_text, pacy_pay_card, pacy_pay_date, pacy_pay_cvc, expect, ):
        try:
            """with allure.step('切换站点模板为模板一后进入前台首页'):
                self.driver.get('https://sso.reportide.com/home/signup')
                self.admin_home().admin_home_login_en()
                time.sleep(2)
                self.admin_home().click_shop_configs()
                time.sleep(2)
                self.admin_home().click_shop_template()
                time.sleep(5)
                temp_name = self.admin_home().get_shop_temp_name()
                if temp_name == 'Default模板':
                    time.sleep(2)
                    self.admin_home().click_website()
                    self.driver.switch_to.window(self.driver.window_handles[-1])
                else:
                    self.admin_home().change_shop_temp_one()
                    self.driver.switch_to.window(self.driver.window_handles[-1])
                    time.sleep(5)"""
            with allure.step('搜索并选择第一款产品，加入购物车'):
                self.driver.get('https://template001.meshopstore.com/')
                time.sleep(3)
                self.shop_home().goto_shop_search_page(count)
                time.sleep(2)
                self.driver.get('https://template001.meshopstore.com/collections/auto/product/plastik-apple-iphones-schutzhulle-%E4%BF%9D%E6%8A%A4%E5%A5%97-%E5%A3%B3-1136514/')
                time.sleep(2)
                self.goods_info().select_goods_sku(e_index, k_text)
                time.sleep(2)
                self.goods_info().click_add_cart()
                time.sleep(3)
            with allure.step('在列表页，选择第二款产品并加入购物车'):
                self.driver.get('https://template001.meshopstore.com/')
                time.sleep(1)
                self.driver.get('https://template001.meshopstore.com/collections/auto/')
                time.sleep(1)
                self.driver.get('https://template001.meshopstore.com/collections/auto/product/apple-iphones-schutzhulle-silizium-%E4%BF%9D%E6%8A%A4%E5%A5%97-%E5%A3%B3-1136515/')
                self.goods_info().click_add_cart()
                time.sleep(3)
            with allure.step('在列表页，选择第三款产品，终端页增加商品数量并加入购物车'):
                self.driver.get('https://template001.meshopstore.com/collections/auto/')
                time.sleep(1)
                self.driver.get('https://template001.meshopstore.com/collections/auto/product/zipper-lace-up-loose-standard-cotton-padded-jacket-874329/')
                self.goods_info().click_add_goods()
                time.sleep(2)
                self.goods_info().click_add_cart()
                time.sleep(3)
            with allure.step('在列表页，选择第四款产品，终端页编辑商品数量并加入购物车'):
                self.driver.get('https://template001.meshopstore.com/collections/auto/')
                time.sleep(1)
                self.driver.get('https://template001.meshopstore.com/collections/auto/product/price-100125/')
                self.goods_info().input_goods_count(count=3)
                self.goods_info().click_add_cart()
                time.sleep(3)
            self.shop_home().click_mini_checkout()
            time.sleep(2)
            self.address().click_address_login()
            time.sleep(3)
            self.my_center().login(email='wjp@163.com', password='123456')
            time.sleep(3)
            js = "var q=document.documentElement.scrollTop=500"
            self.driver.execute_script(js)
            time.sleep(3)
            self.address().click_address_to_shipping()
            time.sleep(1)
            self.freight().select_freight()
            time.sleep(3)
            js = "var q=document.documentElement.scrollTop=500"
            self.driver.execute_script(js)
            time.sleep(3)
            # 选pacy_pay支付
            self.payment().pay_with_pacy_pay(pacy_pay_card, pacy_pay_date, pacy_pay_cvc)
            time.sleep(6)
            element = self.payment().base_if_exists_element(ele_id="submit")
            if element is True:
                self.payment().click_pacy_pay_code()
            else:
                self.driver.switch_to.window(self.driver.window_handles[-1])
            time.sleep(5)
            # 断言
            msage = self.payment().get_checkout_msg()
            self.logger.info("获取的支付信息为：")
            self.logger.info(msage)
            assert expect in msage, "断言出错，获取的支付信息为：{}, 预期结果为：{}".format(msage, expect)
            with allure.step('断言支付结果，并截图'):
                self.screenshot()
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise
