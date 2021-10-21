import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

import pages
from selenium.webdriver.support.select import Select
from pages.pagebase import PageBase


class PageAdminHomeMinix:
    def admin_home(self):
        if not getattr(self, '_admin_home', None):
            self._admin_home = PageAdminHome(self.driver)
        return self._admin_home


# 后台首页
class PageAdminHome(PageBase):
    home_shop = pages.admin.home_shop  # 点击已有商铺名称按钮
    new_shop_email = pages.admin.new_shop_email  # 输入新建商铺邮件
    new_shop_password = pages.admin.new_shop_password  # 新建商铺密码
    new_shop_name = pages.admin.new_shop_name  # 新建商铺名称
    new_shop_url = pages.admin.new_shop_url  # 新建商铺URL
    new_shop_btn = pages.admin.new_shop_btn  # 创建店铺按钮
    next_btn_1 = pages.admin.next_btn_1  # 点击下一步
    first_name = pages.admin.first_name  # 输入姓
    last_name = pages.admin.last_name  # 输入名
    address1 = pages.admin.address1  # 地址
    room_number = pages.admin.room_number  # 输入房间号
    city = pages.admin.city  # 城市
    country = pages.admin.country  # 国家
    province = pages.admin.province  # 省份
    postal_code = pages.admin.postal_code  # 邮编
    phone = pages.admin.phone  # 手机电话
    goto_new_shop = pages.admin.goto_new_shop  # 去新商店后台
    # 店铺登录页面
    next_btn = pages.admin.next_btn  # 下一步按钮
    shop_url_name = pages.admin.shop_url_name  # 店铺网址前缀名
    admin_email = pages.admin.admin_email  # 店铺登录邮箱
    admin_psd = pages.admin.admin_password  # 后台登录密码
    admin_login_btn = pages.admin.admin_login_btn  # 后台密码
    shop_name = pages.admin.shop_name  # 登录的商铺名称
    website = pages.admin.website  # 查看网站前台
    ala_popup_close = pages.admin.ala_popup_close  # 关闭后台弹窗
    language_management = pages.admin.language_management  # 语言管理
    store_configuration = pages.admin.store_configuration  # 商店配置
    shop_template = pages.admin.shop_template  # 模板
    change_language = pages.admin.change_language  # 更换语言
    temp_name = pages.admin.temp_name  # 模板名称
    change_template = pages.admin.change_template  # 更换模板
    use_template = pages.admin.use_template  # 使用模板
    top_save_btn = pages.admin.top_save_btn  # 保存语言按钮
    template_one = pages.admin.template_one
    template_two = pages.admin.template_two
    template_three = pages.admin.template_three
    template_four = pages.admin.template_four
    template_five = pages.admin.template_five
    template_six = pages.admin.template_six
    template_seven = pages.admin.template_seven
    template_eight = pages.admin.template_eight
    template_one_img = pages.admin.template_one_img
    template_two_img = pages.admin.template_two_img
    template_three_img = pages.admin.template_three_img
    template_four_img = pages.admin.template_four_img
    template_five_img = pages.admin.template_five_img
    template_six_img = pages.admin.template_six_img
    template_seven_img = pages.admin.template_seven_img
    template_eight_img = pages.admin.template_eight_img

    def click_home_shop(self):
        """点击已有商铺名称按钮"""
        self.click(self.home_shop)

    def input_new_shop_email(self, new_email):
        """输入新建商铺邮件"""
        self.input(self.new_shop_email, new_email)

    def input_new_shop_password(self, new_password):
        """新建商铺密码"""
        self.input(self.new_shop_password, new_password)

    def input_new_shop_url(self, new_shop_url):
        """新建商铺URL"""
        self.input(self.new_shop_url, new_shop_url)

    def input_new_shop_name(self, new_name):
        """新建商铺名称"""
        self.input(self.new_shop_name, new_name)

    def click_new_shop_btn(self):
        """点击创建店铺按钮"""
        self.click(self.new_shop_btn)

    def click_next_btn_1(self):
        """点击下一步"""
        self.click(self.next_btn_1)

    def select_admin_country(self, country):
        """选择国家"""
        slt = Select(self.find_element_func(country))
        slt.select_by_value(country)

    def select_admin_province(self, province):
        """选择省、洲"""
        alt = Select(self.find_element_func(province))
        alt.select_by_value(province)

    def input_room_number(self, room_number):
        """输入房间号"""
        self.input(self.room_number, room_number)

    def input_first_name(self, first_name):
        """输入姓"""
        self.input(self.first_name, first_name)

    def input_last_name(self, last_name):
        """输入名"""
        self.input(self.last_name, last_name)

    def input_address1(self, address1):
        """输入地址"""
        self.input(self.address1, address1)

    def input_city(self, city):
        """输入城市"""
        self.input(self.city, city)

    def input_postal_code(self, postal_code):
        """输入邮箱"""
        self.input(self.postal_code, postal_code)

    def input_phone(self, phone):
        """输入电话"""
        self.input(self.phone, phone)

    def click_goto_new_shop(self):
        """点击去后台主页"""
        self.click(self.goto_new_shop)

    def input_admin_email(self, admin_email):
        """输入后台邮箱"""
        self.input(self.admin_email, admin_email)

    def input_shop_url_name(self, shop_url_name):
        """输入商店url"""
        self.input(self.shop_url_name, shop_url_name)

    def input_admin_password(self, admin_psd):
        """输入后台密码"""
        self.input(self.admin_psd, admin_psd)

    def click_next_btn(self):
        """点击下一步"""
        self.click(self.next_btn)

    def click_admin_login_btn(self):
        """点击后台登录按钮"""
        self.click(self.admin_login_btn)

    def get_shop_name(self):
        """获取商店名称"""
        return self.text(self.shop_name)

    def click_shop_configs(self):
        """点击商店配置"""
        self.click(self.store_configuration)

    def click_shop_template(self):
        """点击模板"""
        self.click(self.shop_template)

    def click_language_manage(self):
        """点击语言管理"""
        self.click(self.language_management)

    def click_change_language(self):
        """点击更换语言"""
        self.click(self.change_language)

    def click_select_language_btn(self):
        """点击选择语言下拉按钮"""
        self.use_js("$('span[class=\"el-input__suffix-inner\"]>i').click()")

    def click_save_language_btn(self):
        """点击保存语言"""
        self.use_js("$('button[class=\"el-button el-button--primary\"]').click()")

    def get_shop_temp_name(self):
        """获取商店当前模板"""
        return self.text(self.temp_name)

    def click_change_template(self):
        """点击更换模板"""
        self.click(self.change_template)

    def click_use_template(self):
        """点击使用模板"""
        self.click(self.use_template)

    def click_website(self):
        """查看前台"""
        self.click(self.website)

    def click_ala_popup_close(self):
        """关闭后台续费弹窗"""
        self.click(self.ala_popup_close)

    def click_select_template_one(self):
        """"点击选择模板一"""
        element = self.find_element_func((By.XPATH, '//div[2]/div/div[1]/div/div/div/img'))
        self.driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            element,
            "border: 2px solid red;")
        time.sleep(2)
        ActionChains(self.driver).move_to_element(element).perform()
        self.click_red_find_element(
            (
                By.CSS_SELECTOR,
                'div:nth-child(1)>div>div>div:nth-child(1)>div:nth-child(2)>div>button:nth-child(1)>span'))

    def click_select_template_two(self):
        """点击选择模板二"""
        self.move_to_loc(self.template_two_img)
        self.click_find_element(self.template_two)

    def click_select_template_three(self):
        """点击选择模板三"""
        self.move_to_loc(self.template_three_img)
        self.click_find_element(self.template_three)

    def click_select_template_four(self):
        """点击选择模板四"""
        self.move_to_loc(self.template_four_img)
        self.click_find_element(self.template_four)

    def click_select_template_five(self):
        """点击选择模板五"""
        self.move_to_loc(self.template_five_img)
        self.click_find_element(self.template_five)

    def click_select_template_six(self):
        """点击选择模板六"""
        self.move_to_loc(self.template_six_img)
        self.click_find_element(self.template_six)

    def click_select_template_seven(self):
        """点击选择模板七"""
        self.move_to_loc(self.template_seven_img)
        self.click_find_element(self.template_seven)

    def click_select_template_eight(self):
        """点击选择模板八"""
        self.move_to_loc(self.template_eight_img)
        self.click_find_element(self.template_eight)

    def change_temp_language(self):
        """切换模板语言"""
        self.click_language_manage()
        time.sleep(2)
        self.click_change_language()
        time.sleep(2)
        self.click_select_language_btn()
        time.sleep(2)
        self.click_find_element((By.XPATH, '//span[text()="English"]'))
        time.sleep(2)
        self.click_save_language_btn()
        time.sleep(3)
        self.click(self.top_save_btn)

    def change_shop_temp_two(self):
        """切换模板二"""
        self.click_change_template()
        time.sleep(2)
        self.click_select_template_two()
        time.sleep(2)
        self.click_use_template()
        time.sleep(35)
        self.click_website()

    def change_shop_temp_one(self):
        """切换模板一"""
        self.click_change_template()
        time.sleep(2)
        self.click_select_template_one()
        time.sleep(2)
        self.click_use_template()
        time.sleep(50)
        self.click_website()

    def change_shop_temp_three(self):
        """切换模板三"""
        self.click_change_template()
        time.sleep(2)
        self.click_select_template_three()
        time.sleep(2)
        self.click_use_template()
        time.sleep(35)
        self.click_website()

    def change_shop_temp_four(self):
        """切换模板四"""
        self.click_change_template()
        time.sleep(2)
        self.click_select_template_four()
        time.sleep(2)
        self.click_use_template()
        time.sleep(35)
        self.click_website()

    def change_shop_temp_five(self):
        """切换模板五"""
        self.click_change_template()
        time.sleep(2)
        self.click_select_template_five()
        time.sleep(2)
        self.click_use_template()
        time.sleep(35)
        self.click_website()

    def change_shop_temp_six(self):
        """切换模板六"""
        self.click_change_template()
        time.sleep(2)
        self.click_select_template_six()
        time.sleep(2)
        self.click_use_template()
        time.sleep(35)
        self.click_website()

    def change_shop_temp_seven(self):
        """切换模板七"""
        self.click_change_template()
        time.sleep(2)
        self.click_select_template_seven()
        time.sleep(2)
        self.click_use_template()
        time.sleep(35)
        self.click_website()

    def change_shop_temp_eight(self):
        """切换模板八"""
        self.click_change_template()
        time.sleep(2)
        self.click_select_template_eight()
        time.sleep(2)
        self.click_use_template()
        time.sleep(35)
        self.click_website()

    def add_admin_new_shop(self, new_email, new_password, new_shop_name, new_shop_url, ):
        """注册店铺业务方法"""
        self.logger.info(
            "正在调用创建店铺的业务方法，邮箱：{} 密码：{} 店铺名：{} 店铺url:{} ".format(new_email, new_password, new_shop_name, new_shop_url))
        self.input_new_shop_email(new_email)
        self.input_new_shop_password(new_password)
        self.input_new_shop_name(new_shop_name)
        self.input_new_shop_url(new_shop_url)
        self.click_new_shop_btn()

    def edit_shop_information(self, first_name='w', last_name='jp', address1='jingzhoushi 2-3-911',
                              room_number='#9 2305', city='beijing',
                              country="20000", province="20002", postal_code='10086', phone='13300000000'):
        """
        组合业务方法（新创建的信息填写）
        """
        self.logger.info(
            "正在调用店铺注册的填写信息方法，名：{} 姓：{} 地址：{} 城市:{} 国家:{} 省:{} 邮编:{} 电话:{}  ".format(first_name, last_name, address1,
                                                                                    city, country, province,
                                                                                    postal_code, phone))
        self.click_next_btn_1()
        self.input_first_name(first_name)
        self.input_last_name(last_name)
        self.input_address1(address1)
        self.input_room_number(room_number)
        self.input_city(city)
        self.select_admin_country(country)
        self.select_admin_province(province)
        self.input_postal_code(postal_code)
        self.input_phone(phone)
        self.click_goto_new_shop()

    def admin_home_login(self, shop_url_name, admin_email, admin_psd):
        """
        后台登录店铺
        """
        self.logger.info("正在调用登录组合业务方法，店铺名：{} 邮箱：{} 密码：{}".format(shop_url_name, admin_email, admin_psd))
        self.use_js("window.stop()")
        self.click_home_shop()
        self.use_js("window.stop()")
        self.input_shop_url_name(shop_url_name)
        self.click_next_btn()
        time.sleep(1)
        self.input_admin_email(admin_email)
        self.click_next_btn()
        time.sleep(1)
        self.input_admin_password(admin_psd)
        self.click_admin_login_btn()

    def admin_home_login_template001(self, shop_url_name="template001", admin_email="tester@meshop.net",
                                     admin_psd="Tester123456"):
        """
        meshop 店铺 template001 登录
        """
        self.logger.info("正在调用登录组合业务方法，店铺名：{} 邮箱：{} 密码：{}".format(shop_url_name, admin_email, admin_psd))
        self.use_js("window.stop()")
        self.click_home_shop()
        self.use_js("window.stop()")
        self.input_shop_url_name(shop_url_name)
        self.click_next_btn()
        time.sleep(1)
        self.input_admin_email(admin_email)
        self.click_next_btn()
        time.sleep(1)
        self.input_admin_password(admin_psd)
        self.click_admin_login_btn()

    def admin_home_login_fr(self, shop_url_name="testfr", admin_email="tester@meshop.net",
                            admin_psd="Tester123456"):
        """
        法语站后台登录店铺
        """
        self.logger.info("正在调用登录组合业务方法，店铺名：{} 邮箱：{} 密码：{}".format(shop_url_name, admin_email, admin_psd))
        self.use_js("window.stop()")
        self.click_home_shop()
        self.use_js("window.stop()")
        self.input_shop_url_name(shop_url_name)
        self.click_next_btn()
        time.sleep(1)
        self.input_admin_email(admin_email)
        self.click_next_btn()
        time.sleep(1)
        self.input_admin_password(admin_psd)
        self.click_admin_login_btn()

    def admin_home_login_de(self, shop_url_name="testde", admin_email="tester@meshop.net",
                            admin_psd="Tester123456"):
        """
        德语站后台登录店铺
        """
        self.logger.info("正在调用登录组合业务方法，店铺名：{} 邮箱：{} 密码：{}".format(shop_url_name, admin_email, admin_psd))
        self.use_js("window.stop()")
        self.click_home_shop()
        self.use_js("window.stop()")
        self.input_shop_url_name(shop_url_name)
        self.click_next_btn()
        time.sleep(1)
        self.input_admin_email(admin_email)
        self.click_next_btn()
        time.sleep(1)
        self.input_admin_password(admin_psd)
        self.click_admin_login_btn()

    def admin_home_login_en(self, shop_url_name="testen", admin_email="tester@meshop.net",
                            admin_psd="Tester123456"):
        """
        英语站后台登录店铺）
        """
        self.logger.info("正在调用登录组合业务方法，店铺名：{} 邮箱：{} 密码：{}".format(shop_url_name, admin_email, admin_psd))
        self.click_home_shop()
        time.sleep(1)
        self.input_shop_url_name(shop_url_name)
        self.click_next_btn()
        time.sleep(1)
        self.input_admin_email(admin_email)
        self.click_next_btn()
        time.sleep(1)
        self.input_admin_password(admin_psd)
        self.click_admin_login_btn()

    def admin_home_login_jpy(self, shop_url_name="testjpy", admin_email="tester@meshop.net",
                             admin_psd="Tester123456"):
        """
        日语站后台登录店铺
        """
        self.logger.info("正在调用登录组合业务方法，店铺名：{} 邮箱：{} 密码：{}".format(shop_url_name, admin_email, admin_psd))
        self.click_home_shop()
        time.sleep(1)
        self.input_shop_url_name(shop_url_name)
        self.click_next_btn()
        time.sleep(1)
        self.input_admin_email(admin_email)
        self.click_next_btn()
        time.sleep(1)
        self.input_admin_password(admin_psd)
        self.click_admin_login_btn()
