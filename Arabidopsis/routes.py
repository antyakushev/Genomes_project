from os import system
from flask import Flask, render_template, request
from flask_wtf import Form
from wtforms import StringField, SubmitField
app = Flask(__name__)
app.secret_key = 'development key'

class RunnerForm(Form):
  filename = StringField("filename")
  submit = SubmitField("send")

@app.route('/form', methods=['GET', 'POST'])
def runner():
  form = RunnerForm()
 
  if request.method == 'POST':
    system(request.form["filename"]) # Huge security hole, do not do this in real life
    return 'Script is running'
 
  elif request.method == 'GET':
    return render_template('form.html', form=form)