from flask import Flask

app = Flask(__name__)

@app.route('/user/<username>')
def show_user_profile(username="홍길동"):
    return f"<h1>사용자 : {username}</h1>"

@app.route('/admin')
def show_admin_profile():
    return "관리자 : 홍길동"

@app.route('/product')
@app.route('/product/<int:id>')
def show_product_profile(id=0):
    return "상품코드 : {id} 상품 : 사과"

if __name__ == "__main__":
    app.run(debug=True)