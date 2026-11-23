# 🛡️ Web Security Recon Suite (Python CLI)
**Autor:** Sylvio Andrés Burgos (misteorecandy)  
**Licencia:** MIT License  
**Lenguaje:** Python 3  

Suite de herramientas de línea de comandos (CLI) desarrollada en Python para automatizar la fase de reconocimiento pasivo, enumeración y análisis OSINT en auditorías de seguridad web. Permite evaluar cabeceras HTTP, descubrir directorios sensibles ocultos y extraer inteligencia directamente del código fuente HTML de servidores autorizados.

---

## 📦 Módulos Incluidos

### 1. Auditor de Cabeceras (`auditor_web.py`)
Analiza la respuesta HTTP del servidor en tiempo real para detectar fugas de versión del software web (*Server Banner Grabbing*) y verificar la ausencia de cabeceras defensivas críticas (`X-Frame-Options`, `X-Content-Type-Options`, `Strict-Transport-Security`, `Content-Security-Policy`).

### 2. Buscador de Rutas Ocultas (`buscador_rutas.py`)
Realiza enumeración de directorios (*Directory Fuzzing*) probando rutas sensibles comunes (`/admin`, `/login`, `/.env`, `/.git`, `/backup`, etc.) e interpretando los códigos de estado HTTP (`200 OK`, `403 Forbidden`, `301/302 Redirect`).

### 3. Extractor de Inteligencia HTML (`extractor_html.py`)
Ejecuta análisis estático sobre el código fuente crudo de la página web utilizando **Expresiones Regulares (`re`)** para extraer comentarios olvidados por los desarrolladores (`<!-- ... -->`) y detectar correos electrónicos expuestos.

---

## ⚙️ Requisitos e Instalación

Asegurate de tener instalado **Python 3** en tu entorno (Linux, Termux, Windows o macOS).

1. **Cloná este repositorio en tu máquina local:**
   ```bash
   git clone https://github.com
   cd Web-Header-Auditor-Python
   ```

2. **Instalá la dependencia necesaria:**
   ```bash
   pip install requests
   ```

---

## 🚀 Modo de Uso

Ejecutá cualquiera de los tres módulos desde tu terminal pasando como argumento el dominio o la URL del objetivo autorizado que deseás auditar:

### 1. Auditoría de Cabeceras HTTP:
```bash
python3 auditor_web.py scanme.nmap.org
```

### 2. Búsqueda de Directorios Ocultos:
```bash
python3 buscadorrutas.py scanme.nmap.org
```

### 3. Extracción de Comentarios y Correos (OSINT HTML):
```bash
python3 extractor_html.py scanme.nmap.org
```

**Ejemplo de salida (`extractor_html.py`):**
```text
[*] Extrayendo inteligencia del código fuente de: http://nmap.org
------------------------------------------------------------
[+] Comentarios de desarrollador encontrados (4):
  --> Google Analytics Code
  --> END Google Analytics Code
  --> content
  --> wrapper

[+] Correos electrónicos detectados (0):
  [-] Ningún correo expuesto en el HTML.
------------------------------------------------------------
```

---

## 🔍 Vectores Evaluados (Cabeceras)

| Cabecera HTTP | Función Defensiva | Riesgo si está Ausente |
| :--- | :--- | :--- |
| **`Server`** | Identifies software and version of the web server. | Facilita la búsqueda de exploits específicos (*Information Disclosure*). |
| **`X-Frame-Options`** | Controla si la web puede cargarse dentro de un `<iframe\>` externo. | Exposición a ataques de secuestro de clics (*Clickjacking*). |
| **`X-Content-Type-Options`** | Impide que el navegador adivine el tipo de archivo (MIME). | Ejecución de código malicioso disfrazado (*MIME-sniffing*). |
| **`Strict-Transport-Security`** | Obliga al navegador a conectarse únicamente vía HTTPS cifrado. | Vulnerabilidad ante ataques *Man-in-the-Middle* (Downgrade). |
| **`Content-Security-Policy`** | Restringe las fuentes desde donde se pueden cargar scripts. | Alto riesgo de inyección de código *Cross-Site Scripting (XSS)*. |

---

## ⚖️ Aviso Legal (Disclaimer)
Estas herramientas fueron desarrolladas exclusivamente con fines educativos, de investigación y para realizar auditorías de seguridad en sistemas propios o con autorización explícita por escrito. El autor no se hace responsable por el uso indebido de este código.
