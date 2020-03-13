import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns; sns.set()

# Lê e formata os dados
df = pd.read_csv("data/ministerio_saude.csv", sep=";")
df.data = pd.to_datetime(df.data, format="%d/%m/%Y")

# Monta o gráfico
figure, ax = plt.subplots(figsize=(11, 8))
plot = sns.lineplot(data=df, x="data", y="qtde_confirmados", markers=True, dashes=False, ax=ax)
figure.autofmt_xdate()

# Salva o gráfico
figure.savefig("casos_confirmados.png")
