import time

import allure
import pytest

import pages
from case import TestBase
from pages.admin.home import PageAdminHomeMinix
from pages.admin.index import PageAdminIndexMinix
from pages.admin.product_manage import PageProductManageMinix


class TestAdminAddProduct(TestBase, PageAdminHomeMinix, PageProductManageMinix,
                          PageAdminIndexMinix):
    url = pages.admin.admin_login_url
    # url = pages.admin.admin_login_run_url
    # url = pages.admin.admin_login_me_url

    @allure.MASTER_HELPER.step(title='测试后台添加产品的用例')
    @pytest.mark.parametrize("ipu_title,ipt_spu,count,title, expect",
                             [('test001', '10086110', 'white', 'test001', True)])
    def test_add_products(self, ipu_title, ipt_spu, count, title, expect):
        self.admin_home().admin_home_login_report_ide_success()
        time.sleep(3)
        # 调用添加产品业务方法
        self.product_manage().click_icon_close()
        time.sleep(2)
        self.admin_index().click_product_manage()
        time.sleep(3)
        self.admin_index().click_all_product()
        time.sleep(3)
        self.product_manage().add_products(ipu_title, ipt_spu, count)
        time.sleep(3)
        try:
            result = self.product_manage().add_product_if_success()
            self.logger.info("获取的结果消息为：")
            self.logger.info(result)
            # 断言
            assert expect == result
            time.sleep(3)
            self.product_manage().edit_product_del(title)
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.MASTER_HELPER.step(title='测试后台添加产品失败的用例')
    def test_add_products_file_01(self, expect="Size不能为空"):
        try:
            # 调用添加产品业务方法
            time.sleep(3)
            self.product_manage().click_add_products()
            time.sleep(4)
            self.product_manage().input_add_title(ipu_title="test002")
            time.sleep(4)
            self.product_manage().click_save_btn_top()
            masg = self.product_manage().get_fail_msag()
            self.logger.info("获取的提示消息为：")
            self.logger.info(masg)
            assert expect in masg, "断言出错，获取的消息为：{}, 预期结果为：{}".format(masg, expect)
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.MASTER_HELPER.step(title='测试后台添加产品失败的用例')
    def test_add_products_file_02(self, expect="标题不能为空,链接不能为空,Size不能为空"):
        try:
            self.driver.refresh()
            # 调用添加产品业务方法
            time.sleep(3)
            self.product_manage().input_add_spu(ipt_spu="10086")
            time.sleep(4)
            self.product_manage().click_save_btn_top()
            masg1 = self.product_manage().get_fail_msag_1()
            masg2 = self.product_manage().get_fail_msag_2()
            masg3 = self.product_manage().get_fail_msag_3()
            self.logger.info("获取的提示消息为：")
            self.logger.info(masg1)
            self.logger.info(masg2)
            self.logger.info(masg3)
            assert expect in masg1 or masg2 or masg3, "断言出错，获取的消息为：{}, 预期结果为：{}".format(masg1, masg2, masg3, expect)
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.MASTER_HELPER.step(title='测试后台添加产品失败的用例')
    def test_add_products_file_03(self, expect="标题不能为空,链接不能为空"):
        try:
            self.driver.refresh()
            time.sleep(3)
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(3)
            self.product_manage().input_property_count(count='yello')
            time.sleep(3)
            self.product_manage().click_save_btn()
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(2)
            self.product_manage().click_save_btn_top()
            time.sleep(3)
            masg1 = self.product_manage().get_fail_msag_1()
            masg2 = self.product_manage().get_fail_msag_2()
            self.logger.info("获取的提示消息为：")
            self.logger.info(masg1)
            self.logger.info(masg2)
            assert expect in masg1 or masg2, "断言出错，获取的消息为：{}, 预期结果为：{}".format(masg1, masg2, expect)
            self.product_manage().click_cancel_btn_top()
            time.sleep(2)
            self.product_manage().click_discard_changes_btn()
            time.sleep(2)
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.MASTER_HELPER.step(title='测试后台添加产品的用例')
    @pytest.mark.parametrize(
        "ipu_title, ipt_spu, ipu_pdc_key, ipt_pdc_class, i_describe, count, "
        " count_2,count_3, page_title, search_disc, s_describe,inside_links,title,expect",
        [('test10086', '1008611', 'new', 'sdsdsd',
          'Recommendation for you Collection list1 Text advertisements share '
          'website activities, product descriptions and other information for '
          'users, and are welcome messages for users to browse the website.', "xl", 'red', '1.0 Mather', 'test10086',
          'test10086', 'test10086', 'test10086', 'test10086', True)])
    def test_add_products_all(self, ipu_title, ipt_spu, ipu_pdc_key, ipt_pdc_class, i_describe,
                              count, count_2, count_3, page_title, search_disc, s_describe,
                              inside_links, title, expect):

        # self.admin_home().admin_home_login_report_ide_success()
        # time.sleep(3)
        # self.product_manage().click_icon_close()
        # time.sleep(2)
        # self.admin_index().click_product_manage()
        # time.sleep(3)
        # self.admin_index().click_all_product()
        # time.sleep(3)
        # 调用添加产品业务方法
        self.driver.refresh()
        time.sleep(2)
        self.product_manage().click_add_products()
        time.sleep(4)
        self.product_manage().page_add_product(ipu_title, ipt_spu, ipu_pdc_key, ipt_pdc_class,
                                               i_describe,
                                               count, count_2, count_3,
                                               page_title, search_disc, s_describe, inside_links)
        try:
            result = self.product_manage().add_product_if_success()
            self.logger.info("获取的结果消息为：")
            self.logger.info(result)
            # 断言
            assert expect == result
            time.sleep(3)
            self.product_manage().edit_product_del(title)
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.MASTER_HELPER.step(title='测试后台添加导入产品的用例')
    def test_add_import_products(self, title="测试1", expect=True):
        # self.admin_home().admin_home_login_report_ide_success()
        # time.sleep(3)
        # 调用添加产品业务方法
        # self.product_manage().click_icon_close()
        # time.sleep(2)
        # self.admin_index().click_product_manage()
        # time.sleep(3)
        # self.admin_index().click_all_product()
        time.sleep(3)
        self.product_manage().add_import_products()
        try:
            result = self.product_manage().add_product_if_success()
            self.logger.info("获取的结果消息为：")
            self.logger.info(result)
            time.sleep(3)
            self.product_manage().edit_product_del(title)
            # 断言
            assert expect == result
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise


class TestAdminEditProduct(TestBase, PageAdminHomeMinix, PageProductManageMinix,
                           PageAdminIndexMinix):
    url = pages.admin.home_run_url

    # url = pages.admin.admin_login_url

    @allure.MASTER_HELPER.step(title='测试后台产品下架的用例')
    @pytest.mark.parametrize("ipu_title,ipt_spu,count,title",
                             [('test0000', '1008611', 'BLUE', 'test0000')])
    def test_down_products(self, ipu_title, ipt_spu, count, title, expect="下架"):
        try:
            self.admin_home().goto_admin_login_page()
            time.sleep(3)
            self.admin_home().admin_home_login_success()
            # self.admin_home().admin_home_login_reportide_success()
            time.sleep(3)
            self.product_manage().click_icon_close()
            # time.sleep(2)
            self.admin_index().click_product_manage()
            time.sleep(3)
            self.admin_index().click_all_product()
            time.sleep(3)
            self.product_manage().add_products(ipu_title, ipt_spu, count)
            # 调用添加产品业务方法
            self.product_manage().edit_product_down(title)
            product_status = self.product_manage().get_product_status_down()
            self.logger.info("获取的产品状态为：")
            self.logger.info(product_status)
            assert expect == product_status, "断言出错，获取的产品状态为：{}, 预期结果为：{}".format(product_status, expect)
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.MASTER_HELPER.step(title='测试后台产品下架的用例')
    def test_up_products(self, expect="上架"):
        try:
            self.product_manage().edit_product_up()
            product_status = self.product_manage().get_product_status_up()
            self.logger.info("获取的产品状态为：")
            self.logger.info(product_status)
            assert expect == product_status, "断言出错，获取的产品状态为：{}, 预期结果为：{}".format(product_status, expect)
            self.product_manage().click_search_product()
            self.product_manage().edit_test_product_del()
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.MASTER_HELPER.step(title='测试后台产品删除的用例')
    @pytest.mark.parametrize("ipu_title,ipt_spu,count,title",
                             [('testdel', '1000', 'BLUE', 'testdel')])
    def test_delete_products(self, ipu_title, ipt_spu, count, title, expect=False):
        try:
            self.product_manage().add_products(ipu_title, ipt_spu, count)
            product_id = self.product_manage().get_add_goods_id()
            self.product_manage().edit_product_del(title)
            result = self.product_manage().base_if_text_exists_element(product_id)
            time.sleep(3)
            self.logger.info("获取的结果消息为：")
            self.logger.info(result)
            assert expect == result
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.MASTER_HELPER.step(title='测试后台产品固定金额批量改价的用例')
    @pytest.mark.parametrize("ipu_title,ipt_spu, count,title,price",
                             [('testchange', '1000', 'BLUE', 'testchange', "100")])
    def test_product_fixed_price_change(self, ipu_title, ipt_spu, count, title, price, expect="100.00"):
        try:
            self.product_manage().add_products(ipu_title, ipt_spu, count)
            self.product_manage().edit_fixed_price_change(title, price)
            pice = (self.product_manage().get_product_price())[-6:]
            time.sleep(3)
            self.logger.info("获取的结果消息为：")
            self.logger.info(pice)
            assert expect == pice
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.MASTER_HELPER.step(title='测试后台产品系数批量改价的用例')
    def test_product_coefficient_price_change(self, price="0.5", expect="50.00"):
        try:
            self.product_manage().edit_coefficient_price_change(price)
            pice = (self.product_manage().get_product_price())[-5:]
            self.logger.info("获取的结果消息为：")
            self.logger.info(pice)
            assert expect == pice
            self.product_manage().edit_test_product_del()
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.MASTER_HELPER.step(title='测试后台产品id搜索产品的用例')
    def test_search_products_useid(self, ipu_title="testsearchID", ipt_spu='1008611', count='blue',
                                   expect="testsearchID"):
        try:
            self.driver.refresh()
            self.product_manage().add_products(ipu_title, ipt_spu, count)
            product_id = self.product_manage().get_add_goods_id()
            self.product_manage().edit_product_search_id(i_d=product_id)
            goods_title = self.product_manage().get_add_goods_title()
            self.logger.info("获取的产品标题为：")
            self.logger.info(goods_title)
            assert expect == goods_title
            self.product_manage().click_search_product()
            self.product_manage().edit_test_product_del()
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.MASTER_HELPER.step(title='测试后台产品spuid搜索产品的用例')
    @pytest.mark.parametrize("ipu_title,ipt_spu, count,i_d,expect",
                             [('testsearchSPUID', '1008611', 'BLUE', '1008611', "testsearchSPUID")])
    def test_search_products_usespuid(self, ipu_title, ipt_spu, count, i_d, expect):
        try:
            self.driver.refresh()
            self.product_manage().add_products(ipu_title, ipt_spu, count)
            self.product_manage().edit_product_search_spuid(i_d)
            goods_title = self.product_manage().get_add_goods_title()
            self.logger.info("获取的产品标题为：")
            self.logger.info(goods_title)
            assert expect == goods_title
            self.product_manage().click_search_product()
            self.product_manage().edit_test_product_del()
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.MASTER_HELPER.step(title='测试产品下架状态筛选的用例')
    def test_products_search_down(self, text="上架", expect=False):
        try:
            self.driver.refresh()
            self.product_manage().product_search_down()
            result = self.product_manage().base_if_text_down_element(text)
            self.logger.info("获取的结果状态为：")
            self.logger.info(result)
            assert expect == result, "断言出错，获取的结果为：{}, 预期结果为：{}".format(result, expect)
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.MASTER_HELPER.step(title='测试产品系列名称筛选的用例')
    def test_down_products_select(self, input_line="new", expect="new"):
        try:
            self.driver.refresh()
            result = self.product_manage().product_series_name_search(input_line)
            assert expect == result, "断言出错，获取的搜索结果为：{}, 预期结果为：{}".format(result, expect)
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.MASTER_HELPER.step(title='测试综合业务（进入产品编辑页入口和产品分页的用例）')
    def test_goto_products_paging(self, expect=("已选择 30 件产品", "已选择 40 件产品", "已选择 50 件产品")):
        try:
            # self.admin_home().goto_admin_login_page()
            # time.sleep(3)
            # self.admin_home().admin_home_login_success()
            # self.admin_home().admin_home_login_reportide_success()
            # time.sleep(3)
            # self.product_manage().click_icon_close()
            # time.sleep(2)
            # self.admin_index().click_product_manage()
            # time.sleep(3)
            # self.admin_index().click_all_product()
            # time.sleep(3)
            self.driver.refresh()
            result = (self.product_manage().integrated_business())
            assert expect == result, "断言出错，获取的搜索结果为：{}, 预期结果为：{}".format(result, expect)
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise
