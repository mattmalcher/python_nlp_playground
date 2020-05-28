import json
import time
import re


def read_yelp(n_reviews, filename):

    start = time.time()

    # now, with the connection to the file read each line as its own object
    # and append it to the list.
    with open(filename) as json_file:
        # list comprehension to combine the parsed json of the 'next' line for
        # the first 10 lines
        review_data = [json.loads(next(json_file)) for x in range(n_reviews)]

    end = time.time()
    print(f"Data read in {end - start:.3f} seconds")

    return review_data


def doc_stats(doc_list):
    doc_lengths = [len(re.findall(r"\w+", doc["text"])) for doc in doc_list]

    print(
        f"Total Wordcount: {sum(doc_lengths)}, "
        f"N Docs: {len(doc_lengths)}, "
        f"Average Words per Review: {sum(doc_lengths)/len(doc_lengths)}"
    )
