from flask import Flask,request,render_template,session,redirect,url_for,jsonify
from flask_session import Session

app=Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

def calculate_bill(name,presentunit,previousunit):
    total_unit=presentunit-previousunit
    total_amount=total_unit*10
    return total_unit, total_amount


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

@app.route('/bill',methods=['GET','POST'])

def bill():
    if request.method =='POST':
        if 'username' in session:
            name=session['username']
            if name=='John':
              presentunit=int(request.form.get("Present"))
              previousunit=int(request.form.get("Previous"))
              total_unit, total_amount=calculate_bill(name,presentunit,previousunit)
              return jsonify({
                "message": "Success",
                "user": name,
                "total_units_consumed": total_unit,
                "total_amount_rupees": total_amount
            })
        return jsonify({"message": "Error"})
    return render_template("response.html")



if __name__=='__main__':
    app.run(debug=True)