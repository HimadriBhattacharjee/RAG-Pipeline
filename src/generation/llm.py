from groq import Groq
from config.settings import settings


class LLM_Generator:
    def __init__(self, model_name: str):
        
        self.model_name = settings.LLM_MODEL
        self.groq = Groq(model_name=self.model_name, api_key=settings.GROQ_API_KEY,temperature=0.7, max_tokens=2000)
        

def generate(self, prompt: str) -> str:
        response = self.groq.invoke(prompt)
        return response    


