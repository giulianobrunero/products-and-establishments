# Products and establishments API
Esta API permite encontrar y comparar productos alimenticios que diferentes establecimientos tengan en stock, según los valores dietéticos y precios.

# Instalación
### 1) Requisitos de dependencias
1) Python 3.8.10 (puede funcionar con versiones anteriores pero no se asegura)
2) Virtualenv

### 2) Clonar proyecto
```sh
git clone https://github.com/giulianobrunero/products-and-establishments.git
```

### 3) Crear y activar entorno virtual
1) Acceder al proyecto clonado
    ```sh
    cd products-and-establishments
    ```

2) Crea un nuevo entorno virtual
    ```sh
    ~.../products_and_establishments$ virtualenv -p python3 env
    ```

2) Activá el entorno virtual
    ```sh
    ~.../products_and_establishments$ source env/bin/activate
    ```

### 4) Instalar librerias del proyecto
```sh
(env)~.../products_and_establishments$ pip install -r requirements.txt
```

### 5) Correr proyecto
Este comando por defecto corre el proyecto en: http://127.0.0.1:8000/
```sh
(env)~.../products_and_establishments$ ./manage.py runserver
```

# Documentación
##### Mientras el proyecto está corriendo, en este link encontrarás toda la documentación de la API: **http://127.0.0.1:8000/redoc/**
#
*(Asumiendo que el proyecto esta corriendo en http://127.0.0.1:8000)*
[![documentacion](https://i.ibb.co/9q9093H/Captura-de-pantalla-de-2022-07-05-20-35-55.png)](http://127.0.0.1:8000/redoc/)

# Pruebas
##### Mientras el proyecto está corriendo, en este link podrás probar la API: **http://127.0.0.1:8000/swagger/**
#
*(Asumiendo que el proyecto esta corriendo en http://127.0.0.1:8000)*
[![swagger](https://i.ibb.co/VmCJW4k/Captura-de-pantalla-de-2022-07-05-20-48-24.png)](http://127.0.0.1:8000/swagger/)

