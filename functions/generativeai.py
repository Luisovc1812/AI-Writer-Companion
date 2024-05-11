# Importando bibliotecas
import google.generativeai as genai

# Importando outros Scripts
import functions.settings as gsettings # gsettings = General Settings (Configurações Gerais)
from gui.customdialogs import customDialogerCaller as customdialogs

# Configurando Modelo
def connectApi(possibleanexwindow):
    import time
    time.sleep(1) # Espera um segundo para garantir que o script principal tenha iniciado corretamente
    api_key=gsettings.mainSettings["api_key"]
    if api_key != "":
      genai.configure(api_key=api_key)
      print("Chave API configurada.")
    else :
      print("API ausente") 
      customdialogs(possibleanexwindow, 1)

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest", generation_config=generation_config, safety_settings=safety_settings)

# Modelo para palavras Antonimas

antonymFewShots = [
  "Caso não haja contexo o bastante, responda com alguma possibilidade. É probido utilizar frases.",
  "input: abrir",
  "output: fechar",
  "input: comprar",
  "output: vender",
  "input: ligar",
  "output: desligar",
  "input: claro",
  "output: escuro",
  "input: alto",
  "output: baixo",
  "input: preto",
  "output: branco",
  "input: esquerda",
  "output: direita",
]

# Modelo para palavras Sinônimas

synonymFewShots = [
   "Caso não haja contexo o bastante, responda com alguma possibilidade. É probido utilizar frases.",
   "input: morto",
   "output: falecido",
   "input: estudante",
   "output: aluno",
   "input: amor",
   "output: afeto",
   "input: raiva",
   "output: fúria",
   "input: casa",
   "output: moradia",
   "input: desejo",
   "output: ambição",
   "input: trabalho",
   "output: emprego",
]

# Modelo para explicação de palavras/expressões

definitionModel = [
   "Abaixo será indicado uma palavra ou uma expressão. Sua função será primeiro dizer de uma forma curta e fácil de entender qual o significado desta palavra ou expressão. Depois, com uma linha se separação, explique melhor essa palavra ou expressão. Não use formações de texto. Com exceção de linhas, o texto não deve conter formatações para negrito, itálico, bullets, entre outros."
]

# Função para Palavras Antônimas

def generateAntonym(userInput):
   try:
      gotAnswer = model.generate_content(antonymFewShots+[f"input: {userInput}", "output: "]).text
      return gotAnswer
   except:
      return "anerroroccored"

def generateSynonym(userInput):
   try:
      gotAnswer = model.generate_content(synonymFewShots+[f"input: {userInput}", "output: "]).text
      return gotAnswer
   except:
      return "anerroroccored"
   
def generateDefinition(userInput):
   try:
      gotAnswer = model.generate_content(definitionModel+[f"input: {userInput}", "output: "]).text
      return gotAnswer
   except:
      return "anerroroccored"