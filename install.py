import os
import sys
import subprocess
import urllib.request


def obtener_ruta_descargas():
    """Detecta el OS y devuelve la ruta de la carpeta de Descargas."""
    home = os.path.expanduser("~")

    if sys.platform.startswith("win"):
        # Intenta obtener la ruta oficial de Descargas en Windows desde el registro
        import winreg

        try:
            sub_key = r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
                # GUID estándar para la carpeta de Downloads
                downloads, _ = winreg.QueryValueEx(
                    key, "{374DE290-123F-4565-9164-39C4925E467B}"
                )
                return downloads
        except Exception:
            # Si falla, usa la ruta por defecto basada en %USERPROFILE%
            return os.path.join(home, "Downloads")
    else:
        # Para Linux / macOS, verifica las carpetas típicas
        opciones = [
            os.path.join(home, "Downloads"),
            os.path.join(home, "Descargas"),
        ]
        for ruta in opciones:
            if os.path.exists(ruta):
                return ruta
        return home  # Fallback a la carpeta de usuario si no existen


def asegurar_pygame():
    """Verifica si pygame está instalado; si no, lo instala automáticamente."""
    try:
        import pygame

        print("[+] Pygame ya está instalado.")
    except ImportError:
        print("[*] Pygame no detectado. Instalando...")
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", "pygame"]
            )
            print("[+] Pygame instalado correctamente.")
        except Exception as e:
            print(f"[-] Error al instalar Pygame: {e}")
            sys.exit(1)


def descargar_y_ejecutar():
    # URL del RAW corregida
    url_raw = "https://raw.githubusercontent.com/jleonvonb-sketch/jumping-rombi/refs/heads/main/main.py"

    ruta_descargas = obtener_ruta_descargas()
    archivo_destino = os.path.join(ruta_descargas, "main.py")

    print(f"[*] Descargando main.py en: {archivo_destino}")

    try:
        # Descarga el archivo simulando el curl
        urllib.request.urlretrieve(url_raw, archivo_destino)
        print("[+] Descarga completada con éxito.")
    except Exception as e:
        print(f"[-] Error al descargar el archivo: {e}")
        sys.exit(1)

    print("[*] Iniciando Jumping Rombi...")
    try:
        # Ejecuta el juego usando el mismo entorno de Python activo
        subprocess.run([sys.executable, archivo_destino])
    except Exception as e:
        print(f"[-] Error al ejecutar el script: {e}")


if __name__ == "__main__":
    asegurar_pygame()
    descargar_y_ejecutar()