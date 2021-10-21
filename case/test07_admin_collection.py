import time

import allure
import pytest

import pages
from case import TestBase
from pages.admin.home import PageAdminHomeMinix
from pages.admin.index import PageAdminIndexMinix
from pages.admin.product_manage import PageProductManageMinix


class TestAdminCollection(TestBase, PageAdminHomeMinix, PageProductManageMinix,
                          PageAdminIndexMinix):
    # url = pages.admin.home_run_url

    url = pages.admin.home_url

    @allure.MASTER_HELPER.step(title='测试后台创建自动产品系列的用例')
    @pytest.mark.parametrize("collection_title,c_describe,day,page_title,describe_count,collections,expect",
                             [('testAuTocollection', "You can see the blade bears the marker's stamp", "100",
                               "test", "test", "testAuTocollection", "testAuTocollection")])
    def test_add_auto_collect(self, collection_title, c_describe, day, page_title, describe_count, collections,
                              expect):
        try:
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
            self.admin_index().click_product_family()
            time.sleep(3)
            self.product_manage().add_auto_collection(collection_title, c_describe, day, page_title,
                                                      describe_count)
            time.sleep(3)
            self.product_manage().input_coll_search(collections)
            time.sleep(2)
            self.product_manage().click_coll_search_btn()
            time.sleep(2)
            title = self.product_manage().get_product_collection_title()
            self.logger.info("获取的系列名称为：")
            self.logger.info(title)
            time.sleep(5)
            self.product_manage().del_search_collection()
            assert expect == title, "断言出错，获取的系列名称为：{}, 预期结果为：{}".format(title, expect)
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.MASTER_HELPER.step(title='测试后台创建手动产品系列的用例')
    def test_add_manual_collection(self, collection_title='testmanualcollection', collections="testmanualcollection",
                                   expect='testmanualcollection'):
        try:
            # self.admin_home().goto_admin_login_page()
            # time.sleep(3)
            # self.admin_home().admin_home_login_success()
            # time.sleep(3)
            # self.admin_home().admin_home_login_report_ide_success()
            # time.sleep(3)
            # self.product_manage().click_icon_close()
            # time.sleep(2)
            # self.admin_index().click_product_manage()
            # time.sleep(3)
            # self.admin_index().click_product_family()
            # time.sleep(3)
            self.driver.refresh()
            time.sleep(2)
            self.product_manage().add_manual_collection(collection_title)
            time.sleep(3)
            self.product_manage().input_coll_search(collections)
            time.sleep(2)
            self.product_manage().click_coll_search_btn()
            time.sleep(2)
            title = self.product_manage().get_product_collection_title()
            self.logger.info("获取的系列名称为：")
            self.logger.info(title)
            time.sleep(5)
            self.product_manage().del_search_collection()
            assert expect == title, "断言出错，获取的系列名称为：{}, 预期结果为：{}".format(title, expect)
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.MASTER_HELPER.step(title='测试后台手动产品系列筛选的用例')
    def test_manual_collection_screen(self, expect="—"):
        try:
            self.driver.refresh()
            time.sleep(2)
            self.product_manage().manual_collection_screen()
            conditions = self.product_manage().get_product_conditions()
            self.logger.info("获取的系列名称为：")
            self.logger.info(conditions)
            time.sleep(5)
            assert expect == conditions, "断言出错，获取的系列条件为：{}, 预期结果为：{}".format(conditions, expect)
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.MASTER_HELPER.step(title='测试后台产品系列排序产品spu排序的用例')
    @pytest.mark.parametrize("collection_title, day, coll_title, p_spu,location_index,loc_index,expect",
                             [('CollScreen', '200', 'CollScreen', "1016437", 6, 6, "iPhone")])
    def test_manual_collection_p_spu_screen(self, collection_title, day, coll_title, p_spu, location_index, loc_index,
                                            expect):
        try:
            # self.admin_home().goto_admin_login_page()
            # time.sleep(3)
            # self.admin_home().admin_home_login_success()
            # time.sleep(3)
            # self.admin_home().admin_home_login_report_ide_success()
            # time.sleep(3)
            # self.product_manage().click_icon_close()
            # time.sleep(2)
            # self.admin_index().click_product_manage()
            # time.sleep(3)
            # self.admin_index().click_product_family()
            # time.sleep(3)
            self.driver.refresh()
            time.sleep(2)
            self.product_manage().collection_series_sort_example(collection_title, day)
            self.product_manage().collection_series_sort_01(coll_title, p_spu, location_index, loc_index)
            self.driver.switch_to.window(self.driver.window_handles[-1])
            time.sleep(3)
            goods_title = self.product_manage().get_coll_sort_title()
            self.logger.info("获取的产品名称为：")
            self.logger.info(goods_title)
            assert expect == goods_title, "断言出错，获取的产品名称为：{}, 预期结果为：{}".format(goods_title, expect)
            time.sleep(5)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[-1])
            time.sleep(3)
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.MASTER_HELPER.step(title='测试后台产品系列排序产品id排序的用例')
    @pytest.mark.parametrize("coll_title, p_id,location_index,loc_index,expect",
                             [('CollScreen', "1", 5, 5, "iPhone")])
    def test_collection_p_id_screen(self, coll_title, p_id, location_index, loc_index,
                                    expect):
        try:
            # self.admin_home().goto_admin_login_page()
            # time.sleep(3)
            # self.admin_home().admin_home_login_success()
            # time.sleep(3)
            # self.admin_home().admin_home_login_report_ide_success()
            # time.sleep(3)
            # self.product_manage().click_icon_close()
            # time.sleep(2)
            # self.admin_index().click_product_manage()
            # time.sleep(3)
            self.driver.refresh()
            time.sleep(2)
            self.product_manage().collection_series_sort_02(coll_title, p_id, location_index, loc_index)
            self.driver.switch_to.window(self.driver.window_handles[-1])
            time.sleep(3)
            goods_title = self.product_manage().get_coll_sort_title()
            self.logger.info("获取的产品名称为：")
            self.logger.info(goods_title)
            assert expect == goods_title, "断言出错，获取的产品名称为：{}, 预期结果为：{}".format(goods_title, expect)
            time.sleep(3)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[-1])
            time.sleep(3)
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.MASTER_HELPER.step(title='测试后台产品系列排序获取产品spu的用例')
    def test_get_coll_sort_product_spu(self, expect='1016437'):
        try:
            spu = self.product_manage().collection_series_sort_03()
            self.logger.info("获取的产品spu为：")
            self.logger.info(spu)
            assert expect == spu, "断言出错，获取的产品名称为：{}, 预期结果为：{}".format(spu, expect)
            time.sleep(3)
            self.product_manage().click_coll_sort_sure_btn()
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.MASTER_HELPER.step(title='测试后台产品系列排序获取产品spu的用例')
    def test_get_coll_sort_product_id(self, expect='1'):
        try:
            p_id = self.product_manage().collection_series_sort_04()
            self.logger.info("获取的产品spu为：")
            self.logger.info(p_id)
            assert expect == p_id, "断言出错，获取的产品名称为：{}, 预期结果为：{}".format(p_id, expect)
            time.sleep(3)
            self.product_manage().click_coll_sort_sure_btn()
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.MASTER_HELPER.step(title='测试后台产品系列排序清空选中，选中置顶置底的用例')
    def test_coll_sort_other01(self):
        time.sleep(3)
        self.product_manage().collection_series_sort_05()

    @allure.MASTER_HELPER.step(title='测试后台产品系列排序点击下一页，对选中产品进行置顶的用例')
    def test_coll_sort_other02(self, collections='CollScreen'):
        self.product_manage().collection_series_sort_06()
        time.sleep(5)
        self.admin_index().click_product_family()
        self.product_manage().input_coll_search(collections)
        self.product_manage().click_coll_search_btn()
        self.product_manage().del_search_collection()
