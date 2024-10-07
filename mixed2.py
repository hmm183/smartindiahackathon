import requests
from transformers import pipeline

#pipeline
#ask question get logic
#print it
#use api but only limited uses


def learn_more():
    url = "https://chatgpt-api8.p.rapidapi.com/"

    payload = [
            {
                    "content": result["answer"] + ' Can you provide more details about ' + result["answer"] + '?',
                    "role": "user"
            }
    ]
    headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "da622ea81amshdb63bcf0ce1811ep118467jsnc0e72a65fff5",
            "X-RapidAPI-Host": "chatgpt-api8.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    print('answer from api', response.json())

def answer():
    question_answering = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")

    file_path = "data.txt"
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    while True:
        question = input("Ask a question (or type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        global result
        result = question_answering(question=question, context=text)

        print("Answer from script:", result["answer"])
        if question.lower() == "learn more":
            learn_more()
        else:
            pass

answer()
