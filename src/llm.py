from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPEN_AI_KEY"))


def query_llm_with_context(chunks, user_query):

    llm_behaviour = """
                        You are a helpful assistant for answering user queries based on the provided context.
                        use the context to provide accurate and relevant answers. do not make assumptions beyone the context provided.
                        If the context does not contain enough information to answer the query, 
                        let the user know that you cannot provide the answer based on the given context
                        """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": llm_behaviour},
            {"role": "user", "content": f"Query: {user_query}\n\nContext:{chunks}"},
        ],
        temperature=0.4,
    )

    return response.choices[0].message.content