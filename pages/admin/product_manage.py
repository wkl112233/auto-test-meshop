import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pages
from pages.pagebase import PageBase


class PageProductManageMinix:
    def product_manage(self):
        if not getattr(self, '_add_product', None):
            self._product_manage = PageProductManage(self.driver)
        return self._product_manage


class PageProductManage(PageBase):
    """
    产品管理页
    """

    # 点击添加产品
    def click_add_products(self):
        self.click(pages.admin.add_product)

    # 输入产品标题
    def input_add_title(self, ipu_title):
        self.input(pages.admin.ipu_title, ipu_title)

    # 输入spu
    def input_add_spu(self, ipt_spu):
        self.input(pages.admin.ipt_spu, ipt_spu)

    # 点击产品系列
    def click_product_collection(self):
        self.click(pages.admin.ipt_pdc_line)

    # 输入系列关键字
    def input_product_collection_keyword(self, ipu_pdc_key):
        self.input(pages.admin.ipu_pdc_key, ipu_pdc_key)

    # 点击选择关键系列
    def click_selected_product_collection_keyword(self):
        self.click(pages.admin.selc_pdc_key)

    # 输入 产品分类
    def input_product_category(self, ipt_pdc_class):
        self.input(pages.admin.ipt_pdc_class, ipt_pdc_class)

    # 添加分类
    def click_add_category(self):
        self.click(pages.admin.add_class)

    # 输入标签
    def input_product_label(self, inp_pdc_label):
        self.input(pages.admin.inp_pdc_label, inp_pdc_label)

    # 添加标签
    def click_product_label(self):
        element = self.find_element_func(pages.admin.inp_pdc_label)
        time.sleep(2)
        ActionChains(self.driver).move_to_element(element).perform()
        time.sleep(2)
        element.click()

    # 添加标签
    def click_add_label(self):
        self.click(pages.admin.add_label)

    # 点击产品级别
    def click_product_level(self):
        self.click(pages.admin.ipt_pdc_level)

    # 选择级别
    def click_quality_goods(self):
        self.click(pages.admin.quality_goods)

    def click_one_level(self):
        self.click(pages.admin.one_level)

    def click_second_level(self):
        self.click(pages.admin.second_level)

    def click_three_level(self):
        self.click(pages.admin.three_level)

    def click_high_risk_pdc(self):
        self.click(pages.admin.high_risk)

    def click_extremely_risky_pdc(self):
        self.click(pages.admin.extremely_risky)

    # 选择上架下架开关
    def click_select_up_pdc(self):
        self.click(pages.admin.select_up_pdc)

    # 输入产品描述
    def input_add_product_describe(self, i_describe):
        iframe = self.find_element_func(pages.admin.describe_iframe)
        self.driver.switch_to.frame(iframe)
        time.sleep(2)
        self.input(pages.admin.i_describe, i_describe)
        self.driver.switch_to.default_content()

    # 输入产品系列描述
    def input_add_collection_describe(self, c_describe):
        iframe = self.find_element_func(pages.admin.describe_iframe)
        self.driver.switch_to.frame(iframe)
        time.sleep(2)
        self.input(pages.admin.i_describe, c_describe)
        self.driver.switch_to.default_content()

    # 添加图片
    def click_pdc_img(self):
        # self.click_red_find_element(pages.admin.add_img)
        time.sleep(3)
        self.find_element_func((By.CLASS_NAME, "el-upload__input")).send_keys(
            r"C:/meshop-auto-test/image/05.png")
        # r"C:/project/meshop-auto-test/image/05.png")
        # os.system(str(BASE_DIR + '\\data\\shop_data\\upimage_pc.exe'))
        # os.system(str(BASE_DIR + '\\data\\shop_data\\upimage_book.exe'))
        time.sleep(3)

    # 多属性开关

    def click_attribute_switch(self):
        self.click(pages.admin.attribute_switch)

    # 添加其他属性选项
    def click_add_other_properties(self):
        self.click(pages.admin.add_other_properties)

    # 属性选项1
    def input_property_option_one(self, property_option_one):
        self.input(pages.admin.property_option_one, property_option_one)

    # 选项 内容
    def input_property_count(self, count):
        self.input(pages.admin.property_count, count)

    # 属性选项2
    def input_property_option_two(self, property_option_two):
        pass
        self.input(pages.admin.property_option_two, property_option_two)

    # 属性选项3
    def click_property_option_three(self):
        pass

    # 输入页面标题
    def input_page_title(self, page_title):
        self.input(pages.admin.page_title, page_title)

    # 输入搜素引擎描述
    def input_search_disc(self, search_disc):
        self.input(pages.admin.search_describe, search_disc)

    def input_disc(self, s_describe):
        self.input(pages.admin.s_describe, s_describe)

    # 输入内部优化链接
    def input_inside_links(self, inside_links):
        self.input(pages.admin.inside_links, inside_links)

    # 保存添加产品按钮
    def click_save_btn(self):
        self.click(pages.admin.save_btn)

    # 点击顶部保存按钮
    def click_save_btn_top(self):
        self.click(pages.admin.save_btn_top)

    # 点击顶部取消按钮
    def click_cancel_btn_top(self):
        self.click(pages.admin.cancel_btn)

    # 点击放弃修改
    def click_discard_changes_btn(self):
        self.click(pages.admin.give_up_eid)

    # 获取产品ID
    def get_add_goods_id(self):
        return self.text(pages.admin.goods_id)

    # 获取产品名称
    def get_add_goods_title(self):
        return self.text(pages.admin.goods_title)

    # 获取保存成功消息
    def get_save_success_msg(self):
        return self.text(pages.admin.save_msg)

    # 获取失败的信息“SIZE不能为空”
    def get_fail_msag(self):
        return self.text(pages.admin.msage)

    # 获取失败的信息1标题不能为空
    def get_fail_msag_1(self):
        return self.text(pages.admin.msage_1)

    # 获取失败的信息2链接不能为空
    def get_fail_msag_2(self):
        return self.text(pages.admin.msage_2)

    # 获取失败的信息3size不能为空
    def get_fail_msag_3(self):
        return self.text(pages.admin.msage_3)

    # 点击关闭底部到期通条
    def click_icon_close(self):
        self.click((By.CSS_SELECTOR, 'i[class="el-icon-close"]'))

    # 编辑产品SKU
    def edit_product_rep_sku(self, retail_price, market_price, cost_price, weight, sku):
        pass
        self.input((By.CSS_SELECTOR,
                    'td[class="el-table_8_column_49_column_50 is-center "]>div>div>input'),
                   retail_price)
        self.input((By.CSS_SELECTOR,
                    'td[class="el-table_8_column_49_column_51 is-center "]>div>div>input'),
                   market_price)
        self.input((By.CSS_SELECTOR,
                    'td[class="el-table_8_column_49_column_52 is-center "]>div>div>input'),
                   cost_price)
        self.input((By.CSS_SELECTOR,
                    'td[class="el-table_8_column_53 is-center "]>div>div>input'),
                   weight)
        self.input((By.CSS_SELECTOR,
                    'td[class="el-table_8_column_54 is-center "]>div>div>input'),
                   sku)

    def edit_product_run_sku(self, retail_price, market_price, cost_price, weight, sku):
        pass
        self.input((By.CSS_SELECTOR, 'td[class="el-table_4_column_23_column_24 is-center "]>div>div>input'),
                   retail_price)
        self.input((By.CSS_SELECTOR, 'td[class="el-table_4_column_23_column_25 is-center "]>div>div>input'),
                   market_price)
        self.input((By.CSS_SELECTOR, 'td[class="el-table_4_column_23_column_26 is-center "]>div>div>input'),
                   cost_price)
        self.input((By.CSS_SELECTOR, 'td[class="el-table_4_column_27 is-center "]>div>div>input'),
                   weight)
        self.input((By.CSS_SELECTOR, 'td[class="el-table_4_column_28 is-center "]>div>div>input'),
                   sku)

    """
    组合业务（添加产品）
    """

    def page_add_product(self, ipu_title, ipt_spu, ipu_pdc_key, ipt_pdc_class, i_describe,
                         count, count_2, count_3, page_title, search_disc, s_describe,
                         inside_links):
        self.input_add_title(ipu_title)
        time.sleep(5)
        self.input_add_spu(ipt_spu)
        time.sleep(5)
        self.click_product_collection()
        time.sleep(2)
        self.input_product_collection_keyword(ipu_pdc_key)
        time.sleep(5)
        self.click_selected_product_collection_keyword()
        time.sleep(3)
        self.click_product_collection()
        time.sleep(2)
        self.input_product_category(ipt_pdc_class)
        time.sleep(3)
        self.click_add_category()
        time.sleep(2)
        self.click_product_label()
        time.sleep(3)
        self.click_add_label()
        time.sleep(3)
        self.click_product_level()
        time.sleep(2)
        self.click_one_level()
        time.sleep(2)
        self.click_product_level()
        time.sleep(2)
        self.click_select_up_pdc()
        time.sleep(2)
        self.click_select_up_pdc()
        time.sleep(2)
        self.input_add_product_describe(i_describe)
        time.sleep(2)
        self.click_pdc_img()
        time.sleep(2)
        self.input_property_count(count)
        time.sleep(2)
        self.click_add_other_properties()
        time.sleep(2)
        self.input_property_count(count_2)
        time.sleep(2)
        self.click_add_other_properties()
        time.sleep(2)
        self.input_property_count(count_3)
        time.sleep(2)
        self.input_page_title(page_title)
        time.sleep(2)
        self.input_search_disc(search_disc)
        time.sleep(2)
        self.input_disc(s_describe)
        time.sleep(2)
        self.input_inside_links(inside_links)
        time.sleep(2)
        self.click_save_btn()
        time.sleep(4)
        product_id = self.get_add_goods_id()
        self.logger.info("获取的产品ID为：{}".format(product_id))

    def add_products(self, ipu_title, ipt_spu, count):
        self.logger.info("正在调用添加产品业务方法，标题title：{} 产品spu: {} 属性内容：{}".format(ipu_title, ipt_spu, count))
        self.click_add_products()
        time.sleep(6)
        self.input_add_title(ipu_title)
        time.sleep(3)
        self.input_add_spu(ipt_spu)
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)
        self.input_property_count(count)
        time.sleep(3)
        self.click_save_btn()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        self.click_save_btn()
        product_id = self.get_add_goods_id()
        self.logger.info("获取的产品ID为：{}".format(product_id))

    def add_import_products(self):
        self.click(pages.admin.imp_products)
        time.sleep(3)
        # self.click_find_element((By.XPATH, '//span[text()="选取文件"]'))
        # time.sleep(3)
        self.find_element_func((By.CLASS_NAME, "el-upload__input")).send_keys(
            r"C:/meshop-auto-test/data/template.xls")
        # r"C:/project/meshop-auto-test/data/template.xls")
        # os.system(str(BASE_DIR + '\\data\\shop_data\\uptmplate.exe'))
        # os.system(str(BASE_DIR + '\\data\\shop_data\\tmplate_book.exe'))
        time.sleep(3)
        self.click_find_element((By.XPATH, '//span[text()="上传到服务器"]'))
        time.sleep(3)
        self.driver.refresh()

    # 导入测试后台订单列表产品
    def import_test_order_products(self):
        self.click(pages.admin.imp_products)
        time.sleep(3)
        self.find_element_func((By.CLASS_NAME, "el-upload__input")).send_keys(
            r"C:/meshop-auto-test/data/template_001.xls")
        # r"C:/project/meshop-auto-test/data/template_001.xls")
        time.sleep(3)
        self.click_find_element((By.XPATH, '//span[text()="上传到服务器"]'))
        time.sleep(6)
        self.driver.refresh()

    # 判断产品ID
    def add_product_if_success(self):
        product_id = self.get_add_goods_id()
        return self.base_if_text_exists_element(product_id)

    # 获取产品上架状态
    def get_product_status_up(self):
        return self.text((By.CSS_SELECTOR, 'div[class="common-state-tag-container"]>span[class="tag success"]'))

    # 获取产品下架状态
    def get_product_status_down(self):
        return self.text((By.CSS_SELECTOR, 'div[class="common-state-tag-container"]>span[class="tag info"]'))

    # 获取产品价格
    def get_product_price(self):
        return self.text((By.CSS_SELECTOR, 'span[class="product-sellperice"]'))

    # 获取列表全选文本
    def get_product_select(self):
        return self.text((By.CSS_SELECTOR, 'span[class="selection-count-select"]'))

    # 获取产品系列标题文本
    def get_product_collection_title(self):
        return self.text((By.CSS_SELECTOR, 'tr:nth-child(1) > td> div > a > span'))

    # 点击搜索产品列表中的第一个产品
    def click_search_product(self):
        element = self.find_element_func(pages.admin.search_product_click)
        time.sleep(2)
        element.click()

    # 点击变价按钮
    def click_edit(self):
        element = self.find_element_func(pages.admin.click_edit)
        ActionChains(self.driver).move_to_element(element).perform()
        time.sleep(3)
        element.click()

    # 点击批量改价
    def click_change_sell(self):
        element = self.find_element_func(pages.admin.click_change_sell)
        ActionChains(self.driver).move_to_element(element).perform()
        time.sleep(3)
        element.click()

    # 点击批量改价弹窗确定按钮
    def click_change_btn(self):
        element = self.find_element_func(pages.admin.change_sell_btn)
        self.driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            element,
            "border: 2px solid red;")
        time.sleep(2)
        ActionChains(self.driver).move_to_element(element).perform()
        time.sleep(2)
        element.click()

    # 点击状态筛选
    def click_status_filter(self):
        self.click(pages.admin.status_filter)

    # 点击筛选下架按钮
    def click_status_down(self):
        element = self.find_element_func(pages.admin.status_down)
        self.driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            element,
            "border: 2px solid red;")
        time.sleep(2)
        ActionChains(self.driver).move_to_element(element).perform()
        time.sleep(2)
        element.click()

    # 点击id筛选下的产品ID
    def click_id_filter_btn(self):
        element = self.find_element_func(pages.admin.id_filter_btn)
        self.driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            element,
            "border: 2px solid red;")
        time.sleep(2)
        ActionChains(self.driver).move_to_element(element).perform()
        time.sleep(2)
        element.click()

    # 点击产品系列名称下筛选的系列名称
    def click_line_name(self):
        element = self.find_element_func(pages.admin.line_name)
        time.sleep(2)
        ActionChains(self.driver).move_to_element(element).perform()
        time.sleep(2)
        element.click()

    # 点击产品图片
    def click_product_img(self):
        element = self.find_element_func(pages.admin.product_img)
        self.driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            element,
            "border: 2px solid red;")
        time.sleep(2)
        ActionChains(self.driver).move_to_element(element).perform()
        time.sleep(2)
        element.click()

    # 点击产品标题
    def click_product_title(self):
        element = self.find_element_func(pages.admin.product_title)
        self.driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            element,
            "border: 2px solid red;")
        time.sleep(2)
        ActionChains(self.driver).move_to_element(element).perform()
        time.sleep(2)
        element.click()

    # 点击产品小本图标
    def click_product_icon(self):
        element = self.find_element_func(pages.admin.product_icon)
        self.driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            element,
            "border: 2px solid red;")
        time.sleep(2)
        ActionChains(self.driver).move_to_element(element).perform()
        time.sleep(2)
        element.click()

    # 点击产品前台查看
    def click_product_see(self):
        element = self.find_element_func(pages.admin.product_see)
        self.driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            element,
            "border: 2px solid red;")
        time.sleep(2)
        ActionChains(self.driver).move_to_element(element).perform()
        time.sleep(2)
        element.click()

    """
    组合业务（编辑产品下架）
    """

    def edit_product_down(self, title):
        self.input(pages.admin.search_product, title)
        self.click(pages.admin.search_btn)
        time.sleep(8)
        self.click_search_product()
        self.click_edit()
        down_data_click = self.find_element_func((By.XPATH, '//*[text()="产品下架"]'))
        ActionChains(self.driver).move_to_element(down_data_click).perform()
        time.sleep(2)
        down_data_click.click()
        time.sleep(3)

    """
    组合业务（编辑产品上架）
    """

    def edit_product_up(self):
        self.click_search_product()
        self.click_edit()
        down_data_click = self.find_element_func((By.XPATH, '//*[text()="产品上架"]'))
        ActionChains(self.driver).move_to_element(down_data_click).perform()
        time.sleep(2)
        down_data_click.click()
        time.sleep(3)

    """
    组合业务（编辑产品删除）
    """

    def edit_product_del(self, title):
        self.input(pages.admin.search_product, title)
        time.sleep(3)
        self.click(pages.admin.search_btn)
        time.sleep(8)
        self.click_search_product()
        self.click_edit()
        down_data_click = self.find_element_func((By.XPATH, '//*[text()="删除所选产品"]'))
        ActionChains(self.driver).move_to_element(down_data_click).perform()
        time.sleep(2)
        down_data_click.click()
        time.sleep(3)
        self.click((By.CSS_SELECTOR, 'button[class="el-button el-button--danger"]'))
        time.sleep(3)
        self.driver.refresh()

    """
    组合业务（编辑测试的产品删除）
    """

    def edit_test_product_del(self):
        self.click_edit()
        down_data_click = self.find_element_func((By.XPATH, '//*[text()="删除所选产品"]'))
        ActionChains(self.driver).move_to_element(down_data_click).perform()
        time.sleep(2)
        down_data_click.click()
        time.sleep(3)
        self.click((By.CSS_SELECTOR, 'button[class="el-button el-button--danger"]'))
        time.sleep(3)

    """
    组合业务（编辑产品批量改价）
    """

    def edit_fixed_price_change(self, title, price):
        self.input(pages.admin.search_product, title)
        self.click(pages.admin.search_btn)
        time.sleep(8)
        self.click_search_product()
        time.sleep(3)
        self.click_change_sell()
        time.sleep(3)
        self.input((By.CSS_SELECTOR, 'input[placeholder="固定金额"]'), price)
        time.sleep(3)
        self.click((By.CSS_SELECTOR, 'button[class="el-button el-button--primary"]'))
        time.sleep(3)

    def edit_coefficient_price_change(self, price):
        self.click_change_sell()
        time.sleep(3)
        self.click_change_btn()
        time.sleep(3)
        self.input((By.CSS_SELECTOR, 'input[placeholder="系数"]'), price)
        time.sleep(2)
        self.click((By.CSS_SELECTOR, 'button[class="el-button el-button--primary"]'))
        time.sleep(3)

    """
    组合业务（产品搜索）
    """

    def edit_product_search_id(self, i_d):
        self.click(pages.admin.id_filter)
        time.sleep(2)
        self.click_id_filter_btn()
        time.sleep(2)
        self.input(pages.admin.search_product, i_d)
        time.sleep(3)
        self.click(pages.admin.search_btn)
        time.sleep(5)

    def edit_product_search_spuid(self, i_d):
        self.input(pages.admin.search_product, i_d)
        time.sleep(3)
        self.click(pages.admin.search_btn)
        time.sleep(5)

    """
    组合业务（产品状态筛选下架产品筛选）
    """

    def product_search_down(self):
        self.click_status_filter()
        time.sleep(2)
        self.click_status_down()
        time.sleep(2)
        self.click(pages.admin.search_btn)
        time.sleep(2)

    """
    组合业务（产品系列名称筛选）
    """

    def product_series_name_search(self, input_line):
        self.click(pages.admin.product_line)
        time.sleep(2)
        self.input(pages.admin.input_line, input_line)
        time.sleep(2)
        self.click_line_name()
        time.sleep(3)
        self.click(pages.admin.screen_btn)
        time.sleep(3)
        return self.text((By.CSS_SELECTOR, 'span[class="tagtext"]'))

    """
    综合业务（进入产品页编辑，产品列表翻页）
    """

    def integrated_business(self):
        time.sleep(3)
        self.click_product_img()
        time.sleep(3)
        self.click((By.XPATH, "//span[text()='返回']"))
        self.driver.refresh()
        self.click_product_title()
        time.sleep(3)
        self.click((By.XPATH, "//span[text()='返回']"))
        self.driver.refresh()
        self.click_product_icon()
        time.sleep(3)
        self.click((By.XPATH, "//span[text()='返回']"))
        self.driver.refresh()
        self.click_product_see()
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(8)
        self.driver.close()
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(3)
        self.driver.refresh()
        time.sleep(2)
        self.click_find_element(pages.admin.please_select)
        time.sleep(2)
        self.click_find_element(pages.admin.page_30)
        time.sleep(2)
        self.click_find_element(pages.admin.select_result)
        time.sleep(3)
        text_1 = self.get_product_select()
        self.click(pages.admin.please_select)
        time.sleep(2)
        self.click_find_element(pages.admin.page_40)
        time.sleep(2)
        self.click_find_element(pages.admin.select_result)
        time.sleep(3)
        text_2 = self.get_product_select()
        self.click(pages.admin.please_select)
        time.sleep(2)
        self.click_find_element(pages.admin.page_50)
        time.sleep(2)
        self.click_find_element(pages.admin.select_result)
        time.sleep(3)
        text_3 = self.get_product_select()
        time.sleep(3)
        return text_1, text_2, text_3

    # 获取产品系列标题
    def get_coll_title(self):
        return self.text((By.CSS_SELECTOR, 'tr[class="el-table__row"]>td:nth-child(2)>div>a>span'))

    # 输入搜索产品系列标题
    def input_coll_search(self, collections):
        self.input((By.CSS_SELECTOR, 'input[placeholder="搜索产品系列"]'), collections)

    # 点击搜素系列按钮
    def click_coll_search_btn(self):
        self.click((By.CSS_SELECTOR, 'button[class="el-button search-btn el-button--info el-button--medium"]'))

    # 点击删除搜素系列
    def del_search_collection(self):
        self.click_find_element((By.CSS_SELECTOR, 'thead[class="has-gutter"]>tr>th>div>label>span'))
        time.sleep(2)
        self.click((By.CSS_SELECTOR, 'ul>li:nth-child(2)>button>span'))
        time.sleep(2)
        self.click((By.CSS_SELECTOR, 'span[class="dialog-footer"]>button:nth-child(2)>span'))
        time.sleep(3)

    """
    组合业务（创建自动产品系列产品）
    """

    def add_auto_collection(self, collection_title, c_describe, day, page_title, describe_count):
        self.click((By.XPATH, '//span[text()="创建产品系列"]'))
        time.sleep(3)
        self.input((By.CSS_SELECTOR, 'textarea[class="el-textarea__inner"]'), collection_title)
        time.sleep(3)
        loc_1 = self.find_element_func((By.CSS_SELECTOR,
                                        'div:nth-child(1)>div>input[accept="image/jpeg,image/jpg,image/png,image/gif"]'))
        self.driver.execute_script('arguments[0].removeAttribute(\"style\")', loc_1)
        time.sleep(3)
        loc_1.send_keys(
            r"C:/meshop-auto-test/image/01.jpg")
        # r"C:/project/meshop-auto-test/image/01.jpg")
        time.sleep(3)
        loc_2 = self.find_element_func((By.CSS_SELECTOR,
                                        'div:nth-child(2)>div>input[accept="image/jpeg,image/jpg,image/png,image/gif"]'))
        self.driver.execute_script('arguments[0].removeAttribute(\"style\")', loc_2)
        time.sleep(3)
        loc_2.send_keys(
            r"C:/meshop-auto-test/image/01.jpg")
        # r"C:/project/meshop-auto-test/image/02.jpg")
        time.sleep(3)
        self.click_find_element((By.CSS_SELECTOR, ' label:nth-child(3) > span.el-radio__input > span'))
        time.sleep(2)
        # self.click_find_element((By.CSS_SELECTOR, 'div:nth-child(3) > div > div.el-radio-group > '
        # 'label:nth-child(2) > span.el-radio__input > span'))
        # time.sleep(2)
        # self.click_find_element((By.CSS_SELECTOR, 'div:nth-child(3) > div > div.el-radio-group > '
        # 'label:nth-child(1) > span.el-radio__input > span'))
        # time.sleep(2)
        self.input_add_collection_describe(c_describe)
        time.sleep(3)
        self.click_find_element(
            (By.CSS_SELECTOR, 'ul > li:nth-child(1) > div:nth-child(1) > label > span.el-radio__input > span'))
        time.sleep(3)
        self.click_find_element((By.CSS_SELECTOR,
                                 'div.collections-type-wrapper > div > ul > li:nth-child(2) > '
                                 'div:nth-child(1) > label > span.el-radio__input > span'))
        time.sleep(3)
        self.click_find_element((By.CSS_SELECTOR, 'div.conditions-match-wrapper > div > div > label:nth-child(2) > '
                                                  'span.el-radio__input > span'))
        time.sleep(3)
        # self.click_find_element(
        # (By.CSS_SELECTOR, 'div:nth-child(2) > div > div.basic-layout-wrapper.automated-conditions > '
        # 'div.conditions-match-wrapper > div > div > label:nth-child(1) '
        # '> span.el-radio__input > span'))
        # time.sleep(3)
        self.click((By.CSS_SELECTOR, 'input[placeholder="请选择"]'))
        time.sleep(3)
        self.click((By.XPATH, '//span[text()="上架时间"]'))
        time.sleep(3)
        self.input((By.CSS_SELECTOR, 'input[placeholder="请输入"]'), day)
        time.sleep(3)
        # self.click_red_find_element((By.XPATH, "//span[text()='添加其他条件']"))
        # time.sleep(3)
        # self.click((By.CSS_SELECTOR, 'div>div:nth-child(4)>div>div>div>form>div>div>div>div>div>div>input'))
        # time.sleep(3)
        # self.click_red_find_element((By.CSS_SELECTOR, ':nth-child(7)>div>div>ul>li:nth-child(3)>span'))
        # time.sleep(3)
        # self.click((By.CSS_SELECTOR, 'div:nth-child(4)>div>div>div>form>div>div:nth-child(2)>'
        # 'div>div>div>form>div>div>div>div>div>div>input'))
        # time.sleep(3)
        # self.click_red_find_element((By.CSS_SELECTOR, 'body>:nth-child(8)>div>div>ul>li:nth-child(1)'))
        # time.sleep(3)
        # self.input((By.CSS_SELECTOR, 'div:nth-child(4) >div>div:nth-child(1)>div>form>div>div>div>div>'
        # 'div>form>div>div:nth-child(2)>div>div>div>input'), label_title)
        self.input((By.CSS_SELECTOR, 'div:nth-child(3) > div > div:nth-child(1) > div > div > textarea'), page_title)
        time.sleep(2)
        self.input((By.CSS_SELECTOR, 'div:nth-child(3) > div > div > textarea'), describe_count)
        time.sleep(2)
        self.click((By.CSS_SELECTOR, ' footer > div > div > button > span'))

    """
    组合业务（创建手动产品系列产品）
    """

    def add_manual_collection(self, collection_title):
        self.click((By.XPATH, '//span[text()="创建产品系列"]'))
        time.sleep(3)
        self.input((By.CSS_SELECTOR, 'textarea[class="el-textarea__inner"]'), collection_title)
        self.driver.execute_script("var q=document.documentElement.scrollTop=8000")
        time.sleep(3)
        self.click_find_element(
            (By.CSS_SELECTOR, 'ul > li:nth-child(1) > div:nth-child(1) > label > span.el-radio__input > span'))
        time.sleep(3)
        self.click((By.CSS_SELECTOR, ' footer > div > div > button > span'))

    # 获取产品条件
    def get_product_conditions(self):
        return self.text((By.CSS_SELECTOR, 'tbody:nth-child(2)>tr>td:nth-child(3)>div>div'))

    """
    组合业务（手动产品系列筛选）
    """

    def manual_collection_screen(self):
        self.click_find_element((By.CSS_SELECTOR, 'div:nth-child(2)>div>div>div>div>span>button>span>span'))
        time.sleep(2)
        self.click_red_find_element((By.CSS_SELECTOR, 'label:nth-child(2)>span>span'))
        time.sleep(2)
        self.click_coll_search_btn()
        time.sleep(2)

    # 产品排序选中产品移动到位置
    def move_to_location(self, location_index):
        loc = By.CSS_SELECTOR, 'ul:nth-child(8)>li:nth-child({})'.format(location_index)
        self.click_red_find_element(loc)

    def open_to_location_product(self, loc_index):
        loc = By.CSS_SELECTOR, 'div:nth-child(2)>div>div>ul>li:nth-child({})>a:nth-child(2)>i'.format(loc_index)
        self.click_red_find_element(loc)

    # 获取产品排序搜索产品标题
    def get_coll_sort_title(self):
        return self.text((By.XPATH, '//*[text()="iPhone"]'))

    # 点击产品排序弹窗确认按钮
    def click_coll_sort_sure_btn(self):
        self.click((By.CSS_SELECTOR, 'div.el-message-box__wrapper>div>div.el-message-box__btns>button'))

    """
    组合业务（产品系列手动排序）
    """

    def collection_series_sort_example(self, collection_title, day):
        self.click((By.XPATH, '//span[text()="创建产品系列"]'))
        time.sleep(3)
        self.input((By.CSS_SELECTOR, 'textarea[class="el-textarea__inner"]'), collection_title)
        time.sleep(3)
        loc_1 = self.find_element_func((By.CSS_SELECTOR,
                                        'div:nth-child(1)>div>input[accept="image/jpeg,image/jpg,image/png,image/gif"]'))
        self.driver.execute_script('arguments[0].removeAttribute(\"style\")', loc_1)
        time.sleep(3)
        loc_1.send_keys(
            r"C:/meshop-auto-test/image/01.jpg")
        # r"C:/project/meshop-auto-test/image/01.jpg")
        time.sleep(3)
        loc_2 = self.find_element_func((By.CSS_SELECTOR,
                                        'div:nth-child(2)>div>input[accept="image/jpeg,image/jpg,image/png,image/gif"]'))
        self.driver.execute_script('arguments[0].removeAttribute(\"style\")', loc_2)
        time.sleep(3)
        loc_2.send_keys(
            r"C:/meshop-auto-test/image/02.jpg")
        # r"C:/project/meshop-auto-test/image/02.jpg")
        time.sleep(3)
        self.click((By.CSS_SELECTOR, 'input[placeholder="请选择"]'))
        time.sleep(3)
        self.click((By.XPATH, '//span[text()="上架时间"]'))
        time.sleep(3)
        self.input((By.CSS_SELECTOR, 'input[placeholder="请输入"]'), day)
        time.sleep(3)
        self.click((By.CSS_SELECTOR, ' footer > div > div > button > span'))
        time.sleep(3)

    def collection_series_sort_01(self, coll_title, p_spu, location_index, loc_index):
        self.click(pages.admin.product_sequencing)
        time.sleep(2)
        self.input((By.CSS_SELECTOR, 'input[placeholder="请输入产品系列"]'), coll_title)
        time.sleep(2)
        self.click((By.CSS_SELECTOR, 'div[class="search-container"]>div>div>div>button'))
        time.sleep(3)
        self.click_find_element((By.CSS_SELECTOR, 'div:nth-child(2)>ul>li>div>div'))
        self.click((By.CSS_SELECTOR, 'input[placeholder="请选择"]'))
        time.sleep(2)
        self.click((By.XPATH, '//span[text()="手动排序"]'))
        time.sleep(3)
        self.click(
            (By.CSS_SELECTOR, 'button:nth-child(2)>span'))
        time.sleep(20)
        self.input((By.CSS_SELECTOR, 'input[placeholder="默认spu/产品标题搜索"]'), p_spu)
        self.click((By.XPATH, '//span[text()="选中"]'))
        time.sleep(4)
        self.click_coll_sort_sure_btn()
        time.sleep(3)
        self.click_find_element(
            (By.CSS_SELECTOR, 'div[class="top-bar-content"]>div>div:nth-child(2)>div:nth-child(6)>button>span'))
        self.move_to_location(location_index)
        time.sleep(2)
        self.click((By.CSS_SELECTOR, 'button:nth-child(11)>span'))
        time.sleep(20)
        self.open_to_location_product(loc_index)
        time.sleep(3)

    def collection_series_sort_02(self, coll_title, p_id, location_index, loc_index):
        self.click(pages.admin.product_sequencing)
        time.sleep(2)
        self.input((By.CSS_SELECTOR, 'input[placeholder="请输入产品系列"]'), coll_title)
        time.sleep(2)
        self.click((By.CSS_SELECTOR, 'div[class="search-container"]>div>div>div>button'))
        time.sleep(3)
        self.click_red_find_element((By.CSS_SELECTOR, 'div:nth-child(2)>ul>li>div>div'))
        time.sleep(2)
        self.click_find_element((By.CSS_SELECTOR, 'div:nth-child(2)>div>div>input[placeholder="请选择"]'))
        self.click_find_element((By.XPATH, '//span[text()="产品ID"]'))
        self.input((By.CSS_SELECTOR, 'input[placeholder="默认spu/产品标题搜索"]'), p_id)
        self.click((By.XPATH, '//span[text()="选中"]'))
        time.sleep(4)
        self.click_coll_sort_sure_btn()
        time.sleep(3)
        self.click_find_element(
            (By.CSS_SELECTOR, 'div[class="top-bar-content"]>div>div:nth-child(2)>div:nth-child(6)>button>span'))
        self.move_to_location(location_index)
        time.sleep(2)
        self.click((By.CSS_SELECTOR, 'button:nth-child(11)>span'))
        time.sleep(20)
        self.open_to_location_product(loc_index)
        time.sleep(3)

    def collection_series_sort_03(self):
        self.click((By.XPATH, '//span[text()="选中"]'))
        time.sleep(4)
        self.click_coll_sort_sure_btn()
        time.sleep(3)
        self.click((By.XPATH, '//span[text()="获取SPU"]'))
        time.sleep(3)
        return self.text((By.CSS_SELECTOR, 'div>div:nth-child(2)>div>div>p'))

    def collection_series_sort_04(self, p_spu='1016437'):
        self.click_find_element((By.CSS_SELECTOR, 'div:nth-child(2)>div>div>input[placeholder="请选择"]'))
        self.click_find_element((By.XPATH, '//span[text()="默认"]'))
        self.input((By.CSS_SELECTOR, 'input[placeholder="默认spu/产品标题搜索"]'), p_spu)
        self.click((By.XPATH, '//span[text()="选中"]'))
        time.sleep(4)
        self.click_coll_sort_sure_btn()
        time.sleep(2)
        self.click((By.XPATH, '//span[text()="获取ID"]'))
        time.sleep(3)
        return self.text((By.CSS_SELECTOR, 'div>div:nth-child(2)>div>div>p'))

    def collection_series_sort_05(self):
        self.click((By.XPATH, '//span[text()="清空选中"]'))
        self.click((By.XPATH, '//span[text()="选中"]'))
        time.sleep(4)
        self.click_coll_sort_sure_btn()
        time.sleep(2)
        self.click((By.XPATH, '//span[text()="置底"]'))
        time.sleep(2)
        self.click((By.XPATH, '//span[text()="选中"]'))
        time.sleep(2)
        self.click_coll_sort_sure_btn()
        self.click((By.XPATH, '//span[text()="置顶"]'))

    def collection_series_sort_06(self):
        self.click((By.XPATH, '//span[text()="选中"]'))
        time.sleep(4)
        self.click_coll_sort_sure_btn()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)
        self.click((By.XPATH, '//span[text()="下一页"]'))
        time.sleep(3)
        self.click((By.XPATH, '//span[text()="置底"]'))

    """
    组合业务（产品评论）
    """

    def reviews_batch_display(self):
        self.click_find_element((By.CSS_SELECTOR, 'thead:nth-child(2)>tr>th>div>label>span>span'))
        time.sleep(3)
        self.click((By.CSS_SELECTOR, 'div[class="mb15 flex-item"]>button:nth-child(1)>span'))

    def reviews_batch_hiding(self):
        self.click_find_element((By.CSS_SELECTOR, 'thead:nth-child(2)>tr>th>div>label>span>span'))
        time.sleep(3)
        self.click((By.CSS_SELECTOR, 'button:nth-child(2)>span'))

    def reviews_batch_delete(self):
        self.click_find_element((By.CSS_SELECTOR, 'thead:nth-child(2)>tr>th>div>label>span>span'))
        time.sleep(3)
        self.click((By.CSS_SELECTOR, 'button:nth-child(3)>span'))

    def reviews_import_comment(self):
        self.click((By.CSS_SELECTOR, 'button:nth-child(5)>span'))
        # self.click_find_element((By.XPATH, '//span[text()="选取文件"]'))
        time.sleep(3)
        self.find_element_func((By.CLASS_NAME, "el-upload__input")).send_keys(
            r"C:/meshop-auto-test/data/reviews_tmplate.xls")
        # r"C:/project/meshop-auto-test/data/reviews_tmplate.xls")
        # os.system(str(BASE_DIR + '\\data\\shop_data\\reviews.exe'))
        # os.system(str(BASE_DIR + '\\data\\shop_data\\reviews_book.exe'))
        time.sleep(3)
        self.click_red_find_element((By.XPATH, '//span[text()="上传到服务器"]'))
        time.sleep(3)

    def reviews_comment_del(self, email, start_date, start_time, end_date, end_time):
        self.reviews_import_comment()
        self.click((By.XPATH, '//span[text()="更多筛选 "]'))
        time.sleep(2)
        self.click((By.CSS_SELECTOR, 'div[class="el-collapse"]>div>div>div'))
        time.sleep(2)
        self.input((By.CSS_SELECTOR, 'input[placeholder="请输入邮箱"]'), email)
        time.sleep(4)
        self.click((By.CSS_SELECTOR, 'div[class="el-collapse"]>div:nth-child(2)>div>div'))
        time.sleep(2)
        self.click_find_element((By.CSS_SELECTOR, 'div>span:nth-child(3)>i'))
        time.sleep(2)
        self.click((By.CSS_SELECTOR, 'div[class="el-collapse"]>div:nth-child(4)>div>div'))
        time.sleep(2)
        self.click_find_element((By.CSS_SELECTOR, 'label[class="el-radio"]>span>span'))
        time.sleep(2)
        self.click((By.CSS_SELECTOR, 'div[class="el-collapse"]>div:nth-child(3)>div>div'))
        time.sleep(2)
        self.click((By.CSS_SELECTOR, 'input[placeholder="开始日期"]'))
        time.sleep(2)
        self.input((By.CSS_SELECTOR, 'input[placeholder="开始日期"][class="el-input__inner"]'), start_date)
        self.input((By.CSS_SELECTOR, 'input[placeholder="开始时间"][class="el-input__inner"]'), start_time)
        self.input((By.CSS_SELECTOR, 'input[placeholder="结束日期"][class="el-input__inner"]'), end_date)
        self.input((By.CSS_SELECTOR, 'input[placeholder="结束时间"][class="el-input__inner"]'), end_time)
        time.sleep(2)
        self.click((By.CSS_SELECTOR, 'div[class="el-picker-panel__footer"]>button:nth-child(2)>span'))
        time.sleep(2)
        self.click((By.XPATH, '//span[text()="完成"]'))
        time.sleep(4)
        self.reviews_batch_delete()
