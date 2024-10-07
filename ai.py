import requests

url = "https://chatgpt-api8.p.rapidapi.com/"

payload = [
	{
		"content": "who won the super bowl 2019?",
		"role": "user"
	}
]
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "da622ea81amshdb63bcf0ce1811ep118467jsnc0e72a65fff5",
	"X-RapidAPI-Host": "chatgpt-api8.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
