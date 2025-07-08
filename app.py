from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json()
    total_cabezas = int(data['total_cabezas'])
    objetivo_libras = float(data['objetivo_libras'])
    rangos = data['rangos']

    total_libras = 0
    total_cabezas_ingresadas = 0

    for rango in rangos:
        cabezas = int(rango['cabezas'])
        promedio = float(rango['promedio'])
        total_libras += cabezas * promedio
        total_cabezas_ingresadas += cabezas

    faltan_libras = objetivo_libras - total_libras
    faltan_cabezas = total_cabezas - total_cabezas_ingresadas

    return jsonify({
        'total_libras': total_libras,
        'faltan_libras': faltan_libras,
        'faltan_cabezas': faltan_cabezas
    })

if __name__ == '__main__':
    app.run(debug=True)
