import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from calculator_functions import compound_interest_continuously, compound_interest_per_year

class window(tk.Tk):
    """A simple compound interest calculator GUI"""


    def __init__(self):
        """Initialize the compounud interest calculator"""
        tk.Tk.__init__(self)

        # Create main frame
        over_frame = tk.Frame(self)
        over_frame.pack(padx=50)

        # Right frame for entry widgets
        right_frame = tk.Frame(over_frame)
        right_frame.pack(side=tk.RIGHT)

        # Entry widgets
        principal_entry = tk.Entry(right_frame)
        principal_entry.pack(pady=5)

        time_entry = tk.Entry(right_frame)
        time_entry.pack(pady=5)

        rate_entry = tk.Entry(right_frame)
        rate_entry.pack(pady=5)

        #cpy = compound per year
        cpy_entry = tk.Entry(right_frame)
        cpy_entry.pack(pady=5)

        # Left frame for label widgets
        left_frame = tk.Frame(over_frame)
        left_frame.pack(side=tk.LEFT)

        # Label widgets
        principal_label = tk.Label(left_frame, text="Principal : ")
        principal_label.pack(pady=5)

        time_label = tk.Label(left_frame, text="Time in years : ")
        time_label.pack(pady=5)

        rate_label = tk.Label(left_frame, text=r"Rate (% as a decimal): ")
        rate_label.pack(pady=5)

        cpy_label = tk.Label(left_frame, text="Compounds per Year ('oo' if conintuous) : ")
        cpy_label.pack(pady=5)

        # List of entry boxes to pass into class method
        entries = [principal_entry, time_entry, rate_entry, cpy_entry]

        # Button to trigger methods
        button = tk.Button(self, text="Calculate", command= lambda: self.validate(entries))
        button.pack()


    def calculate(self, principal, time, rate, compound_per_year):
        """Calculate compound interest based on user inputs"""

        if compound_per_year == 'oo':
            total = compound_interest_continuously(principal, time, rate)
        else:
            total = compound_interest_per_year(principal, rate, time, compound_per_year)

        # Display calculated total in a messagebox        
        messagebox.showinfo(message=f"Total after compounded interest is : ${"{:.2f}".format(total)}")
        return


    def validate(self, entries):
        """Validate user inputes and trigger calculation"""
        
        try:
            principal = float(entries[0].get())
        except ValueError:
            messagebox.showerror(message="Incorrect value for Principal.")
            return
            
        try:
            time = int(entries[1].get())
        except ValueError:
            messagebox.showerror(message="Incorrect value for Time.")
            return

        try:
            rate = float(entries[2].get())
        except ValueError:
            messagebox.showerror(message="Incorrect value for Rate.")
            return
            
        compound_per_year = entries[3].get()

        if compound_per_year!="oo":
            try:
                compound_per_year = float(compound_per_year)
            except ValueError:
                messagebox.showerror(message="Incorrect value for Compounds per Year.")
                return
        
        self.calculate(principal, time, rate, compound_per_year)
        

if __name__ == "__main__":
    app = window()
    app.mainloop()
