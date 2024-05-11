# Importando bibliotecas
import customtkinter as ctk
import os
from PIL import Image, ImageTk
import threading

# Importando outros Scripts
from gui.wordReplacegui import createWordReplaceGui as wordReplacegui
from gui.aboutgui import createAboutGui as aboutgui
from gui.settingsgui import createSettingsGui as settingsgui
from gui.definitionsgui import createDefinitionGui as definitiongui
from functions.generativeai import connectApi
import functions.settings as gsettings # gsettings = General Settings (Configurações Gerais)
from functions.warningText import setWarningText, setDefaultText

defaultTheme = gsettings.applyedTheme
activeWindow = []

# Cria uma janela gráfica usando a biblioteca tkinter, assim como elementos presentes nesta janela e estilização para eles.

mainWindow = ctk.CTk()

mainWindow.title("AI Writer Companion")
mainWindow.config(background=defaultTheme["background-color"])
mainWindow.geometry(f"900x500+{int((mainWindow.winfo_screenwidth()/2)-450)}+{int((mainWindow.winfo_screenheight()/2)-300)}")
mainWindow.minsize(900, 500)
mainWindow.iconbitmap(os.path.join(os.path.curdir, "media", "logo", "logo.ico"))

mainWindow.grid_columnconfigure(0, weight=0)
mainWindow.grid_columnconfigure(1, weight=1)
mainWindow.grid_rowconfigure(0, weight = 1)


# - Elementos do painel lateral

sidePanel = ctk.CTkFrame(mainWindow, fg_color=defaultTheme["secundary-color"], corner_radius=0)
sidePanel.grid(row=0, column=0, sticky="nsw")
sidePanel.grid_columnconfigure(0, weight=1)
sidePanel.grid_rowconfigure(0, weight=1)
#sidePanel.grid_rowconfigure(1, weight=0)

# - Texto de Aviso

from functions.warningText import setupWarningText
setupWarningText(mainWindow)

# - - Centralizador

sideCenterPanel = ctk.CTkFrame(sidePanel, fg_color="transparent", corner_radius=0)
sideCenterPanel.grid(row=0, column=0, sticky="we", padx=25)
sideCenterPanel.grid_columnconfigure(0, weight=1)
sideCenterPanel.grid_columnconfigure(1, weight=1)
sideCenterPanel.grid_rowconfigure(0, weight=1)
sideCenterPanel.grid_rowconfigure(1, weight=1)
sideCenterPanel.grid_rowconfigure(2, weight=1)
sideCenterPanel.grid_rowconfigure(3, weight=1)

# - - Logo Banner

logobanner = ImageTk.PhotoImage(Image.open(os.path.join(os.path.curdir, "media", "banner", "banner_nobg_blackfont.png")).convert("RGBA").resize((int(250), int(114))))
logobannercanvas = ctk.CTkCanvas(sideCenterPanel, width=logobanner.width(), height=logobanner.height(), bg=defaultTheme["secundary-color"], highlightthickness=0)
logobannercanvas.create_image(logobanner.width()/2, logobanner.height()/2, image=logobanner)
logobannercanvas.grid(row=0,column=0,columnspan=2,pady=8)

# - - Botão Escreva comigo // ESTA ÁREA FOI DESATIVADA POR AINDA NÃO ESTAR COMPLETA //

def setWriteWithMode():
    changeSelectedButton(writeWithbutton)

writeWithbutton = ctk.CTkButton(sideCenterPanel, text="Escreva comigo", command=setWriteWithMode, fg_color="transparent", border_color=defaultTheme["primary-button-color"], border_width=3)
#writeWithbutton.pack(fill="x", padx=50, pady=8)

# - - Botão Sinonimos/Antônimos

def setWordReplaceMode():
    cleanActualScreen()
    changeSelectedButton(wordReplaceButton)
    activeWindow.append(wordReplacegui(mainWindow))

wordReplaceButton = ctk.CTkButton(sideCenterPanel, text="Sinônimos/Antônimos", command=setWordReplaceMode, fg_color="transparent", border_color=defaultTheme["primary-button-color"], border_width=3)
wordReplaceButton.grid(row=1,column=0,columnspan=2,pady=8,padx=5,sticky="we")

# - - Botão Significado

def setDefinitionMode():
    cleanActualScreen()
    changeSelectedButton(definitionButton)
    activeWindow.append(definitiongui(mainWindow)) # MUDAR AQUI

definitionButton = ctk.CTkButton(sideCenterPanel, text="Significado/Definições", command=setDefinitionMode, fg_color="transparent", border_color=defaultTheme["primary-button-color"], border_width=3)
definitionButton.grid(row=2,column=0,columnspan=2,pady=8,padx=5,sticky="we")

# - - Botão Configurações

def setConfigScreen():
    cleanActualScreen()
    changeSelectedButton(configButton)
    activeWindow.append(settingsgui(mainWindow))

configButton = ctk.CTkButton(sideCenterPanel, text="Configurações", command=setConfigScreen, fg_color="transparent", border_color=defaultTheme["primary-button-color"], border_width=3)
configButton.grid(row=3,column=0,pady=8,padx=5,sticky="we")

# - - Botão Sobre

def setAboutScreen():
    cleanActualScreen()
    changeSelectedButton(aboutButton)
    activeWindow.append(aboutgui(mainWindow))

aboutButton = ctk.CTkButton(sideCenterPanel, text="Sobre", command=setAboutScreen, fg_color="transparent", border_color=defaultTheme["primary-button-color"], border_width=3)
aboutButton.grid(row=3,column=1,pady=8,padx=5,sticky="we")

# - - - Alterações de Estilo do Botão Selecionado

allButtons = [writeWithbutton, wordReplaceButton, configButton, aboutButton, definitionButton]

def cleanActualScreen():
    for screen in activeWindow:
        screen.destroy()

def changeSelectedButton(actualButton):
    for button in allButtons:
        if button == actualButton:
            button.configure(fg_color = defaultTheme["primary-button-color"])
        else:
            button.configure(fg_color = "transparent")
    setDefaultText()

# Começa a tentar se conectar usando a chave de API e espera até o fim da thered

def startApiCheck():
    for button in allButtons:
            button.configure(state="disabled")
    
    apiT = threading.Thread(target=connectApi, args=[mainWindow]) # apitT = API Theread
    
    # - Texto de Aguardado conexão via API
    global waitingApiLabel
    waitingApiLabel = ctk.CTkLabel(mainWindow, text="• Tentando se conectar ao Google AI Studio\natravés da chave de API...", text_color="yellow", font=ctk.CTkFont(size=25), bg_color=gsettings.applyedTheme["background-color"])
    waitingApiLabel.grid(row=0, column=1)
    
    apiT.start()
    waitForApiRecheck(apiT)

def waitForApiRecheck(apiThread):
    mainWindow.after(1000, initialApiConnectionStatusCheck, apiThread)

def initialApiConnectionStatusCheck(apiThread):
    if not apiThread.is_alive():
        # Código a ser executado quando a conexão com a API for concluida
        waitingApiLabel.destroy()
        for button in allButtons:
            button.configure(state="enabled")
    else:
        waitForApiRecheck(apiThread)

startApiCheck()

# Inicia a janela gráfica
mainWindow.mainloop()