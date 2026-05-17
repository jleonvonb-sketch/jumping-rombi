                                        INSTRUCCIONES DE INSTALACION
🎮 Guía de Instalación - Jumping Rombi
Para poder jugar, necesitas tener Python instalado en tu computadora y luego ejecutar nuestro script automatizado, que se encargará de configurar todo (incluyendo la librería Pygame y el juego) por ti.

Sigue las instrucciones según tu sistema operativo:

1. Instalar Python
🪟 Windows
Descarga el instalador oficial de Python desde: python.org/downloads.

Abre el archivo descargado.

CRÍTICO: Antes de hacer clic en "Install Now", asegúrate de marcar la casilla que dice "Add python.exe to PATH" en la parte inferior de la ventana. Si no lo haces, los comandos no funcionarán.

Haz clic en Install Now y espera a que termine.

🐧 Linux (Ubuntu / Debian / derivados)
Abre una terminal (Ctrl + Alt + T) y ejecuta los siguientes comandos para actualizar el sistema e instalar Python junto con su gestor de paquetes:

Bash
sudo apt update
sudo apt install python3 python3-pip curl -y
🍏 macOS
Abre la terminal (búscala en el Spotlight con Cmd + Espacio).

Lo más rápido es usar el instalador oficial de python.org/downloads. Descarga el instalador para macOS y ejecútalo siguiendo los pasos en pantalla.

Alternativa si usas Homebrew: Si ya tienes Homebrew instalado, simplemente corre:

Bash
brew install python
2. Descargar y Ejecutar el Instalador del Juego
Una vez que tengas Python instalado, abre la Terminal (en Linux/macOS) o el Símbolo del Sistema / PowerShell (en Windows) y ejecuta los siguientes comandos según tu caso:

En Windows (PowerShell)
Windows no siempre trae curl configurado de la misma forma para guardar archivos, por lo que puedes usar este comando nativo en PowerShell para descargarlo directamente en tu carpeta de Descargas y ejecutarlo:

PowerShell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/jleonvonb-sketch/jumping-rombi/refs/heads/main/install.py" -OutFile "$HOME\Downloads\install.py"; python "$HOME\Downloads\install.py"
En Linux y macOS (Terminal)
Usa curl para descargar el script en tu carpeta de descargas e iniciarlo de inmediato con Python:

Bash
curl -L "https://raw.githubusercontent.com/jleonvonb-sketch/jumping-rombi/refs/heads/main/install.py" -o ~/Downloads/install.py && python3 ~/Downloads/install.py
¿Qué hace este script de instalación?
Detecta automáticamente tu sistema operativo.

Comprueba si tienes instalado pygame (si no lo tienes, lo instala por ti).

Descarga de forma segura el código más reciente de Jumping Rombi en tu carpeta de Descargas.

¡Inicia el juego automáticamente para que empieces a jugar de inmediato!
