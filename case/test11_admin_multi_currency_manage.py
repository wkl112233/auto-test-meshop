import time

import allure
import pytest

import pages
from case import TestBase
from pages.admin.home import PageAdminHomeMinix
from pages.admin.index import PageAdminIndexMinix
from pages.admin.product_manage import PageProductManageMinix
from pages.admin.marketing_manage import PageMarketingManageMinix


class TestMultiCurrency(TestBase, PageAdminHomeMinix, PageProductManageMinix,
                        PageAdminIndexMinix, PageMarketingManageMinix):
    # url = pages.admin.home_run_url

    url = pages.admin.home_url

    @allure.MASTER_HELPER.step(title='测试后台多币种管理添加币种的用例')
    @pytest.mark.parametrize("currency_name, currency_title",
                             [("AFN", "amd")])
    def test_add_currency(self, currency_name, currency_title):
        self.admin_home().goto_admin_login_page()
        time.sleep(3)
        # self.admin_home().admin_home_login_success()
        # time.sleep(3)
        self.admin_home().admin_home_login_report_ide_success()
        time.sleep(3)
        self.product_manage().click_icon_close()
        time.sleep(2)
        self.admin_index().click_marketing_management()
        time.sleep(2)
        self.admin_index().click_multi_currency()
        time.sleep(2)
        self.marketing_manage().add_all_currency()
        time.sleep(2)
        self.marketing_manage().add_part_currency(currency_name)
        time.sleep(2)
        self.marketing_manage().add_search_currency(currency_title)
        time.sleep(5)

    @allure.MASTER_HELPER.step(title='测试后台开启多币种的用例')
    def test_open_currency(self):
        self.driver.refresh()
        self.marketing_manage().add_all_currency()
        time.sleep(3)
        try:
            admin_currency = self.marketing_manage().get_admin_currency()
            self.logger.info("获取的后台主币种为：")
            self.logger.info(admin_currency)
            self.marketing_manage().open_multi_currency()
            expect = (self.marketing_manage().get_shop_currency())[0:3]
            assert expect == admin_currency, "断言出错，获取的前台主币种为：{}, 预期结果为：{}".format(admin_currency, expect)
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.MASTER_HELPER.step(title='测试后台关闭多币种的用例')
    def test_close_currency(self, expect=False):
        try:
            self.driver.close()
            time.sleep(2)
            self.driver.switch_to.window(self.driver.window_handles[-1])
            time.sleep(3)
            self.driver.refresh()
            self.marketing_manage().close_multi_currency()
            result = self.marketing_manage().multi_currency_if_close()
            self.logger.info("获取的结果为：")
            self.logger.info(result)
            assert expect == result, "断言出错，获取的结果为：{}, 预期结果为：{}".format(result, expect)
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.MASTER_HELPER.step(title='测试后台多币种移动的用例')
    def test_move_currency(self):
        # self.admin_home().goto_admin_login_page()
        # time.sleep(3)
        # self.admin_home().admin_home_login_success()
        # time.sleep(3)
        # self.admin_home().admin_home_login_report_ide_success()
        # time.sleep(3)
        # self.product_manage().click_icon_close()
        # time.sleep(2)
        # self.admin_index().click_marketing_management()
        # time.sleep(2)
        # self.admin_index().click_multi_currency()
        time.sleep(2)
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(3)
        self.driver.refresh()
        self.marketing_manage().move_multi_currency()

    @allure.MASTER_HELPER.step(title='测试后台多币种删除的用例')
    def test_delete_currency(self, expect=False):
        try:
            self.driver.refresh()
            time.sleep(2)
            result = self.marketing_manage().del_multi_currency()
            self.logger.info("获取的结果为：")
            self.logger.info(result)
            assert expect == result, "断言出错，获取的结果为：{}, 预期结果为：{}".format(result, expect)
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise
