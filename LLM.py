from langchain_ollama import OllamaLLM, ChatOllama


class LLM():
    
    
    def __init__(self, model_name='gemma'):
        
        self.model = OllamaLLM(model=model_name)
        
    
    
    
    
    
    
        
        

