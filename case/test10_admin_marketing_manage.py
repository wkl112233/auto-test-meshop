import time

import allure
import pytest

import pages
from case import TestBase
from pages.admin.home import PageAdminHomeMinix
from pages.admin.index import PageAdminIndexMinix
from pages.admin.product_manage import PageProductManageMinix
from pages.admin.marketing_manage import PageMarketingManageMinix


class TestAdminMarketing(TestBase, PageAdminHomeMinix, PageProductManageMinix,
                         PageAdminIndexMinix, PageMarketingManageMinix):
    url = pages.admin.home_run_url

    # url = pages.admin.home_url

    @allure.MASTER_HELPER.step(title='测试后台关闭邮件的用例')
    def test_email_close(self, expect="不发送"):
        try:
            self.admin_home().goto_admin_login_page()
            time.sleep(3)
            self.admin_home().admin_home_login_success()
            time.sleep(3)
            # self.admin_home().admin_home_login_report_ide_success()
            # time.sleep(3)
            # self.product_manage().click_icon_close()
            # time.sleep(2)
            self.admin_index().click_marketing_management()
            time.sleep(2)
            self.admin_index().click_mail_marketing()
            time.sleep(2)
            self.marketing_manage().close_payment_success()
            state = self.marketing_manage().get_email_state()
            self.logger.info("获取的邮件状态为：")
            self.logger.info(state)
            assert expect == state, "断言出错，获取的邮件状态为：{}, 预期结果为：{}".format(state, expect)
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.MASTER_HELPER.step(title='测试后台打开邮件的用例')
    def test_email_open(self, expect="发送"):
        try:
            self.marketing_manage().open_payment_success()
            state = self.marketing_manage().get_email_state()
            self.logger.info("获取的邮件状态为：")
            self.logger.info(state)
            assert expect == state, "断言出错，获取的邮件状态为：{}, 预期结果为：{}".format(state, expect)
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.MASTER_HELPER.step(title='测试后台编辑邮件标题的用例')
    def test_edit_email_title(self, email_title="Complete", expect="Complete"):
        try:
            time.sleep(3)
            self.marketing_manage().edit_email_title(email_title)
            title = self.marketing_manage().get_email_title()
            self.logger.info("获取的邮件标题为：")
            self.logger.info(title)
            assert expect == title, "断言出错，获取的邮件标题为：{}, 预期结果为：{}".format(title, expect)
            self.marketing_manage().edit_email_title(email_title="Complete Payment Successfully！")
            time.sleep(3)
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise


class TestAdminCustomScript(TestBase, PageAdminHomeMinix, PageProductManageMinix,
                            PageAdminIndexMinix, PageMarketingManageMinix):
    url = pages.admin.home_run_url

    # url = pages.admin.home_url

    @allure.MASTER_HELPER.step(title='测试后台编辑添加营销代码的用例')
    def test_add_custom_script(self, market_theme="testscript", page=2,
                               custom_script="Hello ,world!",
                               expect="testscript"):
        try:
            self.admin_home().goto_admin_login_page()
            time.sleep(3)
            self.admin_home().admin_home_login_success()
            time.sleep(3)
            # self.admin_home().admin_home_login_report_ide_success()
            # time.sleep(3)
            # self.product_manage().click_icon_close()
            # time.sleep(2)
            self.admin_index().click_marketing_management()
            time.sleep(2)
            self.admin_index().click_marketing_code()
            time.sleep(2)
            self.marketing_manage().add_custom_script(market_theme, page, custom_script)
            time.sleep(3)
            theme = self.marketing_manage().get_script_theme()
            self.logger.info("获取的邮件标题为：")
            self.logger.info(theme)
            assert expect == theme, "断言出错，获取的邮件标题为：{}, 预期结果为：{}".format(theme, expect)
            time.sleep(3)
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.MASTER_HELPER.step(title='测试后台编辑营销代码的用例')
    def test_edit_custom_script(self,
                                custom_script='''<button class="button1" onclick='alert("run!")'>点击我，我是广告</button>''',
                                expect="底部"):

        try:
            self.marketing_manage().edit_custom_script(custom_script)
            time.sleep(3)
            location = self.marketing_manage().get_script_display_location()
            self.logger.info("获取的邮件展示位置为：")
            self.logger.info(location)
            assert expect == location, "断言出错，获取的邮件标题为：{}, 预期结果为：{}".format(location, expect)
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.MASTER_HELPER.step(title='测试后台编辑删除营销代码的用例')
    def test_custom_script_del(self, expect=False):

        try:
            script_id = self.marketing_manage().get_script_id()
            self.marketing_manage().delete_custom_script()
            time.sleep(3)
            result = self.marketing_manage().custom_script_if_delete(script_id)
            self.logger.info("获取的结果为：")
            self.logger.info(result)
            assert expect == result, "断言出错，获取的邮件标题为：{}, 预期结果为：{}".format(result, expect)
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise


class TestDataTracking(TestBase, PageAdminHomeMinix, PageProductManageMinix,
                       PageAdminIndexMinix, PageMarketingManageMinix):
    url = pages.admin.home_run_url

    # url = pages.admin.home_url

    @allure.MASTER_HELPER.step(title='测试后台编辑数据追踪的用例')
    @pytest.mark.parametrize("face_book_pixel, google_analytics, google_ads, google_ads_event",
                             [("123456789045465", "G-R2QHE175ES,UA-151452317-2", "UA-34oepwoo",
                               "UA-34oepwoo/eososos")])
    def test_edit_data_tracking(self, face_book_pixel, google_analytics, google_ads, google_ads_event):
        self.admin_home().goto_admin_login_page()
        time.sleep(3)
        self.admin_home().admin_home_login_success()
        time.sleep(3)
        # self.admin_home().admin_home_login_report_ide_success()
        # time.sleep(3)
        # self.product_manage().click_icon_close()
        # time.sleep(2)
        self.admin_index().click_marketing_management()
        time.sleep(2)
        self.admin_index().click_data_tracking()
        time.sleep(2)
        self.marketing_manage().edit_data_tracking_01()
        time.sleep(3)
        self.marketing_manage().edit_data_tracking_02(face_book_pixel, google_analytics, google_ads, google_ads_event)
        time.sleep(5)
