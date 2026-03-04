import re
import json
from collections import Counter
from nltk.corpus import stopwords

# 1. Clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^\w\s@#]", "", text)
    text = re.sub(r"&amp;", "", text)
    return text

# 2. Extract hashtags and mentions
def extract_entities(text):
    hashtags = re.findall(r"#\w+", text)
    mentions = re.findall(r"@\w+", text)
    return hashtags, mentions

# 3. Simple lemmatization
def lemmatize(text):
    return text.split()

# Load tweets
with open("Debt.json", encoding="utf-8") as f:
    tweets = json.load(f)

mention_counter = Counter()
hashtag_counter = Counter()
word_counter = Counter()
stop = set(stopwords.words("english"))

for t in tweets:
    text = clean_text(t["text"])
    hashtags, mentions = extract_entities(text)
    lemmas = lemmatize(text)

    mention_counter.update(mentions)
    hashtag_counter.update(hashtags)

    clean_words = [w for w in lemmas if w not in stop and len(w) > 2]
    word_counter.update(clean_words)

# print("Top @mentions:", mention_counter.most_common(20))
#print("Top hashtags:", hashtag_counter.most_common(20))
# print("Most common words:", word_counter.most_common(30))



# --- PRINT SAMPLES FOR THE FIRST TWEET ---
sample = tweets[10]["text"]

print("\n=== ORIGINAL TEXT ===")
print(sample)

cleaned = clean_text(sample)
print("\n=== AFTER CLEANING (lowercase, remove URLs & punctuation) ===")
print(cleaned)

hashtags, mentions = extract_entities(cleaned)
print("\n=== AFTER ENTITY EXTRACTION ===")
print("Hashtags:", hashtags)
print("Mentions:", mentions)

tokens = lemmatize(cleaned)
print("\n=== AFTER TOKENISATION ===")
print(tokens)

clean_tokens = [w for w in tokens if w not in stop and len(w) > 2]
print("\n=== AFTER STOPWORD REMOVAL ===")
print(clean_tokens)

print("\n--- END OF SAMPLE CLEANING PIPELINE ---\n")
