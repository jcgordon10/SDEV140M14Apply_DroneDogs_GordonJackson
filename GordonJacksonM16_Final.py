# This program is written by Jackson Gordon

from tkinter import Tk, Label, messagebox, Button, Frame, Entry, END

class MAIN(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.parent = parent
        self.pack()
        self.make_widgets()

    def make_widgets(self):
        self.winfo_toplevel().title("Jackson Gordon")
        Label(self, text="Enter an integer:").grid(row=0, column=1, padx=30)            
        self.entInteger = Entry(self)
        self.entInteger.grid(row=0, column=2, padx=0)
        Button(self, text="Double", command=self.DoubleInt).grid(row=1, column=1, sticky="e", pady=10, padx=10)
        Button(self, text="Half", command=self.HalfInt).grid(row=1, column=2, sticky="w", pady=10, padx=10)
        Button(self, text="Squared", command=self.SquaredInt).grid(row=2, column=1, sticky="e", pady=10, padx=10)
        Button(self, text="Pie!", command=self.PieInt).grid(row=2, column=2, sticky="w", pady=10, padx=10)

    def DoubleInt(self):
        i = self.entInteger.get()
        if i == "":
            messagebox.showwarning(title="Warning!", message="No number was entered!")
        else:
            i = int(i)
            messagebox.showinfo(title="Doubled!", message="2 x " + str(i) + " = " + str(i*2) + "!")
            self.entInteger.delete(0, 'end')

    def HalfInt(self):
        i = self.entInteger.get()
        if i == "":
            messagebox.showwarning(title="Warning!", message="No number was entered!")
        else:
            i = int(i)
            messagebox.showinfo(title="Halved!", message=str(i) + " / 2 = " + str(i/2) + "!")
            self.entInteger.delete(0, 'end')
    
    def SquaredInt(self):
        i = self.entInteger.get()
        if i == "":
            messagebox.showwarning(title="Warning!", message="No number was entered!")
        else:
            i = int(i)
            messagebox.showinfo(title="Squared!", message=str(i) + " * " + str(i) + " = " + str(i*i) + "!")
            self.entInteger.delete(0, 'end')

    def PieInt(self):
        i = self.entInteger.get()
        if i == "":
            messagebox.showwarning(title="Warning!", message="No number was entered!")
        else:
            i = int(i)
            messagebox.showinfo(title="Not that kind of pie!", message=str(i) + " * Pi = " + str(i*3.14159265354) + "!")
            self.entInteger.delete(0, 'end')

root = Tk()
main = MAIN(root)
root.mainloop()