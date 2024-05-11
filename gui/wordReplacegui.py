# Importando bibliotecas
import customtkinter as ctk
import functions.settings as gsettings # gsettings = General Settings (Configurações Gerais)
from functions.generativeai import generateAntonym, generateSynonym
from functions.warningText import setDefaultText, setWarningText

defaultTheme = gsettings.applyedTheme

# Função que será chamada para criar a GUI
def createWordReplaceGui(anexwindow):
    wordReplaceGuiFrame = ctk.CTkFrame(anexwindow, fg_color="transparent", corner_radius=0)
    wordReplaceGuiFrame.grid(row=0, column=1, sticky="nswe")
    wordReplaceGuiFrame.grid_columnconfigure(0, weight=1)
    wordReplaceGuiFrame.grid_rowconfigure(0, weight=1)

    centralizeFrame = ctk.CTkFrame(wordReplaceGuiFrame, fg_color=defaultTheme["accent-color"], corner_radius=0)
    centralizeFrame.grid(row=0, column=0, sticky="ew")
    centralizeFrame.grid_columnconfigure(0, weight=5)
    centralizeFrame.grid_columnconfigure(1, weight=1)
    centralizeFrame.grid_columnconfigure(2, weight=5)
    centralizeFrame.grid_rowconfigure(0, weight=0)
    centralizeFrame.grid_rowconfigure(1, weight=0)
    centralizeFrame.grid_rowconfigure(2, weight=0)
    centralizeFrame.grid_rowconfigure(3, weight=0)
    centralizeFrame.grid_rowconfigure(4, weight=0)
    centralizeFrame.grid_rowconfigure(5, weight=0)

    # Antonimo

    antonymTitleLabel = ctk.CTkLabel(centralizeFrame, text="• Gerar antônimo •", font=ctk.CTkFont(size=25, weight='bold'))
    antonymTitleLabel.grid(row=0, column=0, columnspan=3, sticky="nswe", pady=20)

    global antonymInputEntry
    antonyInputTextVar = ctk.StringVar()
    antonymInputEntry = ctk.CTkEntry(centralizeFrame, font=ctk.CTkFont(size=15), placeholder_text="Sua palavra aqui.", textvariable=antonyInputTextVar)
    antonymInputEntry.bind('<Return>', generateAntonymTrigger)
    antonymInputEntry.grid(row=1, column=0, sticky="ew", padx=32)

    antonymGenerateButton = ctk.CTkButton(centralizeFrame, text=">", fg_color=defaultTheme["primary-button-color"], width=55, command=generateAntonymTrigger)
    antonymGenerateButton.grid(row=1, column=1, sticky="ew", padx=8)

    global antonymOutputEntry
    antonymOutputEntry = ctk.CTkEntry(centralizeFrame, font=ctk.CTkFont(size=15), state="disabled")
    antonymOutputEntry.grid(row=1, column=2, sticky="ew", padx=32)

    # Separador
    sectionSpacer = ctk.CTkFrame(centralizeFrame, fg_color="transparent", height=10)
    sectionSpacer.grid(row=2, column=0, columnspan=3)

    # Sinonimo

    synonymTitleLabel = ctk.CTkLabel(centralizeFrame, text="• Gerar sinônimo •", font=ctk.CTkFont(size=25, weight='bold'))
    synonymTitleLabel.grid(row=3, column=0, columnspan=3, sticky="nswe", pady=20)

    global synonymInputEntry
    synonymInputTextVar = ctk.StringVar()
    synonymInputEntry = ctk.CTkEntry(centralizeFrame, font=ctk.CTkFont(size=15), placeholder_text="Sua palavra aqui.", textvariable=synonymInputTextVar)
    synonymInputEntry.bind('<Return>', generateSynonymTrigger)
    synonymInputEntry.grid(row=4, column=0, sticky="ew", padx=32)

    synonymGenerateButton = ctk.CTkButton(centralizeFrame, text=">", fg_color=defaultTheme["primary-button-color"], width=55, command=generateSynonymTrigger)
    synonymGenerateButton.grid(row=4, column=1, sticky="ew", padx=8)

    global synonymOutputEntry
    synonymOutputEntry = ctk.CTkEntry(centralizeFrame, font=ctk.CTkFont(size=15), state="disabled")
    synonymOutputEntry.grid(row=4, column=2, sticky="ew", padx=32)

    # Separador 2
    sectionSpacer2 = ctk.CTkFrame(centralizeFrame, fg_color="transparent", height=20)
    sectionSpacer2.grid(row=5, column=0, columnspan=3)

    # Retorna o valor da interface

    return wordReplaceGuiFrame

# Função que será chamada ao apertar ENTER ou no botão para gerar um Antônimo
def generateAntonymTrigger(event=None):
    antonymInput = antonymInputEntry.get()

    if (antonymInput != ""):
        aiResponse = generateAntonym(antonymInput).splitlines()[0]
        if aiResponse != "anerroroccored":
            antonymOutputEntry.configure(state="normal")
            antonymOutputEntry.delete('0', 'end')
            antonymOutputEntry.insert('0', aiResponse)
            antonymOutputEntry.configure(state="disabled")
            setDefaultText()
        else: # Caso ocorra algum erro
            setWarningText("Ocorreu um erro com a API!\nNormalmente isto acontece quando você faz\nmuitos prompts em pouco tempo.\n\nTente de novo mais tarde, ou tente\nusar outro prompt.", defaultTheme["danger-color"])
    else:
        print("Input vazio")

# Função que será chamada ao apertar ENTER ou no botão para gerar um Sinonimo
def generateSynonymTrigger(event=None):
    synonymInput = synonymInputEntry.get()

    if (synonymInput != ""):
        aiResponse = generateSynonym(synonymInput).splitlines()[0]
        if aiResponse != "anerroroccored":
            synonymOutputEntry.configure(state="normal")
            synonymOutputEntry.delete('0', 'end')
            synonymOutputEntry.insert('0', aiResponse)
            synonymOutputEntry.configure(state="disabled")
            setDefaultText()
        else: # Caso ocorra algum erro
            setWarningText("Ocorreu um erro com a API!\nNormalmente isto acontece quando você faz\nmuitos prompts em pouco tempo.\n\nTente de novo mais tarde, ou tente\nusar outro prompt.", defaultTheme["danger-color"])
    else:
        print("Input vazio")
    return