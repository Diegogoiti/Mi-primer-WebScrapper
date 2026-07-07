import json

import requests
from bs4 import BeautifulSoup


def obtener_html(url):
    """Realiza la petición HTTP y devuelve el objeto BeautifulSoup."""
    # Simulamos un navegador real en Linux para evitar bloqueos básicos
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            return BeautifulSoup(response.text, "html.parser")
        else:
            print(f"[-] Error en la petición. Código de estado: {response.status_code}")
            return None
    except Exception as e:
        print(f"[-] Ocurrió un error al conectar: {e}")
        return None


def parsear_proyectos(soup):
    """Extrae la información de los proyectos del HTML."""
    if not soup:
        return

    # 1. Buscamos la etiqueta de Vue
    search_tag = soup.find("search")
    if not search_tag:
        print("[-] No se encontró la etiqueta <search> en la página.")
        return

    # 2. Extraemos el atributo de texto y lo convertimos a un diccionario de Python
    data_json = json.loads(search_tag[":results-initials"])

    # 3. Accedemos a la lista de proyectos dentro de la clave "results"
    proyectos = data_json.get("results", [])

    print(f"[+] Se encontraron {len(proyectos)} bloques de proyectos en la página.\n")

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

    soup = obtener_html(url_objetivo)
    parsear_proyectos(soup)

    # print(soup)


if __name__ == "__main__":
    main()
