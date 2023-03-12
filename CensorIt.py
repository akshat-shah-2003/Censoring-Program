import tkinter as tk
import clipboard as cb

# Defining main logic function


def censor():
    t = entry.get()
    uncensored_set = ['darn', 'shoot', 'dang', 'freakin', 'heck', 'shit', 'hell', 'fuck', 'bloody', 'bastard', 'damn', 'dick', 'ass', 'bitch', 'butt']
    for i in uncensored_set:
        if i in t:
            t = t.replace(i, '*'*len(i))
        elif i.capitalize() in t:
            t = t.replace(i.capitalize(), '*'*len(i))
    if t == '':
        t = 'Oh shoot. Darn it! What the heck is going on in this freakin world?'
    else:
        label.config(text="\n"+" "+t+" "+"\n", fg='green')
    return t

# Defining copy function


def copytxt():
    t2 = censor()
    cb.copy(t2)


# Display window
root = tk.Tk()

# Window Interface
root.title("cᴇɴsoʀ ɪᴛ")
root.geometry("1000x350")
root['bg'] = 'light gray'

# Creating Menu bar About section
menubar = tk.Menu(root)
root.config(menu=menubar)
About = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="About", menu=About)
About.add_command(label="Censoring Program by :", font=('Calibri', 10))
About.add_separator()
About.add_command(label="Akshat Shah", font=('Calibri', 10))
About.add_command(label="Anup Dhoble", font=('Calibri', 10))
About.add_command(label="Himanshu Sharma", font=('Calibri', 10))

# Display label
label = tk.Label(root, text="\n    ENTER SOME TEXT    \n",
                 font=('Calibri', 15))
label.pack(padx=10, pady=20)

# Input Dialog box
entry = tk.Entry(root, width=60, font=('Calibri', 15))
entry.pack(padx=10, pady=10)

# Activating "Censor" button
button = tk.Button(root, text="Censor", command=censor,
                   width=8, font=('Calibri', 13))
button.pack(padx=10, pady=10)

# Activating "Copy Output" button
button2 = tk.Button(root, text="Get/Copy", command=copytxt,
                    width=8, font=('Calibri', 13))
button2.pack()

# Activating "Exit" button
button3 = tk.Button(root, text="Exit", command=root.destroy,
                    width=8, font=('Calibri', 13))
button3.pack(padx=10, pady=10)

root.mainloop()
