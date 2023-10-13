# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 16:59:19 2022

@author: saich
"""

from  tkinter import*
from tkinter import ttk
from tkinter import messagebox



import mysql.connector
# Creating connection object
mydb = mysql.connector.connect(
    host = "localhost",
    database="proj",
    user = 'root',
    password = "mercina"
)




root = Tk()
root.geometry("1352x650+0+0")
root.title("EXPENSE MANAGEMENT SYSTEM")
root.configure(background='black')



Tops = Frame(root, width=1350, height=100, bd=4, relief="raise")
Tops.pack(side=TOP)


lblInfo = Label(Tops, font=('arial', 49, 'bold'),text="EXPENSE MANAGEMENT SYSTEM ", bd=5, anchor='w')
lblInfo.grid(row=0, column=0)

bottom = Frame(root, width=1350, height=600, bd=4, relief="raise")
bottom .pack(side=TOP)

bottomLeft = Frame(bottom, width=1000, height=600, bd=4, relief="raise")
bottomLeft .pack(side=LEFT)
#===================================================================================================

bottomLeftTop = Frame(bottomLeft, width=5000, height=300, bd=2, relief="raise")
bottomLeftTop .pack(side=TOP)

bottomLeftTopL = Frame(bottomLeftTop, width=500, height=200, bd=2, relief="raise")
bottomLeftTopL .pack(side=LEFT)

bottomLeftTopR = Frame(bottomLeftTop, width=500, height=200, bd=2, relief="raise")
bottomLeftTopR .pack(side=RIGHT)
#===================================================================================================bottomLeftBottom
bottomLeftBottom = Frame(bottomLeft, width=1000, height=300, bd=2, relief="raise")
bottomLeftBottom .pack(side=BOTTOM)

bottomLeftBottomL = Frame(bottomLeftBottom, width=500, height=400, bd=2, relief="raise")
bottomLeftBottomL .pack(side=LEFT)

bottomLeftBottomR = Frame(bottomLeftBottom, width=500, height=400, bd=2, relief="raise")
bottomLeftBottomR .pack(side=RIGHT)
#===================================================================================================
bottomRight = Frame(bottom, width=350, height=600, bd=2, relief="raise")
bottomRight .pack(side=RIGHT)

#======================================================Exit=============================================
def iExit():
    iExit = messagebox.askyesno("EXPENSE MANAGEMENT SYSTEM", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return
#===================================================Reset===============================================
def Reset():
    
    Budget.set("0")
    
    Month.set("")
    
    
   # VAT.set("")
    #Discount.set("")
    #Tax.set("")
    #SubTotal.set("")
    Total.set("")
    txtReceipt.delete("1.0",END)
    
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    
    

    
#========================================================================================================

 
#=======================================================================================================
      
#=======================================================================================================

    
#=======================================================================================================
    if(var1.get() == 1):
        Food.set(5023)
    elif(var1.get() == 0):
        Food.set(0)
    if(var2.get() == 1):
        Laundry.set(356)
    elif(var2.get() == 0):
        Laundry.set(0)
    if(var3.get() == 1):
        Travelling.set(4699)
    elif(var3.get() == 0):
        Travelling.set(0)
    if(var4.get() == 1):
        Outing.set(10089)
    elif(var1.get() == 0):
        Outing.set(0)
    if(var5.get() == 1):
        Other.set(250)
    elif(var5.get() == 0):
        Other.set(0)
    if(var8.get() == 1):
        VAT.set("Yes")
    elif(var8.get() == 0):
        VAT.set("No")
    if(var9.get() == 1):
        Discount.set("Yes")
    elif(var9.get() == 0):
        Discount.set("No")

    Item1 = float(Budget.get())
    Item2 =  float( CarMileage.get())
    Item3 = float(Food.get())
    Item4 =  float( Laundry.get())
    Item5 = float(Travelling.get())
    Item6 =  float( Outing.get())
    Item7 =  float(Other.get())
    Item8 = "£" , str('%.2f'%((Item1 +Item2) + Item3 +Item4 + Item5 + Item6 + Item7))
    Item9 = ((Item1 - Item2) + Item3 + Item4 + Item5 + Item6 + Item7)
    Item9 = "£" , str('%.2f'%(Item9))
    Item10 = ((Item1 + Item2) +Item3 +Item4 +Item5 +Item6 +Item7)
    Item11 = ((Item1 + Item2) +Item3 +Item4 +Item5 +Item6 +Item7)                  
    Item12 = "£" , str('%.2f'%(Item10 + Item11))
    SubTotal.set(Item8)
    Tax.set(Item9)
    Total.set(Item12)

#=====================================================Reciept===========================================
#******
def Receipt():
    txtReceipt.delete("1.0",END)
    #txtReceipt.insert(END,'Items\t\t\t\t'+"Cost of Items \n\n")
    txtReceipt.insert(END,'======================================' "\n")
    txtReceipt.insert(END,'Month: ' + Month.get()+ "\n")
    txtReceipt.insert(END,'Budget: '+ Budget.get()+ "\n")
    txtReceipt.insert(END,'======================================' "\n")
    #txtReceipt.insert(END,'Type of Car: \t\t\t\t'+ var7.get()+ "\n")
    
    txtReceipt.insert(END,'Cost of Food: '+ Food.get()+ "\n")
    txtReceipt.insert(END,'Cost of Laundry: ' + Laundry.get()+ "\n")
    txtReceipt.insert(END,'Cost of Travelling:' + Travelling.get()+ "\n")
    txtReceipt.insert(END,'Cost of Outing:' + Outing.get()+ "\n")
    txtReceipt.insert(END,'Other cost: ' + Other.get()+ "\n")
    txtReceipt.insert(END,'=======================================' "\n")
    #txtReceipt.insert(END,'Tax: \t\t\t\t'+ Tax.get()+ "\n")
    #txtReceipt.insert(END,'SubTotal: \t\t\t\t'+ SubTotal.get()+ "\n")
    #txtReceipt.insert(END,'Total Cost: \t\t\t\t'+ float(GPS.get())+ "\n")
    k=int(Food.get())+int(Laundry.get())+int(Outing.get())+int(Travelling.get())+int(Other.get())
    s=str(k)
    txtReceipt.insert(END,'Total Expense:'+ s+ "\n")
    
    
    
    mycursor = mydb.cursor()

    sql = "INSERT INTO expense  VALUES (%s, %s)"
    #val = (CustomerName.get(), s)
    val = (Month.get(), s)
    mycursor.execute(sql, val)

    mydb.commit()
    mydb.close()
    
    
    
    
#********
#===================================================1===================================================  
#****
Month=StringVar()



lblMonth = Label(bottomLeftTopL, font=('arial',16,'bold'), text="Month", fg="black", width=15, bd=10, anchor='w')
lblMonth.grid(row=0, column=0)
txtMonth = Entry(bottomLeftTopL, font=('arial',16,'bold'), bd=2, width=24, bg="white", justify='left', textvariable=Month)
txtMonth.grid(row=0, column=1)

#******
#====================================================================================================
#*************************
Food=StringVar()
Laundry=StringVar()
Outing=StringVar()
Travelling=StringVar()
Other=StringVar()


Food.set("0")
Laundry.set("0")
Outing.set("0")
Travelling.set("0")
Other.set("0")

var1= IntVar()
var2= IntVar()
var3= IntVar()
var4= IntVar()
var5= IntVar()



lblFood = Checkbutton(bottomLeftBottomL, font=('arial',16,'bold'), text="Cost of Food", fg="black", width=20,bd=10, anchor='w', onvalue=1, offvalue=0, variable=var1)
lblFood.grid(row=0,column=0)
txtFood = Entry(bottomLeftBottomL,font=('arial',16,'bold'), bd=2, width=14, bg="white", justify='left', textvariable=Food)
txtFood.grid(row=0,column=1)

lblLaundry = Checkbutton(bottomLeftBottomL, font=('arial',16,'bold'),text="Cost of Laundry", fg="black", width=20,bd=10, anchor='w', onvalue=1, offvalue=0, variable=var2)
lblLaundry.grid(row=1,column=0)
txtLaundry = Entry(bottomLeftBottomL, font=('arial',16,'bold'), bd=2, width=14, bg="white", justify='left', textvariable=Laundry)
txtLaundry.grid(row=1,column=1)

lblTravelling = Checkbutton(bottomLeftBottomL, font=('arial',16,'bold'), text="Cost of Travelling", fg="black", width=20,bd=10, anchor='w', onvalue=1, offvalue=0, variable=var3)
lblTravelling.grid(row=2, column=0)
txtTravelling = Entry(bottomLeftBottomL, font=('arial',16,'bold'), bd=2, width=14, bg="white", justify='left', textvariable=Travelling)
txtTravelling.grid(row=2, column=1)

lblOuting = Checkbutton(bottomLeftBottomL, font=('arial',16,'bold'), text="Cost of Outing", fg="black", width=20,bd=10, anchor='w', onvalue=1, offvalue=0, variable=var4)
lblOuting.grid(row=3, column=0)
txtOuting = Entry(bottomLeftBottomL, font=('arial',16,'bold'), bd=2, width=14, bg="white", justify='left', textvariable=Outing)
txtOuting.grid(row=3, column=1)

lblOther = Checkbutton(bottomLeftBottomL, font=('arial',16,'bold'), text="Other Cost", fg="black", width=20,bd=10, anchor='w', onvalue=1, offvalue=0, variable=var5)
lblOther.grid(row=4, column=0)
txtOther = Entry(bottomLeftBottomL, font=('arial',16,'bold'), bd=2, width=14, bg="white", justify='left', textvariable=Other)
txtOther.grid(row=4, column=1)


#btnTotalCost=Button(bottomLeftBottomL,pady=8, bd=2, fg="black",font=('arial', 16,'bold'), width=13, text="Total", bg="white",command=CarCost).grid(row=5, column=0)

btnReceipt=Button(bottomLeftBottomL,pady=8, bd=2, fg="black",font=('arial', 16,'bold'), width=13, text="Receipt", bg="white",command=Receipt).grid(row=5, column=0)
#*************************
#==========================================================2===========================================
#********
var6=IntVar()
var7= StringVar()
var18= StringVar()

Budget= StringVar()

Budget.set("0")
#********


lblBudget= Label(bottomLeftTopR, font=('arial',16, 'bold'),text="Budget", fg="black", width=13,bd=14, anchor='w')
lblBudget.grid(row=1,column=0)
txtBudget = Entry(bottomLeftTopR,font=('arial',16, 'bold'), bd=2, width=16,bg="white", justify = 'left', textvariable=Budget)
txtBudget.grid(row=2,column=0)


#***********
#=============================================================3================================================

#********
#VAT= StringVar()
#Discount= StringVar()
#Tax= StringVar()
SubTotal= StringVar()
Total= StringVar()

var8= IntVar()
var9= IntVar()
 

                    




#btnReset=Button(bottomLeftBottomR,pady=8, bd=2, fg="black",font=('arial', 16,'bold'),width=13,text="Reset", bg="white", command=Reset).grid(row=10, column=0)

#btnExit=Button(bottomLeftBottomR,pady=8, bd=2, fg="black",font=('arial', 16,'bold'),width=13,text="Exit", bg="white", command=iExit).grid(row=10, column=1)

#******
#===============================================4==================================================================================

lblReceipt = Label(bottomRight,font=('arial',16, 'bold') ,text="Expenses:",bd=2,anchor='w')
lblReceipt.grid(row=0,column=0, sticky=W)
txtReceipt = Text(bottomRight,font=('arial', 11, 'bold'), bd=8, width=46, height=26, bg="white")
txtReceipt.grid(row=1,column=0)
mycursor = mydb.cursor()
m=input("Enter month to get total expense:")
s=(m,)
sql = "SELECT * FROM expense WHERE month = %s"

mycursor.execute(sql,s)

myresult = mycursor.fetchone()

print(myresult)

root.mainloop()