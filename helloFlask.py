from flask import Flask , render_template


app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello World</h1>'


@app.route('/render', methods = ["GET" , "POST"])
def index():

   if request.method == 'POST':
       user_id = request.form['user_id'] # formのname = "user_id"を取得
#       return render_template('render.html', user_id = user_id)
       return render_template('render.html')

   else:
       return render_template('render.html')

#    return render_template('render.html')



if __name__ == '__main__':
    app.run(debug=True)


