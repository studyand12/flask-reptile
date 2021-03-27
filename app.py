from flask import Flask, request, render_template
from Service.Request import paqu, xiangqing
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('Home page.html')
    else:
        user = request.form.get('user')
        txt = paqu(user)
        return render_template('video.html', text=txt)


@app.route('/video')
def hello_video():
    if request.method == "GET":
        return render_template('')


@app.route('/post/<string:id>')
def post(id):
    dd = xiangqing(id)
    long_num = len(dd[0])
    print(long_num)
    return render_template('web.html', txt=dd[0], txt1=dd[1], num=long_num)


if __name__ == '__main__':
    app.run()