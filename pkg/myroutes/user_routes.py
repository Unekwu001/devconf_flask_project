'''routes.py'''

from flask import render_template,abort,request,redirect,flash,url_for,make_response,session

from pkg import app,db

from pkg.mymodels import User


@app.route('/')
def user_home():
    return render_template('user/home.html')

@app.route('/signup',methods=['POST','GET'])
def user_signup():
    if request.method=='GET':
        return render_template('user/regform.html')
    else:
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        pwd = request.form.get('pwd')
        '''Insert into the table'''
        u = User(user_email=email,user_fname=fname, user_lname=lname,user_pass=pwd)
        db.session.add(u)
        db.session.commit()
        id = u.user_id
        if id != None:
            flash('Thank you for joining')
        return redirect('/login')

@app.route('/login', methods=['POST','GET'])
def user_login():
    if request.method =='GET':
        return render_template('user/user_login.html')
    else:
        username = request.form.get('username')
        password=request.form.get('password')
        '''METHOD 1'''
        record = db.session.query(User).filter(User.user_email==username,User.user_pass==password).first()
        '''You can pass record to a test template to see the content'''
        # return render_template('user/test.html',record=record)
        if record:
            '''Login is successful, retrieve details as an <Object> of User and save in session and redirect to the dashboard'''
            userID = record.user_id
            session['loggedin'] = userID             
            return redirect('/user_dash')
        else:
            '''Login failed, save feedback in flash and redirect to the login page again (this same route - GET request)'''  
            flash('Failed Login')
            return redirect('/login')

@app.route('/user_dash')
def user_dashboard():
    loggedin = session.get('loggedin')
    '''Run a query that fetches the details of this id from User table, pass d data to  template'''
    if loggedin !=None:
        data = db.session.query(User).filter(User.user_id==loggedin).first()
        return render_template('user/user_dashboard.html',data=data)
    else:
        return redirect('/')

@app.route('/user_logout')
def user_logout():
    if session.get('loggedin') != None:
        session.pop('loggedin')
    return redirect(url_for('user_home'))
    