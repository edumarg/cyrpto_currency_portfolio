from tkinter import *

# For Tkinter documentation go to https://docs.python.org/3/library/tkinter.html
root = Tk()
root.geometry("400x600")
root.title("My Crypto Currency Portfolio")
root.iconbitmap(r'./coin.ico')
root.configure(bg='white')
title = Label(root, text="My Crypto Currencies", justify="center", font="10", pady="30", bg='white')
title.pack()

# adding a area scroll bar -from https://www.youtube.com/watch?v=0WafQCaok6g-
# Create main frame
main_frame = Frame(root,
                   bg='white')
main_frame.pack(fill="both",
                expand=1, )

# create a canvas
my_canvas = Canvas(main_frame,
                   bg='white')
my_canvas.pack(side='left',
               fill='both',
               expand=1)

# add scrollbar to canvas
my_scrollbar = Scrollbar(main_frame,
                         orient='vertical',
                         command=my_canvas.yview)
my_scrollbar.pack(side='right',
                  fill='y')

# configure canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>',
               lambda event: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

# add another frame to canvas
second_frame = Frame(my_canvas,
                     bg='white',
                     borderwidth=0)

# add frame to new windows in canvas
my_canvas.create_window((0, 0),
                        window=second_frame,
                        anchor='nw')


def ask_quit():
    global stop_threads
    root.quit()
    stop_threads = True


root.protocol('WM_DELETE_WINDOW', ask_quit)
