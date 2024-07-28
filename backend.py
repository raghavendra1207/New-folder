from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://root:Graghu678@localhost/jovian?charset=utf8mb4")
def load_jobs():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jovian_job"))
        first_row = result.fetchall()  # Fetch the first row
    data1=[]
    # Convert the Row object to a dictionary
    for i in first_row:
        data1.append(dict(i._mapping))
    return data1

 
#RETREVING SIGN IN DETATILS OF EMPLOYEE
def get_sign_in():
    with engine.connect() as conn:
        result=conn.execute(text("select * from signin")).fetchall()
        list1=[]
        for i in result:
            list1.append(dict(i._mapping))
        return list1
    
def get_sign_in_where(email1):
    
    with engine.connect() as conn:
        result=conn.execute(text("select * from signin where email_id = :val"),
        {'val':email1}).fetchall()
        if(len(result)==1):
            result=[result[0]._mapping]
            return result
            
#RETREVING SIGN IN DETAILS OF ADMIN            
def get_sign_in_where_admin(email1):
    
    with engine.connect() as conn:
        result=conn.execute(text("select * from admin where email = :val"),
        {'val':email1}).fetchall()
        if(len(result)==1):
            result=[result[0]._mapping]
            return result
    
#RETREVING PRODUCTION DETAILS FROM PRODUCTION
def get_production_details():
    with engine.connect() as conn:
        data=conn.execute(text("select * from production")).fetchall()
        result=[]
        for i in data:
            result.append(i._mapping)
        data1=conn.execute(text("select count(ID) from production")).fetchall()
        COUNT_ID=data1[0]._mapping  
        return result,COUNT_ID
    
#Inserting data into Production table
def insert_into_production(data1):
    for i in data1:
        with engine.connect() as conn:
            conn.execute(text("insert into production (Machine_no,Product,Debossed,Color,Resin,MB_Color,MB_Code,Target,MB_Speed,Rejection_Percent) values (:Machine_No,:Product,:Debossed,:Color,:Resin,:MB_Color,:MB_Code,:Target,:MB_Speed,:Rejection_Percent)"),{'Machine_No':i[0],'Product':i[1],'Debossed':i[2],'Color':i[3],'Resin':i[4],'MB_Color':i[5],'MB_Code':i[6],'Target':i[7],'MB_Speed':i[8],'Rejection_Percent':i[9]})
            conn.commit()

#Updating the production table
def update_into_production(values):
    for i in values:
        id=i[0]
        with engine.connect() as conn:
            conn.execute(text("update production set Machine_no=:Machine_No,Product=:Product,Debossed=:Debossed,Color=:Color,Resin=:Resin,MB_Color=:MB_Color,MB_Code=:MB_Code,Target=:Target,MB_Speed=:MB_Speed,Rejection_Percent=:Rejection_Percent where ID=:id"),{'Machine_No':i[1],'Product':i[2],'Debossed':i[3],'Color':i[4],'Resin':i[5],'MB_Color':i[6],'MB_Code':i[7],'Target':i[8],'MB_Speed':i[9],'Rejection_Percent':i[10],'id':i[0]})
            conn.commit()





        

"""  
#INSERTING SIGNUP DETAILS OF EMPLOYEE     
def insert_into_signup_database(name1, name2, email1, password1):
    with engine.connect() as conn:
        result=conn.execute(text("select * from signup where email_id=:email1"),{'email1':email1}).all()
        if(len(result)==0):

            conn.execute(text("insert into signup (first_name, last_name, email_id, password1) values (:name1, :name2, :email1, :password1)"), 
                        {'name1': name1, 'name2': name2, 'email1': email1, 'password1': password1})
            conn.commit()

            conn.execute(text("insert into signin (email_id,password1) values(:email1,:password1) "),{'email1':email1,'password1':password1})
            conn.commit()
            
            
        return result
"""

        


