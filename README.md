<h1>uwu-cli</h1>
Ve tus animes favoritos en español desde la terminal

 <h2>Dependencias</h2>

 - [Python](https://www.python.org/downloads/) interprete del lenguaje Python.
 - [mpv](https://sourceforge.net/projects/mpv-player-windows/files/64bit-v3/) reproductor de video.
 - [ffmpeg](https://ffmpeg.org/download.html) transcodificador de video.
 - [aria2](https://aria2.github.io/) utilidad de descarga de línea de comando.
 - [yt-dlp](https://github.com/yt-dlp/yt-dlp) programa de línea de comandos para descargar vídeos o extraer audio de sitios de streaming.

 **NOTA** Todas las dependencias deben ser agregadas a el `PATH` de windows para que uwu-cli trabaje sin ningun problema.

 <h2>Instalacion</h2>

 <details><summary><h3>Windows</h3></summary>
 
 <br>

 **Requisitos**
 - Install <a href="https://scoop.sh/" target='_blank'>Scoop</a>.
 - Install <a href="https://apps.microsoft.com/detail/9n8g5rfz9xk3?hl=en-us&gl=US" target='_blank'>Terminal Preview</a>.

 ```sh
 scoop install git && scoop bucket add extras
 scoop install git python mpv ffmpeg-shared aria2 yt-dlp https://github.com/NightDarkness/uwu-cli/releases/download/0.2/uwu-cli.json
 python3 -m pip install lxml cloudscraper bs4 keyboard soupsieve
 ```

 <h2>Actualizacion</h2>

 ```sh
 scoop uninstall uwu-cli
 scoop install https://github.com/NightDarkness/uwu-cli/releases/download/0.2/uwu-cli.json
 ```

 ## Uso
 
  **En una terminal nueva**
 
 - uwu-cli [Nombre-del-anime]    Ejemplo : uwu-cli Jujutsu-kaisen
 - uwu-cli [comando]             Ejemplo : uwu-cli -h

</details>
<details><summary><h3>Linux</h3></summary>

   <br>

   **Requisitos**

   <details><summary>Debian</summary>

   ```sh
   sudo apt-get update && apt-get upgrade
   sudo apt install mpv python3-pip git
   python3 -m pip install lxml cloudscraper bs4 keyboard soupsieve
   ```
   </details>

   <details><summary>Kali</summary>

   ```sh
   sudo apt update && sudo dist-upgrade -y
   sudo apt install mpv python3-pip git
   python3 -m pip install lxml cloudscraper bs4 keyboard soupsieve
   ```
   </details>

   <br>

   **Descarga**

   ```sh
   git clone https://github.com/NightDarkness/uwu-cli.git && cd uwu-cli
   sudo chmod +x uwu-cli.sh
   ```

   ## Uso
   
   - ./uwu-cli.sh [Nombre-del-anime]    Ejemplo : ./uwu-cli.sh Jujutsu-kaisen
   - ./uwu-cli.sh [comando]             Ejemplo : ./uwu-cli.sh -h

   **NOTA** Puedes agregar el script a PATH para evitar escribir "./" y poder usar el script en cualquier lugar.

 </details>
</details>

## TO-DO

- [X] Primer release al publico
- [X] Mejorar velocidad de carga
- [X] Mostrar informacion del anime
- [X] Port a Linux
- [ ] Port a MacOS
- [ ] Port a Android (Termux)
- [X] Agregar animes a favoritos
- [X] Descarga de episodios
- [ ] Mejoras de diseño

