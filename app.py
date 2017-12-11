from flask import Flask,render_template,request,make_response,abort
import requests,sys
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World-Sumiran"


@app.route('/authors',methods=['GET'])
def authors():
    data = requests.get('https://jsonplaceholder.typicode.com/users').json()
    posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    users = {d['id']:{'name':d['name'],'count':0} for d in data}
    for post in posts:
        users[post['userId']]['count']+=1
    return render_template('author_count.html',users=users)



@app.route('/form')
def index():
   return render_template('setcookie.html')
   
@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    resp = make_response(render_template('readcookie.html'))
    if request.method == 'POST':
        user_name = request.form['name']
        user_age = request.form['age']
        resp.set_cookie('My_name', user_name)
        resp.set_cookie('My_age', user_age)
    
    return resp
    
@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('My_name')
    age = request.cookies.get('My_age')
    return '<h1>Hello '+name+' & your age is '+age+'</h1>'



@app.route('/robots.txt/')
def custom403():
   abort(403)

@app.route('/html/')
def hpdf():
    return render_template('HPDF.html')
@app.route('/image/')
def Img():
    return render_template("hasura.html")



@app.route('/input')
def student():
   return render_template('input_data.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
       result=request.form
       return render_template("show_result.html",result = result)

if __name__ == "__main__":
    app.run()
           
