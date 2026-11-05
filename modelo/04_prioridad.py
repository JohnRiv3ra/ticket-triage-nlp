import pandas as pd 
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.svm import LinearSVC


df = pd.read_csv("data/tickets_en.csv")
X = df["texto"]
y = df["priority"]
print(y.value_counts())
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
vectorizador = TfidfVectorizer(ngram_range=(1, 2), stop_words="english")
X_train_tfidf = vectorizador.fit_transform(X_train)
X_test_tfidf = vectorizador.transform(X_test)

print(X_train_tfidf.shape, X_test_tfidf.shape)


#modelo = LinearSVC(class_weight="balanced")
modelo = LogisticRegression(max_iter=1000, class_weight="balanced", C=10)
modelo.fit(X_train_tfidf, y_train)
predicciones = modelo.predict(X_test_tfidf) 
accuracy = accuracy_score(y_test, predicciones)
print(f"Accuracy: {accuracy}")
print(classification_report(y_test, predicciones))
matriz = confusion_matrix(y_test, predicciones, labels=modelo.classes_)
tabla = pd.DataFrame(matriz, index=modelo.classes_, columns=modelo.classes_)
print(tabla)

