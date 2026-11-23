import requests
import re
import sys

def analizar_codigo_fuente(url):
    if not url.startswith("http"):
        url = "http://" + url

    print(f"\n[*] Extrayendo inteligencia del código fuente de: {url}")
    print("-" * 60)

    try:
        respuesta = requests.get(url, timeout=5)
        html = respuesta.text

        # 1. Buscar comentarios ocultos <!-- comentario -->
        comentarios = re.findall(r'<!--(.*?)-->', html, re.DOTALL)
        print(f"[+] Comentarios de desarrollador encontrados ({len(comentarios)}):")
        for c in comentarios:
            limpio = c.strip()
            if limpio:
                print(f"  --> {limpio}")

        # 2. Buscar correos electrónicos filtrados
        correos = set(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', html))
        print(f"\n[+] Correos electrónicos detectados ({len(correos)}):")
        if correos:
            for email in correos:
                print(f"  @ {email}")
        else:
            print("  [-] Ningún correo expuesto en el HTML.")

    except Exception as e:
        print(f"[-] Error al analizar: {e}")

    print("-" * 60)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 extractor_html.py <url>")
    else:
        analizar_codigo_fuente(sys.argv.pop(1))
      
