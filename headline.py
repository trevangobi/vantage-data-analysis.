import main
import pandas as pd
headline = main.headline
#Get the columns in Headline table
df = pd.DataFrame(headline)
print("Headline Columns:")
print(df.columns.tolist())
#Get the number of news source we have.
print("NO OF SOURCES: ", headline["source"].nunique())
print("SOURCES ARE:\n")
unique_list = df["source"].unique().tolist()
print(unique_list)
#Number of News per Source
print("News feed per source:\n")
item_counts = df["source"].value_counts()
print(item_counts)
#Bar chart of News feeds.
import matplotlib.pyplot as plt
df["source"].value_counts().plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("News frequency counts")
plt.xlabel("source")
plt.ylabel("count")
plt.tight_layout()
plt.show()