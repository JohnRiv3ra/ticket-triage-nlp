import pandas as pd

tickets = [
    {"asunto": "Printer broken", "cuerpo": "The printer\\nis not working", "categoria": "Hardware", "idioma": "en"},
    {"asunto": None, "cuerpo": "I cannot log in", "categoria": "access", "idioma": "en"},
    {"asunto": "Laptop slow", "cuerpo": "  My laptop is very slow  ", "categoria": "hardware ", "idioma": "en"},
    {"asunto": "Drucker kaputt", "cuerpo": "Der Drucker geht nicht", "categoria": "Hardware", "idioma": "de"},
    {"asunto": "Password reset", "cuerpo": "I forgot my password", "categoria": "Access", "idioma": "en"},
    {"asunto": None, "cuerpo": "Email\\nnot syncing", "categoria": "Software", "idioma": "en"},
    {"asunto": "Password reset", "cuerpo": "I forgot my password", "categoria": "access ", "idioma": "en"},
    {"asunto": "Password reset", "cuerpo": "I forgot my password", "categoria": "Access", "idioma": "en"}
]


df = pd.DataFrame(tickets)
print(df.duplicated())
print(df.duplicated().sum())
print(df["categoria"].value_counts()) 
df["categoria"] = df["categoria"].str.lower().str.strip()
df = df.drop_duplicates()
print(df.shape)
print(df["categoria"].value_counts()) 
mascara = df["idioma"] == "en"
df_en = df[mascara]
df_en["texto"] = df_en["asunto"].fillna("") + " " + df_en["cuerpo"].fillna("")
df_en["texto"] = df_en["texto"].str.replace("\\n", " ", regex=False)
df_en["texto"] = df_en["texto"].str.strip()
print("[" + df_en["texto"].iloc[1] + "]")
print(df_en)
print(df_en.shape)
print(df_en["categoria"].value_counts())
  
