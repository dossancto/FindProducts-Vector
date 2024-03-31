from list_products.utils.envs import ENV
import chromadb.utils.embedding_functions as embedding_functions

def get_openai_embeddings():
  openai_api_key = ENV.OPENAI_API_KEY()
  return embedding_functions.OpenAIEmbeddingFunction(
                  api_key=openai_api_key,
                  model_name="text-embedding-3-small"
              )