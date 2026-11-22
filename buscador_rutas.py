import requests
import sys

def buscar_directorios(url_base):
    if not url_base.startswith("http"):
        url_base = "http://" + url_base
    if not url_base.endswith("/"):
        url_base += "/"

    rutas_comunes = (
        "admin", "login", "dashboard", "config", "backup", 
        "test", "dev", "robots.txt", ".env", ".git", 
        "phpinfo.php", "uploads", "images", "api", "shared"
    )

    print(f"\n[*] Iniciando búsqueda de rutas ocultas en: {url_base}")
    print("-" * 55)

    for ruta in rutas_comunes:
        objetivo = url_base + ruta
        try:
            respuesta = requests.get(objetivo, timeout=3, allow_redirects=False)
            codigo = respuesta.status_code

            if codigo == 200:
                print(f"  [200 OK] ¡ENCONTRADO! -> {objetivo}")
            elif codigo == 403:
                print(f"  [403 PROHIBIDO] Existe pero bloqueado -> {objetivo}")
            elif codigo in (301, 302):
                print(f"  [{codigo} REDIRECCIÓN] -> {objetivo}")
                
        except requests.RequestException:
            pass

    print("-" * 55)
    print("[*] Escaneo finalizado.\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 buscador_rutas.py <url>")
    else:
        buscar_directorios(sys.argv.pop(1))
