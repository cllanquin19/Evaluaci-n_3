from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        # Obtener datos del formulario
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])

        # Calcular el promedio
        promedio = (nota1 + nota2 + nota3) / 3

        # Verificar condiciones de aprobación
        if promedio >= 40 and asistencia >= 75:
            resultado = "Aprobado"
        else:
            resultado = "Reprobado"

        # Pasar resultados a la plantilla
        return render_template('resultado_ejercicio1.html', promedio=promedio, asistencia=asistencia, resultado=resultado)

    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        # Encontrar el nombre más largo
        nombres = [nombre1, nombre2, nombre3]
        nombre_mas_largo = max(nombres, key=len)
        longitud_nombre_mas_largo = len(nombre_mas_largo)

        # Pasar resultados a la plantilla
        return render_template('resultado_ejercicio2.html', nombre_mas_largo=nombre_mas_largo, longitud=longitud_nombre_mas_largo)

    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)







