from pdfreader import read_pdf
from chunking import create_chunks
from embeddings import create_embeddings
from vectorstore import store_in_pinecone

pdf_path = r"../resources/HRPolicy.pdf"

def run():

    #read the content from the pdf
    pdf_content = read_pdf(pdf_path)

    print(pdf_content)

    #Chunk the PDF content into specific size
    chunks = create_chunks(pdf_content)

    #Create embeddings for the chunks
    embeddings = create_embeddings(chunks)

    #Store the embeddings in the Pinecone DB
    store_in_pinecone(chunks, embeddings)

if __name__=="__main__":
    run()