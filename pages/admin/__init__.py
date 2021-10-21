from selenium.webdriver.common.by import By

"""
以下为后台请求url
"""
admin_login_url = 'https://sso.reportide.com/home/login'
admin_login_test_url = 'https://sso.runshopstore.com/home/login'
new_shop_signup = "https://sso.reportide.com/home/signup"
test_new_admin_url = 'https://sso.runshopstore.com/home/signup'
# 新店铺注册页面

new_shop_email = By.CSS_SELECTOR, "#email"  # 新建商铺邮件
new_shop_password = By.CSS_SELECTOR, "#password"  # 新建商铺密码
new_shop_name = By.CSS_SELECTOR, "#shopName"  # 新建商铺名称
new_shop_url = By.CSS_SELECTOR, "#shopUrl"  # 新建商铺URL
new_shop_btn = By.CSS_SELECTOR, "div>button"  # 创建店铺按钮
home_shop = By.XPATH, '//a[@href="/home/login"]'  # 已有商铺名称按钮
next_btn_1 = By.CSS_SELECTOR, 'div[class="form-btn"]>button'  # 点击下一步
first_name = By.CSS_SELECTOR, '#firstname'  # 输入姓
last_name = By.CSS_SELECTOR, '#lastname'  # 输入名
address1 = By.CSS_SELECTOR, '#address1'  # 地址
room_number = By.CSS_SELECTOR, '#address2'  # 房间号
city = By.CSS_SELECTOR, '#city'  # 城市
country = By.CSS_SELECTOR, '#country'  # 国家
province = By.CSS_SELECTOR, '#province'  # 省份
postal_code = By.CSS_SELECTOR, '#zip'  # 邮编
phone = By.CSS_SELECTOR, '#phone'  # 手机电话
goto_new_shop = By.CSS_SELECTOR, '#reg-step-2 > div.login-card-content > div.form-btm-btn.form-btn > button'  # 去新商店后台
# 店铺登录页面

next_btn = By.CSS_SELECTOR, "div>button"  # 下一步按钮
shop_url_name = By.CSS_SELECTOR, "#shopDomain"  # 店铺网址前缀名
admin_email = By.CSS_SELECTOR, "#accountEmail"  # 店铺登录邮箱
admin_password = By.CSS_SELECTOR, "#accountPassword"  # 后台登录密码
admin_login_btn = By.CSS_SELECTOR, 'div>button[type="submit"]'  # 后台密码
shop_name = By.CSS_SELECTOR, 'div[class="navbar-head-title"]'  # 登录的商铺名称

# 切换模板
store_config = By.CSS_SELECTOR, 'i[class="el-icon-setting"]'  # 商店配置
template = By.XPATH, '//span[text()="模板"]'  # 模板
get_tpl_name = By.CSS_SELECTOR, 'span[class="fs16 tpl-name"]'  # 获取模板
change_tpl = By.XPATH, '//span[text()="更换模板"]'  # 更换模板
use_tpl = By.XPATH, '//span[text()="使用模板"]'  # 使用模板
target_tpl = By.XPATH, '//span[text()="使用模板"]'  # Default模板一
hover_tpl = By.CSS_SELECTOR, 'div[class="tpl-list-item-content"]'  # 鼠标滑入模板一
select_tpl = By.CSS_SELECTOR, '#layout-con-right > div > div.tpl-list > div:nth-child(1) > div > div'  # 模板选择按钮
logout_admin_shop = By.CSS_SELECTOR, 'a[href="/home/logout"]'  # 退出后台商铺
website = By.CSS_SELECTOR, 'div:nth-child(2)>a>i'  # 查看网站前台
language_manage = By.XPATH, '//span[text()="语言管理"]'  # 语言管理
store_configuration = By.XPATH, '//*[text()=" 商店配置"]'  # 商店配置
shop_template = By.XPATH, '//*[text()="模板"]'  # 模板
language_management = By.XPATH, '//*[text()="语言管理"]'  # 语言管理
change_language = By.CSS_SELECTOR, 'div>div:nth-child(3)>div>div:nth-child(1)>span:nth-child(2)'  # 更换语言
temp_name = By.CSS_SELECTOR, 'div[class="flex-item mr10 main"]>div:nth-child(3)>div>div:nth-child(1)'  # 模板名称
change_template = By.XPATH, '//*[text()="更换模板"]'  # 更换模板
use_template = By.XPATH, '//*[text()="使用模板"]'  # 使用模板
top_save_btn = By.CSS_SELECTOR, 'button[class="el-button el-button--primary el-button--medium"]'  # 保存语言按钮
template_one = By.CSS_SELECTOR, 'div:nth-child(1)>div>div>div:nth-child(1)>' \
                                'div:nth-child(2)>div>button:nth-child(1)>span'
template_two = By.CSS_SELECTOR, '#layout-con-right>div>div>div:nth-child(2)>div>div>div:nth-child(2)>div>button>span'
template_three = By.CSS_SELECTOR, '#layout-con-right>div>div>div:nth-child(3)>div>div>div:nth-child(2)>div>button>span'
template_four = By.CSS_SELECTOR, '#layout-con-right>div>div>div:nth-child(4)>div>div>div:nth-child(2)>div>button>span'
template_five = By.CSS_SELECTOR, '#layout-con-right>div>div>div:nth-child(5)>div>div>div:nth-child(2)>div>button>span'
template_six = By.CSS_SELECTOR, '#layout-con-right>div>div>div:nth-child(6)>div>div>div:nth-child(2)>div>button>span'
template_seven = By.CSS_SELECTOR, '#layout-con-right>div>div>div:nth-child(7)>div>div>div:nth-child(2)>div>button>span'
template_eight = By.CSS_SELECTOR, '#layout-con-right>div>div>div:nth-child(8)>div>div>div:nth-child(2)>div>button>span'
template_one_img = By.XPATH, '//div[2]/div/div[1]/div/div/div/img'
template_two_img = By.CSS_SELECTOR, '#layout-con-right>div>div>div:nth-child(2)>div>div>img'
template_three_img = By.CSS_SELECTOR, '#layout-con-right>div>div>div:nth-child(3)>div>div>img'
template_four_img = By.CSS_SELECTOR, '#layout-con-right>div>div>div:nth-child(4)>div>div>img'
template_five_img = By.CSS_SELECTOR, '#layout-con-right>div>div>div:nth-child(5)>div>div>img'
template_six_img = By.CSS_SELECTOR, '#layout-con-right>div>div>div:nth-child(6)>div>div>img'
template_seven_img = By.CSS_SELECTOR, '#layout-con-right>div>div>div:nth-child(7)>div>div>img'
template_eight_img = By.CSS_SELECTOR, '#layout-con-right>div>div>div:nth-child(8)>div>div>img'
ala_popup_close = By.XPATH, '//*[@id="layout-con-right"]/div[2]/div[4]/div/div/div[1]/button'
# 后台登录店铺主页菜单项
pdm = By.CSS_SELECTOR, 'i[class="iconfont icon-chanpin"]'  # 产品管理
all_products = By.XPATH, '//span[text()="所有产品"]'  # 所有产品
product_family = By.XPATH, '//span[text()="产品系列"]'  # 产品系列
product_sequencing = By.XPATH, '//span[text()="产品排序"]'  # 产品排序
product_reviews = By.XPATH, '//span[text()="产品评论"]'  # 产品评论
order_management = By.CSS_SELECTOR, 'i[class="iconfont icon-xiadan"]'  # 订单管理
order_list = By.XPATH, '//span[text()="订单列表"]'  # 订单列表
discard_list = By.XPATH, '//span[text()="弃单列表"]'  # 弃单列表
marketing_management = By.CSS_SELECTOR, 'i[class="iconfont icon-yingxiaoguanli"]'  # 营销管理
mail_marketing = By.XPATH, '//span[text()="邮件营销"]'  # 邮件营销
marketing_code = By.XPATH, '//span[text()="营销代码管理"]'  # 营销代码管理
data_tracking = By.XPATH, '//span[text()="数据跟踪"]'  # 数据跟踪
multi_currency = By.XPATH, '//span[text()="多币种管理"]'  # 多币种管理
app_manage = By.XPATH, '//*[text()=" 应用管理"]'  # 应用管理
app_list = By.XPATH, '//*[text()="应用列表"]'  # 应用列表

"""所有产品"""
# 添加产品
add_product = By.XPATH, "//*[text()='添加产品']"
# 导入产品
imp_products = By.XPATH, "//*[text()='导入产品']"
# 下载表单
download_table = By.XPATH, "//*[text()='下载表单']"
# 产品系列名称
product_line = By.CSS_SELECTOR, '#ui-popover-activator--6'
input_line = By.CSS_SELECTOR, 'input[placeholder="输入关键字进行过滤"]'
line_name = By.XPATH, "//span[text()='new']"
screen_btn = By.CSS_SELECTOR, 'button[class="el-button ui-button add-filter el-button--default el-button--medium"]'
#  状态筛选
status_filter = By.CSS_SELECTOR, 'div[class="next-field-connected-wrapper"]>div>div>span>button'
status_down = By.XPATH, "//label/span[text()='下架']"
id_filter = By.CSS_SELECTOR, 'div[class="popover-id-filter"]>span>button'
id_filter_btn = By.XPATH, "//span[text()='产品ID']"
# 搜索 产品按钮
search_product = By.CSS_SELECTOR, 'div[class="el-input el-input--prefix el-input--suffix"]>input'
# 点击搜索列表中的第一个产品
search_product_click = By.XPATH, '//*[@id="table"]/div[2]/div[3]/table/tbody/tr/td[1]/div/label/span'
# 编辑产品状态按钮
click_edit = By.CSS_SELECTOR, 'button[class="el-button product-ref-btn el-button--primary ' \
                              'el-button--mini el-popover__reference"]'
# 批量改价按钮
click_change_sell = By.CSS_SELECTOR, 'button[class="el-button product-ref-btn el-button--primary el-button--mini"]'
# 选择系数按钮
change_sell_btn = By.CSS_SELECTOR, 'label[class="el-radio"]>span>span'
# 清除选择条件
clear_select = By.CSS_SELECTOR, '#el-popover-8946>div[class="remove-button"]>a>span'
# 选择所有产品
all_checkbox = By.CSS_SELECTOR, 'span[class="el-checkbox__input"]>input'
# 搜索按钮
search_btn = By.CSS_SELECTOR, 'div[class="search-right-button"]>button'
# 搜索为空
search_empty = By.CSS_SELECTOR, 'h2[class="empty-search-results__title"]'
# 选择单个产品
select_goods = By.CSS_SELECTOR, 'input[type="checkbox"]'
# 选择框编辑按钮
select_box_edit = By.CSS_SELECTOR, 'button[aria-describedby="el-popover-1020"]'
# 选择编辑产品上下架删除
edit_products = By.CSS_SELECTOR, 'div[class="edit__content-wrapper"]>ul>li>a'
product_img = By.XPATH, '//*[@id="table"]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div/div/a'
product_title = By.XPATH, '//*[@id="table"]/div[2]/div[3]/table/tbody/tr[1]/td[4]/div/div/div[1]/a[text()]'
product_icon = By.CSS_SELECTOR, 'tr[class="el-table__row"]>td:nth-child(8)>div>div>span>div>i'
product_see = By.CSS_SELECTOR, 'tr[class="el-table__row"]>td:nth-child(8)>div>div>span:nth-child(2)>div>i'
please_select = By.CSS_SELECTOR, 'input[placeholder="请选择"]'
page_30 = By.XPATH, "//span[text()='30条/页']"
page_40 = By.XPATH, "//span[text()='40条/页']"
page_50 = By.XPATH, "//span[text()='50条/页']"
select_result = By.XPATH, '//*[@id="table"]/div[2]/div[2]/table/thead/tr/th[1]/div/label/span/span'
"""添加产品页"""
# 输入标题
ipu_title = By.CSS_SELECTOR, 'div[class="titleinput el-textarea"]>textarea'
# 输入 spu
ipt_spu = By.CSS_SELECTOR, 'input[placeholder="请输入SPU"]'
# 输入产品系列
ipt_pdc_line = By.CSS_SELECTOR, 'i[class="el-input__icon el-icon-caret-bottom"]'
# 输入系列关键字
ipu_pdc_key = By.CSS_SELECTOR, 'input[placeholder="输入关键字进行过滤"]'
# 选择系列
selc_pdc_key = By.XPATH, "//*[text()='new']"
# 输入 产品分类
ipt_pdc_class = By.CSS_SELECTOR, 'input[placeholder="产品分类"]'
# 添加产品分类
add_class = By.CSS_SELECTOR, 'span[data-v-8afb2b42]'
# 选择标签
inp_pdc_label = By.CSS_SELECTOR, 'input[placeholder="标签"]'
clk_pdc_label = By.CSS_SELECTOR, 'div[class="productfenlei"]>div>div>div>span>span>i'
# 添加标签
add_label = By.XPATH, "//*[text()='sdsdsd']"
# 正品，一级，二级，三级，高风险，极高风险
quality_goods = By.XPATH, "//span[text()='正品']"
one_level = By.XPATH, "//span[text()='一级']"
second_level = By.XPATH, "//span[text()='二级']"
three_level = By.XPATH, "//span[text()='三级']"
high_risk = By.XPATH, "//span[text()='高风险']"
extremely_risky = By.XPATH, "//span[text()='极高风险']"
# 选择产品级别
ipt_pdc_level = By.CSS_SELECTOR, 'input[placeholder="产品级别"]'
# 选择上架开关
select_up_pdc = By.CSS_SELECTOR, 'div[class="checkboxContent"]>label>span>span'
# 产品描述iframe
describe_iframe = By.CSS_SELECTOR, 'iframe[allowtransparency="true"]'
# 输入描述
i_describe = By.CSS_SELECTOR, 'body[class="mce-content-body "]>p'
# 添加图片
add_img = By.CSS_SELECTOR, ' i[class="el-icon-plus"]'
# 多属性开关
attribute_switch = By.CSS_SELECTOR, 'div[class="moreattributecheck"]'
# 产品属性选项1---7[6]
property_option_one = By.CSS_SELECTOR, 'input[aria-activedescendant="el-autocomplete-1167-item--1"]'
# 选项内容
property_count = By.CSS_SELECTOR, 'input[placeholder="请用逗号隔开各个选项"]'
# 添加其他选项
add_other_properties = By.XPATH, "//*[text()='添加其他选项']"
# 产品属性选项2---8[7]
property_option_two = By.CSS_SELECTOR, 'input[aria-activedescendant="el-autocomplete-7509-item--1"]'
# 产品属性选项3---9[8]
property_option_three = By.CSS_SELECTOR, 'div[class="el-autocomplete inline-input"]'
# 删除属性
delete_attribute = By.XPATH, '//span[text()="删除"]'
# 页面标题
page_title = By.CSS_SELECTOR, 'div[class="el-input"]>input[maxlength="70"]'
# 搜索引擎描述
search_describe = By.CSS_SELECTOR, 'div[class="el-textarea"]>textarea'
s_describe = By.CSS_SELECTOR, 'div:nth-child(3) > div > div > textarea'
# 内部优化链接
inside_links = By.CSS_SELECTOR, 'div[style="flex: 1 1 0%;"]>input'
# 保存按钮
save_btn = By.CSS_SELECTOR, 'div:nth-child(5)>button>span'
# 顶部保存按钮
save_btn_top = By.XPATH, '//*[@id="layout-con-right"]/div/div[2]/div/div/button[2]/span'
# 顶部取消按钮
cancel_btn = By.XPATH, '//*[@id="layout-con-right"]/div/div[2]/div/div/button[1]'
# 放弃修改按钮
give_up_eid = By.CSS_SELECTOR, 'button[class="el-button el-button--danger"]'
# 获取保存成功信息
save_msg = By.CSS_SELECTOR, 'div[class="el-message el-message--success"]>p'
# 获取产品ID
goods_id = By.XPATH, '//*[@id="table"]/div[2]/div[3]/table/tbody/tr[1]/td[3]/div/span'
# 获取产品名称
goods_title = By.CSS_SELECTOR, 'div[class="ui-stack-item"]>a'
# 失败信息
msage = By.XPATH, '//*[@id="layout-con-right"]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/ul/li'
msage_1 = By.XPATH, '//*[@id="layout-con-right"]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/ul/li[1]'
msage_2 = By.XPATH, '//*[@id="layout-con-right"]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/ul/li[2]'
msage_3 = By.XPATH, '//*[@id="layout-con-right"]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/ul/li[3]'
