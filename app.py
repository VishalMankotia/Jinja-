from flask import Flask,render_template,request
from encode import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/analysis')
def Analysis():
    # innn name get from analysisForm.html
    name="Vishal Mankotia"
    n="Govindani"
    return render_template('analysisForm.html',name=name,n=n)
 
@app.route('/aboutus')
def About():
    return render_template('aboutUs.html')

@app.route('/kuch', methods=['POST','GET'])
def kuch():
    result = request.form.to_dict()
    output = result['cover']
    to_hide = result['to_hide']
    file_type = result['file_type']
    final(output,to_hide,file_type)
    print(output,to_hide,file_type)

    return render_template('analysisForm.html')
app.run(debug=True)