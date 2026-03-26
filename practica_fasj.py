from flask import Flask, jsonify
import pyodbc
import pdb

app = Flask(__name__)

def get_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER= 10.79.3.125;" # IP SQL Server
        "DATABASE=AppDistribuidasDB;"
        "UID=sa;"
        "PWD=sa;"
        "TrustServerCertificate=yes;"
        )

@app.route('/api/productos', methods=['GET'])
def get_productos():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("select Id, Nombre, Precio from productos")
        rows = cursor.fetchall()

        productos = []
        for row in rows:
            productos.append({
                "id": row.Id,
                "nombre": row.Nombre,
                "precio": row.Precio
            })
        
        cursor.close()
        conn.close()

        return jsonify(productos)
        
    except Exception as e:
        return jsonify(
            {
                "error": "error al obtener informacion",
                "msg" : str(e)
            }
            ), 500
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)