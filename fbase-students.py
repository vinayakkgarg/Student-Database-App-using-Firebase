import Tkinter as tk
if __name__=='__main__':
    from firebase import firebase
    firebase = firebase.FirebaseApplication("PUT IN FIREBASE URL HERE")
    def addData(event):
        name = str(name_entry.get())
        m1 = int(sub1_entry.get())
        m2 = int(sub2_entry.get())
        m3 = int(sub3_entry.get())
        data  = {'marks1':m1, 'marks2':m2, 'marks3':m3}
        res = firebase.patch('/'+name, data)
       	percentage.insert(tk.END,"Data has been added successfully")
    def delData(event):
        res = firebase.get('/', None)
        for key in res:
    		if (key==enter_name_entry.get()):
    			firebase.delete('/',key)
    	percentage.insert(tk.END,"Data has been deleted successfully")
    def getData(event):
        res = firebase.get('/', None)
        p=0
        for key in res:
    		if (key==enter_name_entry.get()):
                    p = ((res[key]['marks1']+res[key]['marks2']+res[key]['marks3'])/3)
        percentage.insert(tk.END,str(p)+ "%")
    window = tk.Tk()
    window.geometry("650x200")
    window.title("STUDENTS DATABASE APP")
    name_Label=tk.Label(text = "Name :")
    name_Label.grid(column = 0, row = 1)
    sub1_Label=tk.Label(text = "Subject 1 :")
    sub1_Label.grid(column=0, row = 2)
    sub2_Label=tk.Label(text="Subject 2:")
    sub2_Label.grid(column=0, row=3)
    sub3_Label=tk.Label(text="Subject 3:")
    sub3_Label.grid(column=0, row=4)
    name_entry=tk.Entry()
    name_entry.grid(column=1, row=1)
    sub1_entry=tk.Entry()
    sub1_entry.grid(column=1, row=2)
    sub2_entry=tk.Entry()
    sub2_entry.grid(column=1, row=3)
    sub3_entry=tk.Entry()
    sub3_entry.grid(column=1, row=4)
    add_button = tk.Button(window, text = "ADD DATA")
    add_button.grid(column=1, row = 5)
    add_button.bind("<Button-1>", addData)
    enter_name_Label=tk.Label(text = "Enter Name :")
    enter_name_Label.grid(column = 4, row = 1)
    enter_name_entry=tk.Entry()
    enter_name_entry.grid(column=5, row=1)
    result_Label=tk.Label(text = "Result :")
    result_Label.grid(column = 0, row = 7)
    percentage= tk.Text(master = window, height =2, width = 45)
    percentage.grid(column=1, row=7)
    get_button = tk.Button(window, text = "GET DATA")
    get_button.grid(column = 5, row =2)
    get_button.bind("<Button-1>", getData)
    del_button = tk.Button(window, text = "DEL DATA")
    del_button.grid(column = 5, row =3)
    del_button.bind("<Button-1>", delData)
    window.mainloop()
