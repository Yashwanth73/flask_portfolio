from flask import Flask,render_template,request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class Contact(db.Model):
    # Id : Field which stores unique id for every row in 
    # database table.
    # first_name: Used to store the first name if the user
    # last_name: Used to store last name of the user
    # Age: Used to store the age of the user
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    email= db.Column(db.String(20), unique=False, nullable=False)
    message = db.Column(db.String(200), nullable=False)
 
    # repr method represents how one object of this datatable
    # will look like
    def __repr__(self):
        return f"Name : {self.name}, Email: {self.email}, Meaage: {self.message}"

@app.route("/",methods=["GET"])
def home():
    return render_template('index.html')

@app.route("/add",methods=["POST"])
def add():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    if name != '' and email != '' and message !='':
        p = Contact(name=name, email=email, message=message)
        db.session.add(p)
        db.session.commit()
        return redirect('/')
    else:
        return redirect('/')
   

@app.route('/contact-form',methods=['POST'])
def login_form():   
    # return [name,phone]
    profiles = Contact.query.all()
    return render_template('response.html', response=profiles)

if __name__=="__main__":
    app.run(debug=True)
