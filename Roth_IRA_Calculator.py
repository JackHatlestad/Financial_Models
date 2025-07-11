import tkinter as tk
import pandas as pd  

def calc(starting_investment, annual_contribution, current_age, retirement_age,annual_return):
    df = pd.DataFrame([[current_age, starting_investment]], columns=['Age', 'Amount'])
    print(current_age)
    

def main():
   
    root = tk.Tk()
    root.title("Roth IRA Calculator")
    root.geometry("800x700")
    tk.Label(root, text="Roth IRA Calculator", font=("Times New Roman", 16), fg="black").pack()
   
    tk.Label(root, text="What is your starting amount?").pack(side='top', anchor='w')
    starting_investment_entry = tk.Entry(root)
    starting_investment_entry.pack(side='top', anchor='w')
    starting_investment = starting_investment_entry.get()


    tk.Label(root, text="What is your annual contribution?").pack(side='top', anchor='w')
    annual_contribution_entry = tk.Entry(root)
    annual_contribution_entry.pack(side='top', anchor='w')
    annual_contribution = annual_contribution_entry.get()

    tk.Label(root, text="What is your current age?").pack(side='top', anchor='w')
    current_age_entry = tk.Entry(root)
    current_age_entry.pack(side='top', anchor='w')
    current_age = current_age_entry.get()
    print(current_age)

    tk.Label(root, text="What is your retirement age?").pack(side='top', anchor='w')
    retirement_age_entry = tk.Entry(root)
    retirement_age_entry.pack(side='top', anchor='w')
    retirement_age = retirement_age_entry.get()

    tk.Label(root, text="What is your expected annual return?").pack(side='top', anchor='w')
    annual_return_entry = tk.Entry(root)
    annual_return_entry.pack(side='top', anchor='w')
    annual_return = annual_return_entry.get()
    
    tk.Button(root, text="Enter", command=calc(starting_investment, annual_contribution, current_age, retirement_age,
                                                annual_return)).pack(side='top', anchor='w')
    result_label = tk.Label(root, text="", font=("Times New Roman", 9))
    result_label.pack()

    root.mainloop()



if __name__ == "__main__":
    main()