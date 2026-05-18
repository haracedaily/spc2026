from flask import Flask, request, session, render_template, redirect, url_for
from datetime import timedelta

app = Flask(__name__)

app.secret_key='randomKey'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

items = [
    {"id":'item1',"name":"햄버거","price":3000},
    {"id":'item2',"name":"핫도그","price":2000},
    {"id":'item3',"name":"콜라","price":1500},
]
carts = [
]
@app.route('/')
def home():
    return render_template('index.html', items=items)

@app.route('/cart')
def cart():
    cart_items = {}
    total_price=0
    for item_id, quantity in session.get('cart',{}).items():
        item = next((i for i in items if i['id']== item_id), None)
        cart_items[item_id]={'name':item['name'], 'quantity':quantity, 'price':item['price'] }
        total_price += item['price'] * quantity
    return render_template('cart.html', carts = cart_items, total_price = total_price)
    # if session.get('carts'):
    #     return render_template('cart.html',carts=session['carts'])
    # return render_template('cart.html')

@app.route('/subtraction')
def sub():
    name=request.args.get('name')
    carts = session.get('carts')
    for i, cart in enumerate(carts):
        if cart['name']==name:
            if cart['cnt']>1:
                cart['cnt']-=1
            else :
                carts.pop(i)
            break
    session['carts']= carts
    return render_template('cart.html',carts=carts)
@app.route('/add/<item_id>')
def add(item_id):
    print(item_id)
    # item_id = request.args.get('item_id')
    if 'cart' not in session:
        session['cart']={}

    if item_id in session['cart']:
        session['cart'][item_id]+=1
    else:
        session['cart'][item_id]=1
    session.modified=True

    print(session.get('cart'))

    return redirect(url_for('home'))
    # name = request.args.get('name')
    # price = request.args.get('price')
    # carts = session.get('carts', [])

    # for cart in carts:
    #     if cart['name'] == name:
    #         cart['cnt'] += 1
    #         break
    # else:
    #     # for-else 구조: break 안 걸리면 실행됨
    #     carts.append({
    #         'name': name,
    #         'price': price,
    #         'cnt': 1
    #     })

    # session['carts'] = carts

    # return render_template(
    #     'index.html',
    #     items=items,
    #     message=f"{name} 상품을 담았습니다."
    # )

if __name__=='__main__':
    app.run(debug=True)