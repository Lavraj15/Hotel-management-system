

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector

# Database connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="hotel_db"
    )

# Add reservation function
def add_reservation():
    guest_name = entry_guest_name.get()
    room_type = combo_room_type.get()
    stay_duration = entry_stay_duration.get()

    if guest_name and room_type and stay_duration:
        conn = connect_db()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO reservations (guest_name, room_type, stay_duration) VALUES (%s, %s, %s)",
                (guest_name, room_type, stay_duration)
            )
            conn.commit()
            messagebox.showinfo("Success", f"Reservation added successfully for {guest_name}!")
            entry_guest_name.delete(0, tk.END)
            combo_room_type.set('')
            entry_stay_duration.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"Error adding reservation: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        messagebox.showwarning("Input Error", "Please fill all fields.")

# Hover effect functions
def on_enter(e):
    add_button.config(background='#FF6347')

def on_leave(e):
    add_button.config(background='#FFA07A')

def open_main_window():
    root = tk.Tk()
    root.title("Hotel Management System")
    root.state('zoomed')

    style = ttk.Style()
    style.theme_create("colored", parent="alt", settings={
        "TNotebook.Tab": {
            "configure": {"padding": [5, 1], "background": "#FFA500"},
            "map": {"background": [("selected", "#FF4500")]}
        }
    })
    style.theme_use("colored")

    tab_control = ttk.Notebook(root)

    tab_reservations = ttk.Frame(tab_control)
    tab_control.add(tab_reservations, text='Reservations')

    try:
        bg_image = Image.open("background.png")
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(tab_reservations, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.place(relwidth=1, relheight=1)
    except Exception as e:
        messagebox.showwarning("Image Error", f"Error loading background image: {e}")

    frame_reservation = ttk.Frame(tab_reservations, padding="10")
    frame_reservation.place(relx=0.5, rely=0.5, anchor='center')

    ttk.Label(frame_reservation, text="Guest Name:").grid(row=0, column=0, padx=10, pady=5)
    global entry_guest_name
    entry_guest_name = ttk.Entry(frame_reservation)
    entry_guest_name.grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(frame_reservation, text="Room Type:").grid(row=1, column=0, padx=10, pady=5)
    global combo_room_type
    combo_room_type = ttk.Combobox(frame_reservation, values=["Single", "Double", "Suite"])
    combo_room_type.grid(row=1, column=1, padx=10, pady=5)

    ttk.Label(frame_reservation, text="Stay Duration (nights):").grid(row=2, column=0, padx=10, pady=5)
    global entry_stay_duration
    entry_stay_duration = ttk.Entry(frame_reservation)
    entry_stay_duration.grid(row=2, column=1, padx=10, pady=5)

    global add_button
    add_button = tk.Button(frame_reservation, text="Add Reservation", command=add_reservation, background='#FFA07A')
    add_button.grid(row=3, columnspan=2, pady=20)
    add_button.bind("<Enter>", on_enter)
    add_button.bind("<Leave>", on_leave)

    tab_about = ttk.Frame(tab_control)
    tab_control.add(tab_about, text='About')

    ttk.Label(tab_about, text="About Developers ", font=('Helvetica', 18, 'bold')).pack(pady=20)
    ttk.Label(tab_about, text="Frontend Developer ", font=('Helvetica', 12, 'bold')).pack(pady=10)
    ttk.Label(tab_about, text="Developed By: Harshit Hiranwal").pack()
    ttk.Label(tab_about, text="Contact: harshithiranwal@gmail.com").pack()

    try:
        profile_image1 = Image.open("profile.jpg")
        profile_image1 = profile_image1.resize((200, 200), Image.LANCZOS)
        profile_photo1 = ImageTk.PhotoImage(profile_image1)
        profile_label1 = tk.Label(tab_about, image=profile_photo1)
        profile_label1.image = profile_photo1
        profile_label1.pack(pady=10)
    except Exception as e:
        messagebox.showwarning("Image Error", f"Error loading first developer's profile photo: {e}")

    ttk.Label(tab_about, text="Backend Developer ", font=('Helvetica', 12, 'bold')).pack(pady=10)
    ttk.Label(tab_about, text="Developed By: Lav Raj").pack()
    ttk.Label(tab_about, text="Contact: lavraj015@gmail.com").pack()

    try:
        profile_image2 = Image.open("lav.png")
        profile_image2 = profile_image2.resize((200, 200), Image.LANCZOS)
        profile_photo2 = ImageTk.PhotoImage(profile_image2)
        profile_label2 = tk.Label(tab_about, image=profile_photo2)
        profile_label2.image = profile_photo2
        profile_label2.pack(pady=10)
    except Exception as e:
        messagebox.showwarning("Image Error", f"Error loading second developer's profile photo: {e}")

    tab_control.pack(expand=True, fill='both')
    root.mainloop()

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "lavraj" and password == "lav@123":
        login_window.destroy()
        open_main_window()
    else:
        messagebox.showerror("Error", "Invalid username or password")

login_window = tk.Tk()
login_window.title("Login Window")
login_window.state('zoomed')

try:
    login_bg_image = Image.open("background.jpg")
    login_bg_photo = ImageTk.PhotoImage(login_bg_image)
    canvas = tk.Canvas(login_window, width=login_bg_image.width, height=login_bg_image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=login_bg_photo, anchor="nw")
except Exception as e:
    messagebox.showwarning("Image Error", f"Error loading background image: {e}")
    canvas = tk.Canvas(login_window, bg="#fdf6ec")
    canvas.pack(fill="both", expand=True)

login_frame = tk.Frame(canvas, bg='white', padx=40, pady=30, bd=2, relief='ridge')
canvas_window = canvas.create_window(0, 0, window=login_frame, anchor="center")

def center_login_frame(event=None):
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    canvas.coords(canvas_window, canvas_width // 2, canvas_height // 2)

canvas.bind("<Configure>", center_login_frame)


title_label = tk.Label(login_frame, text="Hotel System Login", font=('Helvetica', 18, 'bold'), fg="#333", bg="white")
title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

tk.Label(login_frame, text="Username:", font=('Helvetica', 12), bg='white').grid(row=1, column=0, pady=10, padx=10, sticky='e')
entry_username = tk.Entry(login_frame, font=('Helvetica', 12), width=25)
entry_username.grid(row=1, column=1, pady=10, padx=10)

tk.Label(login_frame, text="Password:", font=('Helvetica', 12), bg='white').grid(row=2, column=0, pady=10, padx=10, sticky='e')
entry_password = tk.Entry(login_frame, font=('Helvetica', 12), show='*', width=25)
entry_password.grid(row=2, column=1, pady=10, padx=10)

login_button = tk.Button(login_frame, text="Login", command=login, font=('Helvetica', 12, 'bold'), bg='#FF7F50', fg='white', relief='flat', padx=10, pady=5)
login_button.grid(row=3, columnspan=2, pady=20)
login_button.bind("<Enter>", lambda e: login_button.config(bg="#FF4500"))
login_button.bind("<Leave>", lambda e: login_button.config(bg="#FF7F50"))

login_window.mainloop()
