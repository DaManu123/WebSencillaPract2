# Web Restaurante - Proyecto Flask

Aplicación web de restaurante desarrollada con Flask y Bootstrap (plantilla Restaurantly).

## Requisitos Previos

- Python 3.8 o superior
- Git

## Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/DaManu123/WebSencillaPract2.git
   cd WebSencillaPract2
   ```

2. **Crear un entorno virtual:**
   ```bash
   python -m venv venv
   ```

3. **Activar el entorno virtual:**
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Instalar las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Ejecutar la aplicación:**
   ```bash
   flask run
   ```

6. **Abrir en el navegador:**
   - Visita: `http://127.0.0.1:5000`

## Estructura del Proyecto

```
websencillapract2/
├── app.py              # Aplicación principal Flask
├── datos.json          # Datos del restaurante (menú, contacto, etc.)
├── requirements.txt    # Dependencias de Python
├── .env                # Variables de entorno (Flask)
├── templates/          # Plantillas HTML
│   ├── base.html       # Plantilla base
│   ├── index.html      # Página de inicio
│   ├── menu.html       # Página del menú
│   ├── contacto.html   # Página de contacto
│   └── reservaciones.html  # Página de reservaciones
└── static/             # Archivos estáticos (CSS, JS, imágenes)
    ├── css/
    ├── js/
    ├── img/
    └── vendor/
```

## Características

- ✅ Diseño responsivo con Bootstrap 5
- ✅ Menú dinámico cargado desde JSON
- ✅ Galería de imágenes con lightbox
- ✅ Formulario de reservaciones
- ✅ Página de contacto con Google Maps
- ✅ Animaciones con AOS (Animate On Scroll)

## Tecnologías Utilizadas

- **Backend:** Flask 3.1.2
- **Frontend:** Bootstrap 5.3.3
- **Plantilla:** Restaurantly by BootstrapMade
- **Librerías:** AOS, Glightbox, Swiper, Bootstrap Icons
