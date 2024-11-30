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
                    "content": f"""I need a skill tree built in JSON format focusing on “{message}”. The tree is allowed to have as many branches extending to other branches as much as it needs. There should be for each leaf a “title”, “description”, and “extend”. The “title” should hold a string with the name of the topic. The “description” should hold a string with a detailed description of what that topic means and what its purpose is. The “branch” should be more dictionaries holding other branches/leafs that allow it to continue extending and repeating the process. 
                                If there are no branches/leafs needed for that one then it should be left as an empty dictionary.
                                "Build a skill tree in JSON format for the topic 'software engineering.' The tree should have multiple branches and leaves. Each leaf should include the following attributes:
                                title: The name of the skill or topic.
                                description: A detailed explanation of the skill or topic, including its importance and purpose.
                                extend: This will either be an empty dictionary or another dictionary with further branches (sub-skills, concepts, etc.) extending from this leaf.
                                The skill tree can have as many branches and sub-branches as necessary, representing the complexity and depth of the topic. For branches that don't have any sub-skills or topics, use an empty dictionary.
                                Please ensure the tree is well-organized, with each branch logically following the previous one and connected in a meaningful way."""
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
    
    # Cleans The Extra Text From The API
    def jsonPrepare(self, message):
        response = self.getMessage(message)
        left = 0
        right = len(response)
        while(left<=right):
            if(response[left] != "{" and response[right-1] != "}"):
                right = right - 1
                left = left + 1
            else:
                break
        while(response[left] != "{"):
            left = left + 1
        while(response[right-1] != "}"):
            right = right - 1
        parsedResponse = response[left:right]
        return eval(parsedResponse)
    
    # Returns To Original Json State
    # Easier For Reading Through CLI
    def revertJson(self, message):
        response = self.jsonPrepare(message)
        return json.dumps(response, indent=4)
    
    # Iterate Through First Dictionaries
    def starterBranches(self, message):
        response = self.jsonPrepare(message)
        for key, value in response.items():
            print(key)
        return None
    
# Main Method Testing
if __name__ == "__main__":
    response = ChatGPTAPI()
    response = response.revertJson("Computer Science")
    print(response)

    
