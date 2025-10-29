import tkinter as tk
from tkinter import messagebox

# STARTUP SCREEN
# has the entry for th e number of players and overs
# change to class, and set line 19 to start match
def setup_screen(root):
    root.config(bg="#e6f7ff")
    tk.Label(root, text=" Cricket Score Tracker", font=("Arial", 16, "bold"), bg="#e6f7ff").pack(pady=20)

    tk.Label(root, text="Enter overs given for team, overs not balls): ", bg="#e6f7ff").pack()
    # label.fetch in function to en loop when needed here (or save to local var)
    overs_entry = tk.Entry(root)
    overs_entry.pack(pady=5)

    tk.Label(root, text="Enter number of  players on each team: ", bg="#e6f7ff").pack()
    players_entry = tk.Entry(root)
    players_entry.pack(pady=5)

    tk.Button(root, text="Start Match", bg="#0099cc", fg="black", 
              command=lambda: messagebox.showinfo("Info", "The macth was started")).pack(pady=20)

# TEMP - Change into root.self (in class) and move into class to be called when needed (2x per execution for each batting team, reset score to the new batting team in between)
def temp_batting_screen():
    batting_window = tk.Toplevel()
    batting_window.title("Team 1 Batting")
    batting_window.geometry("400x400")
    batting_window.config(bg="#e6ffe6")
# ititailizing

    tk.Label(batting_window, text="Team 1 Batting", font=("Arial", 16, "bold"), bg="#e6ffe6").pack(pady=10)
    tk.Label(batting_window, text="Score: 0 / 0", font=("Arial", 14), bg="#e6ffe6").pack(pady=5)
    tk.Label(batting_window, text="Overs: 0.0 / 5", font=("Arial", 12), bg="#e6ffe6").pack(pady=5)

    # NOT WORKING WO FUNCTIONALITY
    # tk.Label(batting_window, text="Run Rate: 0.0 / 5", font=("Arial", 12), bg="#e6ffe6").pack(pady=5)
    # tk.Label(batting_window, text="Run Rate Rerquired : 0.0 / 5", font=("Arial", 12), bg="#e6ffe6").pack(pady=5)


    frame = tk.Frame(batting_window, bg="#e6ffe6")
    frame.pack(pady=10)

    for i in range(7):
        tk.Button(frame, text=str(i), width=4).grid(row=0, column=i, padx=3, pady=3)

    tk.Button(batting_window, text="Wicket", width=10, bg="red", fg="black").pack(pady=10)

def main():
    root = tk.Tk()
    root.title("Cricket Score Tracker")
    root.geometry("400x400")


    setup_screen(root)

    temp_batting_screen()

    root.mainloop()

# infite loop (check for batting later on when to break loop with the final screen)
while True:
    main()
