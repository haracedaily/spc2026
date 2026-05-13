from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route("/")
def home():
    return "hi"

@app.route("/search")
def search():
    query = request.args.get('q')
    print(request.args.keys())
    print(request.args.values())
    page = request.args.get("page",default=1,type=int)
    user_input = f"Your query is {query} and page = {page}"
    return jsonify({"message":user_input})

@app.route('/user/<username>/post')
def show_user_posts(username):
    page = request.args.get('page',default=1,type=int)
    # Flask에서 type지정하면 typeErr일 경우 무시함 => 처리는 어떻게?
    print(page)
    result = f'User is {username} and page is {page}'
    return jsonify({"message":result})

@app.route("/users")
def search_user():
    result = None
    #query parameter로 name, age, phone 
    
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)