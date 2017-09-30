from elasticsearch import Elasticsearch
import time
import random

# connect to es, default is localhost:9200
es = Elasticsearch()

index = 'sensor'
type = 'sen3'

for i in range(1000):
    es.index(index=index, doc_type=type, body={'temp':random.randint(0,100), 'timestamp':int(time.time() + i)})
    print(">>%d", i)

print("Done")

