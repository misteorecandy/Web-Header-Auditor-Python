import sqlite3

def iniciar_base_datos():
    conexion = sqlite3.connect(":memory:")
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE usuarios (id INTEGER, usuario TEXT, clave TEXT, rol TEXT)")
    cursor.execute("INSERT INTO usuarios VALUES (1, 'admin', 'ClaveSuperSecreta999!', 'Administrador')")
    cursor.execute("INSERT INTO usuarios VALUES (2, 'sylvio', '12345', 'Analista')")
    conexion.commit()
    return conexion

# 1. MÉTODO VULNERABLE (Concatenación directa de texto)
def login_vulnerable(conexion, usuario_input, clave_input):
    cursor = conexion.cursor()
    # ¡ERROR FATAL! Se pega el texto del usuario directo en la consulta SQL
    consulta = f"SELECT * FROM usuarios WHERE usuario = '{usuario_input}' AND clave = '{clave_input}'"
    print(f"\n[SQL Ejecutado]: {consulta}")
    
    cursor.execute(consulta)
    resultado = cursor.fetchone()
    
    if resultado:
        print(f"[!] ¡ACCESO CONCEDIDO! Bienvenido {resultado[1]} (Rol: {resultado[3]})")
    else:
        print("[-] Acceso denegado.")

# 2. MÉTODO SEGURO (Consultas Parametrizadas / Prepared Statements)
def login_seguro(conexion, usuario_input, clave_input):
    cursor = conexion.cursor()
    # ¡DEFENSA REAL! Los signos '?' tratan la entrada estrictamente como texto, nunca como comandos SQL
    consulta = "SELECT * FROM usuarios WHERE usuario = ? AND clave = ?"
    cursor.execute(consulta, (usuario_input, clave_input))
    resultado = cursor.fetchone()
    
    if resultado:
        print(f"[OK] Acceso legítimo concedido a {resultado[1]}")
    else:
        print("[OK] ¡ATAQUE BLOQUEADO! El sistema rechazó la inyección SQL.")

if __name__ == "__main__":
    db = iniciar_base_datos()
    
    print("=== PRUEBA 1: Atacando el Login Vulnerable sin saber la clave ===")
    payload_usuario = "admin' OR '1'='1"
    clave_falsa = "cualquier_cosa"
    login_vulnerable(db, payload_usuario, clave_falsa)
    
    print("\n=== PRUEBA 2: Lanzando el mismo ataque contra el Login Seguro ===")
    login_seguro(db, payload_usuario, clave_falsa)
  
