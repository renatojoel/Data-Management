
# Fistly, we will install the necessary libraries for data cleaning and manipulation
# We will use pandas, preprocessor, tweet-processor and nltk for data manipulation and cleaning
# pip install preprocessor - run this command in your terminal to install the preprocessor library
# pip install nltk - run this command in your terminal to install the nltk library
# pip install pandas - run this command in your terminal to install the pandas library
# pip install tweet-preprocessor - run this command in your terminal to install the tweet-preprocessor library
#pip install numpy
#pip install scipy
#pip install scikit-learn




import json # import json p
import preprocessor as p #Library based on tweet data for cleaning
import pandas as pd # This data analysis tool
import nltk # 
import string # for string manipulation
# nltk.download('stopwords')
# nltk.download("punkt")
# nltk.download('punkt_tab') 
from nltk.corpus import stopwords # Natural Language datasets library
stop_words = set(stopwords.words('english'))   # Set stopwords to english only
from nltk.tokenize import word_tokenize  # To split strings to lists
from nltk.stem.porter import PorterStemmer # Process for normalising text for analysis

df = pd.read_json('Debt.json', encoding='utf-8')


# Configure tweet preprocessor 
p.set_options(p.OPT.URL, p.OPT.MENTION, p.OPT.RESERVED, p.OPT.EMOJI, p.OPT.SMILEY)

# Clean Twitter-specific noise 
df["clean_text"] = df["text"].apply(lambda x: p.clean(x))

# Lowercase the cleaned text for uniformity 
df["clean_text"] = df["clean_text"].str.lower()

# Remove punctuation from the cleaned text to focus on words only
df["clean_text"] = df["clean_text"].str.replace(f"[{string.punctuation}]", " ", regex=True)

# Tokenize the cleaned text to split it into individual words for analysis
df["tokens"] = df["clean_text"].apply(word_tokenize)

# Remove stopwords
# stop_words = set(stopwords.words("english"))
# df["tokens"] = df["tokens"].apply(lambda words: [w for w in words if w not in stop_words])

# Stemming to reduce words to their root form for better analysis
stemmer = PorterStemmer()
df["tokens"] = df["tokens"].apply(lambda words: [stemmer.stem(w) for w in words])
#print(df[["text", "clean_text", "tokens"]].head())



def clean_tokens(tokens):
    cleaned = []
    for w in tokens:
        w = w.lower()
        if w in stop_words:
            continue
        if w.isnumeric():
            continue
        if len(w) < 3:   # remove short words (ex: "to", "of")
            continue
        cleaned.append(w)
    return cleaned

df["clean_tokens"] = df["tokens"].apply(clean_tokens)

from collections import Counter

all_words = [word for tokens in df["clean_tokens"] for word in tokens]
freq = Counter(all_words)

print(freq.most_common(20))



from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(
    max_features=30,
    stop_words='english',      # remove stopwords automaticaly
    min_df=2,                  # dont consider words that appear in less than 2 times
    max_df=0.9,                # dont consider words that appear in more than 90% of the times
)

matrix = tfidf.fit_transform(df["clean_text"])
print(tfidf.get_feature_names_out())

