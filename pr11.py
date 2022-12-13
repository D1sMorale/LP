from tkinter import * 
import requests 
import json 

'''--------------------------------------'''
def clickJSON():
    username=str(txt.get())
    response=requests.get(f"https://api.github.com/users/{username}") 
    DataFind=json.loads(response.text) 
    data={
        'company': DataFind['company'],
        'created_at': DataFind['created_at'],
        'email': DataFind['email'],
        'id' : DataFind['id'],
        'name': DataFind['name'],
        'url': DataFind['url'],
        }
    with open('data.txt', 'w') as outfile: 
        json.dump(data, outfile) 
    outfile.close() 
'''--------------------------------------'''
root=Tk() 
root['bg']='white' 
root.title('Практика 11')
root.geometry('640x480')
root.resizable(width=False, height=False)
'''--------------------------------------'''
lbl=Label(root, text='Данные репозитория', bg='white', font=30)
lbl.pack() 
lbl2=Label(root, text='Введите название репозитория', bg='white', font=30)
lbl2.pack()
txt=Entry(root, width=25)
txt.pack()
btn=Button(root, text='Получение данных', bg='blue', command=clickJSON)
btn.pack()
lbl3=Label(root, text='Вариант 9(в поле ввода вводим Automattic)', bg='white', fg='blue', font=15)
lbl3.pack()
'''--------------------------------------'''
root.mainloop() 
