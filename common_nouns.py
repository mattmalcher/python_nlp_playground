from nlp_play.read_data import yelp_json
from nlp_play.nlp import spfuns

# read data
review_data = yelp_json.read_yelp(
    n_reviews=1000, filename="/media/hdd1/yelp/yelp_academic_dataset_review.json"
)

# print doc stats
yelp_json.doc_stats(review_data)

# apply spacy pipeline
parsed_docs = spfuns.parse_docs(doclist=review_data)

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
    if item.label_ == "GPE"  # and item.text != "\n"
]
combined_person = [
    item
    for ent in all_ents
    for item in ent
    if item.label_ == "PERSON"  # and item.text != "\n"
]
combined_product = [
    item
    for ent in all_ents
    for item in ent
    if item.label_ == "PRODUCT"  # and item.text != "\n"
]

# time and money look to work fairly well
combined_time = [
    item
    for ent in all_ents
    for item in ent
    if item.label_ == "TIME"  # and item.text != "\n"
]

combined_money = [
    item
    for ent in all_ents
    for item in ent
    if item.label_ == "MONEY"  # and item.text != "\n"
]
