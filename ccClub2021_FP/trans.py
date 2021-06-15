import csv 
import json 
import re

def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\xa0"
        u"\U0001f97a"
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'_REMOVE_',text)

csvfile  = "ccClub2021_FP.csv"
jsonfile = "db.json"

jsonArray = []
with open(csvfile, encoding='utf-8') as csvf: 
    csvReader = csv.DictReader(csvf) 
    for idx, row in enumerate(csvReader):
        content = [ x for x in deEmojify( row["content"] ).split("#")[1:] if "_REMOVE_" not in x ]
        row["content"] = "".join( " #"+x.rstrip() for x in content ) 
        
        temp = {"model": "Gallery.lottery", "pk": idx, "fields":row}
        jsonArray.append(temp)

with open(jsonfile, 'w', encoding='utf-8') as jsonf: 
    jsonString = json.dumps(jsonArray, indent=4, ensure_ascii=False)
    jsonf.write(jsonString)
