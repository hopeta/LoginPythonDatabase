# importar as biblioteca das paradas
from ast import Pass
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from click import command
import DataBaser

# criar nossa janela
jan = Tk()
jan.title("DP System - Acess Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
#pra dar um charme na transparencia da parada
jan.attributes("-alpha", 0.9)
#agora pra formar um incone padrao, tenha o arquivo em formato ".ico"
jan.iconbitmap(default="icons/LogoIcon.ico")

#======carregar imagens=========
logo = PhotoImage(file="icons/logo.png")

#======widgets==================
#fazer uma paradinha do lado esquerdo, bonita e azul pra por o logotipo da empresa
LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

#agora doutro lado mona, nos podemos criar um separador
RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

#pra botar o logo tipo time
LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE",)
LogoLabel.place(x=50, y=100)

#agora o trem da direita
UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
UserLabel.place(x=5, y=100)

#entrada de dados User
UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150, y=110)

#Senhas
PassLabel = Label(RightFrame, text="Password", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
PassLabel.place(x=5, y=150)

#o detalhe show="*" impede o usuario de ver oq se digita mas retorna o valor real
PassEntry = ttk.Entry(RightFrame, width=30, show="*")
PassEntry.place(x=150, y=160)

#criando os botoes

def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()

    DataBaser.cursor.execute("""
    SELECT User, Password FROM Users
    WHERE User = ? AND Password = ?
    """, (User, Pass))
    print("Selecionou")
    VerifyLogin = DataBaser.cursor.fetchone()
    try:
        if (User in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title="Login Info", message="Acesso Confirmado. Bem Vindo!")
    except:
        messagebox.showinfo(title="Login Info", message="Acesso Negado. Verifique se está cadastrado no sistema!")

LoginButton = ttk.Button(RightFrame, text="Login", width=30, command=Login)
LoginButton.place(x=100, y=225)


def Register():
    #removendo widgets de Login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    #inserindo widgets de cadastro
    NomeLabel = Label(RightFrame, text="Name:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
    NomeLabel.place(x=5, y=5)

    NomeEntry= ttk.Entry(RightFrame, width=39)
    NomeEntry.place(x=100, y=16)

    EmailLabel = Label(RightFrame, text="Email:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    EmailLabel.place(x=5,y=55)

    EmailEntry= ttk.Entry(RightFrame, width=39)
    EmailEntry.place(x=100, y=66)

#pegando os valores de entrada para o database
    def RegisterDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()
#vamos verificar a existencia dos dados criando uma condição para criacao dos dados corretos

        if (Name == "" or Email =="" or User == "" or Pass == ""):
            messagebox.showerror(title="Register Error", message="Preencha todos os campos sem deixar nenhum vazio")
        else:
            DataBaser.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            """, (Name, Email, User, Pass))
            DataBaser.conn.commit()
            #o comando commit salva os valores inseridos no database, e essa alteraçao
            messagebox.showinfo(title="Register Info", message="Register Sucessfull")


    Register = ttk.Button(RightFrame, text="Register", width=30, command=RegisterDataBase)
    Register.place(x=100, y=225)


    def BackToLogin():
        #removendo widget cadastro 
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
        #Trazendo de volta os widget de login
        LoginButton.place(x=100)
        RegisterButton.place(x=125)

    Back = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin)
    Back.place(x=125, y=260)




RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command=Register)
RegisterButton.place(x=125, y=260)

jan.mainloop()