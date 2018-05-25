import subprocess
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
        try:
            command = 'python ./' + request.form["filename"] + ' ./data/TAIR10_GFF3_genes.gff'
            # Security hole, do not do this in real life
            retcode = subprocess.call(command, shell=True)
            if retcode < 0:
                return "Excution was terminated by signal"
            else:
                return "Excuted script"
        except OSError as e:
            return "Execution failed " + request.form["filename"] + " " + str(e)

    elif request.method == 'GET':
        return render_template('form.html', form=form)