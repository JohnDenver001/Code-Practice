import tkinter as tk

def rubut(canvas):
    canvas.create_rectangle(0, 0, 400, 600, fill="#0A1E3F", outline="")

    def draw_cloud(x, y, scale):
        shadow_color = "#0A1E2D"
        cloud_color = "#1C3A64"
        offsets = [(0, 0), (20, -10), (40, 0)]
        for dx, dy in offsets:
            canvas.create_oval(x + dx, y + dy + 5, x + dx + 60*scale, y + dy + 30*scale, fill=shadow_color, outline="")
            canvas.create_oval(x + dx, y + dy, x + dx + 60*scale, y + dy + 30*scale, fill=cloud_color, outline="")

    draw_cloud(30, 30, 1)
    draw_cloud(180, 40, 1.2)
    draw_cloud(100, 70, 0.9)
    draw_cloud(250, 20, 1)

    canvas.create_oval(80, 180, 320, 550, fill="#0F274C", outline="")
    canvas.create_rectangle(120, 250, 280, 450, fill="#2A5D9F", outline="#1E3E70", width=2)
    canvas.create_rectangle(140, 270, 260, 430, fill="#3C76C4", outline="#2C5B9A", width=2)

    canvas.create_line(140, 270, 140, 430, fill="#1C3A64", width=2)
    canvas.create_line(260, 270, 260, 430, fill="#1C3A64", width=2)

    canvas.create_text(200, 340, text="lab u\nhehe", font=("Helvetica", 18, "bold"), fill="#FF69B4")
    canvas.create_text(200, 390, text="pansinin mo na ako pls", font=("Helvetica", 7, "bold"), fill="#FF69B4")

    canvas.create_polygon(140, 160, 260, 160, 250, 230, 150, 230,
                          fill="#3B4E7C", outline="#1D2C50", width=2)
    canvas.create_polygon(140, 160, 150, 230, 145, 230, 135, 160,
                          fill="#273A5D", outline="#1D2C50")  # left shading

    canvas.create_polygon(160, 190, 170, 185, 175, 195, 165, 200,
                          fill="#FF5F5F", outline="#B22222")
    canvas.create_polygon(225, 190, 235, 185, 240, 195, 230, 200,
                          fill="#FF5F5F", outline="#B22222")

    canvas.create_line(200, 150, 200, 130, fill="#78B6F2", width=3)
    canvas.create_oval(195, 120, 205, 130, fill="#FF4C4C", outline="#8B0000")

    canvas.create_rectangle(100, 270, 120, 400, fill="#2C5B9A", outline="#1E3E70")
    canvas.create_line(100, 270, 100, 400, fill="#1C3A64", width=2)
    canvas.create_rectangle(280, 270, 300, 400, fill="#2C5B9A", outline="#1E3E70")
    canvas.create_line(300, 270, 300, 400, fill="#1C3A64", width=2)

    canvas.create_rectangle(150, 450, 180, 520, fill="#1D3B6A", outline="#162D4F")
    canvas.create_line(150, 450, 150, 520, fill="#0E1E33", width=2)
    canvas.create_rectangle(220, 450, 250, 520, fill="#1D3B6A", outline="#162D4F")
    canvas.create_line(250, 450, 250, 520, fill="#0E1E33", width=2)

    canvas.create_rectangle(170, 370, 230, 380, fill="#5594DD", outline="#396EB1")

root = tk.Tk()
root.title("loveylovey my robot for u bb")
canvas = tk.Canvas(root, width=400, height=600)
canvas.pack()

rubut(canvas)
root.mainloop()
