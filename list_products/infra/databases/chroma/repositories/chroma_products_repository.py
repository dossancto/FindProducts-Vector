from dataclasses import asdict
import uuid
from typing import List
import chromadb
from zope.interface import implementer

from domain.products.entities.product import Product
from application.products.data.ProductRepository import ProductRepository
from infra.databases.chroma.utils.embeddings import get_openai_embeddings
from domain.general.SimiliarityData import SimiliarittyData

COLLECTION_NAME = "PRODUCT_COLLECTION"

@implementer(ProductRepository)
class ChromaProductRepository:
    def __init__(self, chroma_client_p = chromadb.Client()) -> None:
        self.chroma_client = chroma_client_p

        self.collection = self.chroma_client.get_or_create_collection(
            name=COLLECTION_NAME
            )

    def save(self, entity: Product) -> str:
        return self.save_batch([entity])[0]

    def save_batch(self, entities: List[Product]) -> List[str]:
        ids = list(map(lambda _: uuid.uuid4().__str__(), entities))

        documents = list(map(lambda x: x.description, entities))
        openai_embedder = get_openai_embeddings()

        embeddings = openai_embedder(documents)

        dict_entities = list(map(lambda x: asdict(x), entities))

        self.collection.add(
            embeddings=embeddings,
            documents=documents,
            metadatas=dict_entities, # type: ignore
            ids=ids
        )

        return ids

    def search_by_similiarity(self, name: List[str], creator: str) -> List[SimiliarittyData[Product]]:
        embedder = get_openai_embeddings()
        embeddinds = embedder(name)
        result =  self.collection.query(
            query_embeddings=embeddinds,
            n_results=3,
            where={'creator_name': creator}
        )

        ids = result['ids'][0]
        distances = result['distances'][0] # type: ignore
        metadatas = result['metadatas'][0] # type: ignore

        product_count = len(ids)
        
        products: List[SimiliarittyData[Product]] = []

        for i in range(0, product_count):
            id = ids[i]
            metadata = metadatas[i]
            distance = distances[i]
            
            product = product_from_metadata(metadata, id)

            products.append(SimiliarittyData(
                data=product,
                distance=distance
            ))

        return products

def product_from_metadata(metadata: chromadb.Metadata, id: str):
    return Product(
        id=id,
        name = metadata.get('name', '').__str__(),
        description= metadata.get('description', '').__str__(),
        creator_name=metadata.get('creator_name', '').__str__(),
        search_field=metadata.get('search_field', '').__str__()
    )
    
