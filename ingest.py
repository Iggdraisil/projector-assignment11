from requests import post
from itertools import chain
import json

if __name__ == '__main__':
    with open("dictionary.json", "r") as file:
        data = json.load(file)
        new_data = [{"word": word, "description": description} for word, description in data.items()]
        new_data = map(json.dumps,
                       chain.from_iterable([[{"index": {"_index": "english_dict"}}, item] for item in new_data]))
        raw_data = "\n".join(new_data) + "\n"
        r = post("http://localhost:9200/english_dict/_bulk", data=raw_data,
                 headers={'content-type': "application/json"})
        print(r)
