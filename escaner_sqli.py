import requests
import sys

def detectar_sqli(url_con_parametro):
    # Payloads clásicos para provocar errores de sintaxis en la base de datos
    payloads = ("'", "\"", "' OR '1'='1", "\" OR \"1\"=\"1")
    
    # Firmas de error que delatan una base de datos expuesta
    errores_db = (
        "you have an error in your sql syntax",
        "warning: mysql",
        "unclosed quotation mark after the character string",
        "quoted string not properly terminated",
        "sqlite3.operationalerror",
        "pg_query()",
        "ora-01756"
    )

    print(f"\n[*] Buscando vulnerabilidades SQL Injection en:\n    {url_con_parametro}")
    print("-" * 65)
    vulnerable = False

    for payload in payloads:
        objetivo = url_con_parametro + payload
        try:
            respuesta = requests.get(objetivo, timeout=5)
            contenido = respuesta.text.lower()

            for error in errores_db:
                if error in contenido:
                    print("[!] ¡VULNERABILIDAD SQLi DETECTADA!")
                    print(f"    -> Payload exitoso: {payload}")
                    print(f"    -> Firma de error encontrada: '{error}'")
                    vulnerable = True
                    break
        except Exception as e:
            print(f"[-] Error de conexión: {e}")
            break
            
        if vulnerable:
            break

    if not vulnerable:
        print("[OK] No se detectaron errores SQL expuestos con los payloads básicos.")
    print("-" * 65)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 escaner_sqli.py <url_con_parametro>")
        print("Ejemplo: python3 escaner_sqli.py \"http://localhost:8081/?id=1\"")
    else:
        detectar_sqli(sys.argv.pop(1))
      
