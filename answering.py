from transformers import pipeline

# Load the question-answering model
question_answering = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# Read the content of the file
file_path = "data.txt"  # Replace with the path to your file
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

while True:
    # Ask a question about the text
    question = input("Ask a question (or type 'exit' to quit): ")
    
    if question.lower() == "exit":
        break
    
    result = question_answering(question=question, context=text)

    # Print the answer
    print("Answer:", result["answer"])
