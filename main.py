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
def confirm():
    
    username_entered = entry_username.get()
    password_entered = entry_password.get()
    
    if username_entered == correct_username and password_entered == correct_password:
        open_main_page()
    else:

        error_label.config(text="Login falhou, tente novamente")
        entry_password.delete(0, 'end')

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
root.geometry('300x350')
root.config(background=color3)
root.resizable(width=False, height=False)


login_label = Label(root, text='Login', fg=color2, font=('Arial', 40, 'bold'))
login_label.place(x=20, y=20)

username_text = Label(root, text='Nome:', fg=color1)
username_text.place(x=30, y=150)
entry_username = Entry(root)
entry_username.place(x=90, y=150)
entry_username.focus()


password_text = Label(root, text='Senha:', fg=color1)
password_text.place(x=30, y=200)
entry_password = Entry(root, show='*')
entry_password.place(x=90, y=200)

error_label = Label(root, fg='red')
error_label.place(x=30, y=270)

login_button = Button(root, command=confirm, text="Login", bg=color4)
login_button.place(x=30, y=230)

root.mainloop()
