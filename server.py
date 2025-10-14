#Diogo Alejandro Vela Macías
#Sexto Semestre
#Arquitectura y servicios distribuidos

from flask import Flask, jsonify, request
import time

app = Flask(__name__)

# Simulamos una base de datos en memoria con algunos usuarios
users_db = {
    1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
    2: {"id": 2, "name": "Bob", "email": "bob@example.com"},
    3: {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
}

# Ruta para obtener la información de un usuario específico mediante su ID
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    print(f"🔵 Servidor: Recibida petición para usuario {user_id}")
    
    # Simulamos una operación que tarda 2 segundos (por ejemplo, consulta a base de datos)
    time.sleep(2)
    
    # Buscamos el usuario en nuestra "base de datos"
    user = users_db.get(user_id)
    
    if user:
        # Si encontramos el usuario, enviamos los datos con un estado de éxito
        print(f"🟢 Servidor: Enviando respuesta para usuario {user_id}")
        return jsonify({"status": "success", "data": user})
    else:
        # Si no existe el usuario, devolvemos un error 404 con mensaje
        print(f"🔴 Servidor: Usuario {user_id} no encontrado")
        return jsonify({"status": "error", "message": "User not found"}), 404

# Ruta para crear un nuevo usuario enviando datos en formato JSON
@app.route('/api/users', methods=['POST'])
def create_user():
    print("🔵 Servidor: Recibida petición para crear usuario")
    
    # Obtenemos los datos JSON que envió el cliente en la petición POST
    data = request.get_json()
    
    # Validamos que los datos obligatorios estén presentes (nombre y email)
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"status": "error", "message": "Missing required fields"}), 400
    
    # Simulamos que el procesamiento tarda 1 segundo 
    time.sleep(1)
    
    # Generamos un nuevo ID para el usuario sumando 1 al máximo ID actual
    new_id = max(users_db.keys()) + 1
    
    # Creamos un nuevo diccionario con la información del usuario
    new_user = {
        "id": new_id,
        "name": data['name'],
        "email": data['email']
    }
    
    # Guardamos el nuevo usuario en nuestra "base de datos"
    users_db[new_id] = new_user
    
    print(f"🟢 Servidor: Usuario {new_id} creado exitosamente")
    
    # Respondemos con un estado 201 (creado) y los datos del nuevo usuario
    return jsonify({"status": "success", "data": new_user}), 201

# Ejecuta el servidor Flask cuando se corre el archivo directamente
if __name__ == '__main__':
    print("🚀 Iniciando servidor síncrono en http://localhost:5000")
    # El servidor se ejecuta en modo debug, accesible desde cualquier IP en el puerto 5000
    app.run(debug=True, host='0.0.0.0', port=5000)


