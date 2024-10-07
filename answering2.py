import transformers

question_answering = transformers.pipeline(
    "question-answering", model="distilbert-base-cased-distilled-squad", use_fast=True
)

with open("data2.txt", "r", encoding="utf-8") as file:
    text = file.read()

context = question_answering.tokenizer(
    text, return_tensors="pt", max_length=4096, truncation=True
)

while True:
    question = input("Ask a question (or type 'exit' to quit): ")

    if question.lower() == "exit":
        break

    answer = question_answering(question=question, context=context)

    print("Answer:", answer["answer"])
