import sys, os, time, platform
from modules import AnimeFLV
import keyboard


class UwuCli():

    def __init__(self):

        if len(sys.argv) > 1:
            self.params = sys.argv[1]
            self.search = self.params.replace('-', ' ')
        else:
            self.params = None
            self.search = 'dungeon meshi'
            
        self.api = AnimeFLV()
        self.search_data = self.api.search(self.search)
        self.anime_data = None
        self.links = None
        self.contador = 0
        self.cursor = None
        self.position = 1
        self.position_cache = 0
        self.cap = None
        self.system = platform.system()
        self.clear_console = 'clear'

        if self.system == 'Windows':
            self.clear_console = 'cls'

        self.cmd_colors = {
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'purple': '\033[95m',
            'sub' : '\033[4m',
            'tick' : '\033[5m',
            'tick2' : '\033[6m',
            'inv' : '\033[7m',
            'end' : '\033[0m'
        }

    def set_zero(self):
        os.system(self.clear_console)
        self.position = 1
        self.position_cache = 0
        self.contador = 0
        self.cursor = None

    def draw(self, ciclos, estado = None):

        os.system(self.clear_console)
        self.position_cache = self.position

        if estado =='busqueda':
            print(f"Resultados para {self.cmd_colors['green'] + self.search.replace('-', ' ') + self.cmd_colors['end']}\n")

            for i in range(ciclos):
                if self.position == i+1:
                    print(f"[{self.cmd_colors['tick2'] + self.cmd_colors['inv']}*{self.cmd_colors['end']}] {self.search_data[i].id.replace('-',' ')}")
                else:
                    print(f"[ ] {self.search_data[i].id.replace('-',' ')}")

            print(f"{self.cmd_colors['yellow']}\n[ESC] Salir\t[i] Info\t[->] Avanzar{self.cmd_colors['end']}")

        elif estado =='info':
            print(f"{self.cmd_colors['tick2'] + self.cmd_colors['blue']}Name:{self.cmd_colors['end']} {self.cmd_colors['purple'] + self.anime_data.title + self.cmd_colors['end']}\n")

            print(f"Clasificacion: {self.anime_data.rating}\t\tEpisodios: {len(self.anime_data.episodes)}\n\nGenero: {self.anime_data.genres}\n\nSinopsis\n\n{self.anime_data.synopsis}\n")

            print(f"{self.cmd_colors['yellow']}\n[ESC] Salir\t[<-] Volver{self.cmd_colors['end']}")

        elif estado == 'episodios':
            print(f"{self.cmd_colors['tick2'] + self.cmd_colors['blue']}Name:{self.cmd_colors['end']} {self.cmd_colors['purple'] + self.anime_data.title + self.cmd_colors['end']}\n")
           
            for i in range(ciclos):
                if self.position == i+1:
                    print(f"[{self.cmd_colors['tick2'] + self.cmd_colors['inv']}*{self.cmd_colors['end']}] Episodio {str(i+1)}")
                else:
                    print(f"[ ] Episodio {str(i+1)}")

            print(f"{self.cmd_colors['yellow']}\n[ESC] Salir\t[<-] Volver\t[->] Avanzar{self.cmd_colors['end']}")

        elif estado =='servidores':
            print(f"{self.cmd_colors['tick2'] + self.cmd_colors['blue']}Name:{self.cmd_colors['end']} {self.cmd_colors['purple'] + self.anime_data.title} Episodio {str(self.cap) + self.cmd_colors['end']}\n")

            for i in range(ciclos):
                if self.position == i+1:
                    print(f"[{self.cmd_colors['tick2'] + self.cmd_colors['inv']}*{self.cmd_colors['end']}] {self.links[0][i]['server']}")
                else:
                    print(f"[ ] {self.links[0][i]['server']}")

            print(f"{self.cmd_colors['yellow']}\n[ESC] Salir\t[<-] Volver\t[->] Avanzar{self.cmd_colors['end']}")

    def selector(self, ciclos, estado):

        while True:

            if self.position != self.position_cache:
                self.draw(ciclos, estado)

            self.cursor = keyboard.read_key()

            if self.cursor == 'down':
                self.position += 1

            if self.cursor == 'up':
                self.position -= 1

            if self.cursor == 'enter' or self.cursor == 'space' or self.cursor == 'right':
                if estado == 'busqueda':
                    self.anime_data = self.api.get_anime_info(self.search_data[self.position-1].id)
                    self.set_zero()
                    self.selector(self.anime_data.episodes[0].id, 'episodios')
                elif estado == 'info':
                    pass
                elif estado == 'episodios':
                    self.links = self.api.get_video_servers(self.anime_data.id, self.position)
                    self.cap = self.position
                    self.set_zero()
                    self.selector(len(self.links[0]), 'servidores')
                elif estado == 'servidores':
                    os.system(self.clear_console)
                    print(f"\n\n{self.cmd_colors['green']}Descargando anime...{self.cmd_colors['end']}")
                    os.system('mpv ' + self.links[0][self.position-1]['code'])
                    self.set_zero()

            if self.cursor == 'i' and estado == 'busqueda':
                self.anime_data = self.api.get_anime_info(self.search_data[self.position-1].id)
                estado = 'info'
                self.set_zero()

            if self.cursor == 'left':
                if estado == 'info':
                    estado = 'busqueda'
                    self.set_zero()
                elif estado == 'servidores':
                    self.set_zero()
                    self.position = self.cap
                    break
                else:
                    self.set_zero()
                    break

            if self.cursor == 'esc':
                os.system(self.clear_console)
                sys.exit()

            if self.position < 1:
                self.position = ciclos
            elif self.position > ciclos:
                self.position = 1

            time.sleep(0.1)

    def run(self):

        if self.params == None:
            print('uwu-cli Version 0.3\n\nusage:\nuwu-cli [Comando]\t\tEx: uwu-cli -h\nuwu-cli [Nombre-del-anime]\t\tEx: uwu-cli Jujutsu-kaisen\n\nComandos:\n-h\t: Muestra todos los comandos y sus funciones.\n-l\t: Muestra los ultimos episodios en emision.\n-n\t: Muestra todos los animes en emision.\n\nCreditos:\nAuthor\t\t: Alfonso Lozano A.K.A. NightDarkness.\nanimeflv api\t: Jorge Alejandro Jiménez Luna.')
            sys.exit()
        elif self.params != None and self.params[0] == '-':
            
            if self.params[1] == 'h' or self.params[1] == 'H':
                print('uwu-cli Version 0.3\n\nusage:\nuwu-cli [Comando]\t\tEx: uwu-cli -h\nuwu-cli [Nombre-del-anime]\t\tEx: uwu-cli Jujutsu-kaisen\n\nComandos:\n-h\t: Muestra todos los comandos y sus funciones.\n-l\t: Muestra los ultimos episodios en emision.\n-n\t: Muestra todos los animes en emision.\n\nCreditos:\nAuthor\t\t: Alfonso Lozano A.K.A. NightDarkness.\nanimeflv api\t: Jorge Alejandro Jiménez Luna.')
            
            elif self.params[1] == 'l' or self.params[1] == 'L':
                os.system(self.clear_console)
                temp = self.api.get_latest_episodes()

                print(f"{self.cmd_colors['green']}Ultimos capitulos{self.cmd_colors['end']}\n")

                for i in temp:
                    print(f"{i.anime.replace('-', ' ')} Episodio {i.id}")

            elif self.params[1] == 'n' or self.params[1] == 'N':
                os.system(self.clear_console)
                temp = self.api.get_latest_animes()

                print(f"{self.cmd_colors['green']}Animes en emision{self.cmd_colors['end']}\n")

                for i in temp:
                    print(f"{i.title}")

        else:
            while True:

                os.system(self.clear_console)

                if len(self.search_data) == 0:

                    if self.contador < 3:
                        self.contador += 1
                        print(f"{self.cmd_colors['yellow']}No hay respuesta del servidor...\n{self.cmd_colors['green']}Reintentando... (intento #{str(self.contador)}){self.cmd_colors['end']}")
                        self.search_data = self.api.search(self.search)
                        time.sleep(0.5)
                    else:
                        print(f"{self.cmd_colors['red']}No hay resultados para: \"{self.cmd_colors['purple'] + self.search + self.cmd_colors['red']}\"{self.cmd_colors['end']}")
                        sys.exit(0)

                elif len(self.search_data) > 0:
                    self.selector(len(self.search_data), 'busqueda')

                    break
        os.system(self.clear_console)
        sys.exit()

app = UwuCli()

if __name__ == "__main__":
    app.run()