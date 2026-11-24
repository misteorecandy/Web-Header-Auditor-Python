# 🛡️ Web Security Recon & Audit Suite (Python CLI)
**Autor:** Sylvio Andrés Burgos (misteorecandy)  
**Licencia:** MIT License  
**Lenguaje:** Python 3  

Suite modular de herramientas de línea de comandos (CLI) y laboratorios prácticos desarrollada en Python para automatizar la fase de reconocimiento, enumeración web, análisis OSINT y detección/mitigación de vulnerabilidades críticas (OWASP Top 10) en entornos autorizados.

---

## 📦 Módulos Incluidos

### 🔍 Fase 1: Reconocimiento y Enumeración
1. **Auditor de Cabeceras (`auditor_web.py`):** Analiza respuestas HTTP en tiempo real para detectar fugas de versión del servidor (*Banner Grabbing*) y verificar la ausencia de cabeceras defensivas críticas (`X-Frame-Options`, `X-Content-Type-Options`, `Strict-Transport-Security`, `Content-Security-Policy`).
2. **Buscador de Rutas Ocultas (`buscadorrutas.py`):** Ejecuta enumeración de directorios (*Directory Fuzzing*) probando rutas sensibles comunes (`/admin`, `/login`, `/.env`, `/.git`, `/backup`, etc.) e interpretando códigos de estado HTTP (`200`, `403`, `301/302`).
3. **Extractor de Inteligencia HTML (`extractor_html.py`):** Realiza análisis estático sobre el código fuente crudo utilizando **Expresiones Regulares (`re`)** para extraer comentarios olvidados de desarrolladores (`<!-- ... -->`) y detectar correos electrónicos expuestos.

### 🎯 Fase 2: Detección Activa y Programación Segura (OWASP Top 10)
4. **Escáner de XSS Reflejado (`escaner_xss.py`):** Realiza pruebas activas inyectando sondas de código JavaScript a través de parámetros GET para verificar si el servidor sanitiza las entradas del usuario o refleja código ejecutable en el navegador.
5. **Detector de Inyección SQL (`escaner_sqli.py`):** Automatiza la detección de fallas *Error-Based SQLi* inyectando caracteres de ruptura de sintaxis (`'`, `"`, `' OR '1'='1`) y rastreando firmas de error expuestas de motores como MySQL, PostgreSQL, Oracle y SQLite.
6. **Laboratorio SQLi: Ataque y Defensa (`lab_sqli.py`):** Entorno autocontenido en memoria utilizando `sqlite3` que demuestra en vivo cómo una consulta concatenada permite evadir un inicio de sesión (*Authentication Bypass*) y cómo los **Prepared Statements (`?`)** neutralizan el ataque por completo.

---

## ⚙️ Requisitos e Instalación

Asegurate de tener instalado **Python 3** en tu entorno (Linux, Termux, Windows o macOS).

1. **Cloná este repositorio en tu máquina local:**
   ```bash
   git clone https://github.com
   cd Web-Header-Auditor-Python
   ```

2. **Instalá la dependencia externa necesaria (`requests`):**
   ```bash
   pip install requests
   ```
   *(Nota: Los módulos `re`, `sys` y `sqlite3` forman parte de la librería estándar de Python).*

---

## 🚀 Modo de Uso

Ejecutá cualquiera de los módulos desde tu terminal pasando como argumento el objetivo autorizado que deseás auditar:

```bash
# 1. Auditar cabeceras HTTP:
python3 auditor_web.py scanme.nmap.org

# 2. Buscar directorios ocultos:
python3 buscadorrutas.py scanme.nmap.org

# 3. Extraer comentarios y correos del HTML:
python3 extractor_html.py scanme.nmap.org

# 4. Detectar Cross-Site Scripting (XSS Reflejado):
python3 escaner_xss.py "http://localhost:8080/?q="

# 5. Detectar Inyección SQL (Error-Based SQLi):
python3 escaner_sqli.py "http://localhost:8081/?id=1"

# 6. Ejecutar el laboratorio interactivo de Ataque vs. Defensa SQLi:
python3 lab_sqli.py
```

---

## 🔍 Vectores Evaluados (Cabeceras HTTP)

| Cabecera HTTP | Función Defensiva | Riesgo si está Ausente |
| :--- | :--- | :--- |
| **`Server`** | Identifica el software y versión del servidor web. | Facilita la búsqueda de exploits específicos (*Information Disclosure*). |
| **`X-Frame-Options`** | Controla si la web puede cargarse dentro de un `<iframe\>` externo. | Exposición a ataques de secuestro de clics (*Clickjacking*). |
| **`X-Content-Type-Options`** | Impide que el navegador adivine el tipo de archivo (MIME). | Ejecución de código malicioso disfrazado (*MIME-sniffing*). |
| **`Strict-Transport-Security`** | Obliga al navegador a conectarse únicamente vía HTTPS cifrado. | Vulnerabilidad ante ataques *Man-in-the-Middle* (Downgrade). |
| **`Content-Security-Policy`** | Restringe las fuentes desde donde se pueden cargar scripts. | Alto riesgo de inyección de código *Cross-Site Scripting (XSS)*. |

---

## ⚖️ Aviso Legal (Disclaimer)
Estas herramientas y laboratorios fueron desarrollados exclusivamente con fines educativos, de investigación académica y para realizar auditorías de seguridad en sistemas propios o con autorización explícita por escrito. El autor no se hace responsable por el uso indebido de este código.
