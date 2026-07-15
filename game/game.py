import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("XO Game")
        self.root.geometry("420x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#2C3E50")

        self.current_player = "X"
        self.board = [""] * 9

        title = tk.Label(
            root,
            text="🎮 XO GAME",
            font=("Arial", 22, "bold"),
            bg="#2C3E50",
            fg="white"
        )
        title.pack(pady=10)

        self.status = tk.Label(
            root,
            text="Player X Turn",
            font=("Arial", 14),
            bg="#2C3E50",
            fg="yellow"
        )
        self.status.pack()

        frame = tk.Frame(root, bg="#2C3E50")
        frame.pack(pady=20)

        self.buttons = []

        for i in range(9):
            btn = tk.Button(
                frame,
                text="",
                font=("Arial", 28, "bold"),
                width=4,
                height=2,
                bg="white",
                command=lambda i=i: self.click(i)
            )
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons.append(btn)

        reset_btn = tk.Button(
            root,
            text="🔄 Restart",
            font=("Arial", 14, "bold"),
            bg="#27AE60",
            fg="white",
            command=self.reset
        )
        reset_btn.pack(pady=15)

    def click(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index]["text"] = self.current_player

            if self.check_winner():
                messagebox.showinfo("Winner", f"Player {self.current_player} Wins!")
                self.reset()
                return

            if "" not in self.board:
                messagebox.showinfo("Draw", "It's a Draw!")
                self.reset()
                return

            self.current_player = "O" if self.current_player == "X" else "X"
            self.status.config(text=f"Player {self.current_player} Turn")

    def check_winner(self):
        wins = [
            (0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)
        ]

        for a,b,c in wins:
            if self.board[a] == self.board[b] == self.board[c] != "":
                self.buttons[a].config(bg="lightgreen")
                self.buttons[b].config(bg="lightgreen")
                self.buttons[c].config(bg="lightgreen")
                return True

        return False

    def reset(self):
        self.current_player = "X"
        self.board = [""]*9
        self.status.config(text="Player X Turn")

        for btn in self.buttons:
            btn.config(text="", bg="white")
    pass

def main():
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    print(__name__)