from selenium.webdriver.common.by import By

"""模板一网址"""
template1_url = "https://testde.reportide.com/"
template1_test_url = "http://template2.meshop.net/"
template1_run_url = "https://testde.runshopstore.com/"
"""
个人中心页
"""
email = By.CSS_SELECTOR, "#inputEmail"
password = By.CSS_SELECTOR, "#inputPassword"
login_btn = By.CSS_SELECTOR, "#btnLogin"
register_page = By.CSS_SELECTOR, "#aRegister>span"
register_btn = By.CSS_SELECTOR, "#btnRegister"
first_name = By.CSS_SELECTOR, "#inputFirstName"
last_name = By.CSS_SELECTOR, "#inputLastName"
nickname = By.CSS_SELECTOR, 'div[class="SectionHeader"]>p>span'
# 提示信息
tips = By.CSS_SELECTOR, 'main>div>div>div>div:nth-child(5)'
logout = By.CSS_SELECTOR, "#btnSignOut"
"""
前台首页
"""
coupon_close = By.XPATH, '//*[@id="ms-coupon-popup"]/div/div[2]/div[1]'  # 优惠券弹窗关闭按钮
# 个人中心图标
icon = By.CSS_SELECTOR, 'div:nth-child(3)>nav>ul>li:nth-child(2)>a'
# 购物车图标
cart = By.CSS_SELECTOR, 'a[data-drawer-id="sidebar-cart"]'
# 搜索图标
search_ico = By.CSS_SELECTOR, 'a[aria-controls="Search"]'
# 搜索输入框
search_inp = By.CSS_SELECTOR, 'div[class="Search__Form"]>input'
# 查看搜索结果page
search_result = By.CSS_SELECTOR, 'a[title="View all"]'
# 搜索商品的名称
search_title = By.CSS_SELECTOR, 'h2>a[href="/product/iphone-1016437/"]'
# 删除商品
remove_goods_btn = By.CSS_SELECTOR, 'div[class="CartItem__Info"]>div>a'
# 获取加入购物车的商品标题
goods_title = By.CSS_SELECTOR, 'h3[class="CartItem__Title Heading"]>a>div'
# 获取购物车的商品的spu值
goods_spu_count = By.CSS_SELECTOR, 'div[class="CartItem__Info"]>div>p'
# mini购物车去结算按钮
mini_checkout = By.CSS_SELECTOR, '#btnShopCartSubmit'
# mini 购物车添加商品数量+按钮
mini_add_goods_plus = By.CSS_SELECTOR, 'button[class="shopcart_add"]'
# mini 购物车减少商品数量—按钮
mini_minus_goods = By.CSS_SELECTOR, 'div[class="QuantitySelector"]>button'
# mini 购物车输入按钮
mini_input_goods = By.CSS_SELECTOR, 'input[name="textfield"]'
# 进入产品系列
product_line = By.XPATH, '//a[@title="auto测试"]'

buy_products = By.XPATH, '//a[@title="iPhone"]'
# 模板一列表页第一款产品图
mobanone_line_products_fist = By.XPATH, '//div[@class="ProductListWrapper"]//a'
# 模板二列表页第一款产品图
mobantow_line_products_fist = By.XPATH, '//div[@class="content have-src product-item-icon-content"]'
# 模板三列表页第一款产品图
mobanthree_line_products_fist = By.XPATH, '//li[@class="productlist-item product-collection-item"]//a'
# 模板七列表页第一款产品图
mobanseven_line_products_fist = By.XPATH, '//div[@class="pro-one-img"]'
# 模板二首页左侧导航
# left_nav = By.XPATH, '//button[@class="com-header-menu"]'
# 模板五首页左侧导航
left_nav = By.XPATH, '//div[@class="head-help"]'
# 打开模板二系列页
mobantow_product_line = By.XPATH, '//*[text()="NEW IN"]'
"""搜索页"""
# 搜索页商品名
goods_name = By.CSS_SELECTOR, 'h3>a'
iphone_goods = By.CSS_SELECTOR, 'h3>a[title="iPhone"]'
iphone_goods_two = By.CSS_SELECTOR, 'h3>a[title="Plastik Apple iPhones Schutzhülle 保护套/壳"]'
# 搜索结果数
goods_index = By.CSS_SELECTOR, 'div[class="Container"]>div>div>div'
# 搜索页翻页
next_page = By.LINK_TEXT, 'Next'
prev_page = By.LINK_TEXT, 'Prev'
"""详情页"""
# 添加商品数量+按钮
add_goods_plus = By.CSS_SELECTOR, 'div.link.increase-quantity.quantity-selector-button'
# 减少商品数量—按钮
minus_goods = By.CSS_SELECTOR, 'div.link.decrease-quantity.quantity-selector-button'
# 输入商品数量input按钮
input_goods = By.CSS_SELECTOR, '#productquntity'
# 加购按钮
add_cart = By.CSS_SELECTOR, 'button[data-shoptype="0"]'
# 立即购买按钮
buy_now = By.CSS_SELECTOR, 'button[data-shoptype="1"]'
# 切换颜色按钮
switch_colors_but = By.XPATH, '//button[@aria-label="Next"]'
# 确定颜色
sure_goods_color = By.CSS_SELECTOR, 'div[class="VariantSelector__Info"]>div:nth-child(2)'
"""地址页元素"""
# 地址页登录
address_login = By.CSS_SELECTOR, 'div[class="section__header"]>div>p>a'
# 地址页邮箱
address_email = By.CSS_SELECTOR, 'input[placeholder="Email"]'
# 地址页推荐按钮
recommend_btn = By.CSS_SELECTOR, 'input[class="input-checkbox"]'
recommend_btn_two = By.XPATH, '//*[@id="checkout_remember_me"]'
# 地址页名
address_first_name = By.CSS_SELECTOR, 'input[placeholder="First name"]'
# 地址页姓
address_last_name = By.CSS_SELECTOR, 'input[placeholder="Last name"]'
# 地址页地址
address = By.CSS_SELECTOR, 'input[placeholder="Address"]'
# 地址页城市
add_city = By.CSS_SELECTOR, 'input[placeholder="City"]'
# 地址页国家
select_country = By.CSS_SELECTOR, '#checkout_shipping_address_country'
# 地址页省、洲
select_province = By.CSS_SELECTOR, '#checkout_shipping_address_province'
# 地址页邮编
add_postal = By.CSS_SELECTOR, 'input[placeholder="Postal code"]'
# 地址页电话
add_phone = By.CSS_SELECTOR, 'input[placeholder="Phone Number"]'
# 地址页折扣m码
code_value = By.CSS_SELECTOR, '#txtCoupon'
"""运费页"""
# 验证地址
sure_address = By.CSS_SELECTOR, 'address[class="address address--tight"]'
# 验证用户
sure_email = By.CSS_SELECTOR, 'bdo[dir="ltr"]'
# 获取运费金额
shipping = By.CSS_SELECTOR, 'span[data-type="shipping"]'
huge_package = By.CSS_SELECTOR, 'div[data-id="2"]>div>div>input'
""""支付页"""
unlimint_pay = By.CSS_SELECTOR, 'div[class="radio__input"]>input[datapaychannelid="121"]'  # 选unlimint支付
pacy_pay = By.CSS_SELECTOR, 'div[class="radio__input"]>input[datapaychannelid="61"]'  # 选pacypay支付
pay_ease_direct = By.CSS_SELECTOR, 'div[class="radio__input"]>input[datapaychannelid="76"]'
# 选Adyen支付
adyen = By.CSS_SELECTOR, 'div[class="radio__input"]>input[datapaychannelid="31"]'
# 选Stripe
stripe = By.CSS_SELECTOR, 'div[class="radio__input"]>input[datapaychannelid="41"]'
# 选Checkout
checkout = By.CSS_SELECTOR, 'div[class="radio__input"]>input[datapaychannelid="51"]'
# 选首信易直连
pay_ease_direct_card_name = By.CSS_SELECTOR, '#input-card-name'
pay_ease_direct_card = By.CSS_SELECTOR, '#input-card-number'
pay_ease_direct_date = By.CSS_SELECTOR, '#input-expire-date'
pay_ease_direct_cvc = By.CSS_SELECTOR, '#input-security-code'
# 输入unlimint卡用户名
unlimint_card_name = By.CSS_SELECTOR, '#input-card-name'
# 输入unlimint卡
unlimint_card = By.CSS_SELECTOR, '#input-card-number'
# 输入unlimint卡日期
unlimint_date = By.CSS_SELECTOR, '#input-expire-date'
# 输入unlimint卡的cvc
unlimint_cvc = By.CSS_SELECTOR, '#input-security-code'
# 输adyen卡号
adyen_card = By.XPATH, '//input[contains(@autocomplete,"cc-number")]'
# 输adyen年月
adyen_year = By.CSS_SELECTOR, '#encryptedExpiryDate'
# 输adyen cvc
adyen_cvc = By.CSS_SELECTOR, '#encryptedSecurityCode'
# 输stripe卡号
stripe_card = By.CSS_SELECTOR, 'input[placeholder="Card number"]'
# 输stripe年月
stripe_year = By.CSS_SELECTOR, 'input[placeholder="MM / YY"]'
# 输stripe cvc
stripe_cvc = By.CSS_SELECTOR, 'input[placeholder="CVC"]'
# 输checkout卡号
checkout_card = By.CSS_SELECTOR, 'input[data-checkout="card-number"]'
# 输checkout月
checkout_mm = By.CSS_SELECTOR, 'input[data-checkout="expiry-month"]'
# 输checkout年
checkout_yy = By.CSS_SELECTOR, 'input[data-checkout="expiry-year"]'
# 输checkout cvc
checkout_cvc = By.CSS_SELECTOR, 'input[data-checkout="cvv"]'
# 输入 pacy_pay卡号
pacy_pay_card = By.CSS_SELECTOR, 'div[class="paycrad-item"]>input'
# 输入 pacy_pay年月CVC
pacy_pay_date = By.CSS_SELECTOR, 'div[class="paycard-container card61"]>div:nth-child(3)>div>input'
pacy_pay_cvc = By.CSS_SELECTOR, 'div[class="paycard-container card61"]>div:nth-child(3)>div:nth-child(2)>input'
# 输入验证码
ck_code_iframe = By.CSS_SELECTOR, 'iframe[name="cko-3ds2-iframe"]'
pacy_pay_code = By.CSS_SELECTOR, '#submit'
mv_code = By.CSS_SELECTOR, '#password'
sure_code = By.CSS_SELECTOR, '#txtButton'
unlimint_code = By.CSS_SELECTOR, '#success'
# 支付结果
pp_but = By.CSS_SELECTOR, '#buttons-container>div>div>div>div.paypal-button-label-container'
pp_pay_btn = By.CSS_SELECTOR, 'input[datapaychannelid="11"]'
pp_iframe = By.CSS_SELECTOR, 'iframe[class="paypal-iframe-style"]'
pp_iframe_two = By.CSS_SELECTOR, 'iframe[title="PayPal"]'
pp_button = By.CSS_SELECTOR, 'div[data-funding-source="paypal"]'
pp_email = By.CSS_SELECTOR, '#email'
pp_next = By.CSS_SELECTOR, '#btnNext'
pp_psd = By.CSS_SELECTOR, '#password'
pp_login = By.CSS_SELECTOR, '#btnLogin'
pp_pay_now = By.CSS_SELECTOR, '#payment-submit-btn'
get_st_msg = By.CSS_SELECTOR, 'div[class="section_main_right"]>div>p'
# ST支付后点击支付页logo
st_zf_logo = By.XPATH, '//*[@class="header_logo_img"]'
# 支付成功信息
get_success_msg = By.CSS_SELECTOR, 'div[class="section_main_right"]>div>p'
# ck支付结果
get_ck_msg = By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div/p[1]'
# adyen frame
iframe = By.XPATH, '//*[@id="adyenButtonContainer"]/div/div/div[2]/div/div[1]/label/span[2]/span/iframe'
iframe1 = By.XPATH, '//*[@id="adyenButtonContainer"]/div/div/div[2]/div/div[2]/div[1]/label/span[2]/span/iframe'
iframe2 = By.XPATH, '//*[@id="adyenButtonContainer"]/div/div/div[2]/div/div[2]/div[2]/label/span/span/iframe'
# stripe frame
st_iframe = By.XPATH, '//*[@id="stripeContainer"]/div/iframe'
# checkout frame
ck_iframe = By.XPATH, '//*[@id="checkoutContainer"]/iframe'
# pacy_pay iframe
pacy_pay_iframe = By.XPATH, '//*[@id="CheckoutDirectIframe"]'
# unlimint_iframe
unlimint_iframe = By.CSS_SELECTOR, '#UnlimintIframe'
# pay_ease_direct_iframe
pay_ease_direct_iframe = By.CSS_SELECTOR, '#PayEaseDirectIframe'
