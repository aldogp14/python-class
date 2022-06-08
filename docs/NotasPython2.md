# GitHub

## ¿Cómo llevar control de mi código?

### Forma manual

La versión está constituido por dos dígitos, versiones primarias y secundarias.

v X.Y.

Reglas

- X (mayor): cuando el programa se considere liberado, estable.
- Y (menor): para modificaciones diarias que pueden realizarse sobre el código
  - cambio de tipo de dato
  - agregar o cambiar variables
  - sintáxis
  - organización de código

### Forma automática

Por medio de un sistema de control de versiones, crea diferentes versiones de nuestros archivos. Cada registro de estos cambios es llamado commit. Un sistema de control de versiones es como un "undo" ilimitado.

- Git de manera local 

- Git + GitHub

__repositorio__: carpeta que contiene el seguimiento de los casos que se realicen en el código.

git add > area staging > git commit > repositorio

**ramas git**: es un apuntador que nos permite hacer referencia a cada una de las confirmaciones de los commits. rama master.

## Configuración git

### Comandos

**git config --global user.name "(nombre)"**

**git config --global user.email correo**

**git init** *inicializar el repositorio en git*

**ls -la**   *revisar el repositorio*

**dir /a** *revisar el repositorio*  para símbolo de sistema (windows)

**git status** *comprobar el repositorio*

​					**--ignored**

**git add** *indicar que Git debe comenzar a controlar el archivo*

**git commit -m "mensaje"**  *confirmar los cambios realizados en el repositorio* 

 **git commit --amend -m "mensaje"** *modificar el mensaje del commit más reciente*

**nano nombre del programa** *modificar el programa*

**git diff** *compara las versiones del programa y arroja las diferencias*

​			**--staged** *compara con los commit, es decir con lo que se deja en el repositorio*

​			**HEAD~#** *compara con cierto commit usando su cabecera*

​			**id** *compara con cierto commit usando su id*

**git log** *lista todos los commits realizados en el repositorio en el orden cronológico inverso*

​			**-N** *donde N indica el número de commits que queremos obtener.*

***cada commit tiene un identificador de 40 caracteres

​			**--oneline** *para obtner ids cortos de los commits (primeros 7 caracteres)*

**git status -u** *nos dice que archivos están pendientes por ser controlados, agregados*

**git rebase --interactive id del commit** *abre typora para modificar el commit, poner reword. ESTO ALTERA LOS IDs DE LOS COMMITS*

**git show** *muestra más detalle del commit indicado por HEAD o ID*

**git checkout HEAD (head se usa para el último commit, se usa viborita # para regresar a anteriores)/ID** *nos permite recuperar versiones anteriores indicando el commit al que queremos volver (HEAD  o ID)*

si no se indica el head o id, checkout toma el último

**git rm** *borrar archivos*

aún cuando borramos un archivo, git tiene una referencia del archivo borrado >> hay que hacer un git commit para confirmar 

**nano .gitignore** *en ese archivo poner el nombre de los archivos que queremos que git ignore*

*con un ! se evita que un archivo sea ignorado"*

ejemplo: a.data b.data c.data y z.data    "*.data !z.data"

**git remote add origin** enlazar repositorio con github

**git remote -v** verificar que se haya enlazado

**git push origin master** 

**git pull origin master**



