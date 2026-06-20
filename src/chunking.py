from typing import List


def create_chunks(
    pdf_content: List[str], chunk_size: int = 900, chunk_overlap: int = 150
):
    # creating chunk variable for storing chunks
    chunks: List[str] = []

    # creating the full text for measuring the length of the text
    full_text = " ".join(pdf_content)

    # measuring text length
    text_length = len(full_text)

    # print(text_length)

    # starting from 0 to make chunks from the start
    start = 0

    # Looping until the end of the text length
    while start < text_length:

        # creating end of the each chunk size, it should be minimum of start + Chunk size or the text length
        end = min(start + chunk_size, text_length)

        # Extract chunk
        chunk = full_text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        # If the end is greater than chunk size the loop should break because its above original text size
        if end >= text_length:
            break

        # creating the start again with overlapping 150 characters
        # Overlapping is used to maintain the continuity of the conversation
        # So the sentence does not break inbetween the chunks
        start = end - chunk_overlap

        # print(f"Starting new chunk again from {start} after over lapping")

    # print(chunks)
    # print(len(chunks))
    return chunks
