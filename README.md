#  Tarea 15: Desarrollo de Módulo Personalizado

## Procedimiento
Para crear este mçodulo personalizado, primero, lo que hemos hecho fue usar esta línea de código en la terminal `docker exec -it odoo18_app15 odoo scaffold gestion_dormir /mnt/extra-addons/` para crear los archivos necesarios para elaborar la aplicación.

Principalmente, de esos archivos, he usado los siguientes:
- **Models**: La cual se encarga del funcionamiento del módulo.
- **Views**: Se ocupa de la interfaz del mismo.
- **Security**: Con el archivo .csv permitimos la visibilidad de la aplicación.

---

## Dentro de Odoo
Al iniciar el docker compose, hacer la base de datos y entrar en Odoo, tenemos que activar el modo de desarrollador en Odoo para poder actualizar la lista de aplicaciones, con el fin de encontrar el módulo que creamos.

<img width="1280" height="1392" alt="Captura de pantalla 2026-02-14 130714" src="https://github.com/user-attachments/assets/470ea5c3-508d-4561-b8e8-9235253f8cbc" />

Una vez hecho esto, volvemos a la lista de aplicaciones y le damos a la opción que pone "Actualizar lista de aplicaciones" y se reacargará la página

<img width="1280" height="326" alt="Captura de pantalla 2026-02-14 130902" src="https://github.com/user-attachments/assets/a59c14bb-4350-4da7-9b4c-b909207d61ce" />

Ahora, lo que tenemos que hacer es buscar nuestra aplicaciones y activarla.

<img width="1280" height="433" alt="Captura de pantalla 2026-02-13 170611" src="https://github.com/user-attachments/assets/09d91037-3803-4f35-bc46-6331a9144d81" />

<img width="1280" height="635" alt="Captura de pantalla 2026-02-13 170622" src="https://github.com/user-attachments/assets/43d4fa72-7695-430d-aaf5-12a9f0e8da5e" />

Una vez instalada la aplicación ya podemos entrar en ella y utilizarla. En este caso, como se trata de nivel de sueño, podemos añadir un alumno con su nivel de sueño para que el Odoo se encargue de decirnos que bebida necesita:

<img width="1280" height="416" alt="Captura de pantalla 2026-02-13 184514" src="https://github.com/user-attachments/assets/61641901-d7ec-46dc-80ee-274862e06ca9" />

<img width="1280" height="433" alt="Captura de pantalla 2026-02-13 185418" src="https://github.com/user-attachments/assets/2f571254-8e17-428b-a68d-5732138c306f" />

<img width="1280" height="433" alt="Captura de pantalla 2026-02-13 185429" src="https://github.com/user-attachments/assets/43553628-74e1-4440-b121-4fc750fdac92" />

<img width="1280" height="433" alt="Captura de pantalla 2026-02-13 185440" src="https://github.com/user-attachments/assets/575dc0bf-19ee-4b39-a969-7f0c36e1c047" />

