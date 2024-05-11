# Importando bibliotecas
import customtkinter as ctk
import functions.settings as gsettings

# - - Texto de avisos

def setupWarningText(anexwindow):
    global warningText
    warningText = ctk.CTkLabel(anexwindow, text="", fg_color=gsettings.applyedTheme["secundary-color"])
    warningText.grid(row=0, column=0, sticky="s")
    setDefaultText()

def setWarningText(text, color="white"):
    warningText.configure(text=text+"\n", text_color=color)
        

def setDefaultText():
    warningText.configure(text="Versão 0.1 (Dev)\n", text_color="gray")