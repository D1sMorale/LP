from tkinter import*
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from tkinter import messagebox
from tkinter import Menu

'''--------------------------------------'''  

def calculator():
    res="Результат : {}".format(chet(combo1.get(), int(txt1.get()), int(txt2.get())))
    lbl2.configure(text=res)
def chet(operation, operand1, operand2):
    result=0
    if operation=='+':
        result=operand1+operand2
    if operation=='-':
        result=operand1-operand2
    if operation=='*':
        result=operand1*operand2
    if operation=='/':
        result=operand1/operand2
    return result    

def clicked():
    res=messagebox.showinfo('Отчёт','Вы выбрали {}'.format(chbox(chk1_state.get(), chk2_state.get(), chk3_state.get())))
def chbox(chk1_state, chk2_state, chk3_state):
    if ((chk1_state==True) and (chk2_state==True) and (chk3_state==True)):
        return 'первый, второй и третий варианты'
    if ((chk1_state==True) and (chk2_state==True)):
        return 'первый и второй варианты'
    if ((chk2_state==True) and (chk3_state==True)):
        return 'второй и третий варианты'
    if ((chk1_state==True) and (chk3_state==True)):
        return 'первый и третий варианты'
    if (chk1_state==True):
        return 'первый вариант'
    if (chk2_state==True):
        return 'второй вариант'
    if (chk3_state==True):
        return 'третий вариант'
    
def _open():
    f=open('Новый текстовый документ 1.txt', 'r')
    res=f.readline()
    text.insert(1.0, res)
    f.close()
def save():
    f1=open('Новый текстовый документ 1.txt', 'w')
    f1.write(text.get(1.0, END))
    text.delete(1.0, END)
    messagebox.showinfo('','Файл был успешно сохранён')
    
'''--------------------------------------'''    

window=Tk()    
window.title('Практика10')             #название окна
window.geometry('600x420')                 #размеры окна
window.resizable(width=False, height=False)#пользователь не может изменять размеры окна

'''--------------------------------------'''

tab_control=ttk.Notebook(window)
tab1=ttk.Frame(tab_control)
tab2=ttk.Frame(tab_control)
tab3=ttk.Frame(tab_control)
tab4=ttk.Frame(tab_control)
tab5=ttk.Frame(tab_control)
tab_control.add(tab1, text='Вкладка 1')
tab_control.add(tab2, text='                                                                  ')
tab_control.add(tab3, text='Вкладка 2')
tab_control.add(tab4, text='                                                                  ')
tab_control.add(tab5, text='Вкладка 3') 
tab_control.pack(expand=1, fill='both')

'''--------------------------------------'''

lbl1=Label(tab1, text='КАЛЬКУЛЯТОР', font=('New Times Roman', 15))
lbl1.grid(column=0, row=0)
txt1=Entry(tab1, width=23)
txt1.grid(column=0, row=1)
combo1 = Combobox(tab1)
combo1['values'] = ('+', '-', '*', '/')
combo1.current(0) 
combo1.grid(column=0, row=2)
txt2=Entry(tab1, width=23)
txt2.grid(column=0, row=3)
btn=Button(tab1, text='    Счет    ', bg='blue',command=calculator)
btn.grid(column=2, row=2)
lbl2=Label(tab1, text='Результат : ', bg='blue', font=('New Times Roman', 12))
lbl2.grid(column=0, row=4)

'''--------------------------------------'''

lbl3=Label(tab3, text='ЧЕКБОКСЫ', font=('New Times Roman', 15))
lbl3.grid(column=0, row=0)
chk1_state=BooleanVar()
chk1_state.set(False)
chk1=Checkbutton(tab3, text='Первый', var=chk1_state)
chk1.grid(column=0, row=1)
chk2_state=BooleanVar()
chk2_state.set(False)
chk2=Checkbutton(tab3, text='Второй', var=chk2_state)
chk2.grid(column=0, row=2)
chk3_state=BooleanVar()
chk3_state.set(False)
chk3=Checkbutton(tab3, text='Третий ', var=chk3_state)
chk3.grid(column=0, row=3)
btn1=Button(tab3, text='Проверка', bg='blue', command=clicked)
btn1.grid(column=1, row=2)

'''--------------------------------------'''

lbl4=Label(tab5, text='РАБОТА С ТЕКСТОМ', font=('New Times Roman', 15))
lbl4.grid(column=0, row=0)
lbl5= Label(tab5, text='Ниже осуществляется ввод', fg='blue', font=('New Times Roman', 12))
lbl5.grid(column=0, row=1)
lbl6= Label(tab5, text='и вывод вашего текста', fg='blue', font=('New Times Roman', 12))
lbl6.grid(column=0, row=2)
text=Text(width=60, height=17, wrap=WORD)
text.pack()
menu = Menu()
new_item=Menu(menu, tearoff=0)
menu.add_cascade(label='Файл',menu=new_item)
new_item.add_command(label='Открыть',command=_open)
new_item.add_separator()
new_item.add_command(label='Сохранить',command=save)
window.config(menu=menu)

'''--------------------------------------'''

window.mainloop()                    #запуск постоянного цикла
