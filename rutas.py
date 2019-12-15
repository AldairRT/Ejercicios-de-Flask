from flask import Flask, url_for, render_template,abort


# creando una aplicacion
app = Flask(__name__)

@app.route('/suma/<num1>/<num2>')
def suma(num1,num2):
  try:
      resultado=int(num1)+int(num2)
  except:
      abort(404)
  return render_template("template2.html", n1=num1,n2=num2,res=resultado)

@app.route('/tabla/<numero>')
def generar_tabla(numero):
    try:
        numero = int(numero)
    except:
        abort(404)
    return render_template("template3.html", valor=numero)

@app.route('/enlaces/')
def enlaces():
    enlaces = [
        {"url": "http://www.google.com", "Texto": "Google"},
        {"url": "https://www.palletsprojects.com/p/flask/", "Texto": "Flask"},
        {"url": "https://jinja.palletsprojects.com", "Texto": "Jinja"},
        {"url": "http://www.python.org", "Texto": "Python"}, ]
    return render_template("template4.html", enl=enlaces)

@app.errorhandler(404) #el codigo 404 se refiere a que la pagina no existe
def page_not_found(error):
    return "Ha ocurrido un problema, por favor vuelva a intentarlo dentro de 24 horas...", 404

app.run(debug=True, port=8000)  # Ejecutarlo desde el puerto 5000