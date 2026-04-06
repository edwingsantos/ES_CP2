#ES 
import tkinter as tk 

root = tk.Tk()

root.title("Testing")
root.configure(background="orange")
root.minsize(250, 250)
root.maxsize(1000, 1000)
root.geometry("300x300+100+100")
label = tk.Label(root, text="This is currently working")
label.config(fg = "blue", background="orange",font=("Times New Roman", 14, "bold"))
#diff thing
root.count = 0 
def add():
    root.count +=1 
    tk.Label(root, text=root.count).pack


btn = tk.Button(root, text="ADD", command=add)
btn.pack()




label.pack()
#image = tk.PhotoImage(file="Notes/291_4k.png")
#tk.Label(root, image=image).pack()

root.mainloop()