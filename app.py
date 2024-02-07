from flask import Flask,request,render_template,session,redirect,url_for
from flask_session import Session
app=Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.secret_key = ''

@app.route('/',methods=['GET','POST'])
def login():
    if request.method =='POST':
        name=request.form.get("name")
        paswd=request.form.get("pass")
        if name=='John' or name=='Bob' or name=='Jack':
            session['username']=name
            return redirect(url_for('bill'))
        else:
            return "User Not Found :("


    return render_template("index.html")

@app.route('/bill',methods=['GET'])

def bill():
    if 'username' in session:
        name=session['username']
        if name=='John':
            presentunit=200
            previousunit=100
            totalunit=presentunit-previousunit
            amountpaid=False
            if amountpaid==False:
                return 'Please Pay the Amount for ' + str(totalunit) + 'Units'
        elif name=='Bob':
            presentunit=200
            previousunit=100
            totalunit=presentunit-previousunit
            amountpaid=True
            if amountpaid==True:
                return 'No due for this Amount '
        elif name=='Jack':
            presentunit=200
            previousunit=50
            totalunit=presentunit-previousunit
            amountpaid=False
            if amountpaid==False:
                return 'Please Pay the Amount for ' + str(totalunit) + ' Units '
        else:
            return 'Error'
    else:
        return redirect(url_for('login'))

if __name__=='__main__':
    app.run(debug=True)