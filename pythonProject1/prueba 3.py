<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prueba Flask</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <div class="container">
        <h1>Bienvenido a la Página Principal</h1>
        <div class="ejercicio-container">
            <h2>Ejercicio 1</h2>
            <form action="{{ url_for('ejercicio1') }}" method="post">
                <!-- Formulario del Ejercicio 1 -->
                <label for="nota1">Nota 1:</label>
                <input type="number" name="nota1" required>
                <label for="nota2">Nota 2:</label>
                <input type="number" name="nota2" required>
                <label for="nota3">Nota 3:</label>
                <input type="number" name="nota3" required>
                <label for="asistencia">Asistencia:</label>
                <input type="number" name="asistencia" required>
                <button type="submit">Enviar</button>
            </form>
            {% if ejercicio1_resultados %}
                <p>Promedio: {{ ejercicio1_resultados.promedio }}</p>
                <p>Estado: {{ ejercicio1_resultados.estado }}</p>
            {% endif %}
        </div>
        <div class="ejercicio-container">
            <h2>Ejercicio 2</h2>
            <form action="{{ url_for('ejercicio2') }}" method="post">
                <!-- Formulario del Ejercicio 2 -->
                <label for="nombre1">Nombre 1:</label>
                <input type="text" name="nombre1" required>
                <label for="nombre2">Nombre 2:</label>
                <input type="text" name="nombre2" required>
                <label for="nombre3">Nombre 3:</label>
                <input type="text" name="nombre3" required>
                <button type="submit">Enviar</button>
            </form>
            {% if ejercicio2_resultados %}
                <p>Nombre más largo: {{ ejercicio2_resultados.nombre_mas_largo }}</p>
                <p>Cantidad de caracteres: {{ ejercicio2_resultados.cantidad_caracteres }}</p>
            {% endif %}
        </div>
    </div>
</body>
</html>
