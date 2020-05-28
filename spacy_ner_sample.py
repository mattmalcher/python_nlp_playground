from nlp_play.read_data import yelp_json
from nlp_play.nlp import spfuns

# read data
review_data = yelp_json.read_yelp(
    n_reviews=10, filename="/media/hdd1/yelp/yelp_academic_dataset_review.json"
)

# apply spacy pipeline
parsed_docs = spfuns.parse_docs(doclist=review_data)


# show sentence deps in browser
# spfuns.show_sentence_displacy(parsed_doc=parsed_docs[0], style="dep")
spfuns.show_sentence_displacy(parsed_doc=parsed_docs[0], style="ent")

# print
