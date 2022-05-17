from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# post --> send data from user to server
# get --> get data from server to user
@app.route('/', methods = ['POST'])
def data():
    form_data = request.form
    f = request.files['file']
    f.save(secure_filename(f.filename))
    print(form_data['name'])
    print(form_data['subject'])
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)