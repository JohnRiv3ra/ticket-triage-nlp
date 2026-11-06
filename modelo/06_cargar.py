import joblib

vectorizador_cat, modelo_cat = joblib.load("models/modelo_categoria.pkl")
vectorizador_pri, modelo_pri = joblib.load("models/modelo_prioridad.pkl")

nuevo = ["My invoice shows a double charge and I need a refund"]
nuevo_tfidf_cat = vectorizador_cat.transform(nuevo)
nuevo_tfidf_pri = vectorizador_pri.transform(nuevo)

print("Categoría:", modelo_cat.predict(nuevo_tfidf_cat))
print("Prioridad:", modelo_pri.predict(nuevo_tfidf_pri))
