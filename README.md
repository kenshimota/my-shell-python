# my-shell-python

Implementación de una shell POSIX construida desde cero en Python para el reto [Build Your Own Shell](https://app.codecrafters.io/courses/shell/overview) de CodeCrafters.

## Funcionalidad

- REPL con prompt `$`.
- Builtins: `echo`, `type`, `pwd`, `cd` y `exit`.
- Ejecución de comandos externos con búsqueda en `PATH`.
- Redirección de salida (`>`, `1>`, `2>`).
- División de argumentos con `shlex`, respetando comillas.
- `cd` con soporte para `~`, rutas relativas, absolutas y `..`.

## Estructura

```
app/
├── main.py                     # REPL y despacho de comandos
└── src/
    ├── bin/
    │   ├── cd.py               # builtin cd
    │   ├── pwd.py              # builtin pwd
    │   ├── type_command.py     # builtin type y búsqueda en PATH
    │   └── run_command_external.py
    └── helpers/
        └── process_arguments.py
```

## Requisitos

- Python 3.14
- [uv](https://docs.astral.sh/uv/)

## Uso

```bash
./your_program.sh
```

Ejemplo:

```text
$ echo hola
hola
$ pwd
/home/usuario
$ cd ..
$ type cd
cd is a shell builtin
```

## Estado

Proyecto en desarrollo. Nuevas etapas del reto se agregan a medida que avanzan.
