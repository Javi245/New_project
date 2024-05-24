import tkinter as tk


class MyFirstGui:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        self.master.geometry("400x200")
        self.button = tk.Button(master, text="Press me", command=master.quit)
        self.button.pack()

        self.canvas = tk.Canvas(master, width=200, height=100)
        self.canvas.pack()

        self.canvas.create_line(0, 0, 200, 100)

        self.label = tk.Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = tk.Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = tk.Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

    def close(self):
        print("Closing the GUI")
        self.master.quit()


root = tk.Tk()
my_gui = MyFirstGui(root)
root.mainloop()
