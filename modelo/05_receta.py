import pandas as pd
import joblib
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

def entrenar(ruta_csv, columna_y):
    df = pd.read_csv(ruta_csv)
    x = df["texto"]
    y = df[columna_y]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)
    vectorizador = TfidfVectorizer(ngram_range=(1, 2), stop_words="english")
    X_train_tfidf = vectorizador.fit_transform(x_train)
    X_test_tfidf = vectorizador.transform(x_test)
    modelo = LogisticRegression(max_iter=1000, class_weight="balanced", C=100)
    modelo.fit(X_train_tfidf, y_train)
    predicciones = modelo.predict(X_test_tfidf)
    print(f"---Modelo para {columna_y}: ---")
    print(classification_report(y_test, predicciones))
    return vectorizador, modelo

vectorizador_cat, modelo_cat = entrenar("data/tickets_en.csv", "queue")
vectorizador_pri, modelo_pri = entrenar("data/tickets_en.csv", "priority")

joblib.dump((vectorizador_cat, modelo_cat), "models/modelo_categoria.pkl")
joblib.dump((vectorizador_pri, modelo_pri), "models/modelo_prioridad.pkl")
print("Modelos guardados")


    # 1. leer el CSV usando ruta_csv (no una ruta escrita a mano)
    # 2. X = la columna "texto"
    # 3. y = la columna que llega en columna_y  (¡sin comillas! es una variable)
    # 4. train_test_split (igual que antes)
    # 5. vectorizador: fit_transform en train, solo transform en test
    # 6. modelo LR con C=10: fit y predict
    # 7. imprimir el classification_report

