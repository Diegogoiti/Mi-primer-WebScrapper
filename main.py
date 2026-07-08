import json

# from ast import While
import requests
from bs4 import BeautifulSoup


class Scrapper:
    def __init__(self):
        self.habilidades = {}
        self.proyectos = []

    """@staticmethod
    def obtener_numero_paginas(url):
        soup = BeautifulSoup(requests.get(url).text, "html.parser")
        pagination = soup.find("search")
        if not pagination:
            return 1
        return int(pagination.get("pagination", {}).get("totalPages", 1))"""

    def obtener_html(self):
        """Realiza la petición HTTP y devuelve el objeto BeautifulSoup."""
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }

        try:
            # Aquí self apuntará correctamente a la instancia de Scrapper
            response = requests.get(self.url, headers=headers, timeout=10)
            if response.status_code == 200:
                return BeautifulSoup(response.text, "html.parser")
            else:
                print(
                    f"[-] Error en la petición. Código de estado: {response.status_code}"
                )
                return None
        except Exception as e:
            print(f"[-] Ocurrió un error al conectar: {e}")
            return None

    def parsear_proyectos(self):
        """Extrae la información de los proyectos del HTML."""
        if not self.soup:
            return

        # 1. Buscamos la etiqueta de Vue
        search_tag = self.soup.find("search")
        if not search_tag:
            print("[-] No se encontró la etiqueta <search> en la página.")
            return

        # 2. Extraemos el atributo de texto y lo convertimos a un diccionario de Python
        # data_json = json.loads(search_tag[":results-initials"])
        raw_json = str(search_tag[":results-initials"])
        data_json = json.loads(raw_json)

        # 3. Accedemos a la lista de proyectos dentro de la clave "results"
        proyectos = data_json.get("results", [])

        if len(proyectos) == 0:
            return
        for proyecto in proyectos:
            self.proyectos.append(proyecto)
            """titulo_sucio = proyecto.get("title", "Sin título")

            # Pasamos el string HTML por BeautifulSoup para extraer solo el texto limpio
            titulo_limpio = BeautifulSoup(titulo_sucio, "html.parser").get_text()

            print(titulo_limpio)

            skills_data = proyecto.get("skills", [])

            # Extraemos el 'anchorText' de cada elemento de la lista
            habilidades = [skill.get("anchorText") for skill in skills_data]

            # Las unimos en un solo string bonito
            habilidades_str = ", ".join(habilidades)

            print(f"Habilidades: {habilidades}")
            print("-" * 40)"""

    def cargar_habilidades(self):
        if not self.proyectos:
            return

        for proyecto in self.proyectos:
            skills_data = proyecto.get("skills", [])

            # Extraemos el 'anchorText' de cada elemento de la lista
            habilidades = [skill.get("anchorText") for skill in skills_data]

            for habilidad in habilidades:
                if habilidad not in self.habilidades:
                    self.habilidades[habilidad] = 1
                else:
                    self.habilidades[habilidad] += 1

    def habilidades_ordenadas(self):
        return sorted(self.habilidades.items(), key=lambda x: x[1], reverse=True)

    def procesar_pagina(self, url):
        self.url = url
        self.soup = self.obtener_html()
        if not self.soup:
            return False  # Falló la conexión

        self.parsear_proyectos()
        if not self.proyectos:
            return False  # Se acabaron los proyectos

        self.cargar_habilidades()
        self.proyectos = []  # Limpiamos para la siguiente
        return True


def main():
    print("[*] Iniciando el scraper de Workana...")

    # URL de la sección de Programación y Tecnología
    # url_objetivo = "https://www.workana.com/jobs?category=it-programming&language=xx"
    # num_paginas = Scrapper.obtener_numero_paginas(url_objetivo)

    # print(f"[*] Número de páginas: {num_paginas}")

    mi_scrapper = Scrapper()
    # mi_scrapper.parsear_proyectos()
    # mi_scrapper.cargar_habilidades()

    i = 1
    while True:
        url = f"https://www.workana.com/jobs?category=it-programming&page={i}"
        print(f"[*] Procesando página {i}...")
        if not mi_scrapper.procesar_pagina(url):
            print("[!] No se encontraron más proyectos. Terminando... ")
            break
        i += 1

    for habilidad, cantidad in mi_scrapper.habilidades_ordenadas():
        print(f"{habilidad}: {cantidad}")


if __name__ == "__main__":
    main()
