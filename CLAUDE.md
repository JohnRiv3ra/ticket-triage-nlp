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
| 1. Python | 3 semanas | Variables, funciones, listas, diccionarios, archivos | 🔄 En curso |
| 2. El modelo | 4 semanas | pandas, limpieza de texto, TF-IDF, métricas (accuracy, F1, matriz de confusión) | ⏳ |
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

## Próximo paso
**Fase 1, sesión 3: funciones (`def`, parámetros, `return`).**
- Para qué: no tener que editar el código para probar cada descripción; escribir la lógica una vez y reutilizarla. La API (Fase 3) llamará a una función parecida.
- Idea de ejercicio: convertir el clasificador de la sesión 2 en `asignar_prioridad(descripcion)` que **devuelva** la prioridad, y probarla con varios tickets.
- Archivo sugerido: `ejercicios/03_funciones.py`.
- Terminar con `git add → commit → push`.

> Al terminar cada sesión, actualiza la bitácora y el "Próximo paso" de este archivo (pídeme permiso antes).
