import hashlib
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import filedialog
from tkinter import Menu
from PIL import ImageTk,Image

import uuid
import hashlib


def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    
    
def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
 

def encrypt():
    mystring = txtarea.get('1.0', END)
    my_hashing_method = hashing_method.get()# get the hashing method
    
    if my_hashing_method == '1':
        hash_object = hashlib.sha256(mystring.encode('utf-8'))
        your_hash.delete(0, END)
        your_hash.insert(INSERT,str(hash_object.hexdigest()) )
        
    elif my_hashing_method == '2':
        hash_object = hashlib.md5(mystring.encode('utf-8'))
        your_hash.delete(0, END)
        your_hash.insert(INSERT,str(hash_object.hexdigest()) )
    
    else:
        your_hash.delete(0, END)
        your_hash.insert(INSERT,"ERROR: choose your hashing method")
        

def openfile():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/",
        title="Open Text file",
        filetypes=(("Text Files", "*.txt"),))

    tf = open(tf)
    data = tf.read()
    txtarea.insert(END, data)
    tf.close()
    
def saveFile():
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = str(txtarea.get(1.0, END)) # starts from `1.0`, not `0.0`
    f.write(text2save)
    f.close()
    
    
# create blank window
window = Tk()
window.title("Get your hash")

window.configure(background="white")
window.config(cursor="hand2")

# setting window size
window.geometry('500x550')

# variables
hashing_method = StringVar()
hashed_text = StringVar()

# canvas for background        
C = Canvas(window, bg="blue", height=250, width=300)

# background image
image = ImageTk.PhotoImage(file = sys.path[0]+"/bg.gif")
background = Label(image=image)
background.bind('<Configure>')
background.place(x=0,y=-0)

# ScrolledText widget
txtarea = scrolledtext.ScrolledText(window, width = 45, height = 15,bg = 'black', fg='white' )
txtarea.place(x=40,y=50)
txtarea.insert(INSERT,"Type your text here") # set scrolledtext content

# Add radio buttons widgets
selected = IntVar()
rad1 = Radiobutton(window,text='sha256', value=1,  font = ("Helvetica",10,"bold"), var = hashing_method)
rad2 = Radiobutton(window,text='md5', value=2,  font = ("Helvetica",10,"bold"), var = hashing_method)

rad1.place(x=155,y=390)
rad2.place(x=235,y=390)

lable_hashing_method = Label(text='choose the hash method',bg = "black",fg='yellow', font = ("Helvetica",10,"bold"))
lable_hashing_method.place(x=40,y=355)


# # ENCRYPTION BUTTON
btn_encrypt = Button(window, text = "hash text",bg = "black",fg='yellow', command = encrypt,font = ("Helvetica",14,'bold'))
btn_encrypt.place(x=170,y=430)


# your hash
your_hash_label = Label(text='your hash ',bg = "black",fg='yellow', font = ("Helvetica",10,"bold"))
your_hash_label.place(x=30,y=470)

your_hash = Entry(window, width=40, textvariable = hashed_text)
your_hash.place(x=30,y=490)



# KEY encryption
# txt_encryption = Entry(window, width = 20)
# txt_encryption.place(x=135,y=350)
# txt_encryption.focus() # set focus to entry widget -> can write text right away




# openfile button
openfiles = Button(window, text = "open file", bg = "black", fg = "white", command = openfile, font = ('calibri', 8, 'bold'))
openfiles.place(x = 375, y=410)

# save button
save_button = Button(window,text="save file",command=saveFile,height = 1, width = 6, bg = "black", fg = "green", font = ('calibri', 8, 'bold'))
save_button.place(x=375,y=450)

# quit button
quit_btt = Button(window, text = 'quit ', command = window.destroy,font =('calibri', 8, 'bold'), bg='black',foreground = 'red')
quit_btt.place(x=375,y=490)


window.mainloop()




