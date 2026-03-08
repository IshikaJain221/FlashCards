from hf_model import query_model

CHUNK_SIZE = 1200

def split_text_into_chunks(text, chunk_size=CHUNK_SIZE):
    """Split text into chunks of approximately chunk_size characters."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        # Avoid cutting in the middle of a word
        if end < len(text):
            end = text.rfind(" ", start, end)
            if end == -1:
                end = start + chunk_size
        chunks.append(text[start:end].strip())
        start = end
    return [chunk for chunk in chunks if chunk]

def build_prompt(chunk):
    """Build a high-quality flashcard generation prompt for a given text chunk."""
    return f"""You are an expert study assistant. Read the following text and generate exactly 5 high-quality flashcards for studying.

Rules:
- Focus on key concepts, definitions, and important facts.
- Avoid trivial or obvious details.
- Keep answers concise and clear (1–2 sentences max).
- Output ONLY in this exact format, with no extra commentary:

Q: <question>
A: <answer>

Q: <question>
A: <answer>

Q: <question>
A: <answer>

Q: <question>
A: <answer>

Q: <question>
A: <answer>

Text:
{chunk}
"""

def generate_flashcards(text):
    """Split text into chunks, generate flashcards for each, and return all combined."""
    chunks = split_text_into_chunks(text)
    print(f"Split into {len(chunks)} chunk(s). Querying LLM for each...\n")

    all_flashcards = []

    for i, chunk in enumerate(chunks, start=1):
        print(f"Processing chunk {i}/{len(chunks)}...")
        prompt = build_prompt(chunk)
        result = query_model(prompt)

        if result:
            all_flashcards.append(f"--- Chunk {i} ---\n{result.strip()}")
        else:
            print(f"Warning: No flashcards returned for chunk {i}.")

    return "\n\n".join(all_flashcards)
