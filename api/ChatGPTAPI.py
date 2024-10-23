# Using the Cheapest GPT-4 Turbo, GPT 4 Vision, ChatGPT OpenAI AI API
# Source https://rapidapi.com/NextAPI/api/cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api

import requests
import json

class ChatGPTAPI:
    
    # Constructor Creating The Url And Header
    def __init__(self):
        apiKey = ""
        with open("apiKey", "r") as file:
            apiKey = file.readline().strip()
        
        url = "https://cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com/v1/chat/completions"
        headers = {
            "x-rapidapi-key": f"{apiKey}",
            "x-rapidapi-host": "cheapest-gpt-4-turbo-gpt-4-vision-chatgpt-openai-ai-api.p.rapidapi.com",
            "Content-Type": "application/json"
        }
        self.url = url
        self.headers = headers

    # Returns The Response Of The Request
    def getResponse(self, message):
        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": f"Build a general skill tree with the topic of {message}. Provide short names for all skills and use level numbering. Be detailed by branching deep within in skill producing more skills inside."
                }
            ],
            "model": "gpt-4o",
        }
        response = requests.post(self.url, headers=self.headers, json=payload)
        return response

    # Returns The Status Code Of The Request
    def getStatusCode(self, message):
        response = self.getResponse(message)
        return response

    # Returns The Message From The AI
    def getMessage(self, message):
        response = self.getResponse(message).text
        response = json.loads(response)
        response = response["choices"][0]["message"]["content"]
        return response
    
# Main Method Testing
if __name__ == "__main__":
    response = ChatGPTAPI()
    response = response.getMessage("Computer Science")
    print(response)

    
