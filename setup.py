# in terminal: python -m spacy download en_core_web_sm
import spacy

spacy.cli.download("en_core_web_sm")
lang_model = spacy.load("en_core_web_sm")
