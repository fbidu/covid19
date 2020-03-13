import pandas as pd
import seaborn as sns

sns.set()

df = pd.read_csv("data/ministerio_saude.csv", sep=";")
df.data = pd.to_datetime(df.data)
sns.lineplot(data=df, x="data", y="qtde_confirmados", markers=True, dashes=False)
