from pdf_reader import extract_text_from_pdf
from flashcard_generator import generate_flashcards

def main(): 
    pdf_path = input("Enter the path to your PDF file: ").strip()

    print("\nExtracting text from PDF...")
    text = extract_text_from_pdf(pdf_path)

    if not text:
        print("No text could be extracted from the PDF. Please check the file.")
        return

    print(f"Extracted {len(text)} characters. Generating flashcards...\n")
    flashcards = generate_flashcards(text)

    if not flashcards:
        print("No flashcards were generated. Please try again.")
        return

    print("=" * 60)
    print("GENERATED FLASHCARDS")
    print("=" * 60)
    print(flashcards)
    print("=" * 60)

if __name__ == "__main__":

    main()
