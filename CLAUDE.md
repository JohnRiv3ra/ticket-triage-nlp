# Ticket Triage NLP — contexto para Claude

## Quién soy y cómo quiero aprender
- Soy John, estudiante de software. Trabajo, así que dedico **1 hora diaria** a este proyecto.
- Nivel: sé lo básico de programación. No conozco HTML ni JavaScript.
- Uso **Windows**. Mi proyecto está en `R:\PROYECTOS_SISTEMAS\ticket-triage-nlp`.
- Repositorio: https://github.com/JohnRiv3ra/ticket-triage-nlp
- Objetivo: **aprender** y tener un proyecto sólido para mi GitHub y LinkedIn.

## Cómo debes trabajar conmigo (importante)
- Responde siempre **en español**.
- Eres mi **tutor**, no quien hace el trabajo: explícame cada concepto y deja que **yo escriba el código a mano**. No crees ni edites archivos del proyecto salvo que te lo pida explícitamente.
- Avanza en **pasos pequeños**. Si un concepto es nuevo, explica primero el "para qué" y cómo se conecta con el proyecto final.
- Cuando algo en un comando sea un valor que yo debo reemplazar (usuario, ruta, etc.), **dímelo explícitamente**. Ya me confundí poniendo `TU_USUARIO` y paréntesis literales.
- Cuando tenga un error, ayúdame a **leer e interpretar el mensaje** antes de darme la solución.
- Cada sesión debe terminar con algo funcionando y un `git add → commit → push`.
- Uso la terminal integrada de VS Code (en el proyecto).

## El proyecto
Sistema que clasifica y prioriza automáticamente tickets de soporte técnico con PLN.
Flujo final: el usuario escribe su problema → el modelo predice **categoría** y **prioridad** → se guarda y se muestra en un panel. Extra: sugerir artículos similares (similitud de coseno).

### Stack decidido
| Capa | Tecnología |
|---|---|
| Modelo | Python + scikit-learn (TF-IDF + Regresión Logística / SVM) |
| API | FastAPI (el modelo se carga dentro de la API como `.pkl`) |
| Base de datos | SQLite al inicio, PostgreSQL al final (SQLAlchemy) |
| Frontend | Primero HTML + CSS + JavaScript, después React |
| Extras opcionales | BETO/DistilBERT para comparar, despliegue en línea |

### Notas a tener presentes
- Muchos datasets de tickets en Kaggle están en inglés; el de "Customer Support on Twitter" no trae etiquetas de categoría ni prioridad. Hay que decidir idioma y dataset en la Fase 2.
- Predecir prioridad es más difícil que categoría; es normal que salga con menor precisión.

## Hoja de ruta (aprox. 5 meses a 1 h/día)
| Fase | Duración | Contenido | Estado |
|---|---|---|---|
| 0. Entorno | 1 semana | Python, VS Code, Git, GitHub | ✅ Completada |
| 1. Python | 3 semanas | Variables, funciones, listas, diccionarios, archivos | ✅ Completada (7 sesiones, 2026-10-25 → 2026-10-30) |
| 2. El modelo | 4 semanas | pandas, limpieza de texto, TF-IDF, métricas (accuracy, F1, matriz de confusión) | 🔄 Siguiente |
| 3. API | 3 semanas | FastAPI, endpoints, SQLite | ⏳ |
| 4. Web básica | 4 semanas | HTML, CSS, JavaScript | ⏳ |
| 5. React | 4 semanas | Componentes, estado, llamadas a la API | ⏳ |
| 6. Pulido | 2–3 semanas | README, despliegue, extras | ⏳ |

## Bitácora de progreso
- **2026-10-25 — Fase 0:** instalé Python, VS Code y Git; creé el repo (README, .gitignore Python, licencia MIT), lo cloné y hice mi primer commit y push.
- **2026-10-25 — Fase 1, sesión 1 (variables):** creé `ejercicios/01_variables.py` con un ticket de ejemplo usando `str`, `int`, `float`, `bool`, `print`, `type()` y f-strings. Funciona.
  - Me costó entender **para qué** sirven las variables; se explicó como "cajas con etiqueta" y su relación con el proyecto (la descripción del ticket, la categoría y la prioridad serán variables que luego llena el modelo).
- **2026-10-25 — Fase 1, sesión 1 (reto terminado):** agregué un segundo ticket (`descripcion2`, `categoria2`, `id_ticket2`, `prioridad2`, más `horas_abierto2` y `resuelto2`). Commit y push hechos (`859ebb2`).
  - Error que cometí: al principio olvidé crear `categoria2` y usé `{categoria}` del primer ticket. No dio error, pero mostraba un dato equivocado → lección: el programa puede "funcionar" y aun así estar mal.
  - Probé `print("Ticket " + id_ticket)` → `TypeError: can only concatenate str (not "int") to str`. Lo entendí solo (no se puede unir texto con número) y lo arreglé con `str(id_ticket)`.
  - Notas para la Fase 2: `"Hardware"` ≠ `"hardware"` (hay que normalizar etiquetas), y hay tickets ambiguos (¿hardware o software?).
  - Pendiente opcional: imprimir el ticket con f-string en vez de `+` y `str()`.
- **2026-10-26 — Fase 1, sesión 2 (condicionales):** creé `ejercicios/02_condicionales.py`. Commit y push hechos (`dac8531`).
  - Ejercicio 1: traducir la prioridad numérica a texto con `if/elif/else` y `==`. Mi `else` avisa cuando el valor es inválido (p. ej. `7`) → programación defensiva.
  - Ejercicio 2: decidir la prioridad leyendo la descripción con `in` y `or`, y guardar la decisión en la variable `prioridad`.
  - Normalización: propuse por mi cuenta normalizar la entrada; usé `descripcion = descripcion.lower()` (hay que guardar el resultado con `=`).
  - Errores que descubrí: palabras clave en MAYÚSCULAS que no coincidían con el texto, y `"caido"` ≠ `"caído"` (`.lower()` no quita tildes). Lo resolví buscando ambas formas con `or`.
  - Lección: el código puede funcionar "de casualidad" con un ejemplo y fallar con otro → probar varios casos.
  - Nota para la Fase 2: quitar tildes también es un paso de normalización; TF-IDF de scikit-learn ya convierte a minúsculas.
- **2026-10-26 — Fase 1, sesión 3 (funciones):** creé `ejercicios/03_funciones.py` con `asignar_prioridad(descripcion)`. Commit y push hechos (`7c00187`).
  - Aprendí `def`, parámetros, `return` vs `print` (`return` entrega el valor para guardarlo; `print` solo lo muestra) y que `return` sale de la función.
  - Por mi cuenta hice que la función devuelva dos valores (`return prioridad, mensaje`) → es una **tupla**; la desempaqué con `numero, mensaje = asignar_prioridad(...)`.
  - Probé 3 descripciones y descubrí un error: buscaba `"lenta"` pero el texto decía `"lento"`. Corregido.
  - Decisión: mantener la carpeta `ejercicios/`. `data/`, `notebooks/`, `models/` y `app/` se crearán cuando se necesiten (Fase 2–3).
  - Vi qué es JSON (pares `"nombre": valor`, parecido a diccionarios; formato de la API). Mi `~/.claude/settings.json` configura la barra de estado de Claude Code (`statusline.py`: % de contexto, límite de 5 h y semanal); se ve en la versión de terminal (`claude`), no en el panel de la extensión.

- **2026-10-27 — Fase 1, sesión 4 (listas y `for`):** creé `ejercicios/04_listas.py`. Commit y push hechos (`980aa46`).
  - Aprendí listas (`[ ]`, índices desde 0, `len()`, `.append()`), el bucle `for` y a anidar un `if` dentro de un `for`.
  - Clasifiqué 9 tickets con `asignar_prioridad` dentro de un `for`, y conté los tickets de cada prioridad con 4 contadores (`+= 1`) → 2 críticos, 2 altos, 2 medios, 3 bajos.
  - Errores que tuve:
    - `NameError: name 'asignar_prioridad' is not defined` → cada archivo `.py` es independiente; copié la función (más adelante se usará `import`).
    - Ejecuté líneas sueltas con Shift+Enter: `File "<stdin>", line 1` significa modo interactivo (`>>>`); se sale con `exit()`. Para correr el archivo: botón ▷ o `python ejercicios/04_listas.py`.
    - Usé `==` en vez de `=` al crear los contadores → `NameError` (con `==` Python compara una variable que todavía no existe).
    - Dejé el `if/elif` fuera del `for` (sin sangría): no dio error, pero solo contó el último ticket. Se arregla seleccionando y presionando Tab.
  - Confusión: entendí el ejercicio como "contar todos" y repetí lo mismo en cada rama. Regla: si todas las ramas de un `if` hacen lo mismo, ese código va fuera del `if`.
  - Lección clave del proyecto: `"crash"` salió como prioridad baja → las reglas a mano no escalan; por eso se necesita el modelo de la Fase 2. La función actual sirve como **clasificador basado en reglas** para comparar contra el modelo en el README.
  - Me cuesta leer los traceback: leerlos de abajo hacia arriba (la última línea es el error).

- **2026-10-30 — Fase 1, sesión 5 (diccionarios):** creé `ejercicios/05_diccionarios.py`. Commit y push hechos (`418c417`).
  - Aprendí diccionarios (`{ }`, `"clave": valor`, leer con `ticket["clave"]`, modificar y agregar claves) y la diferencia con las listas: lista = muchas cosas; diccionario = los datos de una cosa.
  - Hice una **lista de diccionarios** con 5 tickets con `"prioridad": None`, la recorrí con `for` y llené cada prioridad con `asignar_prioridad(ticket["descripcion"])`. La lista quedó cambiada: la variable del `for` es el mismo diccionario, no una copia → flujo del sistema en miniatura (entran sin prioridad, salen clasificados).
  - Tipos: escribí `"false"` (texto) en vez de `False` y `"3"` en vez de `3`; se ven parecidos pero `type()` y `== 3` muestran la diferencia. En la Fase 2, los CSV traen todo como texto → revisar tipos al limpiar.
  - Errores:
    - `KeyError: 'categoria'` → pedí una clave que no existe en ese diccionario.
    - Causa: llamé `tickets` al diccionario del ejercicio 1 (borrando la lista) y seguía usando `ticket`, que después del `for` conserva el **último** valor del bucle. Lo arreglé con un nombre propio.
    - Volví a dejar un `print` dentro del `for` por la sangría (se imprimía 5 veces).
  - `"La impresora no funciona"` salió baja → otra vez las reglas a mano se quedan cortas.
  - Avance: voy más rápido que el plan (5 sesiones en 6 días). Faltan ~2 sesiones de Fase 1: archivos y un repaso integrador.

- **2026-10-30 — Fase 1, sesión 6 (archivos):** creé `ejercicios/06_archivos.py`. Commit y push hechos (`91e9531`).
  - Entendí que las variables viven en la RAM y se pierden al cerrar el programa; para que sobrevivan hay que guardarlas en el disco.
  - Texto: `with open(...)`, modos `"w"` (borra y escribe), `"r"` (lee), `"a"` (agrega al final; al ejecutar 2 veces se duplicaron las líneas) y `encoding="utf-8"` para tildes. `"\n"` = salto de línea.
  - `FileNotFoundError: No such file or directory` → el modo `"r"` no crea archivos; lo interpreté solo.
  - JSON: `import json`, `json.dump(lista, archivo, indent=4, ensure_ascii=False)` para guardar y `json.load(archivo)` para cargar. `None` se guarda como `null`.
  - Error de lógica: clasifiqué los tickets cargados pero no volví a guardarlos → el archivo seguía con `null` (como editar en Word sin guardar). Lo arreglé con un segundo `json.dump` después del `for`.
  - Prueba de fuego: un archivo aparte que solo carga `tickets.json` mostró las prioridades → los datos sobrevivieron. Igual que en el proyecto: un programa entrena y guarda el modelo, y la API lo carga.
  - Los archivos se crean en la carpeta desde donde se ejecuta (raíz del proyecto): `tickets.json` y `tickets.txt` quedaron en la raíz.
  - Pendiente: `ejercicios/06_prueba` (sin `.py`) se subió por error; quiero borrarlo.
  - Para ver el contexto usado: `/context` en el chat, o la barra de estado ejecutando `claude` en la terminal.

- **2026-10-30 — Fase 1, sesión 7 (repaso integrador) → ✅ Fase 1 completada.** Commit y push hechos (`d49efaa`).
  - `import` de módulo propio: moví `asignar_prioridad` a `ejercicios/clasificador.py` (una sola copia) y la importo con `from clasificador import asignar_prioridad` (sin `.py`).
    - `ModuleNotFoundError: No module named 'clasificador'` → había llamado al archivo `07_clasificador.py`; un módulo importable no puede empezar con número.
    - Al importar, Python crea `__pycache__/` (ya excluido por `.gitignore`).
    - Por error escribí una versión distinta de la función (devolvía texto); la reemplacé por la real.
  - `input()`: el programa espera a que escriba y presione Enter; siempre devuelve **str**. Ctrl+C detiene un programa.
  - Las tuplas también se leen por posición (`resultado[0]`), pero llamar la función dos veces duplica el trabajo → mejor desempacar una vez.
  - `07_repaso.py`: carga `tickets.json` → clasifica → cuenta por prioridad → guarda `tickets_clasificados.json` (archivo nuevo, sin sobrescribir la entrada) → resumen. Es el flujo del sistema final en pequeño.
  - Error clave: olvidé `encoding="utf-8"` al abrir → "caído" llegó corrupto y se clasificó como baja, **sin dar error**. Lo descubrí comparando los números con lo esperado y con un `print` de depuración dentro del `for`.
  - Hábitos: avanzar paso a paso ejecutando en cada paso; `print` temporales para investigar y luego borrarlos.

## Próximo paso
**Fase 2, sesión 1: preparar el terreno para el modelo.**
- Para qué: el modelo aprenderá las reglas solo a partir de muchos tickets ya etiquetados, en vez de escribirlas a mano (las reglas fallaron con "crash", "no abre word", "la impresora no funciona").
- Decisiones pendientes: **dataset** (con etiquetas de categoría y prioridad) e **idioma** (español o inglés). Ver "Notas a tener presentes".
- Conceptos nuevos: **entorno virtual** (`venv`) para instalar librerías solo en este proyecto, `pip install`, y un archivo `requirements.txt`.
- Primer contacto con **pandas**: cargar un CSV y explorarlo (`head()`, `shape`, contar etiquetas).
- Crear las carpetas `data/` (y luego `notebooks/`, `models/`) cuando se usen.
- Terminar con `git add → commit → push`.

> Al terminar cada sesión, actualiza la bitácora y el "Próximo paso" de este archivo (pídeme permiso antes).
