from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware  

# Carrega variáveis do .env
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Modelo padrão
MODEL_NAME = "models/gemini-2.5-pro"
    
app = FastAPI()

# --- CONFIGURAÇÃO DO CORS --- # 
# Define quais "origens" (sites) podem acessar nossa API
origins = [
    "*",  # O "*" significa "permitir todos", o que é ótimo para desenvolvimento.
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Permite todos os métodos (POST, GET, etc)
    allow_headers=["*"], # Permite todos os cabeçalhos
)
# --- FIM DA CONFIGURAÇÃO DO CORS --- # 


# Modelo da requisição
class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
def generate_text(request: PromptRequest):
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(request.prompt)
        return {"response": response.text}
    except Exception as e:
        return {"error": str(e)}