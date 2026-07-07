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

    # TODO: Aquí meteremos la clase real cuando inspecciones la página
    # Por ahora usamos un placeholder para que el código no rompa
    clase_proyecto = "project-item"
    proyectos = soup.find_all("div", class_=clase_proyecto)

    print(f"[+] Se encontraron {len(proyectos)} bloques de proyectos en la página.\n")

    for proyecto in proyectos:
        # Aquí irá la lógica para extraer títulos y habilidades
        pass


def main():
    print("[*] Iniciando el scraper de Workana...")

    # URL de la sección de Programación y Tecnología
    url_objetivo = "https://www.workana.com/jobs?category=it-programming"

    soup = obtener_html(url_objetivo)
    parsear_proyectos(soup)


if __name__ == "__main__":
    main()
