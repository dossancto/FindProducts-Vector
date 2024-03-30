import chromadb

chroma_client = chromadb.Client()

collection = chroma_client.create_collection(name="my_collection")

collection.add(
    documents=["Monster de Manga, Mongo Loco", "Monster Pacif Punch", "Cerveja sem gas"],
    metadatas=[{"category": "energetic", "price": 12.5}, {"category": "energetic", "price": 5.0}, {"category": "alcohol"}],
    ids=["a", "b", "c"]
)

results = collection.query(
    query_texts=["5.0"],
    n_results=3
)

print(results)
