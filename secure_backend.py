from flask import Flask,render_template,jsonify
import sqlalchemy





app=Flask(__name__)
object1=[
    {
        'id':1,
        'name':"Data Analyst",
        'location':"Hyderabad",
        'company' :"Wipro" ,
        'salary':110000
    },
    {
        'id':2,
        'name':"Frontend Engineer",
        'location':"Hyderabad",
        'company' :"TCS" ,
        'salary':1100000
    },
    {
        'id':4,
        'name':"Back End Developer",
        'location':"Hyderabad",
        'company' :"DBS",
        'salary':150000
    }
]
@app.route("/")
def hello_world():
    return render_template('practice1.html',object1=object1)

@app.route("/api/json")
def jobs_list():
    return jsonify(object1)
@app.route("/templates/login")
def do_transfer():
    return render_template('login.html')

@app.route("/templates/signup")
def do_signup():
    return render_template('signup.html')

if(__name__=="__main__"):
    app.run("0.0.0.0",debug=True)