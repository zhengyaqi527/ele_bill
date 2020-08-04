
response = {
    'log_id': 623376808640621252, 
    'words_result_num': 37, 
    'words_result': 
        [
            {'words': '11:36'}, {'words': '0.1K/s回lll[55'}, {'words': '订单已送达'}, 
            {'words': '西粉堂新疆米粉(双井店)'}, 
            {'words': '只7号是礼拜天吗'}, {'words': '香料世家鸡肉炒宽粉-中辣'}, {'words': '28'}, {'words': '中辣'}, 
            {'words': 'fanbin'}, {'words': '经典鸡肉拌米粉'}, {'words': '￥25'}, {'words': '微辣'}, 
            {'words': '发)发起人我是石敢当'}, {'words': '菠菜面筋'}, {'words': '￥15'}, {'words': '芝麻馕(半张切好)'}, {'words': '5'}, 
            {'words': '风)风雨长歌'}, {'words': '经典鸡肉炒米粉'}, {'words': '￥25'}, {'words': '微辣'}, 
            {'words': '平)平地摔职业选手'}, {'words': '香料世家鸡肉炒宽粉-微辣'}, {'words': '28'}, {'words': '微辣'}, 
            {'words': '其他'}, 
            {'words': '随机口味新疆果汁1份'}, {'words': 'YO'}, {'words': '店铺红包'}, {'words': '店铺红包'}, {'words': '3'}, {'words': '配送费'}, 
            {'words': '￥5.5'}, {'words': '包装费'}, {'words': '￥10'}, 
            {'words': '联系商家'}, {'words': '实付￥136.5'}
            ]
    }

words_need = []
words_result = response['words_result']
for words in words_result:
    if words['words'] != '订单已送达':
        continue
    

