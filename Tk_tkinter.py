import tkinter as tk
from tkinter import messagebox

class ATMInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("ATM Interface")
        self.master.geometry("400x300")

        self.balance = 1000  # Starting balance
        self.transaction_history = []

        # Widgets
        self.label_balance = tk.Label(self.master, text=f"Balance: ${self.balance}")
        self.label_balance.pack(pady=10)

        self.entry_amount = tk.Entry(self.master)
        self.entry_amount.pack(pady=5)

        self.button_withdraw = tk.Button(self.master, text="Withdraw", command=self.withdraw)
        self.button_withdraw.pack(pady=5)

        self.button_deposit = tk.Button(self.master, text="Deposit", command=self.deposit)
        self.button_deposit.pack(pady=5)

        self.button_transfer = tk.Button(self.master, text="Transfer", command=self.transfer)
        self.button_transfer.pack(pady=5)

        self.button_history = tk.Button(self.master, text="Transaction History", command=self.show_history)
        self.button_history.pack(pady=5)

        self.button_quit = tk.Button(self.master, text="Quit", command=self.master.destroy)
        self.button_quit.pack(pady=5)

    def withdraw(self):
        try:
            amount = float(self.entry_amount.get())
            if amount <= 0:
                raise ValueError("Amount must be greater than 0")

            if amount > self.balance:
                raise ValueError("Insufficient funds")

            # Update balance
            self.balance -= amount

            # Add transaction to history
            self.transaction_history.append(f"Withdrawal: ${amount}")

            # Display updated balance
            self.label_balance.config(text=f"Balance: ${self.balance}")

            # Show success message
            messagebox.showinfo("Success", f"Withdrawal successful! Remaining balance: ${self.balance}")

        except ValueError as e:
            messagebox.showerror("Error", str(e))
            self.entry_amount.delete(0, tk.END)  # Clear entry

    def deposit(self):
        try:
            amount = float(self.entry_amount.get())
            if amount <= 0:
                raise ValueError("Amount must be greater than 0")

            # Update balance
            self.balance += amount

            # Add transaction to history
            self.transaction_history.append(f"Deposit: ${amount}")

            # Display updated balance
            self.label_balance.config(text=f"Balance: ${self.balance}")

            # Show success message
            messagebox.showinfo("Success", f"Deposit successful! New balance: ${self.balance}")

        except ValueError as e:
            messagebox.showerror("Error", str(e))
            self.entry_amount.delete(0, tk.END)  # Clear entry

    def transfer(self):
        try:
            amount = float(self.entry_amount.get())
            if amount <= 0:
                raise ValueError("Amount must be greater than 0")

            if amount > self.balance:
                raise ValueError("Insufficient funds")

            # Update balance
            self.balance -= amount

            # Add transaction to history
            self.transaction_history.append(f"Transfer: ${amount}")

            # Display updated balance
            self.label_balance.config(text=f"Balance: ${self.balance}")

            # Show success message
            messagebox.showinfo("Success", f"Transfer successful! Remaining balance: ${self.balance}")

        except ValueError as e:
            messagebox.showerror("Error", str(e))
            self.entry_amount.delete(0, tk.END)  # Clear entry

    def show_history(self):
        history_str = "\n".join(self.transaction_history)
        messagebox.showinfo("Transaction History", f"Transaction History:\n{history_str}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ATMInterface(root)
    root.mainloop()
