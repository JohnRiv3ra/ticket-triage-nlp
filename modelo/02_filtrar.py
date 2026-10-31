import pandas as pd

df = pd.read_csv("data/tickets_raw.csv")

mascara = df["language"] == "en"


df_en = df[mascara]
print(df.shape)
print(df_en.shape)

df_en = df_en[["subject", "queue", "priority", "body"]]
print(df_en.shape)

df_en["texto"] = df_en["subject"].fillna("") + " " + df_en["body"].fillna("")
df_en["texto"] = df_en["texto"].str.replace("\\n", " ", regex=False)
df_en["texto"] = df_en["texto"].str.strip()



df_en.to_csv("data/tickets_en.csv", index=False)
df_prueba = pd.read_csv("data/tickets_en.csv")
print(df_prueba.shape)

