import pandas as pd

df = pd.read_csv("data/tickets_en.csv")
df["palabras"] = df["texto"].str.split().str.len()

print(df["palabras"].describe())

cortos = df[df["palabras"] < 10]
print("Tickets con menos de 10 palabras:", len(cortos))
#print(cortos[["palabras", "texto", "queue"]])

for n in [3, 5, 8, 10, 15, 20, 30]:
    porcentaje = (df["palabras"] < n).mean()
    print(f"Menos de {n} palabras: {porcentaje:.1%}")
