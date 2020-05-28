import spacy
from spacy import displacy
import json

# now, with the connection to the file open, we read each line as its own
# object and append it to the list.
with open("/media/hdd1/yelp/yelp_academic_dataset_review.json") as json_file:
    # list comprehension to combine the parsed json of the 'next' line for the
    # first 10 lines
    review_data = [json.loads(next(json_file)) for x in range(10)]

# Load Spacy small english language model
lang_model = spacy.load("en_core_web_sm")

# parse the text, creating embeddings, tagging entities and
parsed_doc = lang_model(review_data[0]["text"])

# pull sentences apart
sentence_spans = list(parsed_doc.sents)

# look at the entities for each sentence
for sentence in sentence_spans:
    print(sentence.sent)
    for ent in sentence.ents:
        print("Entities:")
        print(ent.text, ent.label)

# OR... look at them in the browser, using displacy
displacy.serve(sentence_spans, style="dep")
# displacy.serve(parsed_doc, style = "ents")

print()
