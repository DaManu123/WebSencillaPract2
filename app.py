from flask import Flask, render_template
import json
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Inicializar Flask
app = Flask(__name__)

# Función para cargar datos del JSON
def cargar_datos():
    with open('datos.json', 'r', encoding='utf-8') as file:
        return json.load(file)

# Ruta principal
@app.route('/')
def index():
    datos = cargar_datos()
    return render_template('index.html', data=datos)

# Ruta del menú
@app.route('/menu')
def menu():
    datos = cargar_datos()
    return render_template('menu.html', data=datos)

# Ruta de contacto
@app.route('/contacto')
def contacto():
    datos = cargar_datos()
    return render_template('contacto.html', data=datos)

# Ruta de reservaciones
@app.route('/reservaciones')
def reservaciones():
    datos = cargar_datos()
    return render_template('reservaciones.html', data=datos)

if __name__ == '__main__':
    app.run(debug=True)
