import statistics
import pandas as pd
df=pd.read_csv("SOCR-HeightWeight.csv")
weight=df["Weight"].tolist()
weight_=statistics.median(weight)
weight_1=statistics.mode(weight)
weight_2=statistics.mean(weight)
print(weight_,weight_1,weight_2)
