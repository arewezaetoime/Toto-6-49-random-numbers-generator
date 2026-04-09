import random
import tkinter as tk
from tkinter import ttk


def generate_numbers():
    btn.config(state='disabled')
    for entry in entries:
        entry.config(fg='#888888')
    bar.start(10)
    root.after(800, show_numbers)


def show_numbers():
    lucky_nums = random.sample(range(1, 50), 6)
    for i, entry in enumerate(entries):
        num_vars[i].set(str(lucky_nums[i]))
        entry.config(fg='#FFD700')
    bar.stop()
    bar['value'] = 100
    btn.config(state='normal')


root = tk.Tk()
root.title('Toto 6/49')
root.geometry('480x220')
root.resizable(False, False)
root.configure(bg='#0d0d0d')

# Title
tk.Label(
    root,
    text='TOTO 6/49',
    font=('Helvetica', 18, 'bold'),
    bg='#0d0d0d',
    fg='#FFD700'
).pack(pady=(22, 4))

tk.Label(
    root,
    text='Your lucky numbers',
    font=('Helvetica', 10),
    bg='#0d0d0d',
    fg='#666666'
).pack()

# Number entries
frame = tk.Frame(root, bg='#0d0d0d')
frame.pack(pady=14)

num_vars = [tk.StringVar(value='?') for _ in range(6)]
entries = []
for var in num_vars:
    e = tk.Entry(
        frame,
        textvariable=var,
        width=3,
        font=('Helvetica', 26, 'bold'),
        fg='#888888',
        bg='#1a1a1a',
        bd=0,
        justify='center',
        state='readonly',
        readonlybackground='#1a1a1a',
        relief='flat'
    )
    e.pack(side='left', padx=6, ipady=6)
    entries.append(e)

# Progress bar
style = ttk.Style()
style.theme_use('default')
style.configure(
    'gold.Horizontal.TProgressbar',
    troughcolor='#1a1a1a',
    background='#FFD700',
    thickness=4
)
bar = ttk.Progressbar(
    root,
    style='gold.Horizontal.TProgressbar',
    orient='horizontal',
    length=340,
    mode='indeterminate'
)
bar.pack(pady=(0, 12))

# Button
btn = tk.Button(
    root,
    text='✦  Shuffle Numbers  ✦',
    command=generate_numbers,
    font=('Helvetica', 12, 'bold'),
    fg='#0d0d0d',
    bg='#FFD700',
    activebackground='#e6c200',
    activeforeground='#0d0d0d',
    bd=0,
    padx=20,
    pady=8,
    cursor='hand2',
    relief='flat'
)
btn.pack()

root.mainloop()