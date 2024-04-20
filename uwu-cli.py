import sys, os, time, platform
from modules import AnimeFLV
import keyboard


class UwuCli():

    def __init__(self):

        self.api = AnimeFLV()

        if len(sys.argv) > 1:
            self.params = sys.argv[1]
            self.search = self.params.replace('-', ' ')
        else:
            self.params = None
            self.search = 'dungeon meshi'

        self.search_data = self.api.search(self.search)
        self.anime_data = None
        self.contador = 0
        self.position = 1
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

    def viewer(self, anime, episodes):

        self.position = 1

        while True:

            os.system(self.clear_console)
            print(f"{self.cmd_colors['tick2'] + self.cmd_colors['blue']}Name:{self.cmd_colors['end']} {self.cmd_colors['purple'] + anime.replace('-',' ') + self.cmd_colors['end']}\n")

            for i in range(episodes):
                if self.position == i+1:
                    print(f"[{self.cmd_colors['tick2'] + self.cmd_colors['inv']}*{self.cmd_colors['end']}] Episodio {str(i+1)}")
                else:
                    print(f"[ ] Episodio {str(i+1)}")
            
            print(f"{self.cmd_colors['yellow']}\nESC para salir...{self.cmd_colors['end']}")

            cursor = keyboard.read_key()

            if cursor == 'down':
                self.position += 1

            if cursor == 'up':
                self.position -= 1

            if cursor == 'enter' or cursor == 'space':
                link = self.api.get_video_servers(anime, self.position)
                servers = len(link[0])
                cap = self.position
                self.position = 1

                while True:

                    os.system(self.clear_console)
                    print(f"{self.cmd_colors['tick2'] + self.cmd_colors['blue']}Name:{self.cmd_colors['end']} {self.cmd_colors['purple'] + anime.replace('-',' ')} Episodio {str(cap) + self.cmd_colors['end']}\n")

                    for i in range(servers):
                        if self.position == i+1:
                            print(f"[{self.cmd_colors['tick2'] + self.cmd_colors['inv']}*{self.cmd_colors['end']}] {link[0][i]['server']}")
                        else:
                            print(f"[ ] {link[0][i]['server']}")

                    print(f"{self.cmd_colors['yellow']}\nESC para volver...{self.cmd_colors['end']}")

                    cursor = keyboard.read_key()

                    if cursor == 'down':
                        self.position += 1

                    if cursor == 'up':
                        self.position -= 1

                    if cursor == 'enter' or cursor == 'space':
                        print(f"\n\n{self.cmd_colors['green']}Descargando anime...{self.cmd_colors['end']}")
                        os.system('mpv ' + link[0][self.position-1]['code'])
                        break

                    if cursor == 'esc':
                        os.system(self.clear_console)
                        print(f"Volviendo al menu anterior, por favor espera.")
                        self.position = 1
                        self.contador = 0
                        cursor = None
                        break

                    if self.position < 1:
                        self.position = servers
                    elif self.position > servers:
                        self.position = 1

                    time.sleep(0.1)

            if cursor == 'esc':
                cursor = None
                self.position = 1
                self.contador = 0
                os.system(self.clear_console)
                break

            if self.position < 1:
                self.position = episodes
            elif self.position > episodes:
                self.position = 1

            time.sleep(0.1)

    def run(self):

        if self.params == None:
            print('uwu-cli for Windows Version 0.1\n\nusage:\nuwu-cli [Comando]\nuwu-cli [Nombre del anime]\n\nComandos:\n-h\t: Muestra todos los comandos y sus funciones.\n-l\t: Muestra los ultimos episodios en emision.\n-n\t: Muestra todos los animes en emision.\n\nCreditos:\nAuthor\t\t: Alfonso Lozano A.K.A. NightDarkness.\nanimeflv api\t: Jorge Alejandro Jiménez Luna.')
            sys.exit()
        elif self.params != None and self.params[0] == '-':
            
            if self.params[1] == 'h' or self.params[1] == 'H':
                print('uwu-cli for Windows Version 0.1\n\nusage:\nuwu-cli [Comando]\nuwu-cli [Nombre del anime]\n\nComandos:\n-h\t: Muestra todos los comandos y sus funciones.\n-l\t: Muestra los ultimos episodios en emision.\n-n\t: Muestra todos los animes en emision.\n\nCreditos:\nAuthor\t\t: Alfonso Lozano A.K.A. NightDarkness.\nanimeflv api\t: Jorge Alejandro Jiménez Luna.')
            
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
                    os.system(self.clear_console)

                    if self.contador < 3:
                        self.contador += 1
                        print(f"{self.cmd_colors['yellow']}No hay respuesta del servidor...\n{self.cmd_colors['green']}Reintentando... (intento #{str(self.contador)}){self.cmd_colors['end']}")
                        self.search_data = self.api.search(self.search)
                        time.sleep(0.5)
                    else:
                        print(f"{self.cmd_colors['red']}No hay resultados para: \"{self.cmd_colors['purple'] + self.search + self.cmd_colors['red']}\"{self.cmd_colors['end']}")
                        sys.exit(0)

                elif len(self.search_data) == 1:
                    self.search_data = self.api.get_anime_info(self.search_data[0].id)
                    anime = self.search_data.id
                    episodes = self.search_data.episodes[0].id
                    self.viewer(anime, episodes)
                    break

                else:
                    self.position = 1
                    servers = len(self.search_data)

                    while True:

                        os.system(self.clear_console)

                        print(f"Resultados para {self.cmd_colors['green'] + self.search.replace('-', ' ') + self.cmd_colors['end']}\n")

                        for i in range(servers):
                            if self.position == i+1:
                                print(f"[{self.cmd_colors['tick2'] + self.cmd_colors['inv']}*{self.cmd_colors['end']}] {self.search_data[i].id.replace('-',' ')}")
                            else:
                                print(f"[ ] {self.search_data[i].id.replace('-',' ')}")
                        
                        print(f"{self.cmd_colors['yellow']}\nESC para salir...{self.cmd_colors['end']}")

                        cursor = keyboard.read_key()

                        if cursor == 'down':
                            self.position += 1

                        if cursor == 'up':
                            self.position -= 1

                        if cursor == 'enter' or cursor == 'space':
                            self.anime_data = self.api.get_anime_info(self.search_data[self.position-1].id)
                            anime = self.anime_data.id
                            episodes = self.anime_data.episodes[0].id
                            self.viewer(anime, episodes)

                        if cursor == 'esc':
                            os.system(self.clear_console)
                            break

                        if self.position < 1:
                            self.position = servers
                        elif self.position > servers:
                            self.position = 1

                        time.sleep(0.1)
                    break

        sys.exit()

app = UwuCli()

if __name__ == "__main__":
    app.run()