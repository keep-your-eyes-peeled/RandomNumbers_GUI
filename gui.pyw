import tkinter as tk
import random
import threading

def get_random_number(number_from, number_to):
    x=random.randint(number_from, number_to)
    return x

def get_sequence_of_numbers(number_of_numbers, number_from, number_to):
    sequence = []
    for x in range(number_of_numbers):
        sequence.append(int(get_random_number(number_from, number_to)))
    return sequence

def timer():
    number_of_numbers = int(entry_1.get())
    number_from = int(entry_2.get())
    number_to = int(entry_3.get()) 
    sequence = get_sequence_of_numbers(number_of_numbers, number_from, number_to)
    while sequence.count(sequence[0])!=len(sequence):
        sequence = get_sequence_of_numbers(number_of_numbers, number_from, number_to)
        label_4.config(text=sequence)

window = tk.Tk()


label_1 = tk.Label(fg="black", 
    bg="white", 
    font=("Arial", 20),
    text="Enter the number of numbers: ")
label_1.grid()

entry_1 = tk.Entry(fg="black", 
    bg="white", 
    font=("Arial", 20))
entry_1.grid()


label_2 = tk.Label(fg="black", 
    bg="white", 
    font=("Arial", 20),
    text="The numbers in the sequence will be generated from: ")
label_2.grid()

entry_2 = tk.Entry(fg="black", 
    bg="white", 
    font=("Arial", 20))
entry_2.grid()


label_3 = tk.Label(fg="black", 
    bg="white", 
    font=("Arial", 20),
    text="to: ")
label_3.grid()

entry_3 = tk.Entry(fg="black", 
    bg="white", 
    font=("Arial", 20))
entry_3.grid()


button_1=tk.Button(text="Random", command=lambda: threading.Thread(target=timer, daemon=True).start(), font=("Arial", 20))
button_1.grid()

label_4 = tk.Label(fg="black", 
    bg="white", 
    font=("Arial", 24),
    text="")
label_4.grid()



window.mainloop()





