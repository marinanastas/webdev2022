from flask import Flask, render_template, request
import urllib.request
import json
import collections



app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/telegrams')
def telegrams():
    return render_template('telegrams.html')

@app.route('/longread', methods = ['POST', 'GET'])
def longread():
    return render_template('longread.html')

@app.route('/add', methods = ['POST', 'GET'])
def add():
#    if request.method == 'POST':
#        name = request.form['link']
#        mail = request.form['word']
#        plott(getsearcher(link, word))
#        #fin_form = link+'\n'+word
    return render_template('add.html')


if __name__ == '__main__':
    import os
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)



