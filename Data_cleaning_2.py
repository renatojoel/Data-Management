
#pip install matplotlib

import preprocessor as p
import pandas as pd
import json
from nltk.tokenize import word_tokenize
import re

df = pd.read_json('Debt.json', encoding='utf-8')

# 1) Criar clean_text inicial (remover URLs, mentions, emojis, etc.)
p.set_options(p.OPT.URL, p.OPT.MENTION, p.OPT.EMOJI, p.OPT.RESERVED)
df["clean_text"] = df["text"].apply(lambda x: p.clean(x).lower())

# 2) Tokenizar
df["tokens"] = df["clean_text"].apply(word_tokenize)


# 3) Remover ruído

noise_words = [ "china", "usa", "france", "canada", "india", "trump", "biden", "macron", "modi","amp", "like", "shows", "types", "data", "world"]

def remove_noise(tokens):
    cleaned = []
    for w in tokens:
        w = w.lower()
        if len(w) < 3:
            continue
        if w.isnumeric():
            continue
        if w in noise_words:
            continue
        cleaned.append(w)
    return cleaned


df["clean_tokens"] = df["tokens"].apply(remove_noise)

# 4) Criar clean_text final para LDA
df["clean_text"] = df["clean_tokens"].apply(lambda x: " ".join(x))



from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(
    stop_words='english',
    min_df=5,          # ignora palavras raras
    max_df=0.8,        # ignora palavras demasiado comuns
)

X = vectorizer.fit_transform(df["clean_text"])
terms = vectorizer.get_feature_names_out()


from sklearn.decomposition import LatentDirichletAllocation

lda = LatentDirichletAllocation(
    n_components=2,
    random_state=42,
    learning_method='batch'
)

lda.fit(X)


num_words = 10

# for idx, topic in enumerate(lda.components_):
#     print(f"\nTópico {idx+1}:")
#     top_indices = topic.argsort()[-num_words:]
#     print([terms[i] for i in top_indices])

topic_values = lda.transform(X)
df["topic"] = topic_values.argmax(axis=1)

import matplotlib.pyplot as plt

# Mapping numeric topics to human-readable  
topic_names = {
    0: "Public Finance & Macroeconomics",
    1: "Monetary Policy & Markets"
}

# Add topic names to the DataFrame
df["topic_name"] = df["topic"].map(topic_names)

# Count tweets per topic
topic_counts = df["topic_name"].value_counts().sort_index()

plt.figure(figsize=(8,5))

# Draw the bars
bars = plt.bar(topic_counts.index, topic_counts.values, color="steelblue")

plt.xlabel("Topic")
plt.ylabel("Number of Tweets")
plt.title("LDA Topic Distribution")
plt.xticks(topic_counts.index)

# Add the number of tweets inside each bar
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height / 2,                 # vertical position (middle of the bar)
        str(int(height)),           # the number to display
        ha='center', va='center',   # horizontal & vertical alignment
        color='white', fontsize=12, fontweight='bold'
    )

plt.show()






