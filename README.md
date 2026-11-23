# 🛡️ Web Security Recon & Audit Suite (Python CLI)
**Autor:** Sylvio Andrés Burgos (misteorecandy)  
**Licencia:** MIT License  
**Lenguaje:** Python 3  

Suite modular de herramientas de línea de comandos (CLI) desarrollada en Python para automatizar la fase de reconocimiento, enumeración web, análisis OSINT y detección activa de vulnerabilidades (OWASP Top 10) en entornos autorizados.

---

## 📦 Módulos Incluidos

### 1. Auditor de Cabeceras (`auditor_web.py`)
Analiza la respuesta HTTP del servidor en tiempo real para detectar fugas de versión del software web (*Server Banner Grabbing*) y verificar la ausencia de cabeceras defensivas críticas (`X-Frame-Options`, `X-Content-Type-Options`, `Strict-Transport-Security`, `Content-Security-Policy`).

### 2. Buscador de Rutas Ocultas (`buscadorrutas.py`)
Realiza enumeración de directorios (*Directory Fuzzing*) probando rutas sensibles comunes (`/admin`, `/login`, `/.env`, `/.git`, `/backup`, etc.) e interpretando los códigos de estado HTTP (`200 OK`, `403 Forbidden`, `301/302 Redirect`).

### 3. Extractor de Inteligencia HTML (`extractor_html.py`)
Ejecuta análisis estático sobre el código fuente crudo de la página web utilizando **Expresiones Regulares (`re`)** para extraer comentarios olvidados por los desarrolladores (`<!-- ... -->`) y detectar correos electrónicos expuestos.

### 4. Escáner de XSS Reflejado (`escaner_xss.py`)
Realiza pruebas activas inyectando sondas de código JavaScript a través de parámetros GET para verificar si el servidor sanitiza correctamente las entradas del usuario o refleja código ejecutable en el navegador.

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

Ejecutá cualquiera de los cuatro módulos desde tu terminal pasando como argumento el objetivo autorizado que deseás evaluar:

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

### 4. Detección de Cross-Site Scripting (XSS Reflejado):
```bash
python3 escaner_xss.py "http://localhost:8080/?q="
```

**Ejemplo de salida (`escaner_xss.py`):**
```text
[*] Probando inyección XSS en:
    http://localhost:8080/?q=<script>alert('AUDITORIA_XSS')</script>
------------------------------------------------------------
[!] ¡VULNERABILIDAD DETECTADA! (XSS Reflejado)
[+] El servidor reflejó el código JavaScript sin sanitizar.
------------------------------------------------------------
```

---

## 🔍 Vectores Evaluados (Cabeceras)

| Cabecera HTTP | Función Defensiva | Riesgo si está Ausente |
| :--- | :--- | :--- |
| **`Server`** | Identifica el software y versión del servidor web. | Facilita la búsqueda de exploits específicos (*Information Disclosure*). |
| **`X-Frame-Options`** | Controla si la web puede cargarse dentro de un `<iframe\>` externo. | Exposición a ataques de secuestro de clics (*Clickjacking*). |
| **`X-Content-Type-Options`** | Impide que el navegador adivine el tipo de archivo (MIME). | Ejecución de código malicioso disfrazado (*MIME-sniffing*). |
| **`Strict-Transport-Security`** | Obliga al navegador a conectarse únicamente vía HTTPS cifrado. | Vulnerabilidad ante ataques *Man-in-the-Middle* (Downgrade). |
| **`Content-Security-Policy`** | Restringe las fuentes desde donde se pueden cargar scripts. | Alto riesgo de inyección de código *Cross-Site Scripting (XSS)*. |

---

## ⚖️ Aviso Legal (Disclaimer)
Estas herramientas fueron desarrolladas exclusivamente con fines educativos, de investigación y para realizar auditorías de seguridad en sistemas propios o con autorización explícita por escrito. El autor no se hace responsable por el uso indebido de este código.
