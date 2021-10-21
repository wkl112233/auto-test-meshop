# _*_ coding: utf-8 _*_
import time

import allure
import pytest
from case import TestBase
from pages.shop.my_center import ShopMyCenterMinix
from pages.shop.home import ShopHomePageMinix
from pages.admin.home import PageAdminHomeMinix
from pages.admin.index import PageAdminIndexMinix
from tools.read_yaml import read_yaml, set_user, new_user


@allure.severity(allure.severity_level.BLOCKER)  # 阻塞
@allure.epic("前台：登录成功")
@allure.issue("https://template001.meshopstore.com")  # 前台地址
class TestShopLogin(TestBase, ShopHomePageMinix, ShopMyCenterMinix, PageAdminHomeMinix, PageAdminIndexMinix):
    url = "https://sso.meshopstore.com/home/signup"

    @allure.title("测试登录成功的用例")
    @allure.step("首先去后台切换模板到模板一后，进入前台首页")
    def test_login_success(self, expect="jinpeng@meshop.com"):
        try:
            self.admin_home().admin_home_login_template001()
            time.sleep(2)
            # self.admin_home().click_ala_popup_close()
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
            time.sleep(5)
            self.shop_home().click_icon()
            time.sleep(2)
            # self.shop_home().close_coupon_close()
            # time.sleep(2)
            # self.shop_home().click_icon()
            self.my_center().login_success()
            time.sleep(2)
            # 断言
            nickname = self.my_center().get_nickname()
            self.logger.info("获取的用户名称为：")
            self.logger.info(nickname)
            with allure.step('断言登录账户，并截图'):
                assert expect == nickname, "断言出错，登录的账号为：{}, 预期结果为：{}".format(nickname, expect)
                self.screenshot()
                time.sleep(2)
                self.my_center().click_logout()
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise


@allure.severity(allure.severity_level.BLOCKER)  # 阻塞
@allure.feature("前台：测试登录失败提示")
class TestShopLoginErr(TestBase, ShopHomePageMinix, ShopMyCenterMinix):
    url = 'https://template001.meshopstore.com/user/info/login'

    @allure.story("测试登录失败提示")
    @allure.title("{title}")
    @pytest.mark.parametrize("email,password,expect,title", read_yaml("ms_login_err.yaml"))
    def test_login_err(self, email, password, expect, title):
        try:
            # 调用登录业务方法
            self.my_center().login(email, password)
            time.sleep(2)
            # 断言
            tips = self.my_center().get_prompt_message()
            self.logger.info("获取的提示为：")
            self.logger.info(tips)
            with allure.step('断言，登录失败提示，并截图'):
                assert expect == tips, "断言出错，提示信息为：{}, 预期结果为：{}".format(tips, expect)
                self.screenshot()
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise


@allure.severity(allure.severity_level.BLOCKER)  # 阻塞
@allure.feature("前台：测试注册失败提示")
class TestShopRegisterErr(TestBase, ShopHomePageMinix, ShopMyCenterMinix):
    url = 'https://template001.meshopstore.com/user/info/register'

    @allure.title("{title}")
    @pytest.mark.parametrize("first_name,last_name,email,password,expect,title", read_yaml("ms_register_err.yaml"))
    def test_register_err(self, first_name, last_name, email, password, expect, title):
        try:
            # 调用注册业务方法
            self.my_center().logon_register(first_name, last_name, email, password)
            time.sleep(3)
            # 断言
            tips = self.my_center().get_prompt_message()
            self.logger.info("获取的提示为：")
            self.logger.info(tips)
            with allure.step('断言，注册失败提示，并截图'):
                assert expect == tips, "断言出错，提示信息为：{}, 预期结果为：{}".format(tips, expect)
                self.screenshot()
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise


@allure.severity(allure.severity_level.BLOCKER)  # 阻塞
@allure.feature("前台：注册成功")
class TestShopRegister(TestBase, ShopHomePageMinix, ShopMyCenterMinix):
    url = 'https://template001.meshopstore.com/user/info/login'

    @allure.title("测试注册成功的用例")
    @pytest.mark.parametrize("first_name,last_name,email,password,expect", new_user)
    def test_register(self, first_name, last_name, email, password, expect):
        try:
            self.my_center().click_register_page()
            time.sleep(2)
            # 调用注册业务方法
            self.my_center().logon_register(first_name, last_name, email, password)
            time.sleep(2)
            # 断言
            nickname = self.my_center().get_nickname()
            self.logger.info("获取的用户名称为：")
            self.logger.info(nickname)
            self.my_center().click_logout()
            with allure.step('断言，注册成功的用户邮箱，并截图'):
                assert expect == nickname, "断言出错，注册成功后登录的账号为：{}, 预期结果为：{}".format(nickname, expect)
                self.screenshot()
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.title("测试新注册用户登陆成功的用例")
    @pytest.mark.parametrize("email,password,expect", set_user)
    def test_register_success(self, email, password, expect):
        try:
            # 调用注册业务方法
            self.my_center().login(email, password)
            time.sleep(2)
            # 断言
            nickname = self.my_center().get_nickname()
            self.logger.info("获取的用户名称为：")
            self.logger.info(nickname)
            self.my_center().click_logout()
            with allure.step('断言，新注册用户登录成功后的邮箱，并截图'):
                assert expect == nickname, "断言出错，注册成功后登录的账号为：{}, 预期结果为：{}".format(nickname, expect)
                self.screenshot()
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise
