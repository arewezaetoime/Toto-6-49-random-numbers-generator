import random
from tkinter import *
from tkinter import ttk


def random_numbers():
    while len(our_lucky_nums) < 6:
        lucky_num = random.randint(1, 49)
        if lucky_num not in our_lucky_nums:
            our_lucky_nums.append(lucky_num)

    n1.set(our_lucky_nums[0])
    n2.set(our_lucky_nums[1])
    n3.set(our_lucky_nums[2])
    n4.set(our_lucky_nums[3])
    n5.set(our_lucky_nums[4])
    n6.set(our_lucky_nums[5])
    our_lucky_nums.clear()
    bar.stop()
    progress_start()


def progress_start():
    bar.start()
    bar.step(random.randint(1, 100))
    # bar.configure()


our_lucky_nums = []


root = Tk()
root.geometry("450x200")
root.title('Toto 6/49 lucky numbers.')
root.configure(background='black')

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=NSEW)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
# menu = ttk.Menubutton(root)
# menu.place(x=10, y=10)
# options = ttk.OptionMenu(menu, variable='Close')

ttk.Label(mainframe, text='Your lucky numbers are:').grid(column=0, row=1, sticky=N)

bar = ttk.Progressbar(mainframe, orient=HORIZONTAL, length=250, mode='indeterminate')
bar.step(100)
# bar.grid(column=0, row=1, columnspan=2, padx=5, pady=5)
bar.place(x=100, y=30)
# bar.start()

# Our num vars
n1, n2, n3, n4, n5, n6 = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
# Getting values from the list with nums

n1_entry = Entry(root, width=2, font=('Arial', 25, 'bold'), textvariable=n1, state='disabled')
n1_entry.place(x=60, y=60)
n2_entry = Entry(root, width=2, font=('Arial', 25, 'bold'), textvariable=n2, state='disabled')
n2_entry.place(x=120, y=60)
n3_entry = Entry(root, width=2, font=('Arial', 25, 'bold'), textvariable=n3, state='disabled')
n3_entry.place(x=180, y=60)
n4_entry = Entry(root, width=2, font=('Arial', 25, 'bold'), textvariable=n4, state='disabled')
n4_entry.place(x=240, y=60)
n5_entry = Entry(root, width=2, font=('Arial', 25, 'bold'), textvariable=n5, state='disabled')
n5_entry.place(x=300, y=60)
n6_entry = Entry(root, width=2, font=('Arial', 25, 'bold'), textvariable=n6, state='disabled')
n6_entry.place(x=360, y=60)

ttk.Button(mainframe, text='Shuffle the numbers', command=random_numbers).grid(
    column=1,
    row=1,
    sticky=(N, E, S, W))

root.mainloop()
