import time

import allure

import pages
from case import TestBase
from pages.admin.home import PageAdminHomeMinix
from pages.admin.index import PageAdminIndexMinix
from pages.admin.product_manage import PageProductManageMinix
from pages.admin.marketing_manage import PageMarketingManageMinix
from pages.admin.application_manage import PageApplicationManageMinix


class TestApplicationManage(TestBase, PageAdminHomeMinix, PageProductManageMinix,
                            PageAdminIndexMinix, PageMarketingManageMinix, PageApplicationManageMinix):
    # url = pages.admin.home_run_url

    url = pages.admin.home_url

    @allure.MASTER_HELPER.step(title='测试后台多应用管理添加色卡应用用例')
    def test_add_application(self, expect="色卡"):
        self.admin_home().goto_admin_login_page()
        time.sleep(3)
        # self.admin_home().admin_home_login_success()
        # time.sleep(3)
        self.admin_home().admin_home_login_report_ide_success()
        time.sleep(3)
        self.product_manage().click_icon_close()
        time.sleep(2)
        self.admin_index().click_app_manage()
        time.sleep(2)
        self.admin_index().click_app_list()
        time.sleep(2)
        try:
            self.application_manage().add_application()
            time.sleep(2)
            self.admin_index().click_app_manage()
            time.sleep(2)
            self.admin_index().click_app_list()
            time.sleep(2)
            title = self.application_manage().get_application_name()
            self.logger.info("获取的应用标题为：")
            self.logger.info(title)
            assert expect == title, "断言出错，获取的应用标题为：{}, 预期结果为：{}".format(title, expect)
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.MASTER_HELPER.step(title='测试后台多应用管理卸载色卡应用用例')
    def test_uninstall_application(self, expect=False):
        try:
            self.driver.refresh()
            result = self.application_manage().uninstall_application()
            self.logger.info("获取的结果为：")
            self.logger.info(result)
            assert expect == result, "断言出错，获取的应用标题为：{}, 预期结果为：{}".format(result, expect)
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise
