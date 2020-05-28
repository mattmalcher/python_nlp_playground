import json
import spacy
import time
import re

start = time.time()
print("Reading Data")

# number of reviews to read in and process
n_reviews = 100

# now, with the connection to the file read each line as its own object
# and append it to the list.
with open("/media/hdd1/yelp/yelp_academic_dataset_review.json") as json_file:
    # list comprehension to combine the parsed json of the 'next' line for the
    # first 10 lines
    review_data = [json.loads(next(json_file)) for x in range(n_reviews)]

end = time.time()
print(end - start)

doc_lengths = [len(re.findall(r"\w+", review["text"])) for review in review_data]

print(
    f"Total Wordcount: {sum(doc_lengths)}, "
    f"N Reviews: {len(doc_lengths)}, "
    f"Average Words per Review: {sum(doc_lengths)/len(doc_lengths)}"
)


start = time.time()
print("Loading and Applying Model:")

# Load Spacy small english language model
lang_model = spacy.load("en_core_web_sm")

# parse the text, creating embeddings, tagging entities etc
parsed_docs = [lang_model(review["text"]) for review in review_data]

print("Model ran in:")
end = time.time()
print(end - start)


# extract the entities within each doc
all_ents = [doc.ents for doc in parsed_docs]
all_noun_chunks = [list(doc.noun_chunks) for doc in parsed_docs]

# list comprehension to flatten list of tuples (entities per document) into a
# single list of entities:
# combined_entities = [item for ent in all_ents for item in ent]

# filtering this to different entity types shows that the accuracy could be
# better - no category for food, so lots of food ends up as other tags.
combined_gpe = [
    item
    for ent in all_ents
    for item in ent
    if item.label_ == "GPE" and item.text != "\n"
]
combined_person = [
    item
    for ent in all_ents
    for item in ent
    if item.label_ == "PERSON" and item.text != "\n"
]
combined_product = [
    item
    for ent in all_ents
    for item in ent
    if item.label_ == "PRODUCT" and item.text != "\n"
]

# time and money look to work fairly well
combined_time = [
    item
    for ent in all_ents
    for item in ent
    if item.label_ == "TIME" and item.text != "\n"
]

combined_money = [
    item
    for ent in all_ents
    for item in ent
    if item.label_ == "MONEY" and item.text != "\n"
]
