import tkinter as tk
from tkinter import messagebox

class CricketScoreTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Cricket Score Tracker")
        self.root.geometry("400x300")
        self.root.config(bg="white")  # changed to white

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
                 font=("Roboto Condensed", 16, "bold"), bg="white").pack(pady=20)

        tk.Label(self.root, text="Enter overs given for team (overs not balls):",
                 bg="white").pack()
        self.overs_entry = tk.Entry(self.root)
        self.overs_entry.pack(pady=5)

        tk.Label(self.root, text="Enter number of players on each team:",
                 bg="white").pack()
        self.players_entry = tk.Entry(self.root)
        self.players_entry.pack(pady=5)

        tk.Button(self.root, text="Start Match", bg="black", fg="black",
                  command=self.start_match).pack(pady=20)

    def start_match(self):
        try:
            self.total_overs = int(self.overs_entry.get())
            self.players = int(self.players_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for players and overs.")
            return

        self.current_team = 0
        self.open_batting_screen()

    # BATTING SCREEN
    def open_batting_screen(self):
        t = self.current_team

        self.batting_window = tk.Toplevel()
        self.batting_window.title(f"Team {t+1} Batting")
        self.batting_window.geometry("600x300")
        self.batting_window.config(bg="white")  # white bg

        tk.Label(self.batting_window, text=f"Team {t+1} Batting",
                 font=("Roboto Condensed", 16, "bold"), bg="white").pack(pady=10)

        self.score_label = tk.Label(self.batting_window,
            text=f"Score: {self.team_scores[t]} / {self.team_wickets[t]}",
            font=("Roboto Condensed", 14), bg="white")
        self.score_label.pack(pady=5)

        self.overs_label = tk.Label(self.batting_window,
            text=f"Overs: {self.team_balls[t]//6}.{self.team_balls[t]%6} / {self.total_overs}",
            font=("Roboto Condensed", 12), bg="white")
        self.overs_label.pack(pady=5)

        # Required run rate only for team 2
        if t == 1:
            self.rrr_label = tk.Label(self.batting_window, text="Required Run Rate: --",
                                      bg="white", font=("Roboto Condensed", 12))
            self.rrr_label.pack(pady=5)

        frame = tk.Frame(self.batting_window, bg="white")
        frame.pack(pady=10)

        for i in range(7):
            tk.Button(frame, text=str(i), width=4, bg="black", fg="black",
                      command=lambda x=i: self.add_runs(x)).grid(row=0, column=i, padx=3, pady=3)

        tk.Button(self.batting_window, text="Wicket", width=10,
                  bg="black", fg="black", command=self.add_wicket).pack(pady=10)

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
        t = self.current_team

        self.score_label.config(text=f"Score: {self.team_scores[t]} / {self.team_wickets[t]}")
        self.overs_label.config(
            text=f"Overs: {self.team_balls[t]//6}.{self.team_balls[t]%6} / {self.total_overs}"
        )

        if t == 1:
            remaining = (self.team_scores[0] - self.team_scores[1]) + 1
            balls_left = (self.total_overs * 6) - self.team_balls[1]
            if balls_left > 0:
                rrr = remaining / (balls_left / 6)
                self.rrr_label.config(text=f"Required Run Rate: {rrr:.2f}")
            else:
                self.rrr_label.config(text="Required Run Rate: --")

    # INNINGS END CHECK
    def check_innings_end(self):
        t = self.current_team
        max_balls = self.total_overs * 6

        if self.team_wickets[t] >= self.players - 1:
            self.end_innings()
            return

        if self.team_balls[t] >= max_balls:
            self.end_innings()
            return

        # team 2 wins mid-chase
        if t == 1 and self.team_scores[1] > self.team_scores[0]:
            self.end_innings()

    def end_innings(self):
        self.batting_window.destroy()

        if self.current_team == 0:
            messagebox.showinfo("Innings Over", "Team 1 innings complete. Team 2 will now bat.")
            self.current_team = 1
            self.open_batting_screen()
        else:
            self.end_match()

    # MATCH RESULT WINDOW
    def end_match(self):
        s1, s2 = self.team_scores
        b1, b2 = self.team_balls
        w1, w2 = self.team_wickets

        max_balls = self.total_overs * 6
        balls_remaining = max_balls - b2

        # Calculate remaining overs and balls
        rem_overs = balls_remaining // 6
        rem_balls = balls_remaining % 6

        # Decide winner
        if s1 == s2:
            winner_text = "Match Tied!"
        elif s1 > s2:
            winner_text = f"Team 1 wins by {s1 - s2} runs!"
        else:
            winner_text = f"Team 2 wins with {rem_overs}.{rem_balls} overs remaining!"

        # New window for result
        result_window = tk.Toplevel()
        result_window.title("Match Result")
        result_window.geometry("400x300")
        result_window.config(bg="white")

        tk.Label(result_window, text=winner_text,
                 font=("Roboto Condensed", 18, "bold"),
                 bg="white").pack(pady=10)

        summary = (
            f"Team 1: {s1}/{w1} in {b1//6}.{b1%6} overs\n"
            f"Team 2: {s2}/{w2} in {b2//6}.{b2%6} overs"
        )

        tk.Label(result_window, text=summary, bg="white",
                 font=("Roboto Condensed", 14)).pack(pady=20)

        tk.Button(result_window, text="Close", bg="black", fg="black",
                  command=result_window.destroy).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = CricketScoreTracker(root)
    root.mainloop()
