# uwu-cli
>Ve tus animes favoritos en español desde la terminal

 ## Dependencias

 - [Python](https://www.python.org/downloads/) interprete del lenguaje Python.
 - [mpv](https://sourceforge.net/projects/mpv-player-windows/files/64bit-v3/) reproductor de video.
 - [ffmpeg](https://ffmpeg.org/download.html) transcodificador de video.
 - [aria2](https://aria2.github.io/) utilidad de descarga de línea de comando.
 - [yt-dlp](https://github.com/yt-dlp/yt-dlp) programa de línea de comandos para descargar vídeos o extraer audio de sitios de streaming.

 **NOTA** Todas las dependencias deben ser agregadas a el `PATH` de windows para que uwu-cli trabaje sin ningun problema.

 ## Instalacion

 <details><summary>Windows</summary>

 Requisitos
 - Install <a href="https://scoop.sh/" target='_blank'>Scoop</a>.
 - Install <a href="https://apps.microsoft.com/detail/9n8g5rfz9xk3?hl=en-us&gl=US" target='_blank'>Terminal Preview</a>.

 ```sh
 scoop bucket add extras
 scoop install git python mpv ffmpeg-shared aria2 yt-dlp https://github.com/NightDarkness/uwu-cli/releases/download/0.2/uwu-cli.json
 python3 -m pip install lxml cloudscraper bs4 keyboard soupsieve
 ```

 ## Actualizacion

 ```sh
 scoop uninstall uwu-cli
 scoop install https://github.com/NightDarkness/uwu-cli/releases/download/0.2/uwu-cli.json
 ```

 ## Uso
 
  **En una terminal nueva**
 
 - uwu-cli [Nombre-del-anime]    Ejemplo : uwu-cli Jujutsu-kaisen
 - uwu-cli [comando]             Ejemplo : uwu-cli -h

</details>
<details><summary>Linux</summary>

   **COMING SOON**

 </details>
</details>

## TO-DO

- [x] Primer release al publico
- [X] Mejorar velocidad de carga
- [x] Mostrar informacion del anime
- [ ] Port a Linux
- [ ] Descarga de episodios
- [ ] Port a Android (Termux)
- [ ] Mejoras de diseño

