# 🛡️ Web Header Security Auditor (Python CLI)
**Autor:** Sylvio Andrés Burgos (misteorecandy)  
**Licencia:** MIT License  
**Lenguaje:** Python 3  

Herramienta ligera de línea de comandos (CLI) desarrollada en Python para realizar auditorías rápidas de seguridad HTTP. Analiza la respuesta de servidores web en tiempo real para detectar fugas de información tecnológica (*Server Banner Grabbing*) y verificar la ausencia de cabeceras defensivas críticas contra ataques de Clickjacking, XSS y MIME-sniffing.

---

## ⚙️ Requisitos e Instalación

Asegurate de tener instalado **Python 3** en tu entorno (Linux, Termux, Windows o macOS).

1. Cloná este repositorio en tu máquina local:
   ```bash
   git clone https://github.com
   cd Web-Header-Auditor-Python
   ```

2. Instalá la librería `requests`:
   ```bash
   pip install requests
   ```

---

## 🚀 Modo de Uso

Ejecutá el script desde tu terminal pasando como argumento el dominio o la URL del objetivo autorizado que deseás auditar:

```bash
python3 auditor_web.py scanme.nmap.org
```

### Ejemplo de Salida en Terminal:
```text
[*] Analizando objetivo: http://nmap.org
---------------------------------------------
[+] Tecnología del Servidor: Apache/2.4.7 (Ubuntu)

[*] Auditoría de Cabeceras de Seguridad:
  [!] ALERTA: Falta X-Frame-Options
  [!] ALERTA: Falta X-Content-Type-Options
  [!] ALERTA: Falta Strict-Transport-Security
  [!] ALERTA: Falta Content-Security-Policy
```

---

## 🔍 Vectores Evaluados

| Cabecera HTTP | Función Defensiva | Riesgo si está Ausente |
| :--- | :--- | :--- |
| **`Server`** | Identifica el software y versión del servidor. | Facilita la búsqueda de exploits específicos (*Information Disclosure*). |
| **`X-Frame-Options`** | Controla si la web puede cargarse dentro de un `<iframe\>` externo. | Exposición a ataques de secuestro de clics (*Clickjacking*). |
| **`X-Content-Type-Options`** | Impide que el navegador adivine el tipo de archivo (MIME). | Ejecución de código malicioso disfrazado (*MIME-sniffing*). |
| **`Strict-Transport-Security`** | Obliga al navegador a conectarse únicamente vía HTTPS cifrado. | Vulnerabilidad ante ataques *Man-in-the-Middle* (Downgrade). |
| **`Content-Security-Policy`** | Restringe las fuentes desde donde se pueden cargar scripts. | Alto riesgo de inyección de código *Cross-Site Scripting (XSS)*. |

---

## ⚖️ Aviso Legal (Disclaimer)
Esta herramienta fue diseñada exclusivamente con fines educativos, de investigación y para realizar auditorías de seguridad en sistemas propios o con autorización explícita por escrito. El autor no se hace responsable por el uso indebido de este código.
