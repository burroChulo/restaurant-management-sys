import sqlite3
import csv
import os
from datetime import *
from pytz import *
import tkinter as tk
import tkinter.ttk as ttk
#import tkmacosx as tmacc
#from tkmacosx import Button
from PIL import Image, ImageTk

def new_id():
    conn = sqlite3.connect("z_employees.db")
    cursor = conn.cursor()
    cursor.execute("SELECT emp_id FROM employees ORDER BY emp_id DESC LIMIT 1")
    
    student = cursor.fetchone()
    number = student[0]
    newid = int(number) + 1
    
    return newid

def update_table(number):
    #check availability
    check = sqlite3.connect("z_tables.db")
    cursor = check.cursor()
    cursor.execute("SELECT available FROM tables WHERE table_number = ?", (number,))

    item = cursor.fetchone()

    update = sqlite3.connect("z_tables.db")
    uCursor = update.cursor()
    if item[0] == "AVAILABLE":
        uCursor.execute("UPDATE tables SET available = ? WHERE table_number = ?", ("UNAVAILABLE", number,))
    else:
        uCursor.execute("UPDATE tables SET available = ? WHERE table_number = ?", ("AVAILABLE", number,))
    update.commit()
    update.close()

def new_order(number):
    title = "Table" + str(number)
    timeZone = datetime.now(timezone("America/New_York"))
    time = timeZone.strftime("%I:%M %p")

    file_path = f"{title}.txt"

    poll = []

    if os.path.exists(file_path):
        print("already Exists")
        with open (f"orders.txt", "r") as f:
            data=f.readlines()
            datall =  data[0].split()
            print(datall)
            for info in datall:
                if info != str(number):
                    poll.append(info)
                    print(poll)
        with open (f"{title}.txt", "w") as f:
            writing = csv.writer(f)
            writing.writerow(poll)
            


    else:
        passReveal = open(f"{title}.txt", "w")
        passReveal.write(f"{time}\n")
        passReveal.close()

        global listofOrders
        listofOrders = []
        grades_reader=open('orders.txt', 'r')
        for row in grades_reader:
            listofOrders = row.split()

        print(listofOrders)

    with open("orders.txt", "r", newline='') as f:
        if str(number) not in f: 
            with open("orders.txt", "a", newline='') as fr:
                fr.write(f"{number} ")  

def update_order(tableNum, itemNum, quant):
    titke = f"Table{tableNum}.txt"
    conn = sqlite3.connect("z_items.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE item_id = ?", (itemNum,))
    
    item = cursor.fetchone()
    
    total = item[3]*quant
    newInfo = [ tableNum, itemNum, quant, total ]

    with open(f"{titke}", "a", newline='') as file:
        start = csv.writer(file)
        start.writerow(newInfo)

def finishing_order(tableNum, debitOrCash):
    if debitOrCash == 1:
        newInfo = [ "Credit/Debit" ]
    else:
        newInfo = [ "Cash" ]

    with open(f"Table {tableNum}.txt", "a", newline='') as file:
        start = csv.writer(file)
        start.writerow(newInfo)
        pass



def boss_hompage():
    boss = tk.Toplevel(root)
    boss.geometry("1488x945")
    s = tk.Label(boss, image=b_hub).pack()

    header = tk.Label(boss, 
                      text="BOSS",
                      font=('Didot', 48), 
                      bg="#ED3266", fg="white")
    header.place(relx = 0.44, rely = 0.01)

    signoutButton = tk.Button(boss, 
                              image = b_signOut, 
                              bg="white", 
                              highlightthickness=0, takefocus=0, bd=0, 
                              command = lambda: [signInn(), boss.withdraw()])
    signoutButton.place(relx = 0.75, rely = 0.85)

    rev = tk.Button(boss, 
                        image = b_revenue, 
                        bg="white", 
                        highlightthickness=0, takefocus=0, bd=0, 
                        command = lambda: [revenue(), boss.withdraw()])
    rev.place(relx = 0.1, rely = 0.2)

    newAccount = tk.Button(boss, 
                           image = b_createAccount, 
                           bg="white", 
                           highlightthickness=0, takefocus=0, bd=0, 
                           command = lambda: [signUp(), boss.withdraw()])
    newAccount.place(relx = 0.55, rely = 0.2)

def revenue():
    boss = tk.Toplevel(root)
    boss.geometry("1488x945")
    s = tk.Label(boss, image=b_hub).pack()

    back_button = tk.Button(boss, 
                            image=backButt, 
                            bg="#FEB5C9", 
                            highlightthickness = 0, bd = 0, 
                            command= lambda: [boss_hompage(), boss.withdraw()])
    back_button.place(relx=0.06, rely=0.07, anchor= 'center')

    header = tk.Label(boss, 
                      text="REVENUE",
                      font=('Didot', 48), 
                      bg="#ED3266", fg="white")
    header.place(relx = 0.4, rely = 0.01)

    canva = tk.Canvas(boss, 
                       bg="white",
                       width=1276, height=737,
                       highlightthickness=0)
    canva.place(x = 106, y = 132)

    canva.create_text(550, 50, 
                       text="Summary", 
                       font=("Didot", 36), 
                       anchor='nw', 
                       fill="black")
    canva.create_text(250, 250, 
                       text="Total\nRevenue", 
                       font=("Didot", 30), 
                       anchor='nw', 
                       fill="black")

def signUp():
    signUpPage = tk.Toplevel(root)
    signUpPage.geometry("1488x945")
    
    s = tk.Label(signUpPage, image=s_l_page).pack()
    
    sign_up = tk.Label(signUpPage, text="Sign Up", font=('Didot', 48),fg="black",bg="white")
    sign_up.place(relx = 0.43, rely = 0.249)

    fname = tk.Label(signUpPage, text="Full Name:", font=('Didot', 32),fg="black",bg="white")
    fname.place(relx = 0.3, rely = 0.4)

    email = tk.Label(signUpPage, text="Email:", font=('Didot', 32),fg="black",bg="white")
    email.place(relx = 0.345, rely = 0.5)
    
    password = tk.Label(signUpPage, text="Password:", font=('Didot', 32),fg="black",bg="white")
    password.place(relx = 0.31, rely = 0.6)


    back_button = tk.Button(signUpPage,
                            image=backButt,
                            bg="#FFE2EA", highlightthickness = 0, bd = 0, 
                            command=lambda: [boss_hompage(), signUpPage.withdraw()])
    back_button.place(relx=0.05, rely=0.05, anchor= 'center')
    
    name = tk.Entry(signUpPage, 
                    width = 22, 
                    font=("Inria Sans", 25),
                    fg="#FF88A9",bg="#FFE2EA",
                    highlightthickness = 0, bd = 0)
    name.place(relx = 0.435, rely = 0.41)
    
    email = tk.Entry(signUpPage,
                     width = 22, 
                     font=("Inria Sans", 25),
                     fg="#FF88A9",bg="#FFE2EA",
                     highlightthickness = 0, bd = 0)
    email.place(relx = 0.435, rely = 0.51)
    
    peew = tk.Entry(signUpPage,
                  width = 22,
                  font=("Inria Sans", 25),
                  fg="#FF88A9",bg="#FFE2EA",
                  highlightthickness = 0, bd = 0)
    peew.place(relx = 0.435, rely = 0.61)
    
    def adding():
        empId = new_id()
        my_list = name.get().split()
        first = my_list[0]
        last = my_list[1]
        emmy = email.get()
        user = first+last[0]+str(empId)
        passer = peew.get()

        datas = (empId, first, last, emmy, user, passer, 15.0)

        conn = sqlite3.connect("z_employees.db")
        cursor = conn.cursor()
        cursor.executemany("""
                        INSERT OR IGNORE INTO employees (emp_id, f_name, l_name, email, username, password, wage) 
                        VALUES (?, ?, ?, ?, ?, ?, ?)""", 
                        [datas
                        ])
        conn.commit()
        conn.close()

        completion = tk.Frame(signUpPage,  
                              bg ="black",
                              highlightbackground="#FF88A9", highlightthickness=2)
        completion.place(relx = 0.3, rely = 0.3)
        comp = tk.Label(completion,
                        image=b_signUpComplete)
        comp.pack()
        signUpPage.after(750, lambda: [completion.destroy(), boss_hompage(), signUpPage.withdraw()])


    sUp = tk.Button(signUpPage, image = signUpButt, bg="#FFFFFF", highlightthickness=0, bd=0,
                    command=adding)
    sUp.place(relx = 0.38, rely = 0.7)


def host_hompage():
    host = tk.Toplevel(root)
    host.geometry("1488x945")
    s = tk.Label(host, image=host_homepage).pack()

    header = tk.Label(host, 
                      text=f"Welcome, {sexyUserFName}",
                      font=("Inter", 30, "bold"), 
                      bg="white", fg="black")
    header.place(relx = 0.1, rely = 0.23)

    subHeader = tk.Label(host, 
                      text="End Job",
                      font=("Inter", 30, "bold"), 
                      bg="white", fg="black")
    subHeader.place(relx = 0.215, rely = 0.39)

    signoutButton = tk.Button(host, 
                              image = home_signOutButt, 
                              bg="white", 
                              highlightthickness=0, takefocus=0, bd=0, 
                              command = lambda: [signInn(), host.withdraw()])
    signoutButton.place(relx = 0.14, rely = 0.48)

    tableButt = tk.Button(host, 
                         image = home_tableButt, 
                         bg="white", 
                         highlightthickness=0, takefocus=0, bd=0, 
                         command = lambda: [tables(), host.withdraw()])
    tableButt.place(relx = 0.6, rely = 0.43)

def tables():
    tables = tk.Toplevel(root)
    tables.geometry("1488x945")
    s = tk.Label(tables, image=t_hub).pack()

    back_button = tk.Button(tables, 
                            image=backButt, 
                            bg="#FEB5C9", 
                            highlightthickness = 0, bd = 0, 
                            command= lambda: [host_hompage(), tables.withdraw()])
    back_button.place(relx=0.06, rely=0.05, anchor= 'center')

    tableFrame = tk.Frame(tables,  
                          bg ="#FEB5C9",
                          height=802, width=1488)
    tableFrame.place(relx = 0, rely = 0.14)

    def whenClicked(tableNumbers):
        print(tableNumbers)
        overlayer = tk.Frame(tables,  
                          bg ="#FEB5C9"
                          )
        overlayer.place(relx = 0.2, rely = 0.2)
        ss = tk.Label(overlayer, image=t_edit).pack()

        peep = sqlite3.connect("z_tables.db")
        purp = peep.cursor()
        purp.execute("SELECT available FROM tables WHERE table_number = ?", (tableNumbers,))
        
        item = purp.fetchone()

        info = tk.Label(overlayer,
                        text=f"{item[0]}:\nTable {tableNumbers}\n\nDo you wish to toggle?",
                        font=('Didot', 45),
                        bg ="#FFE2EA", fg = "black")
                        
        info.place(relx=0.2, rely=0.15)

        yes = tk.Button(overlayer,
                        image=t_yes,
                        bg ="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                        command = lambda: [new_order(tableNumbers), overlayer.destroy()])
        yes.place(relx=0.375, rely=0.575)
        
        no = tk.Button(overlayer,
                        image=t_no,
                        bg ="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                        command = lambda: [overlayer.destroy(), update_table(tableNumbers)] )                 
        no.place(relx=0.375, rely=0.725)



    def changePage():
        global page_one
        if page_one:
            for widget in tableFrame.winfo_children():
                widget.destroy()

            table1 = tk.Button(tableFrame, 
                            image = t_1, 
                            bg="#FEB5C9", highlightthickness=0, takefocus=0, bd=0, 
                            command = lambda: [whenClicked(1), update_table(1)] )
            table1.place(relx = 0.03, rely = 0)

            table2 = tk.Button(tableFrame, 
                            image = t_2, 
                            bg="#FEB5C9", highlightthickness=0, takefocus=0, bd=0, 
                            command = lambda: [whenClicked(2), update_table(2)] )
            table2.place(relx = 0.21, rely = 0)

            table3 = tk.Button(tableFrame, 
                            image = t_3, 
                            bg="#FEB5C9", highlightthickness=0, takefocus=0, bd=0, 
                            command = lambda: [whenClicked(3), update_table(3)] )
            table3.place(relx = 0.39, rely = 0)

            table4 = tk.Button(tableFrame, 
                            image = t_4, 
                            bg="#FEB5C9", highlightthickness=0, takefocus=0, bd=0, 
                            command = lambda: [whenClicked(4), update_table(4)] )
            table4.place(relx = 0.57, rely = 0)

            table5 = tk.Button(tableFrame, 
                            image = t_5, 
                            bg="#FEB5C9", highlightthickness=0, takefocus=0, bd=0, 
                            command = lambda: [whenClicked(5), update_table(5)] )
            table5.place(relx = 0.75, rely = 0)

            table6 = tk.Button(tableFrame, 
                            image = t_6, 
                            bg="#FEB5C9", highlightthickness=0, takefocus=0, bd=0, 
                            command = lambda: [whenClicked(6), update_table(6)] )
            table6.place(relx = 0.03, rely = 0.3)

            table7 = tk.Button(tableFrame, 
                            image = t_7, 
                            bg="#FEB5C9", highlightthickness=0, takefocus=0, bd=0, 
                            command = lambda: [whenClicked(7), update_table(7)] )
            table7.place(relx = 0.21, rely = 0.3)

            table8 = tk.Button(tableFrame, 
                            image = t_8, 
                            bg="#FEB5C9", highlightthickness=0, takefocus=0, bd=0, 
                            command = lambda: [whenClicked(8), update_table(8)] )
            table8.place(relx = 0.39, rely = 0.3)

            table9 = tk.Button(tableFrame, 
                            image = t_9, 
                            bg="#FEB5C9", highlightthickness=0, takefocus=0, bd=0, 
                            command = lambda: [whenClicked(9), update_table(9)] )
            table9.place(relx = 0.57, rely = 0.3)

            table10 = tk.Button(tableFrame, 
                            image = t_10, 
                            bg="#FEB5C9", highlightthickness=0, takefocus=0, bd=0, 
                            command = lambda: [whenClicked(10), update_table(10)] )
            table10.place(relx = 0.75, rely = 0.3)

            table11 = tk.Button(tableFrame, 
                            image = t_11, 
                            bg="#FEB5C9", highlightthickness=0, takefocus=0, bd=0, 
                            command = lambda: [whenClicked(11), update_table(11)] )
            table11.place(relx = 0.09, rely = 0.6)

            table12 = tk.Button(tableFrame, 
                            image = t_12, 
                            bg="#FEB5C9", highlightthickness=0, takefocus=0, bd=0, 
                            command = lambda: [whenClicked(12), update_table(12)] )
            table12.place(relx = 0.34, rely = 0.6)

            table13 = tk.Button(tableFrame, 
                            image = t_13, 
                            bg="#FEB5C9", highlightthickness=0, takefocus=0, bd=0, 
                            command = lambda: [whenClicked(13), update_table(13)] )
            table13.place(relx = 0.6, rely = 0.6)


            nextP = tk.Button(tableFrame, 
                            image = t_next, 
                            bg="#FEB5C9", highlightthickness=0, takefocus=0, bd=0, 
                            command = changePage)
            nextP.place(relx = 0.932, rely = 0)
            
            page_one = False
        else:
            for widget in tableFrame.winfo_children():
                widget.destroy()

            table14 = tk.Button(tableFrame, 
                                image = t_14, 
                                bg="#FEB5C9", highlightthickness=0, takefocus=0, bd=0, 
                                command = lambda: [whenClicked(14), update_table(14)] )
            table14.place(relx = 0.075, rely = 0)

            table15 = tk.Button(tableFrame, 
                                image = t_15, 
                                bg="#FEB5C9", highlightthickness=0, takefocus=0, bd=0, 
                                command = lambda: [whenClicked(15), update_table(15)] )
            table15.place(relx = 0.5, rely = 0)

            table16 = tk.Button(tableFrame, 
                                image = t_16, 
                                bg="#FEB5C9", highlightthickness=0, takefocus=0, bd=0, 
                                command = lambda: [whenClicked(16), update_table(16)] )
            table16.place(relx = 0.075, rely = 0.5)

            table17 = tk.Button(tableFrame, 
                                image = t_17, 
                                bg="#FEB5C9", highlightthickness=0, takefocus=0, bd=0, 
                                command = lambda: [whenClicked(17), update_table(17)] )
            table17.place(relx = 0.5, rely = 0.5)

            backP = tk.Button(tableFrame, 
                              image = t_back, 
                              bg="#FEB5C9", highlightthickness=0, takefocus=0, bd=0, 
                              command = changePage)
            backP.place(relx = 0, rely = 0)
        
            page_one = True
    
    changePage()


def waiter_hompage():
    waiter = tk.Toplevel(root)
    waiter.geometry("1488x945")
    s = tk.Label(waiter, image=waiter_homepage).pack()

    header = tk.Label(waiter, 
                      text=f"Welcome, {sexyUserFName}",
                      font=("Inter", 30, "bold"), 
                      bg="white", fg="black")
    header.place(relx = 0.1, rely = 0.23)

    subHeader = tk.Label(waiter, 
                      text="End Job",
                      font=("Inter", 30, "bold"), 
                      bg="white", fg="black")
    subHeader.place(relx = 0.215, rely = 0.39)

    signoutButton = tk.Button(waiter, 
                              image = home_signOutButt, 
                              bg="white", 
                              highlightthickness=0, bd=0, 
                              command = lambda: [signInn(), waiter.withdraw()])
    signoutButton.place(relx = 0.14, rely = 0.48)

    menuButt = tk.Button(waiter, 
                         image = home_menuButt, 
                         bg="white", 
                         highlightthickness=0, takefocus=0, bd=0, 
                         command = lambda: [menuHub(), waiter.withdraw()])
    menuButt.place(relx = 0.6, rely = 0.4)

    orderButt= tk.Button(waiter, 
                         image = home_ordersButt, 
                         bg="white", 
                         highlightthickness=0, bd=0, 
                         command = lambda: [orderHub(), waiter.withdraw()])
    orderButt.place(relx = 0.6, rely = 0.64)

def menuHub():
    menu = tk.Toplevel(root)
    menu.geometry("1488x945")
    s = tk.Label(menu, image=m_hub).pack()

    back_button = tk.Button(menu, 
                            image=backButt, 
                            bg="#CC5576", 
                            highlightthickness = 0, bd = 0, 
                            command= lambda: [waiter_hompage(), menu.withdraw()])
    back_button.place(relx=0.06, rely=0.07, anchor= 'center')
    header = tk.Label(menu, 
                      text="MENU",
                      font=('American Typewriter', 55),
                      bg="#CC5576", fg="black")
    header.place(relx = 0.42, rely = 0.04)


    beverages = tk.Button(menu, 
                          image = m_bev, 
                          bg="#FFE2EA", 
                          highlightthickness=0, takefocus=0, bd=0, 
                          command = lambda: [menus("BEVERAGES"), menu.withdraw()])
    beverages.place(relx = 0.08, rely = 0.25)

    appetizers = tk.Button(menu, 
                           image = m_appetizer, 
                           bg="#FFE2EA", 
                           highlightthickness=0, takefocus=0, bd=0, 
                           command = lambda: [menus("APPETIZERS"), menu.withdraw()])
    appetizers.place(relx = 0.6, rely = 0.25)

    mainCourses = tk.Button(menu, 
                            image = m_courses, 
                            bg="#FFE2EA", 
                            highlightthickness=0, takefocus=0, bd=0, 
                            command = lambda: [menus("MAIN COURSES"), menu.withdraw()])
    mainCourses.place(relx = 0.33, rely = 0.475)

    sides = tk.Button(menu, 
                      image = m_sides, 
                      bg="#FFE2EA", 
                      highlightthickness=0, takefocus=0, bd=0, 
                      command = lambda: [menus("SIDES"), menu.withdraw()])
    sides.place(relx = 0.08, rely = 0.75)

    desserts = tk.Button(menu, 
                         image = m_dessert, 
                         bg="#FFE2EA", 
                         highlightthickness=0, takefocus=0, bd=0, 
                         command = lambda: [menus("DESSERTS"), menu.withdraw()])
    desserts.place(relx = 0.6, rely = 0.75)

def menus(typo):
    menu = tk.Toplevel(root)
    menu.geometry("1488x945")
    s = tk.Label(menu, image=m_hub).pack()

    back_button = tk.Button(menu, 
                            image=backButt, 
                            bg="#CC5576", 
                            highlightthickness = 0, bd = 0, 
                            command= lambda: [menuHub(), menu.withdraw()])
    back_button.place(relx=0.06, rely=0.07, anchor= 'center')
    header = tk.Label(menu, 
                      text=typo,
                      font=('American Typewriter', 55),
                      bg="#CC5576", fg="black")
    header.place(relx = 0.35, rely = 0.04)

    def whenClicked(itemNum):
        overlayer = tk.Frame(menu,  
                          bg ="#FEB5C9"
                          )
        overlayer.place(relx = 0.2, rely = 0.2)
        ss = tk.Label(overlayer, image=t_edit).pack()

        info = tk.Label(overlayer,
                        text=f"Add to Order          :",
                        font=('Didot', 48),
                        bg ="#FFE2EA", fg = "white")                
        info.place(relx=0.225, rely=0.15)

        clicked = tk.StringVar() 
        
        # initial menu text 
        clicked.set( "--" ) 
        
        # Create Dropdown menu 
        drop = tk.OptionMenu(overlayer , clicked , *listofOrders)
        drop.config(font=("Didot", 48), bg ="#FFE2EA", fg = "black")
        drop.place(relx=0.55, rely=0.15)

        q = tk.Label(overlayer,
                        text=f"Quantity:",
                        font=('Didot', 48),
                        bg ="#FFE2EA", fg = "white")                
        q.place(relx=0.2, rely=0.25)
        quant = tk.Entry(overlayer, 
                    width = 10, 
                    font=("Inria Sans", 25), 
                    fg="black",bg="white")
        quant.place(relx = 0.425, rely = 0.275)

        yes = tk.Button(overlayer,
                        image=t_yes,
                        bg ="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                        command = lambda: [update_order(int(clicked.get()), itemNum, int(quant.get())), overlayer.destroy()])
        yes.place(relx=0.4, rely=0.55)
        
        no = tk.Button(overlayer,
                        image=t_no,
                        bg ="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                        command = lambda: [overlayer.destroy()] )                 
        no.place(relx=0.4, rely=0.7)


    foodFrame = tk.Frame(menu,  
                         bg ="#FFE2EA",
                         height=802, width=1488)
    foodFrame.place(relx = 0, rely = 0.14)
    
    if typo == "BEVERAGES":
        coke = tk.Button(foodFrame, 
                          image = d_coke, 
                          bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                          command = lambda: [whenClicked(1)] )
        coke.place(relx = 0.05, rely = 0.05)

        mangoSmoothie = tk.Button(foodFrame, 
                                  image = d_mango, 
                                  bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                                  command = lambda: [whenClicked(2)] )
        mangoSmoothie.place(relx = 0.225, rely = 0.05)

        water = tk.Button(foodFrame, 
                          image = d_water, 
                          bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                          command = lambda: [whenClicked(3)] )
        water.place(relx = 0.4, rely = 0.05)

        incaCola = tk.Button(foodFrame, 
                             image = d_inca, 
                             bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                             command = lambda: [whenClicked(4)])
        incaCola.place(relx = 0.55, rely = 0.05)

        morocho = tk.Button(foodFrame, 
                            image = d_morocho, 
                            bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                            command = lambda: [whenClicked(5)] )
        morocho.place(relx = 0.75, rely = 0.05)
        
        sprite = tk.Button(foodFrame, 
                           image = d_sprite, 
                           bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                           command = lambda: [whenClicked(6)] )
        sprite.place(relx = 0.075, rely = 0.5)

        strawberrySmoothie = tk.Button(foodFrame, 
                                        image = d_strawberry, 
                                        bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                                        command = lambda: [whenClicked(7)] )
        strawberrySmoothie.place(relx = 0.22, rely = 0.5)

        fanta = tk.Button(foodFrame, 
                            image = d_fanta, 
                            bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                            command = lambda: [whenClicked(8)] )
        fanta.place(relx = 0.4, rely = 0.5)

        chicha = tk.Button(foodFrame, 
                            image = d_chicha, 
                            bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                            command = lambda: [whenClicked(9)] )
        chicha.place(relx = 0.575, rely = 0.5)

        icedTea = tk.Button(foodFrame, 
                            image = d_tea, 
                            bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                            command = lambda: [whenClicked(10)] )
        icedTea.place(relx = 0.75, rely = 0.5)
    elif typo == "APPETIZERS":
        chipsWGuac = tk.Button(foodFrame, 
                          image = a_chips, 
                          bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                          command = lambda: [whenClicked(11)] )
        chipsWGuac.place(relx = 0.075, rely = 0.05)

        tamales = tk.Button(foodFrame, 
                                  image = a_tamales, 
                                  bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                                  command = lambda: [whenClicked(12)] )
        tamales.place(relx = 0.3, rely = 0.05)

        coxhinas = tk.Button(foodFrame, 
                          image = a_coxhinas, 
                          bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                          command = lambda: [whenClicked(13)] )
        coxhinas.place(relx = 0.53, rely = 0.075)

        humita = tk.Button(foodFrame, 
                             image = a_humita, 
                             bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                             command = lambda: [whenClicked(14)] )
        humita.place(relx = 0.73, rely = 0.15)

        paoQueso = tk.Button(foodFrame, 
                            image = a_paoQueso, 
                            bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                            command = lambda: [whenClicked(15)] )
        paoQueso.place(relx = 0.075, rely = 0.5)
        
        cheeseSticks = tk.Button(foodFrame, 
                           image = a_cheeseSticks, 
                           bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                           command = lambda: [whenClicked(16)] )
        cheeseSticks.place(relx = 0.3, rely = 0.5)

        empCarne = tk.Button(foodFrame, 
                                        image = a_empCarne, 
                                        bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                                        command = lambda: [whenClicked(17)] )
        empCarne.place(relx = 0.5, rely = 0.5)

        empQueso = tk.Button(foodFrame, 
                            image = a_empQueso, 
                            bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                            command = lambda: [whenClicked(18)] )
        empQueso.place(relx = 0.73, rely = 0.5)
    elif typo == "MAIN COURSES":
        ceviche = tk.Button(foodFrame, 
                            image = mc_ceviche, 
                            bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                            command = lambda: [whenClicked(19)] )
        ceviche.place(relx = 0.03, rely = 0.05)

        feijoada = tk.Button(foodFrame, 
                             image = mc_friijoles, 
                             bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                             command = lambda: [whenClicked(20)] )
        feijoada.place(relx = 0.25, rely = 0.05)

        steakTakos = tk.Button(foodFrame,
                               image = mc_steackTako, 
                               bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                               command = lambda: [whenClicked(21)] )
        steakTakos.place(relx = 0.42, rely = 0.05)

        pupusas = tk.Button(foodFrame,
                            image = mc_pupusas, 
                            bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                            command = lambda: [whenClicked(22)] )
        pupusas.place(relx = 0.625, rely = 0.05)

        salvadorTamas = tk.Button(foodFrame,
                                  image = mc_salvTamas, 
                                  bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                                  command = lambda: [whenClicked(23)] )
        salvadorTamas.place(relx = 0.8, rely = 0.05)
        
        mofongo = tk.Button(foodFrame, 
                            image = mc_mofongo, 
                            bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                            command = lambda: [whenClicked(24)] )
        mofongo.place(relx = 0.1, rely = 0.5)

        sopaDeRes = tk.Button(foodFrame,
                              image = mc_sopaRes, 
                              bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                              command = lambda: [whenClicked(25)] )
        sopaDeRes.place(relx = 0.3, rely = 0.5)

        habichuelas = tk.Button(foodFrame,
                                image = mc_habichuelasArroz, 
                                bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                                command = lambda: [whenClicked(26)] )
        habichuelas.place(relx = 0.5, rely = 0.5)

        tocino = tk.Button(foodFrame, 
                           image = mc_tocinoArroz, 
                           bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                           command = lambda: [whenClicked(27)] )
        tocino.place(relx = 0.7, rely = 0.5)
    elif typo == "SIDES":
        friedPlatano = tk.Button(foodFrame, 
                                 image = s_platano, 
                                 bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                                 command = lambda: [whenClicked(28)] )
        friedPlatano.place(relx = 0.05, rely = 0.05)

        tostones = tk.Button(foodFrame, 
                             image = s_tostones, 
                             bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                             command = lambda: [whenClicked(29)] )
        tostones.place(relx = 0.28, rely = 0.05)

        chicharones = tk.Button(foodFrame,
                                image = s_chicharones, 
                                bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                                command = lambda: [whenClicked(30)] )
        chicharones.place(relx = 0.48, rely = 0.05)

        beans = tk.Button(foodFrame,
                          image = s_beans, 
                          bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0,
                          command = lambda: [whenClicked(31)] )
        beans.place(relx = 0.7, rely = 0.05)

        whiteRice = tk.Button(foodFrame, 
                              image = s_wRice, 
                              bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                              command = lambda: [whenClicked(32)] )
        whiteRice.place(relx = 0.05, rely = 0.5)

        mexicanSalad = tk.Button(foodFrame,
                                 image = s_mCSalad, 
                                 bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                                 command = lambda: [whenClicked(33)] )
        mexicanSalad.place(relx = 0.27, rely = 0.5)

        farofa = tk.Button(foodFrame,
                           image = s_farofa, 
                           bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                           command = lambda: [whenClicked(34)] )
        farofa.place(relx = 0.485, rely = 0.5)

        fries = tk.Button(foodFrame, 
                          image = s_fries, 
                          bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                          command = lambda: [whenClicked(35)] )
        fries.place(relx = 0.7, rely = 0.5)
    elif typo == "DESSERTS":
        tresLeches = tk.Button(foodFrame, 
                               image = d_tresLeches, 
                               bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                               command = lambda: [whenClicked(36)] )
        tresLeches.place(relx = 0.05, rely = 0.05)

        acaiBowl = tk.Button(foodFrame, 
                             image = d_acaiBowl, 
                             bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                             command = lambda: [whenClicked(37)] )
        acaiBowl.place(relx = 0.25, rely = 0.05)

        brigadeiro = tk.Button(foodFrame, 
                               image = d_brigadeiro, 
                               bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                               command = lambda: [whenClicked(38)] )
        brigadeiro.place(relx = 0.425, rely = 0.05)

        churros = tk.Button(foodFrame, 
                            image = d_churros, 
                            bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                            command = lambda: [whenClicked(39)] )
        churros.place(relx = 0.6, rely = 0.05)

        flan = tk.Button(foodFrame, 
                         image = d_flan, 
                         bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                         command = lambda: [whenClicked(40)] )
        flan.place(relx = 0.77, rely = 0.05)
        
        atoleElote = tk.Button(foodFrame, 
                               image = d_atoleElote, 
                               bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                               command = lambda: [whenClicked(41)] )
        atoleElote.place(relx = 0.05, rely = 0.5)

        quesitos = tk.Button(foodFrame, 
                             image = d_quesitos, 
                             bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                             command = lambda: [whenClicked(42)] )
        quesitos.place(relx = 0.2, rely = 0.5)

        arrozLeche = tk.Button(foodFrame, 
                               image = d_arrozLeche, 
                               bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                               command = lambda: [whenClicked(43)] )
        arrozLeche.place(relx = 0.415, rely = 0.5)

        arrozDulce = tk.Button(foodFrame, 
                               image = d_arrozDulce, 
                               bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                               command = lambda: [whenClicked(44)] )
        arrozDulce.place(relx = 0.615, rely = 0.5)

        dulceLeche = tk.Button(foodFrame, 
                               image = d_dulceLeche, 
                               bg="#FFE2EA", highlightthickness=0, takefocus=0, bd=0, 
                               command = lambda: [whenClicked(45)] )
        dulceLeche.place(relx = 0.78, rely = 0.5)
    else:
        pass

def orderHub():
    order = tk.Toplevel(root)
    order.geometry("1488x945")    
    s = tk.Label(order, image=o_hub).pack()

    v = tk.StringVar()
    v.set(f"Table {sexysexyOrderNum}'s Order:")

    items = tk.StringVar()

    def changeOrder(up):
        global sexysexyOrderNum
        global sexysexyOrder

        if up == "add":
            sexysexyOrderNum = listofOrders[sexysexyOrder]
            v.set(f"Table {sexysexyOrderNum}'s Order:")

            sexysexyOrder+=1
            
            if sexysexyOrder > len(listofOrders)-1:
                sexysexyOrder = 0
        else:
            sexysexyOrderNum = listofOrders[sexysexyOrder]
            v.set(f"Table {sexysexyOrderNum}'s Order:")

            sexysexyOrder-=1
            
            if sexysexyOrder < 0:
                sexysexyOrder = len(listofOrders)-1
        
        title = f"Table{sexysexyOrderNum}.txt"

        actualOrders = tk.StringVar()
        with open(f"{title}", "r") as file:
            start = csv.reader(file)
            orderInfo = []
            for rows in start:
                if "AM" in rows or "PM" in rows:
                    pass
                else:
                    orderInfo.append(rows)
                    print(orderInfo)
                    actualOrders.set(f"Table {sexysexyOrderNum}'s Order:")

            
                
                
                
        """
        
        conn = sqlite3.connect("z_items.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM items WHERE item_id = ?", (itemNum,))


    
        result = cursor.fetchone()

        

        total = result[3]*quant

        '''newInfo = [ sexysexyOrderNum, itemNum, quant, total ]'''

        with open(f"{titke}", "a", newline='') as file:
            start = csv.writer(file)
            start.writerow(newInfo)

        
        items.set(f"Table {sexysexyOrderNum}'s Order:")"""
    # sexysexyOrderNum
    back_button = tk.Button(order, 
                            image=backButt, 
                            bg="#FF88A9", 
                            highlightthickness = 0, bd = 0, 
                            command= lambda: [waiter_hompage(), order.withdraw()])
    back_button.place(relx=0.04, rely=0.06, anchor= 'center')
    header = tk.Label(order, 
                      textvariable=v,
                      font=("Inter", 40, "bold"), 
                      bg="#FF88A9", fg="white")
    header.place(relx = 0.07, rely = 0.03)

    bck = tk.Button(order, 
                    image=o_prev,
                    bg="#FF88A9", 
                    highlightthickness=0, 
                    takefocus=0, bd=0, 
                    command = lambda: [changeOrder("sub")])
    bck.place(relx = 0.36, rely = 0.09)
    nxt = tk.Button(order, 
                    image=o_next ,
                    bg="#FF88A9", 
                    highlightthickness=0, 
                    takefocus=0, bd=0,
                    command = lambda: [changeOrder("add")])
    nxt.place(relx = 0.41, rely = 0.09)


    canvas = tk.Canvas(order, 
                       bg="#FF88A9",
                       width=663, height=708,
                       highlightthickness=0,
                       scrollregion=(0,0,900,900))
    canvas.place(relx = 0.008, rely = 0.145)
    
    vbar=ttk.Scrollbar(order, orient="vertical", command=canvas.yview)
    vbar.place(relx = 0.463, rely = 0.145, relheight=0.789)

    canvas.configure(yscrollcommand=vbar.set)
    

    canvas.create_text(50, 50, 
                       text="ITEMyItem\nITEMyItem\nITEMyItem\nITEMyItem\nITEMyItem\nITEMyItem\nITEMyItem\nITEMyItem\nITEMyItem\nITEMyItem\nITEMyItem\nITEMyItem\nITEMyItem\nITEMyItem\nITEMyItem\nITEMyItem\n", 
                       font=("Inter", 30), 
                       anchor='nw', 
                       fill="white")


    total = tk.Label(order, 
                      text=f"Total: $0.00",
                      font=("Inter", 40, "bold"), 
                      bg="#FF88A9", fg="white")
    total.place(relx = 0.68, rely = 0.12)

    credit = tk.Button(order, 
                       image=o_credit,
                       bg="#FF88A9", 
                       highlightthickness=0, takefocus=0, bd=0, 
                       command = lambda: [tips(), order.withdraw()])
    credit.place(relx = 0.63, rely = 0.22)

    cash = tk.Button(order, 
                     image=o_cash,
                     bg="#FF88A9", 
                     highlightthickness=0, takefocus=0, bd=0, 
                     command = lambda: [tips(), order.withdraw()])
    cash.place(relx = 0.63, rely = 0.42)

    hold = tk.Button(order, 
                     image=o_hold,
                     bg="#FF88A9", 
                     highlightthickness=0, takefocus=0, bd=0, 
                     command = lambda: [tips(), order.withdraw()])
    hold.place(relx = 0.63, rely = 0.62)

def tips():
    tips = tk.Toplevel(root)
    tips.geometry("1488x945")
    s = tk.Label(tips, image=tip_hub).pack()

    back_button = tk.Button(tips, 
                            image=backButt, 
                            bg="#FEB5C9", 
                            highlightthickness = 0, bd = 0, 
                            command= lambda: [orderHub(), tips.withdraw()])
    back_button.place(relx=0.04, rely=0.06, anchor= 'center')

    tt_15 = tk.Button(tips, 
                      image = ttt_15, 
                      bg="white", 
                      highlightthickness=0, takefocus=0, bd=0, 
                      command = lambda: [purchaseComplete(), tips.withdraw()])
    tt_15.place(relx = 0.2, rely = 0.3)
    tt_20 = tk.Button(tips, 
                      image = ttt_20, 
                      bg="white", 
                      highlightthickness=0, takefocus=0, bd=0, 
                      command = lambda: [purchaseComplete(), tips.withdraw()])
    tt_20.place(relx = 0.4, rely = 0.3)
    tt_25 = tk.Button(tips, 
                      image = ttt_25, 
                      bg="white", 
                      highlightthickness=0, takefocus=0, bd=0, 
                      command = lambda: [purchaseComplete(), tips.withdraw()])
    tt_25.place(relx = 0.6, rely = 0.3)

    customTip = tk.Button(tips, 
                          image = t_custom, 
                          bg="white", 
                          highlightthickness=0, takefocus=0, bd=0, 
                          command = lambda: [customTips(), tips.withdraw()])
    customTip.place(relx = 0.1875, rely = 0.6)

    noTip = tk.Button(tips, 
                      image = t_none, 
                      bg="white", 
                      highlightthickness=0, takefocus=0, bd=0, 
                      command = lambda: [purchaseComplete(), tips.withdraw()])
    noTip.place(relx = 0.1875, rely = 0.775)
    
def customTips():
    tips = tk.Toplevel(root)
    tips.geometry("1488x945")
    s = tk.Label(tips, image=tip_hub).pack()

    header = tk.Label(tips, 
                      text="Enter Amount:",
                      font=('Bangla MN', 40), 
                      bg="white", fg="#FF88A9")
    header.place(relx = 0.2, rely = 0.3)

    frame = tk.Frame(tips,  
                     bg ="white",
                     highlightbackground="#FF88A9", highlightthickness=2)
    frame.place(relx = 0.201, rely = 0.4)
    amtEntry = tk.Entry(frame, 
                        width=27,
                        font=("Inria Sans", 50),
                        fg="#FF88A9",bg="white",
                        highlightthickness = 0, bd = 0)
    amtEntry.pack()

    back = tk.Button(tips, 
                     image = tc_back, 
                     bg="white", 
                     highlightthickness=0, takefocus=0, bd=0, 
                     command = lambda: [orderHub(), tips.withdraw()])
    back.place(relx = 0.4, rely = 0.7)

    nexx = tk.Button(tips, 
                     image = tc_next, 
                     bg="white", 
                     highlightthickness=0, takefocus=0, bd=0, 
                     command = lambda:[purchaseComplete(), tips.withdraw()])
    nexx.place(relx = 0.4, rely = 0.85)

def purchaseComplete():
    tips = tk.Toplevel(root)
    tips.geometry("1488x945")
    ss = tk.Label(tips, image=o_complete).pack()
    
    tips.after(500, lambda:[orderHub(), tips.withdraw()])


def job_select():
    ss = tk.Toplevel(root)
    ss.geometry("1488x945")
    
    s = tk.Label(ss, image=start).pack()
    
    host = tk.Button(ss, 
                     image = start_host, 
                     bg="#FFE2EA", highlightthickness=0, bd=0, 
                     command = lambda: [host_hompage(), ss.withdraw()])
    host.place(relx = 0.34, rely = 0.3 )
    
    waiter = tk.Button(ss, 
                       image = start_waiter, 
                       bg="#FFE2EA", 
                       highlightthickness=0, bd=0, 
                       command = lambda: [waiter_hompage(), ss.withdraw()])
    waiter.place(relx = 0.34, rely = 0.6 )

def signInn():
    Start = tk.Toplevel(root)
    Start.geometry("1488x945")
    
    s = tk.Label(Start, image=s_l_page).pack()

    sign_in = tk.Label(Start, text="Sign In", font=('Didot', 48),fg="black",bg="white")
    sign_in.place(relx = 0.43, rely = 0.249)

    username = tk.Label(Start, text="Username:", font=('Didot', 32),fg="black",bg="white")
    username.place(relx = 0.365, rely = 0.375)

    password = tk.Label(Start, text="Password:", font=('Didot', 32),fg="black",bg="white")
    password.place(relx = 0.365, rely = 0.6)

    name = tk.Entry(Start, 
                    width = 23, 
                    font=("Inria Sans", 25), 
                    fg="black",bg="white")
    name.place(relx = 0.368, rely = 0.43)

    pw = tk.Entry(Start, 
                  width = 23, 
                  font=("Inria Sans", 25), 
                  fg="black",bg="white")
    pw.place(relx = 0.368, rely = 0.65)
    
    def search():
        usus = name.get()
        passer = pw.get()

        print(usus, passer)
        conn = sqlite3.connect("z_employees.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees WHERE username = ? AND password = ?", (usus, passer,))
        
        item = cursor.fetchone()
        
        conn.close()

        if item:
            global sexyUserId
            global sexyUserFName
            sexyUserId = item[0]
            sexyUserFName = item[1]

            if item[0] == 2:
                boss_hompage()
                Start.withdraw()
            else:
                job_select()
                Start.withdraw()
        else:
            errerFrame = tk.Frame(Start,  
                                  bg ="black",
                                  highlightbackground="#FF88A9", highlightthickness=2)
            errerFrame.place(relx = 0.3, rely = 0.3)
            err = tk.Label(errerFrame,
                           image=signInERROR)
            err.pack()
            Start.after(500, errerFrame.destroy)

    logIn = tk.Button(Start, 
                   image = signInButt, 
                   bg="white", 
                   highlightthickness=0, 
                   takefocus=0, bd=0, 
                   command = search)
    logIn.place(relx = 0.375, rely = 0.8)

root = tk.Tk()
root.geometry("1488x945")
root.configure(bg ="magenta")

splashBG = tk.PhotoImage(file = "splash_screen.png")
splashLabel=tk.Label(root, image=splashBG).pack()

root.after(200, lambda:[signInn(), root.withdraw()])

# font=('Didot', 12)


'''APP BACKGROUNDS'''
#LOGIN/JOB SELECTOR
s_l_page = tk.PhotoImage(file = "signup_login.png")
start = tk.PhotoImage(file = "choose job.png")

#HOST/WAITER HOMEPAGE
host_homepage = tk.PhotoImage(file = "host_homepage.png")
waiter_homepage = tk.PhotoImage(file = "waiter_homepage.png")

#HOST: TABLES
t_hub = tk.PhotoImage(file = "table screen.png")
t_edit = tk.PhotoImage(file = "table-edit.png")

#WAITER: MENU
m_hub = tk.PhotoImage(file = "menu-hubScreen.png")
#WAITER: ORDERS
o_hub = tk.PhotoImage(file = "orders screen.png")
o_complete = tk.PhotoImage(file = "order confirmation screen.png")
#WAITER: ORDERS: TIPS
tip_hub = tk.PhotoImage(file = "tips screen.png")

#BOSS PAGE
b_hub = tk.PhotoImage(file = "boss screen.png")
b_signUpComplete = tk.PhotoImage(file = "b_signUp complete.png")


'''APP BUTTONS'''
backButt = tk.PhotoImage(file = "backButton.png")

start_host = tk.PhotoImage(file = "start_host.png")
start_waiter = tk.PhotoImage(file = "start_waiter.png")

signInButt = tk.PhotoImage(file = "sign in button.png")
signUpButt = tk.PhotoImage(file = "sign up button.png")

signInERROR = tk.PhotoImage(file = "signInIncorrectInputs.png")

#HOMEPAGE BUTTONS
home_signOutButt = tk.PhotoImage(file = "home-signOutButt.png")
home_tableButt = tk.PhotoImage(file = "home-tableButt.png")
home_menuButt = tk.PhotoImage(file = "home-menuButt.png")
home_ordersButt = tk.PhotoImage(file = "home-ordersButt.png")

#TABLE BUTTONS
t_1 = tk.PhotoImage(file = "table-1.png")
t_2 = tk.PhotoImage(file = "table-2.png")
t_3 = tk.PhotoImage(file = "table-3.png")
t_4 = tk.PhotoImage(file = "table-4.png")
t_5 = tk.PhotoImage(file = "table-5.png")
t_6 = tk.PhotoImage(file = "table-6.png")
t_7 = tk.PhotoImage(file = "table-7.png")
t_8 = tk.PhotoImage(file = "table-8.png")
t_9 = tk.PhotoImage(file = "table-9.png")
t_10 = tk.PhotoImage(file = "table-10.png")
t_11 = tk.PhotoImage(file = "table-11.png")
t_12 = tk.PhotoImage(file = "table-12.png")
t_13 = tk.PhotoImage(file = "table-13.png")
t_14 = tk.PhotoImage(file = "table-14.png")
t_15 = tk.PhotoImage(file = "table-15.png")
t_16 = tk.PhotoImage(file = "table-16.png")
t_17 = tk.PhotoImage(file = "table-17.png")
t_next = tk.PhotoImage(file = "table-next.png")
t_back = tk.PhotoImage(file = "table-back.png")
t_yes = tk.PhotoImage(file = "table-yes.png")
t_no = tk.PhotoImage(file = "table-no.png")


#MENU BUTTONS
m_bev = tk.PhotoImage(file = "menu-beverage-button.png")
m_appetizer = tk.PhotoImage(file = "menu-appetizer-button.png")
m_courses = tk.PhotoImage(file = "menu-course-button.png")
m_sides = tk.PhotoImage(file = "menu-side-button.png")
m_dessert = tk.PhotoImage(file = "menu-desert-button.png")
#MENU: DRINKS
d_coke = tk.PhotoImage(file = "drinks-coke.png")
d_mango = tk.PhotoImage(file = "drinks-mango mango.png")
d_water = tk.PhotoImage(file = "drinks-water.png")
d_inca = tk.PhotoImage(file = "drinks-inca cola.png")
d_morocho = tk.PhotoImage(file = "drinks-morocho.png")
d_sprite = tk.PhotoImage(file = "drinks-sprite.png")
d_strawberry = tk.PhotoImage(file = "drinks-strawberyy.png")
d_fanta = tk.PhotoImage(file = "drinks-fanta.png")
d_chicha = tk.PhotoImage(file = "drinks-chichi.png")
d_tea = tk.PhotoImage(file = "drinks-iced tea.png")
#MENU: APPETIZERS
a_chips = tk.PhotoImage(file = "appetizers-nachos.png")
a_tamales = tk.PhotoImage(file = "appetizers-tamales.png")
a_coxhinas = tk.PhotoImage(file = "appetizers-coxinhas.png")
a_humita = tk.PhotoImage(file = "appetizers-homus.png")
a_paoQueso = tk.PhotoImage(file = "appetizers-pao de queso.png")
a_cheeseSticks = tk.PhotoImage(file = "appetizers-cheese sticks.png")
a_empCarne = tk.PhotoImage(file = "appetizers-empCarne.png")
a_empQueso = tk.PhotoImage(file = "appetizers-empQueso.png")
#MENU: MAIN COURSES
mc_ceviche = tk.PhotoImage(file = "mains-ceviche.png")
mc_friijoles = tk.PhotoImage(file = "mains-frijolada.png")
mc_steackTako = tk.PhotoImage(file = "mains-bisteak.png")
mc_pupusas = tk.PhotoImage(file = "mains-pupusas.png")
mc_salvTamas = tk.PhotoImage(file = "mains-SALAVADORtamas.png")
mc_mofongo = tk.PhotoImage(file = "mains-mofongo.png")
mc_sopaRes = tk.PhotoImage(file = "mains-sopaRez.png")
mc_habichuelasArroz = tk.PhotoImage(file = "mains-habichuelaArroz.png")
mc_tocinoArroz = tk.PhotoImage(file = "mains-tocinoArroz.png")
#MENU: SIDES
s_platano = tk.PhotoImage(file = "sides-fried platano.png")
s_tostones = tk.PhotoImage(file = "sides-tostones.png")
s_chicharones = tk.PhotoImage(file = "sides-chicharones.png")
s_beans = tk.PhotoImage(file = "sides-beans.png")
s_wRice = tk.PhotoImage(file = "sides-white rice.png")
s_mCSalad = tk.PhotoImage(file = "sides-mexican salda.png")
s_farofa = tk.PhotoImage(file = "sides-farofa.png")
s_fries = tk.PhotoImage(file = "sides-fries.png")
#MENU: DESSERTS 
d_tresLeches = tk.PhotoImage(file = "desserts-tresLeches.png")
d_acaiBowl = tk.PhotoImage(file = "desserts-acaibowl.png")
d_brigadeiro = tk.PhotoImage(file = "desserts-brigabriga.png")
d_churros = tk.PhotoImage(file = "desserts-churros.png")
d_flan = tk.PhotoImage(file = "desserts-flan.png")
d_atoleElote = tk.PhotoImage(file = "desserts-atole de elote.png")
d_quesitos = tk.PhotoImage(file = "desserts-quesoos.png")
d_arrozLeche = tk.PhotoImage(file = "desserts-arrozLeche.png")
d_arrozDulce = tk.PhotoImage(file = "desserts-arrozDulce.png")
d_dulceLeche = tk.PhotoImage(file = "desserts-dulce leche.png")


#ORDER BUTTONS
o_credit = tk.PhotoImage(file = "orders-creditDebit.png")
o_cash = tk.PhotoImage(file = "orders-cash.png")
o_hold = tk.PhotoImage(file = "orders-hold.png")
o_next = tk.PhotoImage(file = "orders-orderNext.png")
o_prev = tk.PhotoImage(file = "orders-orderPrev.png")
#TIPS BUTTONS
ttt_15 = tk.PhotoImage(file = "tips-15Tip.png")
ttt_20 = tk.PhotoImage(file = "tips-20Tip.png")
ttt_25 = tk.PhotoImage(file = "tips-25Tip.png")
t_custom = tk.PhotoImage(file = "tips-customTip.png")
t_none = tk.PhotoImage(file = "tips-noTip.png")
tc_back = tk.PhotoImage(file = "tipscustom-backButt.png")
tc_next = tk.PhotoImage(file = "tipscustom-nextButt.png")


#BUSS BUTTONS
b_revenue = tk.PhotoImage(file = "boss-revenue.png")
b_createAccount = tk.PhotoImage(file = "boss-new account.png")
b_resetPass = tk.PhotoImage(file = "boss-passReset.png")
b_signOut = tk.PhotoImage(file = "boss-signnOut.png")

pw_reset = tk.PhotoImage(file = "boss-resetButt.png")


page_one = True

listofOrders = []
grades_reader=open('orders.txt', 'r')
for row in grades_reader:
    listofOrders = row.split()

print(listofOrders, len(listofOrders))
try:
    sexysexyOrderNum = listofOrders[0]
    sexysexyOrder = 0
except:
    print("file is empty")
root.mainloop()
#finished GUI at 4:57