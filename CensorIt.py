import tkinter as tk
import clipboard as cb

# Defining main logic function
def censor():
    t=entry.get()
    uncensored_set=['darn','shoot','dang','freakin','heck']
    for i in uncensored_set:
      if i in t:
        t=t.replace(i,'*'*len(i))
      elif i.capitalize() in t:  
        t=t.replace(i.capitalize(),'*'*len(i))
    label.config(text="\n"+" "+t+" "+"\n",fg='green')
    return str(t)
        
# Defining copy function
def copytxt():
  t2=censor()
  cb.copy(t2)

# Initializing output window
root=tk.Tk()
    
# Window Interface
root.title("ᴄᴇɴsᴏʀ ɪᴛ")
root.geometry("1000x350")
root['bg']='light gray'

# Creating About section
menubar = tk.Menu(root)
root.config(menu=menubar)
About = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="About", menu=About)
About.add_command(label="Censoring Program by :",font=('Calibri',10))
About.add_separator()
About.add_command(label="Anup Dhoble",font=('Calibri',10))
About.add_command(label="Himanshu Sharma",font=('Calibri',10))
About.add_command(label="Akshat Shah",font=('Calibri',10))

# Display Interface
label=tk.Label(root,text="\n    ENTER SOME TEXT    \n",font=('Calibri',15))
label.pack(padx=10,pady=20)

# Input text box interface
entry=tk.Entry(root,width=60,font=('Calibri',15))
entry.pack(padx=10,pady=10)

# Activating "Censor" button
button=tk.Button(root,text="Censor",command=censor,width=8,font=('Calibri',13))
button.pack(padx=10,pady=10)

# Activating "Copy Output" button
button2=tk.Button(root, text="Copy",command=copytxt,width=8,font=('Calibri',13))
button2.pack()

# Activating "Exit" button
button3=tk.Button(root,text="Exit",command=root.destroy,width=8,font=('Calibri',13))
button3.pack(padx=10,pady=10)

root.mainloop()
