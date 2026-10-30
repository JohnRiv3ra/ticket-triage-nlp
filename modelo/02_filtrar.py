import pandas as pd

df = pd.read_csv("data/tickets_raw.csv")

mascara = df["language"] == "en"
print(mascara.head(10))

df_en = df[mascara]
print(df.shape)
print(df_en.shape)

df_en = df_en[["subject", "queue", "priority", "body"]]
print(df_en.shape)

df_en.to_csv("data/tickets_en.csv", index=False)
df_prueba = pd.read_csv("data/tickets_en.csv")
print(df_prueba.shape)

