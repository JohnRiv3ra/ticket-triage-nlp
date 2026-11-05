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
- **Recuérdame siempre** ejecutar `pip freeze > requirements.txt` después de cada `pip install` (y revisar que la terminal muestre `(.venv)` antes de trabajar; si no, `.venv\Scripts\Activate.ps1`).

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
- **Idioma decidido (2026-10-30): empezar en inglés**, un solo idioma, hasta tener el primer modelo con métricas. Motivo: hay más datasets etiquetados con categoría y prioridad. Si al revisar datasets aparece uno bueno en español, se puede reconsiderar.
- Escribir el entrenamiento como una **receta reutilizable** (p. ej. `entrenar(ruta_csv)`): mismo código, distinto dataset → distinto modelo.

### 💡 Idea futura: sistema bilingüe (ES + EN) — para mejorar el GitHub
Cuando el modelo en inglés funcione, agregar español y **comparar con métricas**:
- **A. Un modelo mezclado:** entrenar una vez con ES + EN juntos (TF-IDF trata `"impresora"` y `"printer"` como palabras distintas). Riesgo: si un idioma domina, el otro se aprende mal.
- **B. Dos modelos + "portero":** detectar el idioma (o que el usuario lo elija en el formulario) y enviar el ticket al modelo de ese idioma.
- **C. Traducir todo a un idioma** (descartada por ahora: depende de un traductor externo).
- Condición obligatoria: **mismas etiquetas** en ambos datasets → hacer un **mapeo** (diccionario) de etiquetas.
- Resultado para el README: "probé un modelo mezclado contra dos modelos separados y estos fueron los resultados".

### 📌 Pendiente para la Fase 6 (pulido) — recordármelo
- **Sacar `CLAUDE.md` del repo público** (decidido 2026-11-02 dejarlo para el final): agregar `CLAUDE.md` al `.gitignore` → `git rm --cached CLAUDE.md` (**con** `--cached`, para no borrarlo del disco) → commit y push. Las versiones viejas quedan en el historial (aceptado).
- Escribir en el README una sección corta **"Qué aprendí construyendo este proyecto"** con lo mejor de la bitácora (versión pulida para reclutadores).
- Mencionar en el README que el dataset es sintético, su licencia CC-BY-NC-4.0 y cómo descargarlo.
- Extra opcional: comparar contra **DistilBERT/BETO entrenado en Google Colab (GPU)** y traer el `.pkl`/modelo con la misma versión de librerías.

## Hoja de ruta (aprox. 5 meses a 1 h/día)
| Fase | Duración | Contenido | Estado |
|---|---|---|---|
| 0. Entorno | 1 semana | Python, VS Code, Git, GitHub | ✅ Completada |
| 1. Python | 3 semanas | Variables, funciones, listas, diccionarios, archivos | ✅ Completada (7 sesiones, 2026-10-25 → 2026-10-30) |
| 2. El modelo | 4 semanas | pandas, limpieza de texto, TF-IDF, métricas (accuracy, F1, matriz de confusión) | 🔄 En curso |
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

- **2026-10-30 — Fase 2, sesión 1 (entorno para el modelo).** Commit y push hechos (`816d76d`).
  - Entorno virtual: `python -m venv .venv` y activarlo con `.venv\Scripts\Activate.ps1` → aparece `(.venv)`. Cada proyecto tiene su propio Python y sus librerías. `.venv` ya está en `.gitignore` (no se sube).
  - `pip install pandas` → pandas 3.1.0 (trae dependencias como `numpy`). El `ModuleNotFoundError` desapareció.
  - `pip freeze > requirements.txt`: la "lista de compras" del proyecto (`nombre==versión`); quien clone el repo usa `pip install -r requirements.txt`. `>` sobrescribe, como el modo `"w"`.
  - Pregunté qué significa "crash": un programa que se cierra de golpe por un error no manejado. En `04_listas.py` es solo texto de un ticket.
  - Decisión: **un solo idioma (inglés) primero**; el sistema bilingüe queda como idea futura (ver sección "Idea futura").

- **2026-10-30 — Fase 2, sesión 2 (dataset y primer contacto con pandas).** Commit y push hechos (`98d2091`).
  - Dataset elegido: **`Tobi-Bueck/customer-support-tickets`** (Hugging Face), archivo `aa_dataset-tickets-multi-lang-5-2-50-version.csv` → guardado como `data/tickets_raw.csv` ("raw" = original, no se toca).
    - Etiquetas: `queue` (10 categorías) y `priority` (high / medium / low). Texto: `subject` + `body`. También trae `type` (Incident, Request, Problem, Change).
    - Probablemente **sintético** (generado con IA) y licencia **CC-BY-NC-4.0** (citar al autor, sin uso comercial) → decirlo en el README.
  - `data/` agregado al `.gitignore`: los datos no se suben; en el README se explicará cómo descargarlos.
  - Script `modelo/01_explorar.py`: `import pandas as pd`, `pd.read_csv()`, `df.shape`, `df.columns`, `df.head(10)` y `df["columna"].value_counts()` (= mis 4 contadores en una línea). `shape`/`columns` sin paréntesis (datos), `head()` con paréntesis (acción).
  - Hallazgos: **28.587 tickets** (16 columnas): **16.338 en inglés**, 12.249 en alemán. Categorías **muy desbalanceadas** (Technical Support 8.362 vs. General Inquiry 405) → mirar **F1 por clase**, no solo accuracy. Prioridad: `low` tiene la mitad que las otras. `subject` vacío en 3.838 tickets; `body` siempre lleno → el modelo leerá sobre todo `body` (más palabras = más pistas).
  - Revisión de viabilidad (inglés): 0 `body` duplicados, mediana de 55 palabras por ticket y la prioridad se relaciona con la categoría con sentido (Service Outages → 70 % high) → las etiquetas no son aleatorias.
  - `NaN` = "no hay dato" (como `None`). `...` en la tabla = pandas esconde columnas. `Kl�rung` = la terminal muestra mal la letra; el archivo está bien.
  - Errores:
    - Creé la carpeta como `models/` y ejecuté `modelo/...` → `[Errno 2] No such file or directory`. Renombrada a `modelo/` (código); `models/` queda reservada para los `.pkl`.
    - La ruta del error mostraba `...\Python311\python.exe` → el **`.venv` no estaba activo** (pandas no se habría encontrado). Lección: leer **todo** el mensaje, no solo la última línea.
    - Conté `priority` dos veces y faltó `queue`; puse un `#print(...)` nuevo en vez de comentar la línea original. `Ctrl + }` comenta/descomenta.
  - Aparte: subí la limpieza de `07_repaso.py` (`e58638c`).

- **2026-10-30 — Fase 2, sesión 3 (filtrar inglés y guardar CSV limpio).** Script `modelo/02_filtrar.py`.
  - **Máscara booleana:** `df["language"] == "en"` compara todas las filas a la vez → columna de `True`/`False` (`dtype: bool`); `df[mascara]` deja solo las filas `True`. Equivale a un `for` + `if` + `.append()` en una línea.
  - **Elegir varias columnas:** `df[["subject", "body", "queue", "priority"]]` → corchete de afuera = "elige de la tabla", de adentro = la **lista** de nombres.
  - Transformación: `(28587, 16)` → filtro de filas → `(16338, 16)` → filtro de columnas → `(16338, 4)`. 16.338 coincide con `value_counts()` → el filtro está bien.
  - `df_en.to_csv("data/tickets_en.csv", index=False)` (como `json.dump`) + prueba de fuego cargándolo de nuevo. Probé quitar `index=False` → aparece una columna extra con los números de fila (el **índice**).
  - **`_raw` = "crudo"** (ingredientes sin cocinar): el original nunca se modifica; la receta (`02_filtrar.py`) crea un archivo nuevo. Si me equivoco, corrijo la receta y la vuelvo a ejecutar. `tickets_raw.csv` 26 MB → `tickets_en.csv` 7 MB.
  - Errores:
    - Creé el script dentro de `ejercicios/modelo/` por error; arrastrarlo en VS Code no funcionó. Lo moví con `Move-Item origen destino` y borré la carpeta con `Remove-Item`. Lección: si el explorador confunde, `ls` en la terminal dice la verdad.
    - Escribí `columnas = df_en[[...]]` (la tabla ya recortada) y luego `df_en[columnas]` → `TypeError: Boolean array expected for the condition, not object`: pandas creyó que era una máscara. Arreglo: `columnas` debe ser solo la lista de nombres. Una línea sin `=` (`df_en[columnas]`) no guarda nada.
    - Los traceback de pandas muestran archivos internos (`generic.py`); lo importante es la última línea y la línea de **mi** código.

- **2026-10-30 — Fase 2, sesión 4 (columna `texto` y limpieza).** Commit y push hechos (`5735a83`). En `modelo/02_filtrar.py`.
  - Crear columna: `df_en["texto"] = df_en["subject"] + " " + df_en["body"]` (como agregar una clave a un diccionario, pero para todas las filas). El `" "` evita `"PrinterDear"`.
  - **El `NaN` contamina:** `NaN + " " + body` → `NaN`. Medí con `.isna().sum()` → **2.607** textos vacíos **sin error**. Arreglo: `.fillna("")` → **0**. Por mi cuenta también puse `fillna` en `body` (programación defensiva).
  - 2.607 ≠ 3.838 porque 3.838 era del dataset completo (EN + DE); un número depende de **sobre qué tabla** se calcula.
  - `.iloc[0]` = fila por posición (como `lista[0]`); `head()` corta los textos largos.
  - Los `\n` del dataset son **literales** (barra + `n`, no saltos de línea) → TF-IDF crearía "palabras" basura como `nI`, `nCould`. Limpieza: `.str.replace("\\n", " ", regex=False)` (`"\\"` = una barra real) y `.str.strip()` (espacios al inicio/final). `.str` aplica métodos de texto a toda la columna.
  - Verificado en todo el dataset: 0 barras, 0 espacios al inicio, 0 vacíos. Los dobles espacios no importan a TF-IDF → no toda limpieza hace falta.
  - "Dear Customer Support Team" se repite en casi todos → no ayuda a distinguir; TF-IDF le da poco peso (la "IDF").
  - Limpieza final del script: borré los `print` de investigación (máscara, `iloc`, `isna`) y dejé los `shape`. Regla: si la línea cambia/guarda datos se queda; si solo mostraba algo para investigar, se borra. No supe cuáles borrar al principio → pedir los números de línea.
  - **Me costó entender la limpieza** → pedí más práctica antes de seguir.

- **2026-10-31 — Fase 2, sesión 5 (práctica de limpieza con dataset de juguete).** Commit y push hechos (`34be343`). Archivo `ejercicios/08_limpieza.py`.
  - `pd.DataFrame(lista_de_diccionarios)`: cada diccionario → fila, cada clave → columna. `None` → `NaN`.
  - Con 6–8 tickets **vi cada paso** en vez de solo números.
  - Etiquetas: `value_counts()` mostró 5 categorías en vez de 3 (`"Hardware"`, `"hardware "`, `"Access"`…). Arreglo **encadenando**: `.str.lower().str.strip()` (se lee de izquierda a derecha). El espacio de `"hardware "` es **invisible** en la tabla.
  - Índice tras filtrar: `0, 1, 2, 4, 5` (las filas conservan su etiqueta) → `.iloc` usa la **posición**, no el índice.
  - Vi las filas 1 y 5 con `texto` = `NaN` sin `fillna`; con `fillna("")` quedaba `" I cannot log in"`. **Truco de los corchetes** `print("[" + texto + "]")` para ver espacios invisibles. Mi predicción falló (creía que no habría espacio) → las predicciones sirven para descubrir.
  - `.strip()` solo quita espacios de los **bordes**, no del medio (no importa para TF-IDF).
  - **Duplicados:** `df.duplicated()` (máscara; marca solo las copias, no el original), `.sum()` para contarlos y `df = df.drop_duplicates()`. Un "casi gemelo" (`"access "` vs `"Access"`) **no** se detecta si se quitan duplicados antes de normalizar → `value_counts()` mostraba `access` dos veces (pista del espacio invisible).
  - `shape` de una columna = `(7,)` (una dimensión); de una tabla = `(filas, columnas)`.
  - Errores (ninguno dio mensaje de error):
    - Volví a crear `df_en = df[mascara]` después de agregar `texto` → la columna desaparecía (como en la sesión 5).
    - Limpié `df["categoria"]` **después** de copiar `df_en` → la copia seguía sucia.
    - Usé `regex=True` → `"\\n"` se interpreta como salto de línea real y no reemplaza nada.
    - Al copiar de `02_filtrar.py` hay que cambiar los nombres de columnas (si no, `KeyError`).
  - **Gran lección: el orden de la receta importa** → normalizar → quitar duplicados → filtrar → unir con `fillna` → limpiar texto. Medir (`value_counts`, `shape`, `.sum()`) y mirar (tabla, corchetes) en cada paso.
  - Pendiente: `modelo/02_filtrar.py` no quita duplicados (el dataset real tiene 0, pero se podría agregar por buena práctica).

- **2026-11-02 — Fase 2, sesión 6 (TF-IDF con textos de juguete).** Commit y push hechos (`c3ea114`). Archivo `ejercicios/09_tfidf.py`.
  - `pip install scikit-learn` → **1.9.1** (trae `scipy` y `joblib`; `joblib` servirá para guardar el modelo `.pkl`) + `pip freeze > requirements.txt`. Se instala como `scikit-learn`, se importa como `sklearn`.
  - Para qué: el modelo es una calculadora y no sabe leer → TF-IDF traduce cada texto a una **fila de números**. Analogía: hoja de cuadros (columnas = palabras del vocabulario, filas = tickets, número = importancia; 0 = no aparece).
  - **TF** = cuántas veces está la palabra en el ticket; **IDF** = qué tan rara es en todos los tickets (las comunes pesan poco).
  - Código: `from sklearn.feature_extraction.text import TfidfVectorizer`; `vectorizador = TfidfVectorizer()` (traductor vacío); `matriz = vectorizador.fit_transform(textos)` (**fit** = aprende el vocabulario, **transform** = llena los números); `get_feature_names_out()` (vocabulario); `matriz.shape` → `(4, 11)`. Para verla: `pd.DataFrame(matriz.toarray(), columns=...).round(2)`.
  - Vocabulario: en **minúsculas**, orden **alfabético**, sin repetidas, e **ignora palabras de 1 letra** (`"I"`).
  - Los números de una fila son relativos entre sí ("pastel" del mismo tamaño por ticket): `password` vale 0.53 en un ticket y 0.49 en otro.
  - Experimento: agregué `"The printer is broken again"` → en la fila 1 `broken` bajó (0.59 → 0.54, ahora está en 2 tickets) y `my` **subió** (0.47 → 0.54) sin cambiar su ticket → el peso depende de **todos** los tickets juntos (por eso es `fit`). `shape` → `(5, 12)` por `again`.
  - Me costó entender el código al principio → se explicó línea por línea con la analogía antes de seguir. Lo que dice la ejecución vale más que una tabla copiada a mano (el tutor copió mal un número).
  - Error: creé el archivo en `ejercicios/ejercicios/` (otra vez carpeta anidada) → `Move-Item` + `Remove-Item`. Truco: hacer clic en la carpeta correcta antes de crear el archivo.

- **2026-11-02 — Fase 2, sesión 7 (TF-IDF real + entrenamiento/prueba).** Commit y push hechos (`f5a7a4a`). Archivo `modelo/03_entrenar.py`.
  - TF-IDF con todos los tickets en inglés: `(16338, 5073)` → vocabulario de solo **5.073 palabras** (pocas para 16 mil textos; probablemente porque el dataset es sintético → dato para el README). La matriz es **dispersa** (guarda solo los no-ceros); no usar `toarray()` con datos reales (~83 millones de casillas).
  - **`X`** = lo que el modelo lee (`df["texto"]`); **`y`** = lo que adivina (`df["queue"]` = categoría; `priority` vendrá después). `queue` ("cola") es como el dataset llama a la categoría.
  - `train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)` → devuelve 4 cosas (desempacar en orden: `X_train, X_test, y_train, y_test`). `random_state` = azar repetible; `stratify=y` = misma proporción de categorías en ambos lados (clave por el desbalance).
  - Resultado: `(13070,)` entrenamiento y `(3268,)` prueba. Predije 3.276: el razonamiento estaba bien, pero me equivoqué en la cuenta (16338 × 0.2 = 3267.6 → se redondea hacia arriba a 3.268). Una sola columna → `shape` de una dimensión.
  - **Fuga de datos (data leakage):** hacer el `fit` con todos los tickets deja que el modelo "vea el examen" → métricas infladas **sin error**. Correcto: `fit_transform(X_train)` y solo `transform(X_test)` → `(13070, 4911)` y `(3268, 4911)`. Las 162 palabras que faltan solo aparecen en prueba. Mismas columnas en ambos lados (obligatorio). En la API también se usará solo `transform`.
  - Errores:
    - `FileNotFoundError` por escribir `data/tickets.csv` en vez de `tickets_en.csv`. Esta vez la ruta del error mostraba `.venv` → entorno activo ✔️.
    - `NameError: name 'X' is not defined` → usé `X` y `y` sin crearlos antes.
    - Escribí `y = df["texto"]` (copiando la línea de `X`) → la "respuesta" era la misma pregunta. Me confundió que la categoría se llame `queue` y no `categoria`.
    - `print(matriz.shape)` quedó fuera del comentario `""" """` → `NameError`, porque `matriz` se creaba dentro del comentario.
  - Idea: entrenar en **Google Colab** y traer el `.pkl` con `joblib` se puede (ojo: misma versión de scikit-learn). Para TF-IDF + LR no hace falta (entrena en segundos aquí); tiene sentido para **BETO/DistilBERT** (GPU) en la Fase 6. A los reclutadores les importa la reproducibilidad y el criterio para elegir la herramienta, no Colab por sí solo.

- **2026-11-03 — Fase 2, sesión 8 (primer modelo: Regresión Logística para la categoría).** Commit y push hechos (`f4c7b4d`). En `modelo/03_entrenar.py`.
  - `LogisticRegression(max_iter=1000)` = el "estudiante" vacío; `modelo.fit(X_train_tfidf, y_train)` estudia (recibe preguntas **y** respuestas); `modelo.predict(X_test_tfidf)` hace el examen (solo preguntas). `max_iter` = vueltas de estudio máximas.
  - **Accuracy** = aciertos / total (`accuracy_score(y_test, predicciones)`, primero las correctas). Primer resultado: **0.47**.
  - **Línea base** = el "modelo flojo" que siempre responde la categoría más común: Technical Support = **29 %** de los tickets en inglés. El tutor dijo primero 51 % por usar el conteo del dataset completo (EN + DE) → otra vez: un número depende de sobre qué tabla se calcula. 47 % > 29 % → el modelo sí aprendió, pero todavía es bajo.
  - Predije "más del 60 %" porque los 10 primeros tickets dieron 6/10 → con 3.268 salió 47 %. Una muestra pequeña engaña.
  - **`classification_report`** (nota por categoría): `support` = cuántos hay en el examen; **precision** = cuando dice X, ¿acierta?; **recall** = de los X reales, ¿cuántos encontró?; **F1** = combina ambas. `macro avg` = todas las categorías valen igual (el número honesto para el README); `weighted avg` = pesan las grandes.
  - Hallazgos: General Inquiry precision 1.00 pero recall 0.02 (encontró 1 de 47); todas las categorías pequeñas con recall muy bajo. Technical Support recall 0.73 / precision 0.45 → el modelo la usa "por si acaso". Billing es la mejor (F1 0.76: vocabulario propio como *invoice*, *refund*). Customer Service, IT Support y Product Support entre las peores → hipótesis: se confunden entre sí (falta comprobarlo con la matriz de confusión).
  - Experimento **`class_weight="balanced"`** (los errores en categorías pequeñas cuentan más). Predije: recall de GI sube ✅, precision de GI baja ✅, accuracy sube ❌. Resultado: accuracy 0.47 → **0.43**, macro F1 0.37 → **0.42**, ninguna categoría con F1 < 0.25 (antes 4). La accuracy bajó porque Technical Support perdió ~350 aciertos (recall 0.73 → 0.36) y la accuracy cuenta tickets, no categorías.
  - **Trade-off precision/recall:** si el modelo se "atreve" más con una categoría, encuentra más pero se equivoca más al usarla.
  - **Decisión: me quedo con `class_weight="balanced"`** (mejor macro F1; más justo con categorías como Human Resources). Para el README: "subí el macro F1 de 0.37 a 0.42 a cambio de 4 puntos de accuracy, y por qué".

- **2026-11-04 — Fase 2, sesión 9 (matriz de confusión).** Commit y push hechos (`7a49af2`). En `modelo/03_entrenar.py`.
  - Para qué: el `classification_report` da la **nota** de cada categoría; la matriz dice **con quién** se confunde.
  - Código: `confusion_matrix(y_test, predicciones, labels=modelo.classes_)` (primero las correctas, como en `accuracy_score`) → `pd.DataFrame(matriz, index=modelo.classes_, columns=modelo.classes_)` para ponerle nombres. `modelo.classes_` = las categorías que aprendió, en orden alfabético.
  - Leerla: **filas = lo que era de verdad**, **columnas = lo que dijo el modelo**, **diagonal = aciertos**, fuera de la diagonal = errores.
  - `[10 rows x 10 columns]` no era un error: pandas escondió columnas. Arreglo arriba del script: `pd.set_option("display.max_columns", None)` y `pd.set_option("display.width", None)` (configuración → antes de cualquier `print`).
  - La tabla "cuadra": la suma de la fila Billing = 319 = su `support`. **Recall = diagonal ÷ total de la fila** (232/319 = 0.73); **precision = diagonal ÷ total de la columna** (232/297 = 0.78) → el `classification_report` sale de esta tabla.
  - Predicciones: fila más limpia **Billing** ✅ (limpia en fila y en columna; Service Outages tiene más recall pero su columna recibe muchos ajenos). Par más confundido **General Inquiry ↔ Human Resources** ❌ (3 y 0) → dos categorías pequeñas no tienen por qué parecerse; importa si usan las **mismas palabras**.
  - **Hipótesis de la sesión 8 confirmada:** Technical, IT, Product Support y Customer Service forman un "grupo de confusión". Mayores errores: Technical → IT **156**, Technical → Product **125**, Product → Technical **119**, Technical → Customer Service **91**.
  - Technical ↔ Product es casi simétrico (125 / 119) → vocabulario casi igual; como el dataset es sintético, las etiquetas podrían ser ambiguas incluso para un humano (límite del modelo; dato para el README). Technical → IT (156) vs. IT → Technical (65) no es simétrico, en parte porque Technical es mucho más grande.
  - Fue un día difícil (se cayeron dos oportunidades de trabajo) y me costó concentrarme; hice la sesión por disciplina y dejé el mini-ejercicio para la próxima. Voy a releer esta sesión con calma.

- **2026-11-04 — Fase 2, sesión 10 (repaso de la matriz + bigramas).** Commit y push hechos (`a201c0c`). En `modelo/03_entrenar.py`.
  - Volví con ánimo. Pregunté qué puestos buscar: lo más alcanzable hoy es **Soporte / Help Desk** (conozco el problema que resuelve mi proyecto) y **Data Analyst junior** (en paralelo); **QA** como puerta a desarrollo; **Backend junior** después de la Fase 3; **trainee de ML/IA** como meta de mediano plazo. No hace falta terminar el proyecto para postular. Pendiente: decirle al tutor mi país y mi trabajo actual para afinar las recomendaciones y el LinkedIn.
  - Mini-ejercicio de la columna `General Inquiry`: la mayoría de los errores vienen de **Technical Support** (39) ✅, porque es la más grande y tiene más tickets para "regalar". Calculé la **precision a mano**: 28 ÷ 170 = **0.16** ✅ (igual al reporte).
  - Me confundí: dije que GI se predice mucho "porque tiene más tickets", pero es la que tiene **menos**. La causa real es **`class_weight="balanced"`**: cada ticket de GI pesa ~7 y uno de Technical ~0.35 → fallar un GI "duele" ~20 veces más → el modelo **se atreve** a decir GI cuando duda (recall 0.02 → 0.60, precision 0.16).
  - **Bigramas:** `TfidfVectorizer(ngram_range=(1, 2))` = palabras sueltas (unigramas) **más pares** de palabras (bigramas), como `"password reset"`. Un par dice más que cada palabra por separado.
  - Predije que el vocabulario sería "el doble, ~10 mil" ❌ → salió **4.911 → 81.602** (×16): cada palabra va seguida de muchas palabras distintas, así que los pares crecen multiplicando, no sumando (~76.700 bigramas).
  - No predije la dirección del macro F1 ("no me acuerdo") → lección: aunque no recuerde el número, **apostar por una dirección** (sube / baja / igual).
  - Resultado: accuracy 0.43 → **0.53**, **macro F1 0.42 → 0.55**. **Sin trade-off** (subieron ambas). Las 4 del grupo de confusión mejoraron (Technical 0.44 → 0.56, IT 0.36 → 0.46, Product 0.36 → 0.48, Customer Service 0.38 → 0.46), pero siguen entre las más bajas. GI: precision 0.16 → 0.48; HR: F1 0.32 → 0.59.
  - Matriz, fila Technical: predije que bajarían los tres cruces ✅ → IT 156 → 127, Product 125 → 119, Customer Service 91 → 86; aciertos de Technical **341 → 491** (+150). Gran parte vino de la columna GI (39 → 9): los bigramas le quitaron la costumbre de decir GI "por si acaso".
  - **Technical ↔ Product casi no mejoró** (125 → 119) y Product → Technical **subió** (119 → 132): sigue siendo el par más confundido → refuerza la idea de que en este dataset (sintético) comparten casi el mismo vocabulario; el límite podría estar **en los datos**, no en el modelo.
  - Lección: una métrica general (macro F1) puede esconder un problema concreto que solo se ve en la matriz.
  - Frase para el README: "La matriz de confusión mostró que 4 categorías de soporte se confundían entre sí. Agregué bigramas (`ngram_range=(1, 2)`) para capturar frases como 'password reset', y el macro F1 subió de 0.42 a 0.55." → orden **diagnóstico → hipótesis → cambio → medición**.

- **2026-11-04 — Fase 2, sesión 11 (stop words).** Commit y push hechos (`4d56943`). En `modelo/03_entrenar.py`.
  - Le dije al tutor que soy de **Durán, Ecuador** (junto a Guayaquil). Dónde buscar: LinkedIn, Multitrabajos, Computrabajo y **pasantías preprofesionales** de la universidad. Empresas de Guayaquil (bancos, retail, telecom, puertos, logística) tienen mesa de ayuda y datos; remoto depende del inglés. Como en Ecuador los tickets llegan **en español**, el **sistema bilingüe** gana valor para reclutadores locales. Pendiente: decirle mi trabajo actual y mi nivel de inglés.
  - **Stop words** = palabras que aparecen en casi todo y no dicen de qué trata el ticket (`the`, `is`, `my`, `not`…). `TfidfVectorizer(ngram_range=(1, 2), stop_words="english")` las borra antes de armar el vocabulario (varias opciones separadas por **coma**). Regla del experimento: **un cambio a la vez**.
  - Duda previa: podía empeorar, porque al borrar `not` desaparece el par `"not working"`, y la IDF ya le baja el peso a las palabras comunes.
  - Predicciones: macro F1 sube ✅; columnas bajan ❌ → **subieron** de 81.602 a **93.859**. Al borrar las palabras vacías, las palabras con significado **quedan pegadas** y forman pares nuevos y más variados (`"my printer is broken"` → `"printer broken"`). Las palabras sueltas bajaron (~300), pero los pares nuevos fueron muchos más.
  - Resultado: accuracy 0.53 → **0.56**, **macro F1 0.55 → 0.58**. General Inquiry F1 0.55 → 0.67; Billing 0.76 → 0.79.
  - **Advertencia:** una mejora pequeña (+3) puede deberse en parte al sorteo de `train_test_split` (otro examen podría dar 0.57 o 0.59). Para medirlo mejor existe la **validación cruzada** (más adelante). +3 alcanza para quedarnos con el cambio.
  - **Decisión: me quedo con `stop_words="english"`.**
  - Resumen de experimentos (para el README):

    | Versión | Accuracy | Macro F1 |
    |---|---|---|
    | LR básica | 0.47 | 0.37 |
    | + `class_weight="balanced"` | 0.43 | 0.42 |
    | + bigramas `ngram_range=(1, 2)` | 0.53 | 0.55 |
    | + `stop_words="english"` | 0.56 | **0.58** |

## Próximo paso
**Fase 2, sesión 12: cambiar el "estudiante" — SVM con `LinearSVC`.**
- Comparar siempre contra el **macro F1 actual: 0.58** (bigramas + stop words + `balanced`) y mirar en la matriz el par **Technical ↔ Product**.
- Probar **un cambio a la vez**: `from sklearn.svm import LinearSVC` en lugar de `LogisticRegression` (mismo TF-IDF; mantener `class_weight="balanced"`).
- Más adelante: **validación cruzada** para saber si las mejoras pequeñas son reales.
- Seguir la tabla de experimentos de la sesión 11 (para el README).
- Después: el mismo proceso para la **prioridad** (`y = df["priority"]`), y convertir el script en la receta reutilizable `entrenar(ruta_csv)`.
- Predecir antes de ejecutar (aunque sea solo la dirección).
- Recordar: `(.venv)` activo y `pip freeze > requirements.txt` si se instala algo.
- Terminar con `git add → commit → push`.

> Al terminar cada sesión, actualiza la bitácora y el "Próximo paso" de este archivo (pídeme permiso antes).
