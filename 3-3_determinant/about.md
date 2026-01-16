# Day 7 – Determinant of a 3×3 Matrix (GUI using Python)

## Topic
**CO1 – Matrices and Determinants**

---

## Objective
To calculate the **determinant of a 3×3 matrix** using Python and visualize the  
**step-by-step calculation** through a **Tkinter-based GUI**.

---

## Mathematical Concept
For a 3×3 matrix:

| a  b  c |
| d  e  f |
| g  h  i |

The determinant is given by:

|A| = a(ei − fh) − b(di − fg) + c(dh − eg)

This method is known as the **cofactor expansion**.

---

## Approach Used
- Accept matrix values from the user using a GUI
- Apply the determinant formula programmatically
- Display each calculation step clearly
- Show the final determinant value

---

## Python Code (Tkinter GUI)

```python
import tkinter as tk
from tkinter import messagebox

def find_determinant_3x3():
    try:
        a = float(ea.get()); b = float(eb.get()); c = float(ec.get())
        d = float(ed.get()); e = float(ee.get()); f = float(ef.get())
        g = float(eg.get()); h = float(eh.get()); i = float(ei.get())

        det = a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)

        steps = (
            "|A| = a(ei − fh) − b(di − fg) + c(dh − eg)\n\n"
            f"= {a}({e}×{i} − {f}×{h}) − {b}({d}×{i} − {f}×{g}) + {c}({d}×{h} − {e}×{g})\n"
            f"= {a*(e*i - f*h)} − {b*(d*i - f*g)} + {c*(d*h - e*g)}\n"
            f"= {det}"
        )

        out.config(state="normal")
        out.delete("1.0", tk.END)
        out.insert(tk.END, steps)
        out.config(state="disabled")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

root = tk.Tk()
root.title("3×3 Matrix Determinant")
root.geometry("520x480")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

FONT_T = ("Segoe UI", 15, "bold")
FONT_L = ("Segoe UI", 11)
FONT_E = ("Segoe UI", 11)
FONT_C = ("Consolas", 11)

tk.Label(root, text="3×3 Matrix Determinant", font=FONT_T,
         fg="white", bg="#1e1e1e").pack(pady=10)

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(pady=5)

def lab(t, r, c):
    tk.Label(frame, text=t, font=FONT_L,
             fg="white", bg="#1e1e1e").grid(row=r, column=c, padx=6, pady=6)

labels = [("a","b","c"),("d","e","f"),("g","h","i")]
for r in range(3):
    for c in range(3):
        lab(labels[r][c], r, c)

ea=tk.Entry(frame, width=6, font=FONT_E); eb=tk.Entry(frame, width=6, font=FONT_E); ec=tk.Entry(frame, width=6, font=FONT_E)
ed=tk.Entry(frame, width=6, font=FONT_E); ee=tk.Entry(frame, width=6, font=FONT_E); ef=tk.Entry(frame, width=6, font=FONT_E)
eg=tk.Entry(frame, width=6, font=FONT_E); eh=tk.Entry(frame, width=6, font=FONT_E); ei=tk.Entry(frame, width=6, font=FONT_E)

entries = [[ea,eb,ec],[ed,ee,ef],[eg,eh,ei]]
for r in range(3):
    for c in range(3):
        entries[r][c].grid(row=r, column=c+3)

tk.Button(root, text="Find Determinant (3×3)",
          font=("Segoe UI",11,"bold"),
          bg="#007acc", fg="white",
          command=find_determinant_3x3).pack(pady=10)

card = tk.Frame(root, bg="#252526", bd=2, relief="groove")
card.pack(padx=20, pady=10, fill="x")

tk.Label(card, text="Solution Steps",
         font=("Segoe UI",11,"bold"),
         fg="#9cdcfe", bg="#252526").pack(anchor="w", padx=10, pady=5)

out = tk.Text(card, height=8, font=FONT_C,
              bg="#1e1e1e", fg="white",
              wrap="word", state="disabled")
out.pack(padx=10, pady=5, fill="x")

root.mainloop()
