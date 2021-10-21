import time

import allure

import pages
from case import TestBase
from pages.admin.home import PageAdminHomeMinix
from pages.admin.index import PageAdminIndexMinix
from pages.admin.product_manage import PageProductManageMinix


class TestAdminReviews(TestBase, PageAdminHomeMinix, PageProductManageMinix,
                       PageAdminIndexMinix):
    # url = pages.admin.home_run_url

    url = pages.admin.home_url

    @allure.MASTER_HELPER.step(title='测试后台评论批量隐藏的用例')
    def test_reviews_batch_hiding(self):
        self.admin_home().goto_admin_login_page()
        time.sleep(3)
        # self.admin_home().admin_home_login_success()
        # time.sleep(3)
        self.admin_home().admin_home_login_report_ide_success()
        time.sleep(3)
        self.product_manage().click_icon_close()
        time.sleep(2)
        self.admin_index().click_product_manage()
        time.sleep(3)
        self.admin_index().click_product_reviews()
        time.sleep(3)
        self.product_manage().reviews_batch_hiding()

    @allure.MASTER_HELPER.step(title='测试后台评论批量显示的用例')
    def test_reviews_batch_display(self):
        self.driver.refresh()
        self.product_manage().reviews_batch_display()
        time.sleep(5)

    @allure.MASTER_HELPER.step(title='测试后台评论批量删除的用例')
    def test_reviews_batch_delete(self, email="981291891@qq.com", start_date="2021-01-01", start_time="00:00:00",
                                  end_date="2021-01-02", end_time="00:00:00"):
        self.product_manage().reviews_comment_del(email, start_date, start_time, end_date, end_time)
        time.sleep(5)

    @allure.MASTER_HELPER.step(title='测试后台导入评论的用例')
    def test_import_reviews(self):
        self.product_manage().reviews_import_comment()
        time.sleep(5)
