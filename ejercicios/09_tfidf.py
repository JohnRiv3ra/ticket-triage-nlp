import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

textos = [
    "The printer is not working",
    "My printer is broken",
    "I forgot my password",
    "Password reset please",
    "The printer is broken again"
]

vectorizador = TfidfVectorizer()
matriz = vectorizador.fit_transform(textos)

print(vectorizador.get_feature_names_out())
print(matriz.shape)

tabla = pd.DataFrame(matriz.toarray(), columns=vectorizador.get_feature_names_out())
print(tabla.round(2))
