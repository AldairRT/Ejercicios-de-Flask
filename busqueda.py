from flask import Flask, url_for, render_template, abort
# Creando la Aplicacion
app = Flask(__name__)

campos = ('Nombre', 'Primer Appelido', 'Segundo Appelido')
ruta = 'archivo.txt'
@app.route('/alumno/<cuenta>')
def mostrar(cuenta):
    falla = True
    with open(ruta, 'tr') as archivo:
        base = eval(archivo.read())
    for registro in base:
        try:
            if registro['Cuenta'] == int(cuenta):
                alumno = registro
                falla = False
                break
        except:
            abort(404)
    if falla:
        abort(404)
    return render_template("mostrar.html", alumno=alumno)

@app.errorhandler(404)  # codigo 404 se refiere a que la pagina no existe
def page_not_found(error):
    return 'Vuelva a intentarlo dentro de 24 horas..', 404
app.run(debug=True, port=8000)  # Ejecutarlo puerto 8000