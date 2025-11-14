import tkinter as tk
from tkinter import messagebox

class CricketScoreTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Cricket Score Tracker")
        self.root.geometry("400x300")
        self.root.config(bg="#e6f7ff")

        # match settings
        self.total_overs = 0
        self.players = 0

        # team score 
        self.score = 0
        self.wickets = 0
        self.balls = 0

        self.setup_screen()

    # SETUP SCREEN 
    # Ask for overs and players

    def setup_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=" Cricket Score Tracker",
                 font=("Arial", 16, "bold"), bg="#e6f7ff").pack(pady=20)

        tk.Label(self.root, text="Enter overs given for team (overs not balls):",
                 bg="#e6f7ff").pack()
        self.overs_entry = tk.Entry(self.root)
        self.overs_entry.pack(pady=5)

        tk.Label(self.root, text="Enter number of players on each team:",
                 bg="#e6f7ff").pack()
        self.players_entry = tk.Entry(self.root)
        self.players_entry.pack(pady=5)

# 
        tk.Button(self.root, text="Start Match", bg="#0099cc", fg="black",
                  command=self.start_match).pack(pady=20)

    def start_match(self):
        try:
            self.total_overs = int(self.overs_entry.get())
            self.players = int(self.players_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers. for players and overs")
            return

        # print to console (your requirement)
        print("Overs per team:", self.total_overs)
        print("Players per team:", self.players)

        # automatically open the batting screen
        self.open_batting_screen()

    # batting screen 
    # 0-6 buttons 
 
    def open_batting_screen(self):
        self.batting_window = tk.Toplevel()
        self.batting_window.title("Team 1 Batting")
        self.batting_window.geometry("400x600")
        # change size? idk
        self.batting_window.config(bg="#e6ffe6")

# 
        tk.Label(self.batting_window, text="Team 1 Batting",
                 font=("Arial", 16, "bold"), bg="#e6ffe6").pack(pady=10)

        self.score_label = tk.Label(self.batting_window,
                                    text=f"Score: {self.score} / {self.wickets}",
                                    font=("Arial", 14), bg="#e6ffe6")
        self.score_label.pack(pady=5)

        self.overs_label = tk.Label(self.batting_window,
                                    text=f"Overs: {self.balls//6}.{self.balls%6} / {self.total_overs}",
                                    font=("Arial", 12), bg="#e6ffe6")
        self.overs_label.pack(pady=5)

        frame = tk.Frame(self.batting_window, bg="#e6ffe6")
        frame.pack(pady=10)



        # run buttons 0–6
        for i in range(7):
            tk.Button(frame, text=str(i), width=4,
                      command=lambda x=i: self.add_runs(x)).grid(row=0, column=i, padx=3, pady=3)
            # might change size layout later

        # wicket button
        tk.Button(self.batting_window, text="Wicket", width=10,
                  bg="red", fg="black", command=self.add_wicket).pack(pady=10)

    # UPDATE FUNCTIOns
    # For runs and wickets
    def add_runs(self, runs):
        self.score += runs
        self.balls += 1
        self.update_labels()

    def add_wicket(self):
        self.wickets += 1
        self.balls += 1
        self.update_labels()

    def update_labels(self):
        self.score_label.config(text=f"Score: {self.score} / {self.wickets}")
        self.overs_label.config(text=f"Overs: {self.balls//6}.{self.balls%6} / {self.total_overs}")


# Loop
if __name__ == "__main__":
    root = tk.Tk()
    app = CricketScoreTracker(root)
    root.mainloop()
