// Primeras 4 preguntas técnicas de Node.js

// 1. ¿Qué es Node.js y para qué se utiliza principalmente en el desarrollo backend?: Node.js es un entorno de ejecución de JavaScript del lado del servidor, esto nos permite crear backends

// 2. ¿Qué es el módulo fs en Node.js y para qué se utiliza? Da un ejemplo sencillo de cómo leer un archivo de texto usando este módulo.: El módulo fs (file system) en Node.js proporciona una API para interactuar con el sistema de archivos. Se utiliza para leer, escribir, actualizar y eliminar archivos y directorios. Ejemplo sencillo de cómo leer un archivo de texto:
const fs = require('fs');

fs.readFile('archivo.txt', 'utf8', (err, data) => {
    if (err) {
        console.error('Error al leer el archivo:', err);
        return;
    }
    console.log('Contenido del archivo:', data);
});

// 3. Explica qué es el event loop en Node.js y por qué es importante para el rendimiento de aplicaciones backend: Node.js es monohilo, sin embargo el hilo principal no se bloquea gracias al event loop, este redirigue las request a otros hilos para que puedan procesar las solicitudes en segundo plano. De esta manera el hilo principal no se bloqueará y podrá seguir recibiendo nuevas solicitudes.

// 4. Explica qué es un callback en Node.js, cómo se utiliza y cuáles son los problemas que pueden surgir al usarlos. Da un ejemplo sencillo: Un callback es una función que se pasa como argumento a otra función y se ejecuta después de que la operación asíncrona se haya completado. Se utiliza para manejar operaciones asíncronas, como la lectura de archivos o las solicitudes de red. Sin embargo, el uso excesivo de callbacks puede llevar a un problema conocido como "callback hell", donde el código se vuelve difícil de leer y mantener debido a la anidación profunda de funciones. Ejemplo sencillo:
function leerArchivo(nombreArchivo, callback) {
    fs.readFile(nombreArchivo, 'utf8', (err, data) => {
        if (err) {
            return callback(err);
        }
        callback(null, data);
    });
}

// 4 Ejercicios de Node.js