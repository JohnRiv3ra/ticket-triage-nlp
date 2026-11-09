import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


vectorizador_cat, modelo_cat = joblib.load("models/modelo_categoria.pkl")

df = pd.read_csv("data/tickets_en.csv")
x = df["texto"]
y = df["queue"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)

print(x_test.shape)
x_test_tfidf = vectorizador_cat.transform(x_test)
probabilidades = modelo_cat.predict_proba(x_test_tfidf)
confianza = probabilidades.max(axis=1)
debajo = (confianza < 0.50).sum()
predicciones = modelo_cat.predict(x_test_tfidf)
arriba = confianza >= 0.50


print("Accuracy en todos:", accuracy_score(y_test, predicciones))
print("Accuracy solo arriba:", accuracy_score(y_test[arriba], predicciones[arriba]))

print("Van a revisión humana:", debajo, "de", len(confianza))
print(confianza[:10])
for umbral in [0.50, 0.60, 0.70, 0.80, 0.90]:
    arriba = confianza >= umbral
    porcentaje_humano = (confianza < umbral).mean()
    acierto = accuracy_score(y_test[arriba], predicciones[arriba])
    print(f"Umbral {umbral}: revisión humana {porcentaje_humano:.0%}, acierto del modelo {acierto:.2f}")

