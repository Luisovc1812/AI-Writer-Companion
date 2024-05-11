# Importando bibliotecas
import customtkinter as ctk

# Importando outros Scripts
import functions.settings as gsettings # gsettings = General Settings (Configurações Gerais)
from functions.generativeai import generateDefinition
from functions.warningText import setDefaultText, setWarningText

defaultTheme = gsettings.applyedTheme

# Função que será chamada para criar a GUI
def createDefinitionGui(anexwindow):
    definitionGuiFrame = ctk.CTkFrame(anexwindow, fg_color=defaultTheme["accent-color"], corner_radius=0)
    definitionGuiFrame.grid(row=0, column=1, sticky="nswe", pady=35)
    definitionGuiFrame.grid_columnconfigure(0, weight=10)
    definitionGuiFrame.grid_columnconfigure(1, weight=1)
    definitionGuiFrame.grid_rowconfigure(0, weight=0)
    definitionGuiFrame.grid_rowconfigure(1, weight=0)
    definitionGuiFrame.grid_rowconfigure(2, weight=8)

    titleLabel = ctk.CTkLabel(definitionGuiFrame, text="• Significado/Definições de Palavras e Expressões •", font=ctk.CTkFont(size=20, weight='bold'))
    titleLabel.grid(row=0, column=0, columnspan=2, sticky="new", pady=8, padx=5)

    global inputEntry
    wordInputTextVar = ctk.StringVar()
    inputEntry = ctk.CTkEntry(definitionGuiFrame, font=ctk.CTkFont(size=15), placeholder_text="Escreva uma palavra/expressão aqui para ver seu significado.", textvariable=wordInputTextVar)
    inputEntry.grid(row=1, column=0, sticky="ew", pady=8, padx=5)
    inputEntry.bind('<Return>', generateDefinitionTrigger)

    sendInputButton = ctk.CTkButton(definitionGuiFrame, text="Enviar", fg_color="green", text_color="white", font=ctk.CTkFont(size=18), command=generateDefinitionTrigger)
    sendInputButton.grid(row=1, column=1, sticky="ew", pady=8, padx=5)

    global replyTextbox
    replyTextbox = ctk.CTkTextbox(definitionGuiFrame, font=ctk.CTkFont(size=15), wrap="word")
    replyTextbox.grid(row=2, column=0, columnspan=2, pady=8, padx=5, sticky="nswe")
    replyTextbox.insert('0.0', "A resposta da AI aparecerá aqui! Neste primeiro parágrafo, haverá uma resposta curta e direta para a palavra/expressão da qual você está consultando.\n\nJá neste segundo parágrafo, você encontrará uma resposta mais completa.\n\nContexto e histórico de perguntas não serão salvos na AI para que cada pergunta seja a mais objetiva possível.")
    replyTextbox.configure(state="disabled")

    return definitionGuiFrame

# Função que será chamada ao apertar ENTER ou no botão para enviar pergunta
def generateDefinitionTrigger(event=None):
    wordInput = inputEntry.get()

    if (wordInput != ""):
        aiResponse = generateDefinition(wordInput)
        if aiResponse != "anerroroccored":
            replyTextbox.configure(state="normal")
            replyTextbox.delete('0.0', 'end')
            replyTextbox.insert('0.0', aiResponse)
            replyTextbox.configure(state="disabled")
            setDefaultText()
        else: # Caso ocorra algum erro
            setWarningText("Ocorreu um erro com a API!\nNormalmente isto acontece quando você faz\nmuitos prompts em pouco tempo.\n\nTente de novo mais tarde, ou tente\nusar outro prompt.", defaultTheme["danger-color"])
    else:
        print("Input vazio")
    return