import json

import requests
from bs4 import BeautifulSoup


class Scrapper:
    def __init__(self, url):
        self.url = url
        # Ahora que es un método de la clase, lo llamas usando self.obtener_html()
        self.soup = self.obtener_html()

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
        data_json = json.loads(search_tag[":results-initials"])

        # 3. Accedemos a la lista de proyectos dentro de la clave "results"
        proyectos = data_json.get("results", [])

        print(
            f"[+] Se encontraron {len(proyectos)} bloques de proyectos en la página.\n"
        )

        for proyecto in proyectos:
            titulo_sucio = proyecto.get("title", "Sin título")

            # Pasamos el string HTML por BeautifulSoup para extraer solo el texto limpio
            titulo_limpio = BeautifulSoup(titulo_sucio, "html.parser").get_text()

            print(titulo_limpio)

            skills_data = proyecto.get("skills", [])

            # Extraemos el 'anchorText' de cada elemento de la lista
            habilidades = [skill.get("anchorText") for skill in skills_data]

            # Las unimos en un solo string bonito
            habilidades_str = ", ".join(habilidades)

            print(f"Habilidades: {habilidades}")
            print("-" * 40)


def main():
    print("[*] Iniciando el scraper de Workana...")

    # URL de la sección de Programación y Tecnología
    url_objetivo = "https://www.workana.com/jobs?category=it-programming&language=xx"

    mi_scrapper = Scrapper(url_objetivo)
    mi_scrapper.parsear_proyectos()


if __name__ == "__main__":
    main()
