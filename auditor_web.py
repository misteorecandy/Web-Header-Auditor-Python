import requests
import sys

def auditar_cabeceras(url):
    if not url.startswith("http"):
        url = "http://" + url
        
    print(f"\n[*] Analizando objetivo: {url}\n" + "-"*45)
    try:
        respuesta = requests.get(url, timeout=5)
        cabeceras = respuesta.headers
        
        servidor = cabeceras.get('Server', 'Oculto (Protegido)')
        print(f"[+] Tecnología del Servidor: {servidor}")
        
        protecciones = [
            'X-Frame-Options',
            'X-Content-Type-Options',
            'Strict-Transport-Security',
            'Content-Security-Policy'
        ]
        
        print("\n[*] Auditoría de Cabeceras de Seguridad:")
        for header in protecciones:
            if header in cabeceras:
                print(f"  [OK] {header}: Configurada")
            else:
                print(f"  [!] ALERTA: Falta {header}")
                
    except Exception as e:
        print(f"[-] Error de conexión: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso correcto: python3 auditor_web.py <url>")
        print("Ejemplo: python3 auditor_web.py scanme.nmap.org")
    else:
        auditar_cabeceras(sys.argv[1])
      
