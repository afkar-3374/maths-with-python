import tkinter as tk
from tkinter import messagebox

def find_determinant():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        d = float(entry_d.get())

        det = a*d - b*c

        steps = (
            "|A| = ad − bc\n\n"
            f"= ({a} × {d}) − ({b} × {c})\n"
            f"= {a*d} − {b*c}\n"
            f"= {det}"
        )

        result_text.config(state="normal")
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, steps)
        result_text.config(state="disabled")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

# ---------------- WINDOW ---------------- #
root = tk.Tk()
root.title("2×2 Matrix Determinant")
root.geometry("420x420")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

# ---------------- FONTS ---------------- #
TITLE_FONT = ("Segoe UI", 15, "bold")
LABEL_FONT = ("Segoe UI", 11)
ENTRY_FONT = ("Segoe UI", 11)
CODE_FONT = ("Consolas", 11)

# ---------------- TITLE ---------------- #
tk.Label(
    root,
    text="2×2 Matrix Determinant",
    font=TITLE_FONT,
    fg="white",
    bg="#1e1e1e"
).pack(pady=12)

# ---------------- MATRIX INPUT ---------------- #
matrix_frame = tk.Frame(root, bg="#1e1e1e")
matrix_frame.pack(pady=5)

def mlabel(text, r, c):
    tk.Label(
        matrix_frame,
        text=text,
        font=LABEL_FONT,
        fg="white",
        bg="#1e1e1e"
    ).grid(row=r, column=c, padx=6, pady=6)

mlabel("a", 0, 0)
mlabel("b", 0, 1)
mlabel("c", 1, 0)
mlabel("d", 1, 1)

entry_a = tk.Entry(matrix_frame, width=6, font=ENTRY_FONT)
entry_b = tk.Entry(matrix_frame, width=6, font=ENTRY_FONT)
entry_c = tk.Entry(matrix_frame, width=6, font=ENTRY_FONT)
entry_d = tk.Entry(matrix_frame, width=6, font=ENTRY_FONT)

entry_a.grid(row=0, column=2)
entry_b.grid(row=0, column=3)
entry_c.grid(row=1, column=2)
entry_d.grid(row=1, column=3)

# ---------------- BUTTON ---------------- #
tk.Button(
    root,
    text="Find Determinant",
    font=("Segoe UI", 11, "bold"),
    bg="#007acc",
    fg="white",
    padx=10,
    pady=5,
    command=find_determinant
).pack(pady=12)

# ---------------- RESULT CARD ---------------- #
result_frame = tk.Frame(root, bg="#252526", bd=2, relief="groove")
result_frame.pack(padx=20, pady=10, fill="x")

tk.Label(
    result_frame,
    text="Solution Steps",
    font=("Segoe UI", 11, "bold"),
    fg="#9cdcfe",
    bg="#252526"
).pack(anchor="w", padx=10, pady=5)

result_text = tk.Text(
    result_frame,
    height=7,
    font=CODE_FONT,
    bg="#1e1e1e",
    fg="white",
    wrap="word",
    state="disabled"
)
result_text.pack(padx=10, pady=5, fill="x")

root.mainloop()
