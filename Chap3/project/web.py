from flask import Flask, render_template, request
from weather_advance import *
app = Flask(__name__, template_folder='E:\Python\python3')

@app.route("/", methods = ['GET','POST'])
def check():
    if request.method == 'POST':
        if request.form['action'] == '查询':
            play.input_str = request.form.get('city')
        elif request.form['action'] == '历史':
            play.input_str = 'history'
        elif request.form['action'] == '帮助':
            play.input_str = 'help'
        play.data_import()
        result = play.check()
        return render_template('web.html', result = result)
    else:
        return render_template('web.html')

if __name__ == "__main__":
    play = WeatherChecker()
    app.run(debug=True)
