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

        # store for two teams
        self.team_scores = [0, 0]
        self.team_wickets = [0, 0]
        self.team_balls = [0, 0]

        self.current_team = 0  # 0 = Team 1, 1 = Team 2

        self.setup_screen()

    # SETUP SCREEN 
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

        tk.Button(self.root, text="Start Match", bg="#0099cc", fg="black",
                  command=self.start_match).pack(pady=20)

    def start_match(self):
        try:
            self.total_overs = int(self.overs_entry.get())
            self.players = int(self.players_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers. for players and overs")
            return

        print("Overs per team:", self.total_overs)
        print("Players per team:", self.players)

        self.current_team = 0
        self.open_batting_screen()

    # BATTING SCREEN
    def open_batting_screen(self):
        t = self.current_team

        self.batting_window = tk.Toplevel()
        self.batting_window.title(f"Team {t+1} Batting")
        self.batting_window.geometry("600x300")
        self.batting_window.config(bg="#e6ffe6")

        tk.Label(self.batting_window, text=f"Team {t+1} Batting",
                 font=("Arial", 16, "bold"), bg="#e6ffe6").pack(pady=10)

        self.score_label = tk.Label(self.batting_window,
                                    text=f"Score: {self.team_scores[t]} / {self.team_wickets[t]}",
                                    font=("Arial", 14), bg="#e6ffe6")
        self.score_label.pack(pady=5)

        self.overs_label = tk.Label(self.batting_window,
                                    text=f"Overs: {self.team_balls[t]//6}.{self.team_balls[t]%6} / {self.total_overs}",
                                    font=("Arial", 12), bg="#e6ffe6")
        self.overs_label.pack(pady=5)

        frame = tk.Frame(self.batting_window, bg="#e6ffe6")
        frame.pack(pady=10)

        for i in range(7):
            tk.Button(frame, text=str(i), width=4,
                      command=lambda x=i: self.add_runs(x)).grid(row=0, column=i, padx=3, pady=3)

        tk.Button(self.batting_window, text="Wicket", width=10,
                  bg="red", fg="black", command=self.add_wicket).pack(pady=10)

    # SCORING
    def add_runs(self, runs):
        t = self.current_team
        self.team_scores[t] += runs
        self.team_balls[t] += 1
        self.update_labels()
        self.check_innings_end()

    def add_wicket(self):
        t = self.current_team
        self.team_wickets[t] += 1
        self.team_balls[t] += 1
        self.update_labels()
        self.check_innings_end()

    def update_labels(self):
        # self current team pointing to wrong team?
        
        t = self.current_team
        self.score_label.config(text=f"Score: {self.team_scores[t]} / {self.team_wickets[t]}")
        self.overs_label.config(text=f"Overs: {self.team_balls[t]//6}.{self.team_balls[t]%6} / {self.total_overs}")

    # INNINGS END CHECK
    def check_innings_end(self):
        t = self.current_team

        max_balls = self.total_overs * 6

        # wickets lost
        if self.team_wickets[t] >= self.players - 1:
            # -1? or just 0?  
            self.end_innings()
            return

        # overs used up
        if self.team_balls[t] >= max_balls:
            # n
            self.end_innings()
            return

    def end_innings(self):
        self.batting_window.destroy()

        # TEAM 1 DONE
        if self.current_team == 0:
            messagebox.showinfo("Innings Over", "Team 1 innings complete. Team 2 will now bat.")
            self.current_team = 1
            self.open_batting_screen()
            return

        # TEAM 2 DONE so MATCH OVER (only when current team =/= 0)
        self.end_match()

    # MATCH RESULT (Calculate winner, end program + display winner)
    def end_match(self):
        s1, s2 = self.team_scores
        b2 = self.team_balls[1]  # balls used by team 2

        max_balls = self.total_overs * 6
        balls_remaining = max_balls - b2

        # Convert balls remaining
        overs = balls_remaining // 6
        balls = balls_remaining % 6

        if s1 == s2:
            messagebox.showinfo("Match Result", "The match is a tie!")
            return

        if s1 > s2:
            message = f"Team 1 wins by {overs}.{balls} overs/balls remaining!"
        else:
            message = f"Team 2 wins by {overs}.{balls} overs/balls remaining!"

        messagebox.showinfo("Match Result", message)


if __name__ == "__main__":
    root = tk.Tk()
    app = CricketScoreTracker(root)
    root.mainloop()
