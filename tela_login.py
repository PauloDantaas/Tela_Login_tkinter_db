# Credits for the original author - Paulo Dantas

from time import sleep
from tkinter import *
from tkinter import messagebox
import mysql.connector



# -------------------Conexão com o DB --------------------------------#
try:
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = '815878330000',
        database = 'python_database'
    )
except Exception as error:
    messagebox.showwarning('Xampp not Connect', error)
#---------------------------------------------------------------------#


class Tela_Login:
    def __init__(self):
        self.window = Tk()
        self.window.title('Tela de Usuário')
        self.window.geometry('400x400+400+165')
        self.window.resizable(0,0)
        self.window.config(bg = 'white')

        global e_mail 
        global senha

        e_mail = StringVar()
        senha = StringVar()
        
        self.frame = Frame(self.window, bg='#05879c', width=400,height=1).place(x=1, y=67)
        
        self.text_login = Label(self.window, text = 'Login', font='Arial 30 bold', bg = 'white', fg = '#05879c').place(x= 145, y=15)
        self.text_usuario = Label(self.window, text = 'Seu e-mail ', font='Helvica 12 italic', bg = 'white', fg='#083238').place(x=0, y=130)
        self.entry_usuario = Entry(self.window,bd=3 ,font='Arial',bg='white',fg='black', width=40, textvariable=e_mail).place(x= 3, y=160, height=30)
      
        self.text_senha = Label(self.window, text = 'Sua senha', font='Helvica 12 italic', bg='white',fg = '#083238').place(x = 0, y = 225)
        self.entry_senha = Entry(self.window, bd=3,font='Arial',bg='white',fg='black',width=40,textvariable=senha ,show='*').place(x=3, y=254, height=30)
      
        self.button_logar = Button(self.window, text = 'Logar',bd = 0, font='Arial 12 bold', width =30, height=1, bg ='#05879c', fg='white', 
                                   command=self.logs).place(x=25,y=295)
               
        self.frame_BOTOM = Frame(self.window, bg='#cedee0', width=400, height=60).pack(side = BOTTOM)
        
        self.button_2 = Label(self.frame_BOTOM, text = 'Ainda não tem conta?',font='Arial 10 bold',
                              width=30, height =1, bg='#cedee0', fg ='black').place(x = 95, y = 360)
        
        self.button_cadastro = Button(self.frame_BOTOM,text = 'Cadastrar', bd = 0, font='Arial 10 bold',bg = '#cedee0', fg='#05879c' ,
                                      command=self.chamarTela_Cadastro,width=10, height=1).place(x=290, y= 360)
        
        self.window.mainloop()

    

   
 # -------------------Verificação de E-mail e Senha no MySQL --------------------------------#      
    def logs(self):
        
        mycursor = mydb.cursor()
        sql = "SELECT * FROM python_database.login WHERE BINARY Email='%s' AND BINARY password='%s'" % (e_mail.get(),senha.get())
        mycursor.execute(sql)
                     
        if mycursor.fetchone():
            msg = messagebox.showinfo('MySql','Autenticado !')
            
            if msg == 'ok':
                self.window.destroy()
                messagebox.showinfo('MySql','Logado !')
                

            elif e_mail.get() == '' and senha.get() == '':
                messagebox.showerror('MySql','Usuário ou Senha Inválidos !')     
        

        else:
            messagebox.showerror('MySql','Usuário ou Senha Inválidos !')
# ----------------------------------------------------------------------------------------------#        


    def chamarTela_Cadastro(self):
        mycursor = mydb.cursor()
        
        sql = "SELECT * FROM python_database.login;"
        mycursor.execute(sql)
                     
        if mycursor.fetchone():
            sleep(1)
            self.window.destroy()
            messagebox.showinfo('MySql!','Em Breve postarei aqui.')
            
        
        mycursor.close()

        
