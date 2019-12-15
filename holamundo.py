from flask import Flask, url_for, render_template


# creando una aplicacion
app = Flask(__name__)


# definir una ruta index
@app.route('/')
def index():
    return '<img src="'+ url_for('static',filename='img/codigo-imagen.png')+'"/>'
    return "Hola desde Flask-Codigo Norte"


@app.route('/login')
def login():
    return "Estas en el login de Usuario"


@app.route('/compras')
def compras():
    return "Estas en el modulo de Compras"


@app.route('/productos/')
@app.route('/productos/<codigo>')
@app.route('/productos/<codigo>/<int:valor>')
def productos(codigo="Valor 0 por defecto", valor="0"):
    return 'El producto es: {} {}'.format(codigo, valor)

@app.route('/template1/')
@app.route('/template1/<nombre>')
def saluda(nombre=None):
    return render_template("template1.html",nom=nombre)
@app.errorhandler(404) #el codigo 404 se refiere a que la pagina no existe
def page_not_found(error):
    return "Ha ocurrido un problema, por favor vuelva a intentarlo dentro de 24 horas...", 404


@app.route('/pagina')
def pagina():
    return render_template('index.html')


app.run(debug=True, port=8000)  # Ejecutarlo desde el puerto 5000
