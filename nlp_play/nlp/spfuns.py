import spacy
import time
from spacy import displacy


def parse_docs(doclist, spacy_model="en_core_web_sm"):

    start = time.time()
    print(f"Loading and Applying Model: {spacy_model}")

    # Load Spacy small english language model
    lang_model = spacy.load(spacy_model)

    # define step to add to processing pipeline
    # https://github.com/explosion/spaCy/issues/1717
    def remove_whitespace_entities(doc):
        doc.ents = [e for e in doc.ents if not e.text.isspace()]
        return doc

    # add to processing pipeline
    lang_model.add_pipe(remove_whitespace_entities, after="ner")

    # parse the text, creating embeddings, tagging entities etc
    parsed_docs = [lang_model(doc["text"]) for doc in doclist]

    end = time.time()
    print(f"Model ran in: {end - start:.1f} seconds")

    return parsed_docs


def show_sentence_displacy(parsed_doc, style="dep"):

    if style == "dep":
        # pull sentences apart so we show one per line
        sentence_spans = list(parsed_doc.sents)
        displacy.serve(sentence_spans, style=style)

    elif style == "ent":
        displacy.serve(parsed_doc, style=style)

    else:
        print("Invalid Style - choose 'ent' or 'dep'")


def print_sentence_ents(parsed_doc):

    # pull sentences apart
    sentence_spans = list(parsed_doc.sents)

    # look at the entities for each sentence
    for sentence in sentence_spans:
        print(sentence.sent)
        for ent in sentence.ents:
            print("Entities:")
            print(ent.text, ent.label)
