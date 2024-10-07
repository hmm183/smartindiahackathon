import requests
from transformers import pipeline


def learn_more():
    url = "https://chatgpt-api8.p.rapidapi.com/"

    payload = [
            {
                    "content": result["answer"]+' explain more about this',
                    "role": "user"
            }
    ]
    headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "da622ea81amshdb63bcf0ce1811ep118467jsnc0e72a65fff5",
            "X-RapidAPI-Host": "chatgpt-api8.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    print('answer from api',response.json())



def answer():
    question_answering = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
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
