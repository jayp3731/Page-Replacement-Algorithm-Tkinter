from tkinter import *
from collections import deque
import tkinter as tk
import matplotlib.pyplot as plt
import ipdb
from tkinter import messagebox
from tkinter.ttk import Combobox


root = Tk()
root.title("belady algorithm")
root.geometry("900x600")
root.resizable(0, 0)
root.configure(background='light cyan')
#root.configure(background='MistyRose1')
#root.title("OS PROJECT")

title_label = Label(root, text="Page Replacement Algorithm", bg="CYAN", font="comicsansms 30 bold", width=100)
title_label.pack(fill=X)

#mylabel = Label(root,text="Page Replacement Algorithms",font=("Courier",15))
#tlabel.grid(row=1,column=2)

dropdown = [1,2,3,4,5,6,7,8,9,10]


mylabel1 = Label(root, text="Enter the number of frames: ",bg="YELLOW", font="comicsansms 15 bold", width=23)
mylabel1.place(x=40,y=70)

mylabel2 = Label(root, text="Enter the reference string:",bg="YELLOW", font="comicsansms 15 bold", width=21)
mylabel2.place(x=41, y=110)

mylabel1 = Label(root, text="Enter the Multiple frames: ",bg="YELLOW", font="comicsansms 15 bold", width=23)
mylabel1.place(x=40,y=150)

framevalue = 1
stringvalue = []
stringvalue1 = []

#e=Entry(root, textvariable=framevalue, width=10, font="comicsansms 15 bold")
#e.place(x=350, y=70)

e=Combobox(root, textvariable=framevalue, width=2, value=dropdown, font="comicsansms 15 bold", state="readonly")
e.place(x=350, y=70)

e1=Entry(root, textvariable=stringvalue, width=20, font="comicsansms 15 bold")
e1.place(x=350, y=110)

e2=Entry(root, textvariable=stringvalue1, width=20, font="comicsansms 15 bold")
e2.place(x=350, y=150)

def onclick():
    topw = Toplevel()
    topw.title('FIFO WORKING...')
    topw.geometry("900x600")
    topw.configure(background='MistyRose1')
    capacity = int(e.get())
    f, fault, top, pf = [], 0, 0, 'No'
    s = list(map(int, e1.get().strip().split()))

    mylabel = Label(topw, text="String", bg="YELLOW", font="comicsansms 15 bold", width=5)
    mylabel.place(x=20, y=30)
    mylabel1 = Label(topw, text="Frame", bg="YELLOW", font="comicsansms 15 bold", width=5)
    mylabel1.place(x=100, y=30)
    mylabel2 = Label(topw, text="Fault", bg="YELLOW", font="comicsansms 15 bold", width=5)
    mylabel2.place(x=150 + (50 * capacity), y=30)

    a = 0
    print("\nString|Frame →\t", end='')
    for i in range(capacity):
        print(i, end=' ')
    print("Fault\n   ↓\n")
    for i in s:
        if i not in f:
            if len(f) < capacity:
                f.append(i)
            else:
                f[top] = i
                top = (top + 1) % capacity
            fault += 1
            pf = 'Yes'
        else:
            pf = 'No'
        print("   %d\t\t" % i, end='')
        a += 1

        mylabel1 = Label(topw, text="%d" % i, bg="YELLOW", font="comicsansms 15 bold", width=2)
        mylabel1.place(x=30, y=30 + (50 * a))

        d = 0
        for x in f:
            # print(f, end=' ')
            print(x, end=' ')
            mylabel = Label(topw, text="%d " % x, bg="YELLOW", font="comicsansms 15 bold", width=2)
            mylabel.place(x=100 + (50 * d), y=30 + (50 * a))
            d += 1

        # print("value of row %d ="%b)
        for x in range(capacity - len(f)):
            print(' ', end=' ')
        if pf == "Yes":
            mylabel2 = Label(topw, text=" %s" % pf, bg="YELLOW", fg="Green2", font="comicsansms 15 bold", width=3)
        else:
            mylabel2 = Label(topw, text=" %s" % pf, bg="YELLOW", fg="maroon", font="comicsansms 15 bold", width=3)
        mylabel2.place(x=150 + (50 * capacity), y=30 + (50 * a))
        print(" %s" % pf)
    results['text'] = "\nTotal requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%" % (len(s), fault, (fault / len(s)) * 100)


def onclick1():
    topw = Toplevel()
    topw.title('FIFO WORKING...')
    topw.geometry("900x600")
    topw.configure(background='MistyRose1')

    capacity = int(e.get())
    f,st,fault,pf = [],[],0,'No'
    s = list(map(int, e1.get().strip().split()))

    mylabel = Label(topw, text="String", bg="YELLOW", font="comicsansms 15 bold", width=5)
    mylabel.place(x=20, y=30)
    mylabel1 = Label(topw, text="Frame", bg="YELLOW", font="comicsansms 15 bold", width=5)
    mylabel1.place(x=100, y=30)
    mylabel2 = Label(topw, text="Fault", bg="YELLOW", font="comicsansms 15 bold", width=5)
    mylabel2.place(x=150 + (50 * capacity), y=30)

    print("\nString|Frame →\t", end='')
    for i in range(capacity):
        print(i, end=' ')
    print("Fault\n   ↓\n")
    a = 0
    for i in s:
        if i not in f:
            if len(f) < capacity:
                f.append(i)
                st.append(len(f) - 1)
            else:
                ind = st.pop(0)
                f[ind] = i
                st.append(ind)
            pf = 'Yes'
            fault += 1
        else:
            st.append(st.pop(st.index(f.index(i))))
            pf = 'No'
        print("   %d\t\t" % i, end='')
        a += 1

        mylabel1 = Label(topw, text="%d" % i, bg="YELLOW", font="comicsansms 15 bold", width=2)
        mylabel1.place(x=30, y=30 + (50 * a))

        d = 0
        for x in f:
            print(x, end=' ')
            mylabel = Label(topw, text="%d " % x, bg="YELLOW", font="comicsansms 15 bold", width=2)
            mylabel.place(x=100 + (50 * d), y=30 + (50 * a))
            d += 1

        for x in range(capacity - len(f)):
            print(' ', end=' ')
        if pf == "Yes":
            mylabel2 = Label(topw, text=" %s" % pf, bg="YELLOW", fg="Green2", font="comicsansms 15 bold", width=3)
        else:
            mylabel2 = Label(topw, text=" %s" % pf, bg="YELLOW", fg="maroon", font="comicsansms 15 bold", width=3)
        mylabel2.place(x=150 + (50 * capacity), y=30 + (50 * a))
        print(" %s" % pf)
    results['text'] = "\nTotal Requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%" % (len(s), fault, (fault / len(s)) * 100)

def onclick2():
    topw = Toplevel()
    topw.title('FIFO WORKING...')
    topw.geometry("900x600")
    topw.configure(background='MistyRose1')

    capacity = int(e.get())
    f,fault,pf = [],0,'No'
    s = list(map(int, e1.get().strip().split()))

    mylabel = Label(topw, text="String", bg="YELLOW", font="comicsansms 15 bold", width=5)
    mylabel.place(x=20, y=30)
    mylabel1 = Label(topw, text="Frame", bg="YELLOW", font="comicsansms 15 bold", width=5)
    mylabel1.place(x=100, y=30)
    mylabel2 = Label(topw, text="Fault", bg="YELLOW", font="comicsansms 15 bold", width=5)
    mylabel2.place(x=150 + (50 * capacity), y=30)

    print("\nString|Frame →\t", end='')
    for i in range(capacity):
        print(i, end=' ')
    print("Fault\n   ↓\n")
    occurance = [None for i in range(capacity)]
    a = 0
    for i in range(len(s)):
        if s[i] not in f:
            if len(f) < capacity:
                f.append(s[i])
            else:
                for x in range(len(f)):
                    if f[x] not in s[i + 1:]:
                        f[x] = s[i]
                        break
                    else:
                        occurance[x] = s[i + 1:].index(f[x])
                else:
                    f[occurance.index(max(occurance))] = s[i]
            fault += 1
            pf = 'Yes'
        else:
            pf = 'No'
        print("   %d\t\t" % s[i], end='')
        a += 1

        mylabel1 = Label(topw, text="%d" % s[i], bg="YELLOW", font="comicsansms 15 bold", width=2)
        mylabel1.place(x=30, y=30 + (50 * a))

        d = 0
        for x in f:
            print(x, end=' ')
            mylabel = Label(topw, text="%d " % x, bg="YELLOW", font="comicsansms 15 bold", width=2)
            mylabel.place(x=100 + (50 * d), y=30 + (50 * a))
            d += 1

        for x in range(capacity - len(f)):
            print(' ', end=' ')
        if pf == "Yes":
            mylabel2 = Label(topw, text=" %s" % pf, bg="YELLOW", fg="Green2", font="comicsansms 15 bold", width=3)
        else:
            mylabel2 = Label(topw, text=" %s" % pf, bg="YELLOW", fg="maroon", font="comicsansms 15 bold", width=3)
        mylabel2.place(x=150 + (50 * capacity), y=30 + (50 * a))
        print(" %s" % pf)
    results['text'] = "\nTotal requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%" % (len(s), fault, (fault / len(s)) * 100)

def FIFO(capacity, ref_string):
    frames = deque([])
    page_fault = 0
    for page in ref_string:
        if page in frames:
            continue
        else:
            page_fault += 1
            if len(frames) < capacity:
                frames.append(page)
                print("Appended %s"% str(page))
            else:
                removed = frames.popleft()
                print('Removed  %s'% str(removed))
                frames.append(page)
                print("Appended %s" % str(page))
    print('page fault num = %s' % page_fault)
    return page_fault


def LFU(capacity, ref_string):
    counting = dict()
    frames = []
    page_fault = 0
    for page in ref_string:
        print(('-' * 20))
        print(counting)
        print(frames)
        print(('page now: ', page))

        if page in frames:
            print(('page already in frame: %s\n' % page))
            continue
        else:
            page_fault += 1
            if len(frames) < capacity:
                frames.append(page)
                print(("Appended %s" % str(page)))
            else:
                print(('find min ', counting))
                least_freq = min(counting.values())
                least_used = list(counting.keys())[list(counting.values()).index(least_freq)]
                print(('Removed  %s' % str(least_used)))

                frames.remove(least_used)

                del counting[least_used]

                frames.append(page)
                print(("Appended %s" % str(page)))

        # count this page
        if page not in list(counting.keys()):
            counting[page] = 1
        else:
            counting[page] += 1

    return page_fault


def graph1():
    reference_string = list(map(int, e1.get().strip().split()))
    capacitys = list(map(int, e2.get().strip().split()))
    pfs = []
    for capacity in capacitys:
        page_fault = FIFO(capacity, reference_string)
        pfs.append(page_fault)

    plt.bar(capacitys, pfs, color='lightblue')
    plt.xticks(capacitys, [str(x) for x in capacitys])
    plt.yticks(pfs, [str(y) for y in pfs])
    plt.xlabel('Capacity')
    plt.ylabel('Page Fault number')

    plt.show()

def graph2():
    reference_string = list(map(int, e1.get().strip().split()))
    capacitys = list(map(int, e2.get().strip().split()))
    pfs = []
    for capacity in capacitys:
        page_fault = LFU(capacity, reference_string)
        pfs.append(page_fault)

    plt.bar(capacitys, pfs, color='lightblue')
    plt.xticks(capacitys, [str(x) for x in capacitys])
    plt.yticks(pfs, [str(y) for y in pfs])
    plt.xlabel('Capacity')
    plt.ylabel('Page Fault number')

    plt.show()

myButton1 = Button(root, text="FIFO",bg="ORANGE2", width=10, height=1, command=onclick, font="comicsansms")
myButton1.place( x=440, y=190 )

myButton2 = Button(root, text="LRU",bg="ORANGE2", width=10, height=1, command=onclick1, font="comicsansms")
myButton2.place( x=440, y=230 )

myButton3 = Button(root, text="Optimal page",bg="ORANGE2", width=10, height=1, command=onclick2, font="comicsansms")
myButton3.place( x=440, y=270 )

myButton4 = Button(root, text="Graph(FIFO)",bg="ORANGE2", width=10, height=1, command=graph1, font="comicsansms")
myButton4.place( x=570, y=190 )

myButton5 = Button(root, text="Graph(LRU)",bg="ORANGE2", width=10, height=1, command=graph2, font="comicsansms")
myButton5.place( x=570, y=230 )

Button(root, text='EXIT',width=10,height=1, bg='grey',fg='white',font="comicsansms",command=root.destroy).place(x=570,y=270)

lower_frame = tk.Frame(root, bg='#42c2f4', bd=10,width=500, height=220)
lower_frame.place(x=60,y=320)

bg_color = 'white'
results = tk.Label(lower_frame, anchor='nw', justify='left', bd=4)
results.config(font=20, bg=bg_color)
results.place(relwidth=1, relheight=1)

root.mainloop()