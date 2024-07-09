from tkinter import *

# Function to convert miles to kilometers
def miles_to_km():
    miles_value = float(miles_input.get())
    km_value = miles_value * 1.609
    km_result_label.config(text=f"{km_value:.2f}")

# Setup the main window
window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=300, height=100)

# Setup input for miles
miles_input = Entry(window)
miles_input.grid(column=1, row=0)

# Setup miles label
miles_label = Label(window, text="Miles")
miles_label.grid(column=2, row=0)

# Setup "is equal to" label
is_equal_label = Label(window, text="is equal to")
is_equal_label.grid(column=0, row=1)

# Setup result label for kilometers
km_result_label = Label(window, text="0")
km_result_label.grid(column=1, row=1)

# Setup kilometers label
km_label = Label(window, text="Km")
km_label.grid(column=2, row=1)

# Setup calculate button
calculate_button = Button(window, text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

# Keep the window open
window.mainloop()
