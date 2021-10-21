import time

from selenium.webdriver import ActionChains

import pages
from selenium.webdriver.common.by import By
from pages.pagebase import PageBase


class PageMarketingManageMinix:
    def marketing_manage(self):
        if not getattr(self, '_add_product', None):
            self._marketing_manage = PageMarketingManage(self.driver)
        return self._marketing_manage


class PageMarketingManage(PageBase):
    """
    营销管理页
    """

    # 点击编辑关闭支付成功邮件
    def open_payment_success(self):
        self.click_red_find_element((By.CSS_SELECTOR, 'tr>td:nth-child(2)>div'))
        time.sleep(2)
        self.click((By.XPATH, '//span[text()="编辑邮件"]'))
        time.sleep(2)
        self.click((By.CSS_SELECTOR, 'div:nth-child(4)>div>div>label:nth-child(2)>span'))
        time.sleep(2)
        self.click((By.CSS_SELECTOR, 'button[class="el-button el-button--primary el-button--medium"]'))

    def close_payment_success(self):
        self.click_find_element((By.CSS_SELECTOR, 'tr>td:nth-child(2)>div'))
        time.sleep(2)
        self.click((By.XPATH, '//span[text()="编辑邮件"]'))
        time.sleep(2)
        self.click((By.CSS_SELECTOR, 'div:nth-child(4)>div>div>label:nth-child(1)>span'))
        time.sleep(2)
        self.click((By.CSS_SELECTOR, 'button[class="el-button el-button--primary el-button--medium"]'))

    # 点击编辑关闭发货邮件
    def close_send_goods(self):
        self.click_find_element((By.CSS_SELECTOR, 'tr[class="el-table__row el-table__row--striped"]'
                                                  '>td:nth-child(2)>div'))
        time.sleep(2)
        self.click((By.XPATH, '//span[text()="编辑邮件"]'))
        time.sleep(2)
        self.click((By.CSS_SELECTOR, 'div:nth-child(4)>div>div>label:nth-child(1)>span'))
        time.sleep(2)
        self.click((By.CSS_SELECTOR, 'button[class="el-button el-button--primary el-button--medium"]'))

    # 点击编辑关闭忘记密码邮件
    def close_forge_password(self):
        self.click_find_element((By.CSS_SELECTOR, 'tr:nth-child(3)>td:nth-child(2)>div'))
        time.sleep(2)
        self.click((By.XPATH, '//span[text()="编辑邮件"]'))
        time.sleep(2)
        self.click((By.CSS_SELECTOR, 'div:nth-child(4)>div>div>label:nth-child(1)>span'))
        time.sleep(2)
        self.click((By.CSS_SELECTOR, 'button[class="el-button el-button--primary el-button--medium"]'))

    # 编辑邮件标题
    def edit_email_title(self, email_title):
        self.click_find_element((By.CSS_SELECTOR, 'tr>td:nth-child(2)>div'))
        time.sleep(2)
        self.click((By.XPATH, '//span[text()="编辑邮件"]'))
        time.sleep(2)
        self.input((By.CSS_SELECTOR, 'input[class="el-input__inner"]'), email_title)
        time.sleep(2)
        self.click((By.CSS_SELECTOR, 'button[class="el-button el-button--primary el-button--medium"]'))

    # 获取邮件发送状态
    def get_email_state(self):
        return self.text((By.CSS_SELECTOR, 'tr>td:nth-child(4)>div'))

    # 获取邮件标题
    def get_email_title(self):
        return self.text((By.CSS_SELECTOR, 'tr>td:nth-child(3)>div>span'))

    # 选择营销代码显示页面
    def select_display_page(self, page):
        loc = By.CSS_SELECTOR, 'div:nth-child(7)>div>div>ul>li:nth-child({})>span'.format(page)
        self.click_find_element(loc)

    # 选择营销代码显示页面位置为头部
    def select_script_location_top(self):
        # self.click_find_element((By.CSS_SELECTOR, 'div:nth-child(7)>div>div>ul>li:nth-child(1)>span'))
        self.click_find_element((By.CSS_SELECTOR, 'div:nth-child(8)>div>div>ul>li:nth-child(1)>span'))

    # 选择营销代码显示页面位置为底部
    def select_script_location_down(self):
        # self.click_find_element((By.CSS_SELECTOR, 'div:nth-child(7)>div>div>ul>li:nth-child(2)>span'))
        self.click_find_element((By.CSS_SELECTOR, 'div:nth-child(8)>div>div>ul>li:nth-child(2)>span'))

    # 判断代码是否删除成功
    def custom_script_if_delete(self, script_id):
        return self.base_if_text_exists_element(script_id)

    # 获取邮件标题
    def get_script_theme(self):
        return self.text((By.CSS_SELECTOR, 'tr:last-child>td:nth-child(2)>div>span'))

    # 获取邮件展示位置
    def get_script_display_location(self):
        return self.text((By.CSS_SELECTOR, 'tr:last-child>td:nth-child(4)>div>span'))

    # 获取邮件标题
    def get_script_id(self):
        return self.text((By.CSS_SELECTOR, 'tr:last-child>td>div>span'))

    # 添加自定义脚本
    def add_custom_script(self, market_theme, page, custom_script):
        self.click((By.XPATH, '//span[text()="添加自定义脚本"]'))
        time.sleep(2)
        self.input((By.CSS_SELECTOR, 'div[class="el-form-item is-required"]>div>div>input'), market_theme)
        self.click((By.CSS_SELECTOR, 'input[placeholder="请选择页面"]'))
        self.select_display_page(page)
        time.sleep(2)
        self.click((By.CSS_SELECTOR, 'div>div:nth-child(2)>span:nth-child(2)>span>i'))
        self.click((By.CSS_SELECTOR, 'input[placeholder="请选择位置"]'))
        self.select_script_location_top()
        time.sleep(2)
        self.input((By.CSS_SELECTOR, 'textarea[placeholder="请输入内容"]'), custom_script)
        time.sleep(2)
        self.click((By.CSS_SELECTOR, 'button[class="el-button el-button--primary"]'))

    # 编辑自定义脚本
    def edit_custom_script(self, custom_script):
        self.click_find_element((By.CSS_SELECTOR, 'tr:last-child>td:nth-child(2)>div>span'))
        time.sleep(2)
        self.click_find_element((By.CSS_SELECTOR, 'tr:last-child>td:nth-child(5)>div>button>span>svg'))
        time.sleep(2)
        self.click((By.CSS_SELECTOR, 'div>div:nth-child(2)>span:nth-child(2)>span>i'))
        self.click_find_element((By.CSS_SELECTOR, 'label[class="el-checkbox"]>span'))
        self.click((By.CSS_SELECTOR, 'div>div:nth-child(2)>span:nth-child(2)>span>i'))
        self.click((By.CSS_SELECTOR, 'input[placeholder="请选择位置"]'))
        self.select_script_location_down()
        time.sleep(2)
        self.input((By.CSS_SELECTOR, 'textarea[placeholder="请输入内容"]'), custom_script)
        time.sleep(2)
        self.click((By.CSS_SELECTOR, 'button[class="el-button el-button--primary"]'))

    # 删除自定义脚本
    def delete_custom_script(self):
        self.click_red_find_element((By.CSS_SELECTOR, 'tr:last-child>td>div>span'))
        time.sleep(3)
        self.click_find_element((By.CSS_SELECTOR, 'tr:last-child>td:nth-child(5)>div>button>span>i'))
        time.sleep(3)

    # 添加数据追踪
    def add_data_tracking(self, face_book_pixel, google_analytics, google_ads, google_ads_event):
        self.input(
            (By.CSS_SELECTOR, 'form>div:nth-child(1)>div:nth-child(2)>div>div>div:nth-child(2)>div>div>div>textarea'),
            face_book_pixel)
        self.input(
            (By.CSS_SELECTOR, 'form>div:nth-child(2)>div:nth-child(2)>div>div>div:nth-child(2)>div>div>div>textarea'),
            google_analytics)
        self.input((By.CSS_SELECTOR,
                    'form>div:nth-child(2)>div:nth-child(2)>div:nth-child(2)'
                    '>div>div:nth-child(2)>div>div>div>textarea'),
                   google_ads)
        self.input((By.CSS_SELECTOR,
                    'form>div:nth-child(2)>div:nth-child(2)>div:nth-child(3)'
                    '>div>div:nth-child(2)>div>div>div>textarea'),
                   google_ads_event)
        time.sleep(3)
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        time.sleep(4)
        self.click((By.XPATH, '//span[text()="保存"]'))

    # 编辑数据追踪
    def edit_data_tracking_01(self, face_book_pixel="test", google_analytics="test", google_ads="test",
                              google_ads_event="test"):
        self.click((By.CSS_SELECTOR, 'form>div:nth-child(1)>div:nth-child(2)>div>div>div>div>button>span'))
        time.sleep(2)
        self.input(
            (By.CSS_SELECTOR, 'form>div:nth-child(1)>div:nth-child(2)>div>div>div:nth-child(2)>div>div>div>textarea'),
            face_book_pixel)
        self.click((By.CSS_SELECTOR, 'div:nth-child(2)>div:nth-child(2)>div>div>div>div>button>span'))
        time.sleep(2)
        self.input(
            (By.CSS_SELECTOR, 'form>div:nth-child(2)>div:nth-child(2)>div>div>div:nth-child(2)>div>div>div>textarea'),
            google_analytics)
        self.click((By.CSS_SELECTOR, 'div:nth-child(2)>div:nth-child(2)>div:nth-child(2)>div>div>div>button>span'))
        time.sleep(2)
        self.input((By.CSS_SELECTOR,
                    'form>div:nth-child(2)>div:nth-child(2)>div:nth-child(2)'
                    '>div>div:nth-child(2)>div>div>div>textarea'),
                   google_ads)
        self.click((By.CSS_SELECTOR, 'div:nth-child(2)>div:nth-child(2)>div:nth-child(3)>div>div>div>button>span'))
        time.sleep(2)
        self.input((By.CSS_SELECTOR,
                    'form>div:nth-child(2)>div:nth-child(2)>div:nth-child(3)'
                    '>div>div:nth-child(2)>div>div>div>textarea'),
                   google_ads_event)
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        time.sleep(3)
        self.click((By.XPATH, '//span[text()="保存"]'))

    def edit_data_tracking_02(self, face_book_pixel, google_analytics, google_ads,
                              google_ads_event):
        self.click((By.CSS_SELECTOR, 'form>div:nth-child(1)>div:nth-child(2)>div>div>div>div>button>span'))
        time.sleep(2)
        self.input(
            (By.CSS_SELECTOR, 'form>div:nth-child(1)>div:nth-child(2)>div>div>div:nth-child(2)>div>div>div>textarea'),
            face_book_pixel)
        self.click((By.CSS_SELECTOR, 'div:nth-child(2)>div:nth-child(2)>div>div>div>div>button>span'))
        time.sleep(2)
        self.input(
            (By.CSS_SELECTOR, 'form>div:nth-child(2)>div:nth-child(2)>div>div>div:nth-child(2)>div>div>div>textarea'),
            google_analytics)
        self.click((By.CSS_SELECTOR, 'div:nth-child(2)>div:nth-child(2)>div:nth-child(2)>div>div>div>button>span'))
        time.sleep(2)
        self.input((By.CSS_SELECTOR,
                    'form>div:nth-child(2)>div:nth-child(2)>div:nth-child(2)'
                    '>div>div:nth-child(2)>div>div>div>textarea'),
                   google_ads)
        self.click((By.CSS_SELECTOR, 'div:nth-child(2)>div:nth-child(2)>div:nth-child(3)>div>div>div>button>span'))
        time.sleep(2)
        self.input((By.CSS_SELECTOR,
                    'form>div:nth-child(2)>div:nth-child(2)>div:nth-child(3)'
                    '>div>div:nth-child(2)>div>div>div>textarea'),
                   google_ads_event)
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        time.sleep(3)
        self.click((By.XPATH, '//span[text()="保存"]'))

    # 获取前台币种
    def get_shop_currency(self):
        return self.text((By.CSS_SELECTOR, 'header>div>div>div>div:nth-child(1)'))

    # 获取后台默认币种
    def get_admin_currency(self):
        return self.text((By.CSS_SELECTOR, 'div[class="el-card__body"]>div>div:nth-child(2)>div>div:nth-child(2)'))

    # 选择币种
    def select_currency(self, currency_name):
        loc = By.XPATH, '//*[text()="{}"]'.format(currency_name)
        self.click_find_element(loc)

    # 编辑添加全部币种
    def add_all_currency(self):
        self.click((By.XPATH, '//span[text()="添加币种"]'))
        self.click_find_element((By.CSS_SELECTOR, 'div[class="content"]>label>span'))
        time.sleep(3)
        self.click_find_element((By.XPATH, '//span[text()="确定"]'))

    # 编辑添加部分币种
    def add_part_currency(self, currency_name):
        self.click((By.XPATH, '//span[text()="添加币种"]'))
        self.click_find_element((By.CSS_SELECTOR, 'div[class="content"]>label>span'))
        time.sleep(3)
        self.select_currency(currency_name)
        self.click_find_element((By.XPATH, '//span[text()="确定"]'))

    # 编辑添加搜索币种
    def add_search_currency(self, currency_title):
        self.click((By.XPATH, '//span[text()="添加币种"]'))
        self.input((By.CSS_SELECTOR, 'input[placeholder="币种名称或者币种"]'), currency_title)
        time.sleep(2)
        self.click((By.CSS_SELECTOR, 'div[class="search"]>div>div>button>span'))
        time.sleep(2)
        self.click_find_element((By.CSS_SELECTOR, 'div[class="body"]>div>label>span'))
        time.sleep(2)
        self.click_find_element((By.XPATH, '//span[text()="确定"]'))

    # 开启多币种和关闭关闭多币种
    def open_multi_currency(self):
        self.click((By.CSS_SELECTOR, 'span[class="el-switch__core"]'))
        time.sleep(2)
        self.click_find_element(pages.admin.website)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(3)

    # 关闭多币种和关闭关闭多币种
    def close_multi_currency(self):
        self.click((By.CSS_SELECTOR, 'span[class="el-switch__core"]'))
        time.sleep(2)
        self.click_find_element(pages.admin.website)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(3)

    # 判断前台多币种是否关闭
    def multi_currency_if_close(self):
        admin_currency = self.get_shop_currency()
        if admin_currency is None:
            return True
        else:
            return False

    # 移动多币种
    def move_multi_currency(self):
        # 起点
        loc = By.CSS_SELECTOR, 'div>div:nth-child(3)>div:nth-child(2)>div:nth-child(2)'
        start = self.find_element_func(loc)
        start_x = start.location.get('x')
        loc_1 = By.CSS_SELECTOR, 'div>div:nth-child(3)>div:nth-child(3)>div:nth-child(2)'
        end = self.find_element_func(loc_1)
        end_x = end.location.get('x')
        end_y = end.location.get('y')
        time.sleep(2)
        actions = ActionChains(self.driver)
        time.sleep(2)
        actions.move_to_element(start)
        actions.perform()
        self.driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            start,
            "background: #f47920")
        actions.click_and_hold(start).perform()
        actions.move_to_element_with_offset(end, end_x, 0).perform()
        actions.release().perform()
        self.driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            end,
            "background: #CC0000")
        time.sleep(5)

    # 删除多币种
    def del_multi_currency(self):
        self.click_red_find_element(
            (By.CSS_SELECTOR, 'div>div:nth-child(3)>div:nth-child(8)>div:nth-child(4)>i:nth-child(2)'))
        time.sleep(3)
        return self.base_if_text_exists_element(text="ARS")
