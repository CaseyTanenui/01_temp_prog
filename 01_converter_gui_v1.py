from tkinter import *


class Convertor:

    def __init__(self):

        # Set up gui frame
        self.temp_frame = Frame()
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame, text = "Temperature Convertor", font = ("Arial", "16", "bold"))

        self.temp_heading.grid(row=0)

        instructions = "Please enter a temperature below and then press one of the buttons to convert it from centergrade to " \
                       "fahrenheit" \

        self.temp_instructions = Label(self.temp_frame, text = instructions, wrap=250, width=40, justify="left")

        self.temp_instructions.grid(row=1)

# main routine goes here
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    Convertor()
    root.mainloop(0)
