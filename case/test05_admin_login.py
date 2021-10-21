import time

import allure
import pytest

from case import TestBase
from pages.admin.home import PageAdminHomeMinix
from pages.admin.index import PageAdminIndexMinix
from tools.read_yaml import admin_new_arr, admin_set_arr


@allure.severity(allure.severity_level.BLOCKER)  # 阻塞
@allure.epic("后台：登录")
@allure.issue("https://sso.reportide.com/home/signup")  # 后台地址
class TestAdminLogin(TestBase, PageAdminHomeMinix, PageAdminIndexMinix):
    url = 'https://sso.reportide.com/home/signup'

    @allure.title('测试店铺登录信息输入正确，登录成功用例')
    def test_admin_login(self, expect="testde"):
        try:
            self.admin_home().goto_admin_login_page()
            time.sleep(1)
            # 调用登录业务方法
            # self.admin_home().admin_home_login_success()
            # time.sleep(6)
            self.admin_home().admin_home_login_report_ide_success()
            time.sleep(3)
            # 断言
            shop_name = self.admin_home().get_shop_name()
            self.logger.info("获取的店铺名为：")
            self.logger.info(shop_name)
            assert expect == shop_name, "断言出错，登录的店铺账号为：{}, 预期结果为：{}".format(shop_name, expect)
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.MASTER_HELPER.step(title='测试后台切换模板的用例')
    @pytest.mark.skip(reason="暂时跳过")
    def test_change_back_template(self):
        # self.admin_home().goto_admin_login_page()
        # time.sleep(3)
        # self.admin_home().admin_home_login_success()
        # time.sleep(3)
        self.admin_index().change_tpl_language()
        time.sleep(3)
        # self.admin_index().change_shop_tpl_one()
        self.admin_index().change_shop_tpl_one()
        # self.admin_index().change_shop_tpl_three()
        # self.admin_index().change_shop_tpl_four()
        # self.admin_index().change_shop_tpl_five()
        time.sleep(5)


class TestAdminRegister(TestBase, PageAdminHomeMinix):
    # url = pages.admin.home_url
    url = 'https://sso.reportide.com/home/signup'

    @allure.MASTER_HELPER.step(title='新店铺注册信息输入正确，注册成功')
    # @pytest.mark.skip(reason="暂停注册")
    @pytest.mark.parametrize("new_email, new_password, new_shop_name, new_shop_url,expect",
                             admin_new_arr)
    def test_admin_shop_register(self, new_email, new_password, new_shop_name, new_shop_url, expect):
        try:
            # 调用新建店铺业务
            self.admin_home().add_admin_new_shop(new_email, new_password, new_shop_name, new_shop_url)
            # 调取登录后台店铺
            # self.login.page_mis_login(shop_url_name=new_shop_url, mis_email=new_email,
            # mis_password = new_password)
            time.sleep(30)
            self.admin_home().edit_shop_information()
            time.sleep(6)
            shop_name = self.admin_home().get_shop_name()
            self.logger.info("获取的店铺名为：")
            self.logger.info(shop_name)
            # 断言
            assert expect == shop_name, "断言出错，获取的店铺账号为：{}, 预期结果为：{}".format(shop_name, expect)
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise


class TestAdminShopLogin(TestBase, PageAdminHomeMinix):
    # url = pages.admin.home_url
    url = 'https://sso.reportide.com/home/signup'

    @allure.MASTER_HELPER.step(title='新创建店铺登录验证，登录成功')
    @pytest.mark.parametrize("shop_url_name, admin_email, admin_password,expect",
                             admin_set_arr)
    def test_admin_shop_login(self, shop_url_name, admin_email, admin_password, expect):
        try:
            # 调用店铺登录业务
            self.admin_home().goto_admin_login_page()
            time.sleep(3)
            self.admin_home().admin_home_login(shop_url_name, admin_email, admin_password)
            time.sleep(6)
            # 断言
            shop_name = self.admin_home().get_shop_name()
            self.logger.info("获取的店铺名为：")
            self.logger.info(shop_name)
            assert expect == shop_name, "断言出错，获取的店铺账号为：{}, 预期结果为：{}".format(shop_name, expect)
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise
