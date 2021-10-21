import time

import allure
import pytest
from case import TestBase
from pages.shop.goods_terminal_page import PageGoodsInfoMinix
from pages.shop.home import ShopHomePageMinix


@allure.severity(allure.severity_level.CRITICAL)  # 阻塞
@allure.epic("前台：加购")
@allure.feature("商品加入购物车功能")
@allure.issue("https://template001.meshopstore.com")  # 前台地址
class TestShopCart(TestBase, ShopHomePageMinix, PageGoodsInfoMinix):
    url = 'https://template001.meshopstore.com'

    @allure.story("单件商品加入购物车")
    @allure.title('测试单件商品加入购物车的用例')
    @pytest.mark.parametrize("count, e_index, k_text,expect",
                             [('iphon', '0', 'iPhone 11pro max', 'Plastik')])
    def test_search_join_to_cart(self, count, e_index, k_text, expect):
        try:
            self.shop_home().goto_shop_search_page(count)
            self.shop_home().click_goods_name_two()
            self.driver.switch_to.window(self.driver.window_handles[-1])
            time.sleep(2)
            self.goods_info().select_goods_sku(e_index, k_text)
            time.sleep(3)
            self.goods_info().click_add_cart()
            time.sleep(5)
            # 断言
            goods_name = self.shop_home().page_get_cart_goods_title()
            self.logger.info("获取的商品标题为：")
            self.logger.info(goods_name)
            with allure.step('断言获取的商品标题，并截图'):
                self.screenshot()
            assert expect in goods_name, "断言出错，商品标题为：{}, 预期结果为：{}".format(goods_name, expect)
            time.sleep(2)
            self.shop_home().click_remove_goods()
        except Exception as e:
            # 日志
            self.logger.error(e)
            # 截图
            self.screenshot()
            # 抛异常
            raise

    @allure.story("多件商品加入购物车")
    @allure.title('测试多件商品加入购物车的用例')
    def test_more_goods_join_to_cart(self, count='iphon', e_index='0', k_text='iPhone 11pro'):
        self.driver.get('https://template001.meshopstore.com')
        time.sleep(2)
        self.shop_home().goto_shop_search_page(count)
        self.shop_home().click_goods_name_two()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        self.goods_info().select_goods_cart_buy(e_index, k_text)
        time.sleep(2)
        self.shop_home().close_mini_cart()
        time.sleep(4)
        self.shop_home().goto_shop_search_page(count)
        time.sleep(2)
        with allure.step('切换另一件商品，进入商品终端页'):
            self.driver.get(
                "https://template001.meshopstore.com/product/"
                "apple-iphones-hinterdeckel-stil-silizium-%E4%BF%9D%E6%8A%A4%E5%A5%97-%E5%A3%B3-1136529/")
        time.sleep(2)
        self.goods_info().click_add_cart()
        time.sleep(3)
        with allure.step('断言购物车是否加入两件了商品，并截图'):
            self.screenshot()
        time.sleep(2)
        self.shop_home().click_remove_goods()
        time.sleep(3)
        self.shop_home().click_remove_goods()

    @allure.story("编辑和修改商品信息并加入购物车")
    @allure.title('测试编辑和修改商品必选区信息并加购的用例')
    def test_update_few_join_to_cart(self, count='iphon', e_index='0', k_text='iPhone 11pro max'):
        self.driver.get('https://template001.meshopstore.com')
        time.sleep(2)
        self.shop_home().goto_shop_search_page(count)
        self.shop_home().click_goods_name_two()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.goods_info().select_goods_sku(e_index, k_text)
        time.sleep(3)
        self.goods_info().click_add_goods()
        self.goods_info().click_add_cart()
        time.sleep(3)
        with allure.step('断言增加商品数量加入购物车，并截图'):
            self.screenshot()
        self.shop_home().close_mini_cart()
        with allure.step('切换商品必选区'):
            self.goods_info().select_goods_sku(e_index="0", k_text="iPhone 11")
        time.sleep(2)
        self.goods_info().click_minus_goods()
        self.goods_info().click_add_cart()
        time.sleep(3)
        with allure.step('断言减少商品数量加入购物车，并截图'):
            self.screenshot()
        self.shop_home().close_mini_cart()
        with allure.step('切换商品必选区'):
            self.goods_info().select_goods_sku(e_index="0", k_text="iPhone 11pro")
        self.goods_info().input_goods_count(count=3)
        self.goods_info().click_add_cart()
        time.sleep(3)
        with allure.step('断言修改商品数量加入购物车商品数量，并截图'):
            self.screenshot()
        time.sleep(2)
        self.shop_home().click_remove_goods()
        time.sleep(2)
        self.shop_home().click_remove_goods()
        time.sleep(2)
        self.shop_home().click_remove_goods()

    @allure.story('删除迷你购物车的商品')
    @allure.title('测试删除迷你购物车商品的用例')
    def test_delete_cart_item(self):
        with allure.step('打开列表页，选择产品并进入商品终端页'):
            self.driver.get('https://template001.meshopstore.com/collections/auto/')
            time.sleep(3)
            self.driver.get(
                "https://template001.meshopstore.com/product/"
                "mid-calf-pleated-v-neck-three-quarter-sleeve-summer-womens-dress-1211467-100119/")
        self.goods_info().click_add_cart()
        time.sleep(3)
        self.shop_home().click_remove_goods()
        time.sleep(5)
        with allure.step('断言删除MINI购物车商品数量，并截图'):
            self.screenshot()

    @allure.story('编辑迷你购物车商品信息')
    @allure.title('测试编辑迷你购物车商品数量的用例')
    def test_edit_minn_cart_item(self):
        with allure.step('前台进入商品终端页'):
            self.driver.get('https://template001.meshopstore.com/product/'
                            'apple-iphones-hinterdeckel-stil-silizium-%E4%BF%9D%E6%8A%A4%E5%A5%97-%E5%A3%B3-1136529/')
        self.goods_info().click_add_cart()
        time.sleep(3)
        self.goods_info().click_mini_add_goods_plus()
        time.sleep(2)
        with allure.step('断言增加MINI购物车商品数量，并截图'):
            self.screenshot()
        self.goods_info().click_mini_minus_goods()
        time.sleep(2)
        with allure.step('断言减少MINI购物车商品数量，并截图'):
            self.screenshot()
        self.goods_info().input_mini_input_goods(count="5")
        time.sleep(5)
        with allure.step('断言编辑的迷你购物车商品数量，截图'):
            self.screenshot()
        time.sleep(2)
        self.shop_home().click_remove_goods()
