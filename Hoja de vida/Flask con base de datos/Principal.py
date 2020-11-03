from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class students(db.Model):
   id = db.Column('id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   ciudad = db.Column(db.String(50))
   direccion= db.Column(db.String(200))
   codigo = db.Column(db.String(10))
   edad = db.Column(db.String(10))
   

   def __init__(self,datos):
       self.name = datos["name"]
       self.ciudad = datos["ciudad"]
       self.direccion = datos["direccion"]
       self.codigo = datos["codigo"]
       self.edad = datos["edad"]

class formacion(db.Model):
   id = db.Column('id', db.Integer, primary_key = True)
   bachillerato = db.Column(db.String(100))
   universidad = db.Column(db.String(100))
   maestria= db.Column(db.String(100))
   otro = db.Column(db.String(100))
   student_id = db.Column(db.Integer, db.ForeignKey('student.id'))

   def __init__(self,datos):
       self.bachillerato = datos["bachillerato"]
       self.universidad = datos["universidad"]
       self.maestria = datos["maestria"]
       self.otro = datos["otro"]
       self.student_id = datos["student_id "]

class Interes(db.Model):
    id = db.Column('id', db.Integer, primary_key = True)
    Tecnologias_de_interes = db.Column(db.String(50))
    pasatiempos = db.Column(db.String(150))
    informacion_adicional  = db.Column(db.String(150))
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))

    def __init__(self, datos):
        self.Tecnologias_de_interes = datos["Tecnologias_de_interes"]
        self.pasatiempos = datos["pasatiempos"]
        self.informacion_adicional = datos["informacion_adicional"]
        self.student_id = datos["student_id "]

@app.route('/show_all.html')
def show_all():
   return render_template('show_all.html', students = students.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['ciudad'] or not request.form['direccion']:
         flash('Por favor ingrese todos los campos', 'error')
      else:  
         datos = {
         'name' : request.form['name'], 
         'ciudad' : request.form['ciudad'],
         'direccion' : request.form['direccion'], 
         'codigo' : request.form['codigo'], 
         'edad' : request.form['edad']
       }
      student = students(datos)
      db.session.add(students)
      db.session.commit()
      flash('El registro se agregó correctamente')
      return redirect(url_for('show_all'))
   return render_template('new.html')

@app.route("/update", methods=["POST"])
def update():
    name = request.form.get("oldname")
    student = students.query.filter_by(name=name).first()
    return render_template('update.html', result = student, oldname = name)

@app.route("/update_record", methods=["POST"])
def update_record():
    name = request.form.get("oldname")
    student = students.query.filter_by(name=name).first()
    student.name = request.form['nombre']
    student.ciudad = request.form['ciudad']
    student.direccion = request.form['direccion']
    student.codigo = request.form['codigo']
    student.edad = request.form['edad']
    db.session.commit()
    return redirect('/show_all.html')

@app.route("/delete", methods=["POST"])
def delete():
    name = request.form.get("oldname")
    student = students.query.filter_by(name=name).first()
    db.session.delete(student)
    db.session.commit()
    return redirect("/show_all.html")

@app.route('/Formacion_academica', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
       if not request.form['bachillerato'] or not request.form['universidad'] or not request.form['maestria'] or not request.form['otro']:
           flash('Por favor ingrese todos los campos', 'error')
       else:
         datos = {
            'bachillerato' : request.form['bachillerato'], 
            'universidad' : request.form['universidad'], 
            'maestria' : request.form['maestria'],
            'otro' : request.form['otro '],  
            'students_id' : request.form['students_id'] 
         }
         student = students(datos)

         db.session.add(student)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('show_all'))
   return render_template('new.html')
@app.route('/Intereses', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
       if not request.form['tecnologias_de_interes'] or not request.form['pasatiempos'] or not request.form['informacion_adicional']:
           flash('Por favor ingrese todos los campos', 'error')
       else:
         datos = {
            'tecnologias_de_interes' : request.form['tecnologias_interes'], 
            'pasatiempos' : request.form['pasatiempos'], 
            'informacion_adicional' : request.form['informacion_adicional'], 
            'students_id' : request.form['students_id'] 
         }
         student = students(datos)

         db.session.add(student)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('show_all'))
   return render_template('new.html')
@app.route("/")
def Inicio ():
   return render_template("Inicio.html")  

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)

 