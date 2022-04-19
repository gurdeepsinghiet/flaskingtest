from config import db ,app
from flask import Flask, request, flash, url_for, redirect, render_template,session,jsonify
from passlib.hash import sha256_crypt
from config import db ,app
class registration(db.Model):
    id = db.Column('studentid', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    add = db.Column(db.String(100))
    pincode = db.Column(db.String(100))

    def __init__(self, name, email, password, add, pincode):
        self.name = name
        self.email = email
        self.password = password
        self.add = add
        self.pincode = pincode


class students(db.Model):

    id = db.Column('student_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(50))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))

    def __init__(self, name, email,city, addr, pin):
        self.name = name
        self.email = email
        self.city = city
        self.addr = addr
        self.pin = pin



class Employess(db.Model):
    id = db.Column('emp_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    jobTitle = db.Column(db.String(50))
    designation = db.Column(db.String(200))
    contactAddress = db.Column(db.String(10))

    def __init__(self, name, jobTitle, designation, contactAddress):
        self.name = name
        self.jobTitle = jobTitle
        self.designation = designation
        self.contactAddress = contactAddress




# list of employee data dictionary
employees = [
    {
        "name": "Rohan",
        "designation": "Software Tester",
        "salary": "45000",
        "Department": "Security"
    },
    {
        "name": "Saurabh",
        "designation": "Dev Ops",
        "salary": "50000",
        "Department": "Operations"
    },
    {

        "name": "Gaurav",
        "designation": "Software Developer",
        "salary": "60000",
        "Department": "Engineering"
    }

]


@app.route("/")
def hello_world():

    if not session.get("isLogin"):
        name = "Hello world from flak"
        return render_template("index.html", name=name)
    else:
        return redirect(url_for('showRecord'))

@app.route("/testing")
def gapi1():
    return {
        'message' : "restapi popluated"
    },202


@app.route("/testing/<int:bnm>")
def gapi2(bnm):
    return {
        'message' : bnm
    },202

@app.route("/get/students")
def getStudent():
    return jsonify([
        {
            "name" : s.name,
            "email" : s.email,
            "city": s.city,

        }
    for s in students.query.all() ] )

@app.route("/get/students/<int:id>")
def getStudentbyId(id):
    regUser = registration.query.filter_by(id=id).first()
    return { "name" : regUser.name,"email" : regUser.email,"city"  : regUser.add }

@app.route("/createRegistration",methods=["POST"])
def createRegistration():
    data=request.get_json()
    u=registration(data["name"],data["email"],data["password"],data["addr"],data["pin"])
    db.session.add(u)
    db.session.commit()
    return {"message" : "data posted successfully"}

@app.route("/getregRecord",methods=["GET"])
def getregRecord():
     return jsonify([{ "name" : s.name , "email" : s.email , "address": s.add}  for s in registration.query.all()])

@app.route("/getregbyId/<string:email>")
def getregbyId(email):
    regUser = registration.query.filter_by(email=email).first()
    return {"name" : regUser.name, "address" : regUser.add, "email" : regUser.email}

@app.route("/postRegitsrtiondata",methods=["POST"])
def postRegitsrtiondata():
    data=request.get_json()
    reg=registration(data["name"],data["email"],data["password"],data["add"],data["pincode"])
    db.session.add(reg)
    db.session.commit()
    return {"message" : "your registartion data is posted"}


@app.route("/about2")
def abtus():
    name = "Hello world from flak"
    return render_template("about2.html", employees=employees)


# parametrize route
@app.route("/blog/<int:blognumber>/<string:author>")
def blogs(blognumber, author):
    name = "Hello world from flak"
    return render_template("blog.html", blognumber=blognumber, author=author)


@app.route("/about")
def about():
    return render_template("about.html", name="Hello about me page")

@app.route("/login")
def login():
    if not session.get("isLogin"):
        return render_template("login.html", name="Hello about me page")
    else:
        return redirect(url_for('showRecord'))

@app.route("/helloworld1")
def company():
    return "<h1>About me page for company</h1>"


@app.route("/contactform")
def contactform():
    return render_template("contact.html", name="this is contact page")


@app.route("/createRecord", methods=['GET', 'POST'])
def createRecord():
    if (request.method == 'POST'):
        student = students(request.form['name'], request.form['city'], request.form['email'], request.form['addr'],
                           request.form['pin'])
        db.session.add(student)
        db.session.commit()

        return redirect(url_for('showRecord'))

@app.route("/showTest", methods=["GET"])
def showSometest():
    return "Rest api from post man"

@app.route("/addtwonumber/<int:x>/<int:y>",methods=["GET"])
def suming(x,y):
    return {"sum" : x+y}

@app.route("/multyplynumbers/<int:x>/<int:y>")
def mul(x,y):
    return  {"multyply" : x*y}

@app.route("/hdfc/getInterset/<int:p>/<int:r>/<int:t>")
def interst(p,r,t):
    return  {"simple Interst" : p*r*t/100}

@app.route("/axis/getInterset/<int:p>/<int:r>/<int:t>")
def interstaxis(p,r,t):
    return  {"simple Interst" : p*7*t/100}

@app.route("/showRecord")
def showRecord():
    if not session.get("isLogin"):
        name = "Hello world from flak"
        return render_template("login.html", name=name)
    return render_template("show_all.html", students=students.query.all())


@app.route("/registrationform")
def register():
    return render_template("registration.html", name="this is contact form")


@app.route("/createreg", methods=['GET', 'POST'])
def getreg():
    if (request.method == 'POST'):
        secure_password = sha256_crypt.encrypt(str(request.form['password']))
        reg = registration(request.form['name'], request.form['email'], secure_password, request.form['add'],request.form['pincode'])
        db.session.add(reg)
        db.session.commit()
        return  redirect(url_for('showRecord'))

@app.route("/loginpost",methods=['GET', 'POST'])
def loginpost():
    if(request.method == 'POST'):
        username = request.form["email"]
        print(username)
        password = request.form["password"]
        regUser = registration.query.filter_by(email=username).first()
        print(regUser)
        if sha256_crypt.verify(password,regUser.password):
            session['isLogin'] = True
            return  redirect(url_for('showRecord'))

    return redirect(url_for('login'))


@app.route("/logout")
def logout():
    session['isLogin'] = None
    return redirect(url_for("login"))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
