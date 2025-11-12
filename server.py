#Diogo Alejandro Vela Macías
#Sexto Semestre
#Arquitectura y servicios distribuidos

from flask import Flask, jsonify, request
import time

app = Flask(__name__)

# 1. ESTRUCTURA DE DATOS:
# Los usuarios se almacenan en un diccionario de Python (users_db).
# Esto simula una base de datos en memoria donde cada 'key' es el ID del usuario.
users_db = {
    1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
    2: {"id": 2, "name": "Bob", "email": "bob@example.com"},
    3: {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
}

# 2. ENDPOINTS DISPONIBLES:
# Ruta '/api/users/<id>' (GET) para obtener un usuario específico.
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    print(f"Servidor: Recibida petición para usuario {user_id}")
    
    # 3. COMPORTAMIENTO SÍNCRONO:
    # Aquí se simula el delay (procesamiento, consulta a BD).
    # El servidor se bloquea aquí por 2 segundos, haciendo que el cliente espere.
    time.sleep(2)
    
    user = users_db.get(user_id)
    
    # 4. RESPUESTAS:
    # Si se encuentra, devuelve un JSON con 'status: success' y los datos.
    if user:
        print(f"Servidor: Enviando respuesta para usuario {user_id}")
        return jsonify({"status": "success", "data": user})
    else:
        # Si no, devuelve un JSON 'status: error' y un código HTTP 404.
        print(f"Servidor: Usuario {user_id} no encontrado")
        return jsonify({"status": "error", "message": "User not found"}), 404

# 2. ENDPOINTS DISPONIBLES:
# Ruta '/api/users' (POST) para crear un nuevo usuario.
@app.route('/api/users', methods=['POST'])
def create_user():
    print("Servidor: Recibida petición para crear usuario")
    data = request.get_json()
    
    # 4. RESPUESTAS: Error 400 (Bad Request) si faltan datos en el JSON.
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"status": "error", "message": "Missing required fields"}), 400
    
    # 3. COMPORTAMIENTO SÍNCRONO:
    # Simula 1 segundo de bloqueo para la creación.
    time.sleep(1)
    
    new_id = max(users_db.keys()) + 1
    new_user = {
        "id": new_id,
        "name": data['name'],
        "email": data['email']
    }
    users_db[new_id] = new_user
    
    print(f"Servidor: Usuario {new_id} creado exitosamente")
    
    # 4. RESPUESTAS: Éxito 201 (Created) con los datos del nuevo usuario.
    return jsonify({"status": "success", "data": new_user}), 201

if __name__ == '__main__':
    print("Iniciando servidor síncrono en http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)