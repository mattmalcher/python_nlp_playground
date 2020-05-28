# Use python built in lib for parsing JSON
import json

# now, with the connection to the file open, we read each line as its own object and append it to the list.
with open("/media/hdd1/yelp/yelp_academic_dataset_review.json") as json_file:
    # list comprehension to combine the parsed json of the 'next' line for the first 10 lines
    review_data = [json.loads(next(json_file)) for x in range(10)]

# this can be indexed as follows - remember python is 0 indexed:
print(review_data[0]["text"])
