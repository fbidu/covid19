import pandas as pd
import seaborn as sns; sns.set()

# Lê e formata os dados
df = pd.read_csv("data/ministerio_saude.csv", sep=";")
df.data = pd.to_datetime(df.data, format="%d/%m/%Y")

# Monta o gráfico
plot = sns.lineplot(data=df, x="data", y="qtde_confirmados", markers=True, dashes=False)

# Salva o gráfico
figure = plot.get_figure()
figure.savefig("casos_confirmados.png")
