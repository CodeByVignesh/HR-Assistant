from src.embeddings import embed_user_query
from src.vectorstore import matched_chunks
from src.llm import query_llm_with_context


def answer_user_query(user_query):

    # Convert the user query into the embeddings
    user_query_embeddings = embed_user_query(user_query)
    # print(user_query_embeddings)
    # print(user_query_embeddings.data[0].embedding)

    # pass the embeddings to get the matching chunks
    matching_chunks = matched_chunks(user_query_embeddings)
    # print(matching_chunks)

    # pass this matched chunks with user query for the llm to generate the output
    llm_response = query_llm_with_context(user_query=user_query, chunks=matching_chunks)

    print(llm_response)
    return llm_response


if __name__ == "__main__":
    answer_user_query("what is the leave policy?")
