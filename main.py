from tkinter import *





# Define colors
color1 = "Black"
color2 = "LightBlue"
color3 = "White"
color4 = "Snow"

# Define correct password and username
correct_password = "12345"
correct_username = 'igor'

# Function to verify login
def confirm(event=None):
    
    username_entered = entry_username.get()
    password_entered = entry_password.get()
    
    if username_entered == correct_username and password_entered == correct_password:
        open_main_page()
    elif username_entered == correct_username and password_entered != correct_password:

        error_label_password.config(text="Login falhou, tente outra senha")
        entry_password.delete(0, 'end')
    elif username_entered != correct_username and password_entered != correct_password:
        error_label_password.config(text="Login falhou, senha e nome de usuario errados")
        entry_username.delete(0, 'end')
        entry_password.delete(0, 'end')
    else:
        error_label_username.config(text="Login falhou, nome de usuario errado ")
        entry_username.delete(0, 'end')
        entry_username.focus()
        

# Function to open main page
def open_main_page():

    main_page = Toplevel(root)
    main_page.title('Main Page')
    main_page.geometry('400x300')
    
    label = Label(main_page, text=f'Login feito com sucesso! Bem-Vindo, {correct_username}!')
    label.pack()

# Login window
root = Tk()
root.title('Login')
root.geometry('500x650')
root.config(background=color3)
root.resizable(width=False, height=False)


login_label = Label(root, text='Login', fg=color2, font=('Arial', 40, 'bold'), bg=color3)
login_label.place(x=20, y=20)

username_text = Label(root, text='Nome:', font=('Arial', 15, 'bold'),fg=color1, bg=color3,)
username_text.place(x=30, y=150)
entry_username = Entry(root, width=30)
entry_username.place(x=110, y=160)
entry_username.focus()


error_label_username = Label(root, fg='red')
error_label_username.place(x=30, y=180)


password_text = Label(root, text='Senha:', font=('Arial', 15, 'bold'),fg=color1, bg=color3)
password_text.place(x=30, y=200)
entry_password = Entry(root, show='*', width=30)
entry_password.place(x=110, y=200)
entry_password.bind("<Return>", confirm)

error_label_password = Label(root, fg='red')
error_label_password.place(x=30, y=270)

# Criar botão com a imagem redimensionada
login_button = Button(root, command=confirm, text="Login")
login_button.place(x=30, y=230)

root.mainloop()
