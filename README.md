# Coderhouse-57830-Gonzalo-Veglio

# Optlog

**Optlog** es un sistema web de logística diseñado para gestionar envíos, clientes, productos, camiones, choferes y rutas. Este proyecto utiliza Python y Django para el backend, HTML, CSS, y JavaScript para el frontend, y Bootstrap 5 como framework para los estilos.

## Descripción

El objetivo de **Optlog** es proporcionar una plataforma integral para la gestión logística. El sistema permite a los usuarios administrativos gestionar clientes, productos, pedidos, y camiones. Además, ofrece una interfaz para el seguimiento de envíos.

## Funcionalidades

### Funcionalidades Implementadas

- **Gestión de Clientes**: CRUD (Crear, Leer, Actualizar, Eliminar) para clientes.
- **Gestión de Productos**: CRUD para productos.
- **Gestión de Pedidos**: CRUD para pedidos con relaciones a productos y clientes.
- **Gestión de Camiones**: CRUD para camiones.
- **Gestión de Choferes**: CRUD para choferes.
- **Gestión de Envios**: CRUD para envíos con relaciones a camiones y choferes.
- **Gestión de Rutas**: CRUD para hojas de ruta (rutas).
- **Autenticación de Usuarios**: Utiliza el modelo de usuario integrado de Django para el login y permisos.


### Funcionalidades en Progreso

- **Modulo de Hoja de Ruta**: Creacion de un modulo que permita agrupar a los envios en un mismo recorrido para tener contro de la mercaderia y dar una mejora trazabilidad a cada uno de los envios.
- **Gráficos mejorados**: Implementación de gráficos mejorados para poder ver, en tiempo real, los datos necesarios para la optimizacion de informacion ante nuestros cliente y la toma de deciciones 

## Instalación

Para instalar y ejecutar el proyecto localmente, sigue estos pasos:

1. **Clona el repositorio:**

     - git clone https://github.com/clicpaq-desarrollo/Coderhouse-57830-Gonzalo-Veglio.git
     - cd optlog

2. **Crea un entorno virtual y activa:**
     - python -m venv .venv

     - .venv\Scripts\activate  # En Windows

     - source .venv/bin/activate  # En macOS/Linux

3. **Instala las dependencias:**

     - pip install -r requirements.txt

4. **Realiza las migraciones de la base de datos:**

     - python manage.py makemigrations
     - python manage.py migrate

5. **Crea un superusuario para acceder al panel de administración:**
 
     - python manage.py createsuperuser

6. **Inicia el servidor de desarrollo:**
 
     - python manage.py runserver

7. **Accede a la aplicación en tu navegador:**
 
     - http://127.0.0.1:8000/

8. **Accede al panel de administración de Django:**
 
     - http://127.0.0.1:8000/admin/


**Estructura del Proyecto**

- __core__: Contiene archivos y configuraciones básicas del proyecto, como base.html y footer.html.
- __clientes__: Gestión de clientes.
- __productos__: Gestión de productos.
- __pedidos__: Gestión de pedidos.
- __camiones__: Gestión de camiones.
- __choferes__: Gestión de choferes.
- __envios__: Gestión de envíos. 
- __miscelaneas__: Gestión de datos misceláneos, como localidades   
- __tracking__: Seguimiento de envíos.

 
