# Importando bibliotecas
import customtkinter as ctk
from PIL import Image, ImageTk
import os
import webbrowser

# Importando outros Scripts
import functions.settings as gsettings # gsettings = General Settings (Configurações Gerais)

# Função para mostrar uma mensagem personalizada na tela.
def customDialogerCaller(anexwindow, dialog):

    global fullScreenBG
    fullScreenBG = ctk.CTkFrame(anexwindow, fg_color=gsettings.applyedTheme["secundary-color"], corner_radius=0)
    fullScreenBG.grid(row=0, column=0, columnspan=2, sticky="nswe")
    fullScreenBG.grid_rowconfigure(0, weight=1)
    fullScreenBG.grid_columnconfigure(0, weight=1)
    
    global dialogBG
    dialogBG = ctk.CTkFrame(fullScreenBG)
    dialogBG.grid(row=0, column=0)
    dialogBG.grid_rowconfigure(0, weight=0)
    dialogBG.grid_rowconfigure(1, weight=0)
    dialogBG.grid_rowconfigure(2, weight=0)
    dialogBG.grid_rowconfigure(3, weight=0)
    dialogBG.grid_columnconfigure(0, weight=1)
    dialogBG.grid_columnconfigure(1, weight=1)

    if dialog == 1:
        apiKeyDialog()

# Mensagem de pedido da chave API
def apiKeyDialog():
    dialogBG.grid_columnconfigure(0, weight=10)

    # Titulo
    titleLabel = ctk.CTkLabel(dialogBG, text="Chave de API necessária", font=ctk.CTkFont(size=30, weight='bold'))
    titleLabel.grid(row=0, column=0, columnspan=2, padx=8, pady=8)
    
    # Descrição
    descriptionLabel = ctk.CTkLabel(dialogBG, text="Para utilizar esta ferramenta é necessário uma chave API\n do Google AI Studio. Caso você não tenha uma chave API, você\n pode gerar a sua em:\n\nhttps://aistudio.google.com/app/apikey\n(ou apertando o botão abaixo)\n\nPor questões de comodidade, sua chave API será salva em um\narquivo local chamado de \"settings.json\".\n\nNão compartilhe sua chave ou este arquivo com ninguém!", font=ctk.CTkFont(size=20))
    descriptionLabel.grid(row=1, column=0, columnspan=2, padx=8, pady=8)

    # Botão para chave de API
    getApiKeyButton = ctk.CTkButton(dialogBG, text="Acessar Google AI Studio para conseguir uma Chave de API 🗝️", fg_color="orange", font=ctk.CTkFont(size=20), text_color="black", command=getApiKeyButtonPress)
    getApiKeyButton.grid(row=2, column=0, columnspan=2, padx=8, pady=8)

    # Caixa de Input para Chave API
    apiKeyEntryTextVar = ctk.StringVar()
    global apiKeyEntry
    apiKeyEntry = ctk.CTkEntry(dialogBG, font=ctk.CTkFont(size=18), placeholder_text="Chave API (API Key)", textvariable=apiKeyEntryTextVar)
    apiKeyEntry.grid(row=3, column=0, padx=8, pady=8, sticky="ew")
    apiKeyEntry.bind('<Return>', saveApiKey)

    # Botão para salvar Chave API
    apiKeySaveButton = ctk.CTkButton(dialogBG, text="Salvar", fg_color="green", font=ctk.CTkFont(size=20), text_color="black", command=saveApiKey)
    apiKeySaveButton.grid(row=3, column=1, padx=8, pady=8, sticky="ew")

def getApiKeyButtonPress():
    openUrlOnBrowser("https://aistudio.google.com/app/apikey")

def openUrlOnBrowser(url):
    webbrowser.open(url=url, new=0, autoraise=True)

def saveApiKey(event=None):
    if (apiKeyEntry.get() != ""):
        gsettings.mainSettings["api_key"] = apiKeyEntry.get()
        gsettings.saveConfigsChange()
        fullScreenBG.destroy()
        from gui.maingui import startApiCheck
        startApiCheck()