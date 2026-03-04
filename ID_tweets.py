import json

# Open the existing JSON file and load all previously saved tweets.
with open("debt.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Extract all existing tweet IDs to avoid duplicates.
ids = {tweet["id"] for tweet in data}   # using a set for faster lookup

# List of new tweets to add (each tweet must be a complete object).
new_tweets = [
    {
        'id': '2024878511375233380', 
        'author_id': 'Heinrich Leopold\n@LeopoldHeinrich', 
        'text': 'US nominal #GDP growth stands around $1.5 trn versus US #debt growth of $2.5 trn, which means the US needs for evey  1 $ economic growth 1.66 $ new debt. This cannot carry on for very long.', 
        'created_at': '2026-02-20T16:07:12.000Z', 
        'lang': 'en'
        },
        {
        'id': '2024122309175382390', 
        'author_id': 'World Bank Data\n@worldbankdata', 
        'text': 'Interest payments in low- and middle-income countries reached about US$415 billion in 2024 — more than double a decade ago — even while debt growth slowed sharply.\n\nExplore the changing #debt landscape in 9 charts: \nwrld.bg/YCoB50YhafO', 
        'created_at': '2026-02-18T14:02:19.000Z', 
        'lang': 'en'
        }, 
        {
        'id': '2023759349458301046', 
        'author_id': 'Addis Fortune\n@addis_fortune', 
        'text': 'Ethiopia and France have sealed a debt restructuring deal alongside an 81.5 million euro support package, reinforcing their strategic partnership and backing the macroeconomic reform agenda. #Ethiopia #France #Debt\n\nRead more - \nshorturl.at/KfjcA', 
        'created_at': '2026-02-17T14:00:03.000Z', 
        'lang': 'en'
        }
        ]

# Check for duplicates before adding new tweets.
added = 0
for tweet in new_tweets:
    if tweet["id"] not in ids:
        data.append(tweet)     # add the tweet to the dataset
        ids.add(tweet["id"])   # update the set of known IDs
        added += 1             # count how many were added

print(f"{added} new tweets added.")

# Save the updated list of tweets back to the JSON file.
with open("debt.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("File updated successfully.")

