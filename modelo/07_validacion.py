import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

df = pd.read_csv("data/tickets_en.csv")
x = df["texto"]
y = df["queue"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)

receta = make_pipeline(
    TfidfVectorizer(ngram_range=(1, 2), stop_words="english"),
    LogisticRegression(max_iter=1000, class_weight="balanced", C=10)
)
print("Entrenando 5 rondas... (puede tardar unos minutos)")
notas = cross_val_score(receta, x_train, y_train, cv=5, scoring="f1_macro", n_jobs=-1)

print("Las 5 notas:", notas.round(3))
print("Promedio:", notas.mean().round(3))
print("Variación (std):", notas.std().round(3))
