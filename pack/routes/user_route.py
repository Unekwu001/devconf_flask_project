from flask import render_template,flash,session,make_response,redirect,request
from pack import app,db
from pack.mymodels import User

@app.route("/home")
def home():
    return render_template('user/home.html')

@app.route("/userdash")
def user_dash():
    loggedin=session.get('loggedin')
    if loggedin !=None:
        data=db.session.query(User).filter(User.user_id==loggedin).first()
        return render_template('user/user_dashboard.html',data=data)
    else:
        return redirect("/home")

@app.route("/userlogin",methods=['GET','POST'])
def user_login():
    if request.method=='GET':
        return render_template('user/user_login.html')
    else:
        username=request.form.get('username')
        password=request.form.get('password')

        #METHOD 1
        record=db.session.query(User).filter(User.user_fname==username,User.user_pass==password).first()
        if record:
            userID=record.user_id
            session['loggedin']=userID
            return redirect("/userdash")
        else:
            msg='invalid login'
            flash(msg)
            return redirect("/userlogin")
        #METHOD 2
        #record=db.session.query(User).filter(User.user_email==username).filter(User.user_pass==password).all()


@app.route("/userlay")
def user_layout():
    return render_template('user/layout.html')

@app.route("/signup",methods=['POST','GET'])
def user_signup():
    if request.method=='GET':
        return render_template('user/regform.html')
    else:
        fullname=request.form.get('fname')
        lastname=request.form.get('fname')
        email=request.form.get('email')
        password=request.form.get('pwd')
        d=User(user_email=email,user_pass=password,user_fname=fullname,user_lname=lastname)
        db.session.add(d)
        db.session.commit()
        id=d.user_id
        if id !=None:
            flash('thanks')
        return redirect("/userlogin")
  

@app.route('/user_logout')
def user_logout():
    if session.get('loggedin') !=None:
       session.pop('loggedin')
    return redirect("/home")