# Coderhouse-57830-Gonzalo-Veglio

# Optlog

**Optlog** es un sistema web de logística diseñado para gestionar envíos, clientes, productos, camiones, choferes y rutas. Este proyecto utiliza Python y Django para el backend, HTML, CSS, y JavaScript (limitado) para el frontend, y Bootstrap 5 como framework.

## Descripción

El objetivo de **Optlog** es proporcionar una plataforma integral para la gestión logística. El sistema permite a los usuarios administrativos gestionar clientes, productos, pedidos, y camiones. Además, ofrece una interfaz para el seguimiento de envíos y la planificación de rutas.

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

- **Panel de Administración**: Personalización de vistas para la gestión de modelos en el panel de administración de Django.
- **Gráficos Simples**: Implementación de gráficos básicos para visualizar datos.

## Instalación

Para instalar y ejecutar el proyecto localmente, sigue estos pasos:

1. **Clona el repositorio:**

    git clone https://github.com/tu-usuario/optlog.git
   cd optlog

2. **Crea un entorno virtual y activa:**
     python -m venv .venv
    .venv\Scripts\activate  # En Windows
    source .venv/bin/activate  # En macOS/Linux

3. **Instala las dependencias:**

     pip install -r requirements.txt

4. **Realiza las migraciones de la base de datos:**

 python manage.py makemigrations
python manage.py migrate

5. **Crea un superusuario para acceder al panel de administración:**
 
python manage.py createsuperuser

6. **Inicia el servidor de desarrollo:**

 
python manage.py runserver

7. **Accede a la aplicación en tu navegador:**
 
http://127.0.0.1:8000/

8. **Accede al panel de administración de Django:**
 
http://127.0.0.1:8000/admin/


Estructura del Proyecto
core: Contiene archivos y configuraciones básicas del proyecto, como base.html y footer.html.
clientes: Gestión de clientes.
productos: Gestión de productos.
pedidos: Gestión de pedidos.
camiones: Gestión de camiones.
choferes: Gestión de choferes.
envios: Gestión de envíos. 
miscelaneas: Gestión de datos misceláneos, como localidades  
usuarios: Gestión de usuarios con el modelo integrado de Django.
tracking: Seguimiento de envíos.
Qué Falta Hacer
Completar el panel de administración: Añadir funcionalidades adicionales y vistas personalizadas para una mejor gestión.
Implementar gráficos: Añadir gráficos simples para visualizar datos relacionados con envíos, pedidos, etc.
Mejorar la interfaz de usuario: Añadir más estilos y mejorar la experiencia del usuario.
Documentación adicional: Completar la documentación del proyecto y agregar instrucciones para el despliegue en producción.