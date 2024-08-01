from elasticsearch import Elasticsearch

# Connect to the Elasticsearch instance
# es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

#es = Elasticsearch(hosts=[{'host': 'localhost', 'port': 9200}],scheme="http")

#es = Elasticsearch('http://localhost:9200')

es = Elasticsearch(
    [
        {'host': 'localhost', 'port': 9200, "scheme": "https"}
    ],

)


# Check if the connection is established
if es.ping():
    print("Connected to Elasticsearch")
else:
    print("Could not connect to Elasticsearch")

# Define the index name
index_name = "sample_index"

# Create an index
if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name)
    print(f"Index '{index_name}' created.")
else:
    print(f"Index '{index_name}' already exists.")

# Add a document to the index
doc = {
    "title": "Elasticsearch Basics",
    "content": "This is a basic example of Elasticsearch with Python",
    "tags": ["elasticsearch", "python", "example"]
}

#: INSERT = index, UPDATE
res = es.index(index=index_name, id=1, body=doc)
#res = es.index(index=index_name, id=2, body=doc2)
print(f"Document added: {res['result']}")

# Refresh the index to make the document searchable
es.indices.refresh(index=index_name)

# Search for the document
search_body = {
    "query": {
        "match": {
            "content": "example"
        }
    }
}

# SELECT = search
res = es.search(index=index_name, body=search_body)
print("Search results:")
for hit in res['hits']['hits']:
    print(hit['_source'])


# DELETE, Delete the index
es.indices.delete(index=index_name)
print(f"Index '{index_name}' deleted.")
