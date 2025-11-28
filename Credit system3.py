def exit():
    window.destroy()
 
def convert():
    c1 = float(m1.get())
    c2 = float(m2.get())
    c = float(e1.get())
    p = 1+c1/100
    f = ((c*(p**c2)*(p-1)))/(p**c2-1)
    t1.config(state='normal')
    t1.delete('1.0', tk.END)
    t1.insert(tk.END,f)
    t1.config(state='disabled')

import tkinter as tk
window = tk.Tk()
window.geometry("500x450")
window.config(bg="#A569BD")
window.resizable(width=False,height=False)
window.title('Calcul de payment de Crédit système!')
 
l1 = tk.Label(window,text="Payment annuel de Credit",font=("Arial", 35),fg="white",bg="black")
l2= tk.Label(window,text="Credit Total(USD dollars): ",font=("Arial", 10,"bold"),fg="white",bg="#A569BD")
l3= tk.Label(window,text="Taut d'intêtet de Crédit % ",font=("Arial", 10,"bold"),fg="white",bg="#A569BD")
l4= tk.Label(window,text="Durée de Crédit(nombre d'années) ",font=("Arial", 10,"bold"),fg="white",bg="#A569BD")
l5= tk.Label(window,text="Payement annuel est : ",font=("Arial", 10,"bold"),fg="white",bg="#A569BD")
 
empty_l1 = tk.Label(window,bg="#A569BD")
empty_l2 = tk.Label(window,bg="#A569BD")
empty_l3 = tk.Label(window,bg="#A569BD")
empty_l4 = tk.Label(window,bg="#A569BD")
 
e1= tk.Entry(window,font=('Arial',20))
m1= tk.Entry(window,font=('Arial',20))

m2= tk.Entry(window,font=('Arial',20))
 
btn1 = tk.Button(window,text="Somme annuel à payer!",font=("Arial", 10),command=convert)
btn2 = tk.Button(window,text="Quitter program",font=("Arial", 10),command=exit)
 
t1=tk.Text(window,state="disabled",width=15,height=0)
 
l1.pack()
l2.pack()
e1.pack()
l3.pack()
m1.pack()
l4.pack()
m2.pack()
e1.pack()
empty_l1.pack()
m1.pack()
empty_l2.pack()
m2.pack()
empty_l3.pack()
empty_l4.pack()
btn1.pack()
l5.pack()
t1.pack()
empty_l2.pack()
btn2.pack()
 
window.mainloop()
