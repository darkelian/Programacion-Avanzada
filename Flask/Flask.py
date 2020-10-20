from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def Inicio_Elian():
   return render_template('Elian/Inicio.html')


@app.route('/Formacion_Elian')
def Formacion_Elian():
   return render_template('Elian/Formacion.html')

@app.route('/Tecnologia_Elian')
def Tecnologia_Elian():
   return render_template('Elian/Tecnologias.html')
@app.route('/Inicio_Dayana')
def Inicio_Dayana():
   return render_template('Dayana/Hoja de vida.html')

@app.route('/Formacion_Dayana')
def Formacion_Dayana():
   return render_template('Dayana/Formacion.html')

@app.route('/Tecnologias_Dayana')
def Tecnologias_Dayana():
   return render_template('Dayana/Tecnologias.html')

if __name__ == '__main__':
   app.run()