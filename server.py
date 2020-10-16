import json
from flask import Flask, request
from flask import render_template
from ele.ele_bill import analyse_img, get_token
from ele.ai_account import gen_accounts

app = Flask(__name__, template_folder="ele/templates", static_folder="ele/static")

# 进入首页
@app.route('/')
def home():
    return render_template('index.html')

# 上传账单截图
@app.route('/upload', methods=["POST"])
def upload():
    f = request.files['file']
    f.save("./ele/static/img/ele_bill.png")
    print(f)
    res = {"code": 0}
    return json.dumps(res)

# 获取账单    
@app.route('/get_bill', methods=["GET"])
def get_bill():
    token = get_token()
    path = "./ele/static/img/ele_bill.png"
    ocr_res = analyse_img(token, path)
    words = ocr_res['words_result']
    print(words)
    accounts = gen_accounts(words)
    return json.dumps(accounts)

@app.route('/get_json')
def get_json():
    json = {'words_result': [{'words': '17:30'}, {'words': '88K/s⑧ HD alll HD all C95'}, {'words': '订单已送达'}, {'words': '麦当劳麦乐送(北京双井桥店)'}, 
    {'words': '美3'}, {'words': '麦乐鸡5块'}, {'words': '￥11.5'}, {'words': '那么大鸡排'}, {'words': '￥13'}, {'words': '发)发起人1号订餐人'}, 
    {'words': '小食纷享盒(含那么大鸡排'}, {'words': '￥31'}, {'words': '其他'}, {'words': '店铺红包'}, {'words': '￥15'}, {'words': '配送费(配送费)'}, 
    {'words': '￥5'}, {'words': '电话商家'}, {'words': '已优惠￥15实付￥455'}]}
    return json

if __name__ == '__main__':
  app.run(debug=True)