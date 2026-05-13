from flask import Flask,send_from_directory,jsonify

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

###################
# 정적 페이지 라우팅#
##################
@app.route('/')
def home():
    return send_from_directory('static','index.html')

@app.route('/user')
def user():
    return send_from_directory('static','user.html')

@app.route('/product')
def product():
    return send_from_directory('static','product.html')

###################
# API 페이지 라우팅#
##################
@app.route('/api/user/<id>')
def search_user(id):
    users = None
    return jsonify({"result":users})

@app.route('/api/product/<id>')
def search_user(id):
    products=None
    return jsonify({"result":products})

if __name__ == "__main__":
    app.run(debug=True)