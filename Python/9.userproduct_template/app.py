from flask import Flask,render_template,request

app = Flask(__name__)
users = {
    1: {"id": 1, "name": "홍길동", "email": "hong@example.com"},
    2: {"id": 2, "name": "김철수", "email": "kim@example.com"},
    3: {"id": 3, "name": "이영희", "email": "lee@example.com"},
    4: {"id": 4, "name": "박민수", "email": "park@example.com"},
    5: {"id": 5, "name": "최지우", "email": "choi@example.com"},
}

products = {
    101: {"id": 101, "name": "Laptop", "price": 1200},
    102: {"id": 102, "name": "Keyboard", "price": 80},
    103: {"id": 103, "name": "Mouse", "price": 40},
    104: {"id": 104, "name": "Monitor", "price": 300},
    105: {"id": 105, "name": "Headset", "price": 150},
    106: {"id": 106, "name": "Laptop", "price": 1500},
}
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/user')
@app.route('/user/<id>')
def user(id=0):
    result = users
    id=int(id)
    if id:
        result = {key:user for key,user in users.items() if key==id}
    print(result)
    return render_template('user.html',users=result)

@app.route('/product')
def product():
    result = products
    # id, name
    # found = list(products.values())
    id = request.args.get('id')
    name = request.args.get('name')
    if id:
        id = int(id)
        result = {key:product for key,product in result.items() if key==id}
    if name:
        result = {key:product for key,product in result.items() if product.get("name").lower()==name.lower()}
    print(result)
    return render_template('product.html', products=result)

if __name__ == "__main__":
    app.run(debug=True)

# 1. /user 라는 경로를 만들고 URL파라미터를 기반으로 사용자를 조회할수 있게 한다.
#    /user는 모든 사용자 /user/1 홍길동 /user/2 김철수 등
# 2. /product 로 쿼리 파라미터를 기반으로 상품을 조회할수 있다
#    /product는 모든 상품, /product?id=101 로 상품 검색 ?name 으로도 상품 검색
