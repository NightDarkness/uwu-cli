# uwu-cli
>Ve tus animes favoritos en español desde la terminal

 ## Dependencias

 - [mpv](https://sourceforge.net/projects/mpv-player-windows/files/64bit-v3/) reproductor de video.
 - [ffmpeg](https://ffmpeg.org/download.html) transcodificador de video.
 - [aria2](https://aria2.github.io/) utilidad de descarga de línea de comando.
 - [yt-dlp](https://github.com/yt-dlp/yt-dlp) programa de línea de comandos para descargar vídeos o extraer audio de sitios de streaming.

 **NOTA** Todas las dependencias deben ser agregadas a el `PATH` de windows para que uwu-cli trabaje sin ningun problema.

 ## Instalacion

 Requisitos
 - install [Python](https://www.python.org/downloads/).
 - Install [Scoop](https://scoop.sh/).
 - Install [Terminal Preview](https://apps.microsoft.com/detail/9n8g5rfz9xk3?hl=en-us&gl=US).

 ```sh
 pip install lxml cloudscraper bs4 keyboard soupsieve
 scoop bucket add extras
 scoop install mpv ffmpeg-shared aria2 yt-dlp git
 scoop install https://github.com/NightDarkness/uwu-cli/releases/download/first_release/uwu-cli.json
 ```

## TO-DO

- [x] Primer release al publico
- [ ] Hacer port a Linux
- [ ] Mejorar velocidad de carga
- [ ] Descarga de episodios

