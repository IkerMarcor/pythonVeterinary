<<<<<<< HEAD
from doctest import run_docstring_examples
from urllib.request import Request
from flask import Flask, render_template,request,flash,redirect,url_for
=======
from distutils.log import debug

from flask import Flask, render_template,request,flash,redirect,url_for
from waitress import serve
from sympy import true
from fuctions import *
>>>>>>> d50554acab903b109a236a0777a1409ebb1ccf35

app = Flask(__name__)
app.secret_key = b'1293hda7821hgdn{q'

<<<<<<< HEAD
=======
@app.route("/Sign-in", methods=['GET','POST'])
def Sign():
    if request.method == 'GET':
        return render_template('Sign-in.html')
    if request.method == 'POST':
        if 'Sign-in' in request.form:
            value = request.form['Sign-in']
            if  value== "Sign in":
                if request.form['password'] != "" and request.form["username"]:
                    valuep = request.form['password']
                    valuename = request.form['username']
                    print(verify_password_user(valuep,valuename))
                    if verify_password_user(valuep,valuename):
                       return redirect('Base.html')
                    else:
                        return redirect('Base.html')
                else:
                    return redirect('Base.html')
        



        else:
            return print("no existe")               
    else:
        return redirect('Base.html')
                

>>>>>>> d50554acab903b109a236a0777a1409ebb1ccf35
@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('Base.html')

@app.route("/sign-in", methods=['GET','POST'])
def Sign():
    if request.method == 'GET':
        return render_template('Sign-in.html')
    if request.method == 'POSt':
        value = Request.form['sign-in']
        #if value == 'submit':
            
if __name__ == "__main__":
<<<<<<< HEAD
    app.run(debug=True)
=======
    app.run(debug=true)
>>>>>>> d50554acab903b109a236a0777a1409ebb1ccf35
