

from ourapp import app
from flask import render_template, redirect, url_for , request, flash, get_flashed_messages
from ourapp import db
from ourapp.models import User
from ourapp.forms import Userform, Adminform
import os

#S3 Buckets
import boto3
BUCKET_NAME = "easerismbucket"
s3 = boto3.client("s3",aws_access_key_id="#",
         aws_secret_access_key= "#")



# thi3 necessery for hosting  and best way to give path
base_path = os.path.dirname(__file__)
UPLOAD_PATH = 'static/uploads'
app.config["UPLOAD_PATH"] = UPLOAD_PATH



@app.route("/")

@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/aboutus")
def aboutus_page():
    return render_template("aboutus.html")

@app.route("/gallery")
def gallery_page():
    pics = User.query.all()
    return render_template("gallery.html", pics=pics)

@app.route("/upload",methods=["GET","POST"])
def upload_page():
    form = Userform()
    if form.validate_on_submit(): # submission
        
        pic = request.files['pic']  # should get a from  normal wtf cannot read image
        imagefilename= pic.filename
        pic.save(os.path.join( base_path + "/" + app.config['UPLOAD_PATH'],imagefilename))

        filelink = base_path + "/" + UPLOAD_PATH + "/"+ imagefilename
        s3.upload_file(filelink, BUCKET_NAME, imagefilename)

        

        user_to_create = User(username=form.username.data, email_address=form.email_address.data,filename=imagefilename) # add to database
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for("gallery_page"))

    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
   
    return render_template("upload.html",form=form)




@app.route("/admin", methods=["GET","POST"])
def admin():
    adminform = Adminform()
    if adminform.validate_on_submit():
        return redirect(url_for('admindash_page'))

    return render_template("adminvalidation.html",form=adminform)

@app.route("/qwdwGKJDIIUVJKNCIVYVU123iu1get9q7w097rhoihfohwogkeoieugorgouweoiggoiergoibfugwergohopergowerghwerowheoiworworowhbfboifhhifieruoiwehjbfkjbbfwguiw63487td9b")
def admindash_page():
    user = User.query.all()
    return render_template("admindash.html",users=user)

