# 😝 Workana IT Market Skills Scraper

Un web scraper automatizado, modular y de alto rendimiento desarrollado en **Python** empleando `BeautifulSoup` y `Requests`. Diseñado bajo los principios **KISS** y **POO**, esta herramienta extrae, procesa y categoriza dinámicamente las habilidades técnicas reales más demandadas en el mercado freelance tecnológico de Workana.

---

## 🔥 ¿Por qué es diferente?

La mayoría de los scrapers básicos fallan ante la paginación o colapsan por excepciones de red mal gestionadas. Este desarrollo fue estructurado en **una sola hora de puro flujo lógico**, destacando por:

* **Inyección de Datos Directa:** En lugar de realizar un parsing ineficiente de todo el árbol HTML nodo por nodo, localiza e interpreta los objetos JSON crudos (`:results-initials`) inyectados en el DOM.
* **Paginación Inteligente y Autolimitada:** Control de flujo continuo mediante un bucle dinámico que detecta respuestas de servidor (como estados `404`) o páginas vacías para terminar la ejecución limpiamente sin desperdiciar peticiones ni bloquear IPs.
* **Arquitectura Resiliente:** Manejo robusto de excepciones ante fallas de resolución DNS o caídas temporales de la red.

---

## 🛠️ Stack Tecnológico

* **Lenguaje:** Python 3
* **Librerías principales:** `BeautifulSoup4`, `Requests`
* **Paradigma:** Programación Orientada a Objetos (POO)

---

## 🚀 Instalación y Uso rápido

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Diegogoiti/Mi-primer-WebScrapper.git
   cd Mi-primer-WebScrapper
