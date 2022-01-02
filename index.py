from flask import Flask,render_template,request
import sqlite3 as sql
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/form_data',methods=["POST","GET"])    
def form_data():
    if request.method=="POST":
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']
        connection=sql.connect('database2.db')
        cur=connection.cursor()
        cur.execute("INSERT INTO details (name,email,password) VALUES(?,?,?)",(name,email,password))
        connection.commit()
        connection.close()
        
        return render_template('index.html',msg="data inserted")
@app.route("/data_fetch")
def data_fetch():
    connection=sql.connect('database2.db')
    connection.row_factory=sql.Row
    cur=connection.cursor()
    cur.execute("SELECT * FROM details")   
    connection.commit()  
    rows=cur.fetchall()
    connection.close()

    return render_template('data.html',rows=rows)
if __name__=='__main__':
    app.run(debug = True)    