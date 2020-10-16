import re
import pprint

# 标记订单起始、价格
TITLE_reg = re.compile(r'订单已送达')
PRICE_reg = re.compile(r'^-?￥?(?P<price>[0-9]{0,3}(?:\.[0-9]{1,2})?)$')

# 标记折扣、附加费关键字
DISCOUNT_wds = ['红包', '满减', '立减']
ADDITION_wds = ['配送费', '包装费']


def ocr():
    resp = {
        'words_result': [
            {'words': '23:15'}, {'words': '19.0K/sH令〔50'}, 
            {'words': '订单已送达'}, {'words': '阿甘锅盔(合生汇店)'}, 
            {'words': 'R)风雨长歌'}, {'words': '酸辣粉'}, {'words': '￥18'}, 
            {'words': '发)发起人石敢当'}, {'words': '三姐妹套餐(牛肉+梅干菜+'}, 
            {'words': '￥42'}, {'words': '酸辣粉'}, 
            {'words': '￥18'}, {'words': '德谟克利希'}, 
            {'words': '三姐妹套餐(牛肉+梅干菜+'}, {'words': '￥42'}, 
            {'words': '其他'}, {'words': '店 铺满减'}, {'words': '20'}, 
            {'words': '首次光顾立减'}, {'words': '-￥4'}, 
            {'words': '店铺红包'}, {'words': '￥6'}, {'words': '配送费'}, 
            {'words': '￥5.4'}, {'words': '包装费'}, {'words': '￥4'}, 
            {'words': '③联系商家'}, {'words': '实付￥994'}, {'words': '配送信息'}, 
            {'words': '送达时间'}, {'words': '尽快送达'}
            ], 
        'log_id': 1302606979516071936, 
        'words_result_num': 31}
    return resp['words_result']

# 判断是否是店名title
def is_title(word):
    return bool(TITLE_reg.findall(word))

# 判断是否是价格
def extract_price(word):
    prices = PRICE_reg.findall(word)
    try:
        return prices and float(prices[0])
    except ValueError:
        return None

# 判断是否是折扣
def is_discount(wd):
    for discount in DISCOUNT_wds:
        if discount in wd:
            return True
    return False

# 判断是否是附加费用
def is_addition(wd):
    for addition in ADDITION_wds:
        if addition in wd:
            return True
    return False

# 判msg列表中最后一个元素的信息（折扣、附加费或其他）
def extract_attr(msg):
    if not msg:
        return
    try:
        attr = msg.pop()
        if is_discount(attr):
            return 'discount'
        elif is_addition(attr):
            return 'addition'
        return msg.pop()
    except IndexError:
        return 'pre'

# 生成账单
def gen_accounts(words):
    order_msg = []
    orders = []

    title = None
    discount = 0
    addition = 0
    total = 0

    title_flag = False
    for word in words:
        wd = word.get('words')
        if not wd:
            continue
        # 提取本次订单店名
        if is_title(wd):
            title_flag = True
            continue
        elif title_flag:
            title = wd
            title_flag = False
            continue
        # 如果检测是金额，就拿order_msg list中最后一个数据，来判断当前的金额是附加费、折扣、商品金额或者其他
        price = extract_price(wd)
        if price and order_msg:
            attr = extract_attr(order_msg)
            if not attr:
                continue
            if 'discount' == attr:
                discount += price
            elif 'addition' == attr:
                addition += price
            elif 'pre' == attr and orders:
                orders[-1]['order_price'] += price
            else:
                orders.append({'author': attr, 'order_price': price})
            total += price
            order_msg.clear()
        else:
            order_msg.append(wd)

    for order in orders:
        # 实付款
        total_actual = total - discount * 2
        # 商品原价+附加费
        total_order = total - discount - addition
        order_price = order['order_price']
        actual_price = total_actual / total_order * order_price
        order['actual_price'] = '%.2f' % actual_price

    accounts = {
        "store": title,
        "total_order": total_order,
        "total_actual": total_actual,
        "addition": addition,
        "discount": discount,
        "guests": orders
        }

    pprint.pprint(accounts)   
    
    return accounts

if __name__ == '__main__':
    words = ocr()
    gen_accounts(words)
