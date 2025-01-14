import requests
import json
import time

class GrammarGinger:
    def __init__(self, prompt):
        prompt = prompt.split(" ")
        url = "https://ginger4.p.rapidapi.com/correction"
        querystring = {"lang":"US","generateRecommendations":"false","flagInfomralLanguage":"true"}

        headers = {
            "x-rapidapi-key": "81461a1b2amshe01e0315fcbd693p17de7bjsnddeee99c5837",
            "x-rapidapi-host": "ginger4.p.rapidapi.com",
            "Content-Type": "text/plain",
            "Accept-Encoding": "identity"
        }
        self.url = url
        self.querystring = querystring
        self.headers=headers
        self.prompt = prompt
        self.foundMistake = False
    
    # Analyzes All Words And Makes Changes If Needed
    def analyzeWords(self):
        index = 0
        for word in self.prompt:
            response = requests.post(self.url, headers=self.headers, data=word, params=self.querystring)
            if(response.status_code == 200):
                loadResponse = json.loads(response.text)
                if(len(loadResponse["GingerTheDocumentResult"]["Corrections"]) > 0):
                    self.foundMistake = True
                    self.prompt[index] = loadResponse["GingerTheDocumentResult"]["Corrections"][0]["Suggestions"][0]["Text"]
                    index += 1
                else:
                    index += 1
                time.sleep(1)
            else:
                raise ValueError(f"Unexpected status code: {response.status_code}")

    # Puts The Words Back Into One Full String  
    def rebuildPrompt(self):
        prompt = ""
        for word in self.prompt:
            prompt = prompt + word
            if(word == self.prompt[-1]):
                break
            prompt = prompt + " "
        return prompt
        
    
if __name__ == "__main__":
    word = GrammarGinger("Softwar Enginer")
    word.analyzeWords()
    print(word.prompt)
    print(word.rebuildPrompt())
    

    


