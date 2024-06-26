#importing modules
import customtkinter 
from customtkinter import *

#creating gui
class App(CTk):
    def __init__(self):
        super().__init__()

        #config gui 
        self.title('CALCULATOR')
        self.ewidth = 400
        self.bwidth = 80
        self.resizable(False,False)
        self.iconbitmap('ico.ico')

        #adding entry box
        self.display = CTkEntry(master=self,width=self.ewidth,)
        self.display.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
        
        #func for error handling
        def iserror(func, *args, **kw):
            try:
                func(*args, **kw)
                return False
            except Exception:
                return True

        #inserting numbers
        def number(num):
            self.display.insert(END,num)

        #clearall
        def clearall():
            self.display.delete(0,END)

        #insert oprations
        def opr(sym):
            self.display.insert(END,sym)
        
        #backspace
        def clear():
            all = self.display.get()
            self.display.delete(0,END)
            all = all[0:-1]
            self.display.insert(0,all)

        #calcuating
        def equal():

            #translating the input of user 
            table = {'x':'*','÷':'/','²':'**2','³':'**3','√':'**0.5'}
            value=self.display.get()
            value.maketrans(table)
            
            #check error
            if value.endswith(("+","-","x","÷")):
                return

            else :

                trans = value.maketrans(table)
                value = value.translate(trans)

                if iserror(eval,value) == True:
                    self.display.delete(0,END)
                    self.display.configure(placeholder_text="Syntax Error!")

                if any(l.isalpha() for l in value):
                    self.display.delete(0,END)
                    self.display.configure(placeholder_text="Error!")
                
                else:
                    #calculating
                    result = eval(value)

                    self.display.delete(0,END)
                    self.display.insert(0,result)
            
            
        
        #btn config
        self.btn0 = CTkButton(master=self,text=0, command=lambda: number(0),width=self.bwidth,fg_color='blue')
        self.btn1 = CTkButton(master=self,text=1, command=lambda: number(1),width=self.bwidth,fg_color='blue')
        self.btn2 = CTkButton(master=self,text=2, command=lambda: number(2),width=self.bwidth,fg_color='blue')
        self.btn3 = CTkButton(master=self,text=3, command=lambda: number(3),width=self.bwidth,fg_color='blue')
        self.btn4 = CTkButton(master=self,text=4, command=lambda: number(4),width=self.bwidth,fg_color='blue')
        self.btn5 = CTkButton(master=self,text=5, command=lambda: number(5),width=self.bwidth,fg_color='blue')
        self.btn6 = CTkButton(master=self,text=6, command=lambda: number(6),width=self.bwidth,fg_color='blue')
        self.btn7 = CTkButton(master=self,text=7, command=lambda: number(7),width=self.bwidth,fg_color='blue')
        self.btn8 = CTkButton(master=self,text=8, command=lambda: number(8),width=self.bwidth,fg_color='blue')
        self.btn9 = CTkButton(master=self,text=9, command=lambda: number(9),width=self.bwidth,fg_color='blue')


        #btn grid
        self.btn0.grid(row=5,column=1,pady=5,padx=10)
        self.btn1.grid(row=4,column=0,pady=5,padx=10)
        self.btn2.grid(row=4,column=1,pady=5,padx=10)
        self.btn3.grid(row=4,column=2,pady=5,padx=10)

        self.btn4.grid(row=3,column=0,pady=5,padx=10)
        self.btn5.grid(row=3,column=1,pady=5,padx=10)
        self.btn6.grid(row=3,column=2,pady=5,padx=10)
        
        self.btn7.grid(row=2,column=0,pady=5,padx=10)
        self.btn8.grid(row=2,column=1,pady=5,padx=10)
        self.btn9.grid(row=2,column=2,pady=5,padx=10)


        #opr btn config
        self.add = CTkButton(master=self,text="+",command=lambda: opr('+'),width=self.bwidth)
        self.sub = CTkButton(master=self,text="-",command=lambda: opr('-'),width=self.bwidth)
        self.mul = CTkButton(master=self,text="X",command=lambda: opr('x'),width=self.bwidth)
        self.div = CTkButton(master=self,text="÷",command=lambda: opr('÷'),width=self.bwidth)
        self.eq = CTkButton(master=self,text="=",command=lambda: equal(),width=self.bwidth)
        self.allc = CTkButton(master=self,text="C",command=lambda:clearall(),width=self.bwidth,fg_color='red')
        self.clear = CTkButton(master=self,text="<--",command=lambda:clear(),width=self.bwidth,fg_color='red')
        self.sqb = CTkButton(master=self,text="x²", command=lambda: opr('²'),width=self.bwidth)
        self.cub = CTkButton(master=self,text="x³", command=lambda: opr("³"),width=self.bwidth)
        self.srb = CTkButton(master=self,text="(x)√", command=lambda: opr("√"),width=self.bwidth)


        #opr btn grid
        self.add.grid(row=2,column=3,pady=5,padx=10)
        self.sub.grid(row=3,column=3,pady=5,padx=10)
        self.mul.grid(row=4,column=3,pady=5,padx=10)
        self.div.grid(row=5,column=3,pady=5,padx=10)

        self.eq.grid(row=5,column=2,pady=5,padx=10)
        self.allc.grid(row=5,column=0,pady=5,padx=10)
        self.clear.grid(row=1,column=3,pady=5,padx=10)

        self.sqb.grid(row=1,column=0,pady=5,padx=10)
        self.srb.grid(row=1,column=1,pady=5,padx=10)
        self.cub.grid(row=1,column=2,pady=5,padx=10)






root = App()
root.mainloop()
