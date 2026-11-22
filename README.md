# 🛡️ Web Security Recon Suite (Python CLI)
**Autor:** Sylvio Andrés Burgos (misteorecandy)  
**Licencia:** MIT License  
**Lenguaje:** Python 3  

Suite ligera de herramientas de línea de comandos (CLI) desarrollada en Python para automatizar la fase de reconocimiento y enumeración web en auditorías de seguridad. Permite detectar fugas de información tecnológica (*Server Banner Grabbing*), evaluar cabeceras defensivas HTTP y descubrir directorios o archivos ocultos en servidores autorizados.

---

## 📦 Módulos Incluidos

### 1. Auditor de Cabeceras (`auditor_web.py`)
Analiza la respuesta del servidor en tiempo real para detectar fugas de versión del software web y verificar la ausencia de cabeceras críticas (`X-Frame-Options`, `X-Content-Type-Options`, `Strict-Transport-Security`, `Content-Security-Policy`).

### 2. Buscador de Rutas Ocultas (`buscador_rutas.py`)
Realiza enumeración de directorios (*Directory Fuzzing*) probando rutas sensibles comunes (`/admin`, `/login`, `/.env`, `/.git`, `/backup`, etc.) e interpretando los códigos de estado HTTP (`200 OK`, `403 Forbidden`, `301/302 Redirect`).

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

Ejecutá cualquiera de los dos módulos desde tu terminal pasando como argumento el dominio o la URL del objetivo autorizado que deseás auditar:

### Auditoría de Cabeceras HTTP:
```bash
python3 auditor_web.py scanme.nmap.org
```

**Ejemplo de salida:**
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

### Búsqueda de Directorios Ocultos:
```bash
python3 buscadorrutas.py scanme.nmap.org
```

**Ejemplo de salida:**
```text
[*] Iniciando búsqueda de rutas ocultas en: http://nmap.org/
-------------------------------------------------------
  [301 REDIRECCIÓN] -> http://nmap.org/images
  [301 REDIRECCIÓN] -> http://nmap.org/shared
-------------------------------------------------------
[*] Escaneo finalizado.
```

---

## 🔍 Vectores Evaluados (Cabeceras)

| Cabecera HTTP | Función Defensiva | Riesgo si está Ausente |
| :--- | :--- | :--- |
| **`Server`** | Identifica el software y versión del servidor. | Facilita la búsqueda de exploits específicos (*Information Disclosure*). |
| **`X-Frame-Options`** | Controla si la web puede cargarse dentro de un `<iframe\>` externo. | Exposición a ataques de secuestro de clics (*Clickjacking*). |
| **`X-Content-Type-Options`** | Impide que el navegador adivine el tipo de archivo (MIME). | Ejecución de código malicioso disfrazado (*MIME-sniffing*). |
| **`Strict-Transport-Security`** | Obliga al navegador a conectarse únicamente vía HTTPS cifrado. | Vulnerabilidad ante ataques *Man-in-the-Middle* (Downgrade). |
| **`Content-Security-Policy`** | Restringe las fuentes desde donde se pueden cargar scripts. | Alto riesgo de inyección de código *Cross-Site Scripting (XSS)*. |

---

## ⚖️ Aviso Legal (Disclaimer)
Estas herramientas fueron desarrolladas exclusivamente con fines educativos, de investigación y para realizar auditorías de seguridad en sistemas propios o con autorización explícita por escrito. El autor no se hace responsable por el uso indebido de este código.
