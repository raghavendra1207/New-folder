from flask import Flask,request,render_template,jsonify,url_for,session,redirect
from backend import get_sign_in_where,get_sign_in_where_admin,insert_into_production,get_production_details,update_into_production
from flask_login import logout_user,LoginManager
app=Flask(__name__)
app.static_folder = 'static'
app.secret_key="my_secret_key"


# HOME PAGE
@app.route("/")
def display_home():
  
    return render_template('secure_login1.html')

# SECURE ADMIN LOGIN

@app.route("/secure_admin_login")
def display_admin():
    return render_template("secure_admin_login.html")

@app.route("/secure_admin_login",methods=["GET","POST"])
def display_admin_lg():
    if(request.method=="POST"):
        email=request.form["email1"]
        password=request.form["password1"]
        data1=get_sign_in_where_admin(email)
        if(data1==None):
            return render_template("secure_admin_login.html",object1="You are not registered")
        elif(email==data1[0]['email'] ):
            if(data1[0]['password']==password):
                session['logged_in']=True
                session['email']=email
                return render_template("/SecureHyderabadHome.html")
            else:
                return render_template("secure_admin_login.html",object2="Your Password is Wrong")
            
#This is Employee Login            

@app.route("/secure_login2")
def display_sign_in():
    
    return render_template("secure_login2.html")

@app.route("/secure_login2",methods=["GET","POST"])
def display_sign_in_log():
    if(request.method=="POST"):
        email=request.form["email1"]
        password=request.form["password1"]
        data1=get_sign_in_where(email)
        if(data1==None):
            return render_template("secure_login2.html",object1="You are Not Registered")
        elif(email==data1[0]["email_id"]):
            if(password==data1[0]["password1"]):
                return render_template("SecureHyderabadHome.html")
            else:
                return render_template("secure_login2.html",object2="Your Password is Wrong")
            
#THIS IS STORE            
@app.route("/StoreSecureHyderabad")
def display_StoreSecureHyderabad():
    if('logged_in' in session and session['logged_in']):
        return render_template("StoreSecureHyderabad.html")
    else:
        return redirect(url_for("display_home"))

#THIS IS 

@app.route("/PPLSecureHyderabad")
def display_PPLSecureHyderabad():
    if('logged_in' in session and session['logged_in']):
        return render_template("PPLSecureHyderabad.html")
    else:
        return redirect(url_for("display_home"))

#THIS IS QUALITY

@app.route("/QualitySecureHyderabad")
def display_QualitySecureHyderabad():
    if('logged_in' in session and session['logged_in']):
        return render_template("QualitySecureHyderabad.html")
    else:
        return redirect(url_for("display_home"))

#THIS IS PRODUCTION 

"""@app.route("/ProductionSecureHyderabad")
def display_ProductionSecureHyderabad():
    object1=get_production_details()  
    
    return render_template("ProductionSecureHyderabad.html",object1=object1)

@app.route("/ProductionSecureHyderabad",methods=["GET","POST"])
def load_data1():
    if(request.method=="POST"):
        data1=request.form
        data_total=[]
        
        for i in range(1,13):
            
            data2=[data1["Mc_No"+str(i)],data1["Product"+str(i)],data1["Debossed"+str(i)],data1["Color"+str(i)],data1["Resin"+str(i)],data1["MB_Color"+str(i)],data1["MB_Code"+str(i)],data1["Target"+str(i)],data1["MB_Speed"+str(i)],data1["Rejection"+str(i)]]
            count=0
            for j in data2:
                if(len(j)!=0):
                    count+=1
            if(count!=0):
                data_total.append(data2)

        
        insert_into_production(data_total)
        object1=get_production_details()    

        return render_template("ProductionSecureHyderabad.html",object1=object1)

"""

# this is redirection to practice1.html
@app.route("/ProductionSecureHyderabad")
def load_practice1():
    if('logged_in' in session and session['logged_in']):
        object1,COUNT_ID=get_production_details()
        list2=[]
        for i in object1:
            list4=[]
            for j in i.values():
                list4.append(j)
            list2.append(list4)
        
        object1=list2
        
        return render_template("practice1.html",object1=object1)
    else:
        return redirect(url_for('display_home'))

@app.route("/practice1",methods=["GET","POST"])
def load_data1():
    if(request.method=="POST" and 'logged_in' in session and session['logged_in']):
        data1=request.form
        #this is for the table rows retrieved from data_base
        data_updated=[]
        data_retrieved,COUNT_ID=get_production_details()
        for i in range(1,COUNT_ID['count(ID)']+1):
            data_1=[data1["Mc_No2"+str(i)],data1["Product2"+str(i)],data1["Debossed2"+str(i)],data1["Color2"+str(i)],data1["Resin2"+str(i)],data1["MB_Color2"+str(i)],data1["MB_Code2"+str(i)],data1["Target2"+str(i)],data1["MB_Speed2"+str(i)],data1["Rejection2"+str(i)]]
            data_updated.append(data_1)
        for_update=[]    
        for i in range(0,len(data_updated)):
            if(data_retrieved[i]['Machine_no']!=data_updated[i][0] or data_retrieved[i]['Product']!=data_updated[i][1] or data_retrieved[i]['Debossed']!=data_updated[i][2] or data_retrieved[i]['Color']!=data_updated[i][3] or data_retrieved[i]['Resin']!=data_updated[i][4] or data_retrieved[i]['MB_Color']!=data_updated[i][5] or data_retrieved[i]['MB_Code']!=data_updated[i][6] or data_retrieved[i]['Target']!=data_updated[i][7] or data_retrieved[i]['MB_Speed']!=data_updated[i][8] or data_retrieved[i]['Rejection_Percent']!=data_updated[i][9]):
                data_updated[i].insert(0,data_retrieved[i]['ID'])
                for_update.append(data_updated[i])
        update_into_production(for_update)
                    
        






        #this is for the table rows from 1 to 17
        data_total=[]
        data2=[]
        for i in range(1,3):
            
            
            data2=[data1["Mc_No"+str(i)],data1["Product"+str(i)],data1["Debossed"+str(i)],data1["Color"+str(i)],data1["Resin"+str(i)],data1["MB_Color"+str(i)],data1["MB_Code"+str(i)],data1["Target"+str(i)],data1["MB_Speed"+str(i)],data1["Rejection"+str(i)]]
            
            count=0
            for j in data2:
                if(len(j)!=0):
                    count+=1
            if(count!=0):
                data_total.append(data2)

        insert_into_production(data_total)
        object1,COUNT_ID=get_production_details()
        list2=[]
        for i in object1:
            list4=[]
            for j in i.values():
                list4.append(j)
            list2.append(list4)
        
        object1=list2
        
        
        return render_template("practice1.html",object1=object1)

"""

@app.route("/login",methods=['GET','POST'])
def insert_into_database():
    if (request.method=='POST'):
        email=request.form["email1"]
        password=request.form["password1"]
        
        data1=get_sign_in_where(email)
        
        if (data1==None):
            return render_template("login.html",object="you are not registered")
        elif ( email==data1[0]['email_id'] and data1[0]['password1']==password ):
            return render_template("nav.html")

        
@app.route("/signup")
def load_signup():
    return render_template("signup.html") 

@app.route("/signup",methods=['GET','POST'])
def load_signup_with_data():
    if (request.method=='POST'):
        email=request.form["email1"]
        password=request.form["password1"]
        name1=request.form["name1"]
        name2=request.form["name2"]
        
        
        result=insert_into_signup_database(name1,name2,email,password)
        print(result)
        if(len(result)>0):
            return render_template("signup.html",object1="you already registered")
        else:
            return render_template("login.html")

@app.route("/admin")
def display_sign_in_as():
    return render_template("admin_login.html")
        
@app.route("/admin",methods=['GET','POST'])
def insert_into_database_admin():
    if (request.method=='POST'):
        email=request.form["email1"]
        password=request.form["password1"]
        
        data1=get_sign_in_where(email)
        
        if (data1==None):
            return render_template("login.html",object="you are not registered")
        elif ( email==data1[0]['email_id'] and data1[0]['password1']==password ):
            return render_template("admin_home.html")        
        
"""


 #this is logout 
 
@app.route("/logout")

def logout():
    session['logged_in']=False
    return redirect(url_for("display_home"))
if(__name__=="__main__"):
    app.run("0.0.0.0",debug=True)