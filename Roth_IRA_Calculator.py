import tkinter as tk
import pandas as pd  
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

current_canvas = None

def calc(root, starting_investment, annual_contribution, current_age, retirement_age,annual_return, result_label):
    global current_canvas

    if current_canvas is not None:
        current_canvas.get_tk_widget().destroy()
        current_canvas = None
    
    if current_age < 18:
        result_label.config(text="You must be at least 18 years old to open a Roth IRA Account")
    
    elif retirement_age < current_age:
        result_label.config(text="Retirement Age must be older then your current age")
    else: 
    
        df = pd.DataFrame([[current_age, starting_investment]], columns=['Age', 'Amount'])
        age = current_age
        total_amount = starting_investment

        for i in range(retirement_age - current_age):
            total_amount = (total_amount * annual_return) + annual_contribution
            age = age + 1
            new_row = {"Age": age, "Amount": total_amount}
            df = df._append(new_row, ignore_index=True)
    
        fig = Figure(figsize=(5, 4), dpi=100)
        ax = fig.add_subplot(111)
        df.plot(x='Age', y='Amount', kind='line', title='Roth IRA Wealth Accumulation Graph', marker='o', ax=ax)
    
        result_label.config(text=f"When you are {age}, you will have ${total_amount:,.2f}")
        current_canvas = FigureCanvasTkAgg(fig, master=root)
        current_canvas.draw()
        current_canvas.get_tk_widget().pack()

    
def main():
   
    root = tk.Tk()
    root.title("Roth IRA Calculator")
    root.geometry("800x700")
    tk.Label(root, text="Roth IRA Calculator", font=("Times New Roman", 16), fg="black").pack()
   
    tk.Label(root, text="What is your starting amount?").pack(side='top', anchor='w')
    starting_investment_entry = tk.Entry(root)
    starting_investment_entry.pack(side='top', anchor='w')

    tk.Label(root, text="What is your annual contribution?").pack(side='top', anchor='w')
    annual_contribution_entry = tk.Entry(root)
    annual_contribution_entry.pack(side='top', anchor='w')
 
    tk.Label(root, text="What is your current age?").pack(side='top', anchor='w')
    current_age_entry = tk.Entry(root)
    current_age_entry.pack(side='top', anchor='w')
   
    tk.Label(root, text="What is your retirement age?").pack(side='top', anchor='w')
    retirement_age_entry = tk.Entry(root)
    retirement_age_entry.pack(side='top', anchor='w')

    tk.Label(root, text="What is your expected annual return?").pack(side='top', anchor='w')
    annual_return_entry = tk.Entry(root)
    annual_return_entry.pack(side='top', anchor='w')
    
    tk.Button(
    root,
    text="Enter",
    command=lambda: calc(
        root,
        int(starting_investment_entry.get()),
        int(annual_contribution_entry.get()),
        int(current_age_entry.get()),
        int(retirement_age_entry.get()),
        float(annual_return_entry.get()[:-1]) / 100 + 1,
        result_label
    )
).pack(side='top', anchor='w')
    result_label = tk.Label(root, text="", font=("Times New Roman", 9))
    result_label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()