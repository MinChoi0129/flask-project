from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome(): return render_template('welcome.html', image_file = "image/everytime.png")

@app.route('/register')
def register(): return render_template('register.html', subTitle = '회원가입')

@app.route('/login')
def login(): return render_template('login.html', subTitle = '로그인')

@app.route('/mypage/<myname>')
def myPage(myname):
    return render_template('mypage.html', subTitle = myname, image_file = 'image/' + myname + '.png')


if __name__ == '__main__':
    app.run(host='192.168.0.24', port=5050, debug=True)