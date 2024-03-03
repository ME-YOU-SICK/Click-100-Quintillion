import tkinter as tk
import random

class ClickerGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Clicker Game")

        self.points = 0
        self.click_points = 1
        self.click_multiplier = 1
        self.bonus_chance = 0.1
        self.upgrade_cost = 10
        
        self.create_widgets()

    def create_widgets(self):
        self.master.config(bg="lightblue")

        self.win_text = tk.Label(self.master, text="Reach 100 Quintillion To Win", font=("Arial", 14, "bold"), bg="lightblue", fg="purple")
        self.win_text.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        self.points_label = tk.Label(self.master, text="Points: 0", font=("Arial", 12), bg="lightblue", fg="green")
        self.points_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        self.click_button = tk.Button(self.master, text="Click", bg="red", fg="white", font=("Arial", 12, "bold"), command=self.click)
        self.click_button.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.upgrade_button = tk.Button(self.master, text="Upgrade", font=("Arial", 12, "bold"), bg="purple", fg="white", command=self.purchase_upgrade)
        self.upgrade_button.grid(row=2, column=1, padx=10, pady=10, sticky="e")

    def click(self):
        self.points += self.click_points * self.click_multiplier
        if random.random() < self.bonus_chance:
            self.points += self.click_points * self.click_multiplier * 4
        self.update_points_label()
        self.check_achievements()

    def update_points_label(self):
        self.points_label.config(text="Points: " + str(self.points))
        if self.points >= 100000000000000000:
            tk.messagebox.showinfo("Congratulations!", "You have reached 100 Quintillion points and won the game!")

    def purchase_upgrade(self):
        if self.points >= self.upgrade_cost:
            self.click_multiplier += 1
            self.points -= self.upgrade_cost
            self.upgrade_cost = int(self.upgrade_cost * 1.1)  # increase upgrade cost by 10%
            self.update_points_label()
        else:
            tk.messagebox.showinfo("Insufficient Points", "You need at least " + str(self.upgrade_cost) + " points to purchase this upgrade.")

    def check_achievements(self):
        milestones = [1000, 10000, 100000, 1000000]
        if self.points in milestones:
            self.change_interface_color()

    def change_interface_color(self):
        colors = ["lightblue", "lightgreen", "lightyellow", "lightcoral", "lightsalmon"]
        new_color = random.choice(colors)
        self.master.config(bg=new_color)
        self.win_text.config(bg=new_color)
        self.points_label.config(bg=new_color)
        self.click_button.config(bg=new_color)
        self.upgrade_button.config(bg=new_color)

def main():
    root = tk.Tk()
    root.geometry("300x200")
    root.resizable(False, False)
    game = ClickerGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
