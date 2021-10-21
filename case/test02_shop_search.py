import time

import allure
import pytest

from case import TestBase
from pages.shop.home import ShopHomePageMinix


@allure.severity(allure.severity_level.CRITICAL)  # 严重
@allure.epic("前台: 搜索")
@allure.feature("搜索功能")
@allure.issue("https://template001.meshopstore.com")  # 前台地址
class TestShopSearch(TestBase, ShopHomePageMinix):
    url = 'https://template001.meshopstore.com'

    @allure.story("搜索商品spu")
    @allure.title("测试搜索商品spu的用例")
    @pytest.mark.parametrize("count,expect", [("100130", "1 results for 100130")])
    def test_search_spu(self, count, expect):
        try:
            self.shop_home().goto_shop_search_page(count)
            time.sleep(3)
            # 断言
            number_results = self.shop_home().get_goods_index()
            self.logger.info("获取的搜索结果数量为：")
            self.logger.info(number_results)
            with allure.step('断言，搜索商品的spu'):
                assert expect in number_results, "断言出错，搜索结果为：{}, 预期结果为：{}".format(number_results, expect)
                self.screenshot()
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.story("搜索商品标题")
    @allure.title("测试搜索商品标题的用例")
    @pytest.mark.parametrize("count,expect", [("iphone", "iPhone")])
    def test_search_title(self, count, expect):
        try:
            self.shop_home().goto_shop_search_page(count)
            time.sleep(3)
            # 断言
            goods_name = self.shop_home().get_goods_name()
            self.logger.info("获取的商品标题为：")
            self.logger.info(goods_name)
            with allure.step('断言，搜索结果标题'):
                assert expect in goods_name, "断言出错，搜索结果为：{}, 预期结果为：{}".format(goods_name, expect)
                self.screenshot()
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.story("搜索结果页翻页")
    @allure.title("测试搜索结果页翻页")
    def test_search_turn_page(self, count="1"):
        self.shop_home().goto_shop_search_page(count)
        time.sleep(3)
        self.shop_home().click_next_page()
        time.sleep(3)
        with allure.step('截图'):
            self.screenshot()
        self.shop_home().click_prev_page()
        time.sleep(3)
        with allure.step('截图'):
            self.screenshot()
