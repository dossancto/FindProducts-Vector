from dataclasses import asdict
import uuid
from typing import List
import chromadb
from zope.interface import implementer

from domain.products.entities.product import Product
from application.products.data.ProductRepository import ProductRepository
from domain.general.SimiliarityData import SimiliarittyData

COLLECTION_NAME = "PRODUCT_COLLECTION"

@implementer(ProductRepository)
class ChromaProductRepository:
    def __init__(self, chroma_client_p: chromadb.ClientAPI = chromadb.Client()) -> None:
        self.chroma_client = chroma_client_p

        self.collection = self.chroma_client.get_or_create_collection(name=COLLECTION_NAME)

    def save(self, entity: Product) -> str:
        return self.save_batch([entity])[0]

    def save_batch(self, entities: List[Product]) -> List[str]:
        ids = list(map(lambda x: uuid.uuid4().__str__(), entities))

        documents = list(map(lambda x: x.search_field, entities))

        dict_entities = list(map(lambda x: asdict(x), entities))

        self.collection.add(
            documents=documents,
            metadatas=dict_entities,
            ids=ids
        )

        return ids

    def search_by_similiarity(self, name: List[str], creator: str) -> List[SimiliarittyData[Product]]:
        result =  self.collection.query(
            query_texts=name,
            n_results=2,
            where={'creator_name': creator}
        )

        ids = result['ids'][0]
        distances = result['distances'][0]
        metadatas = result['metadatas'][0]

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
        name = metadata.get('name', ''),
        description= metadata.get('description', ''),
        creator_name=metadata.get('creator_name', ''),
        search_field=metadata.get('search_field', '')
    )
    