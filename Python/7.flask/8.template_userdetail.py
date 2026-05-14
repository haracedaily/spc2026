from flask import Flask, render_template

app=Flask(__name__)


users = [
    { 'name': 'Alice', 'age':25, "phone": "123-456-7890"},
    { 'name': 'Bob', 'age':30, "phone": "123-456-7890"},
    { 'name': 'Charlie', 'age':26, "phone": "123-456-7890"},
    { 'name': 'Drain', 'age':25, "phone": "123-456-7890"},
]

@app.route("/")
def index():
    final_html = render_template('users_detail.html', users=users)
    
    print(final_html)
    return final_html

if __name__ == "__main__":
    app.run(debug=True)