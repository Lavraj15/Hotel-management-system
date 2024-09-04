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
        except mysql.connector.Error as e:
            conn.rollback()
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

# Main window setup
def setup_main_window():
    global root
    root = tk.Tk()
    root.title("Hotel Management System")
    root.state('zoomed')  # Open in full-screen mode

    # Style for tabs
    style = ttk.Style()
    style.theme_create("colored", parent="alt", settings={
        "TNotebook.Tab": {
            "configure": {"padding": [5, 1], "background": "#FFA500"},
            "map": {"background": [("selected", "#FF4500")]}
        }
    })
    style.theme_use("colored")

    # Tabbed interface
    tab_control = ttk.Notebook(root)

    # Reservations tab
    tab_reservations = ttk.Frame(tab_control)
    tab_control.add(tab_reservations, text='Reservations')

    # Load and display a background image in reservations tab
    try:
        bg_image = Image.open("background.png")  # Ensure 'hotel_background.jpg' is in the same directory
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(tab_reservations, image=bg_photo)
        bg_label.place(relwidth=1, relheight=1)
    except Exception as e:
        messagebox.showwarning("Image Error", f"Error loading background image: {e}")

    # Frame for reservation information
    global frame_reservation, entry_guest_name, combo_room_type, entry_stay_duration, add_button
    frame_reservation = ttk.Frame(tab_reservations, padding="10")
    frame_reservation.place(relx=0.5, rely=0.5, anchor='center')

    ttk.Label(frame_reservation, text="Guest Name:").grid(row=0, column=0, padx=10, pady=5)
    entry_guest_name = ttk.Entry(frame_reservation)
    entry_guest_name.grid(row=0, column=1, padx=10, pady=5)

    ttk.Label(frame_reservation, text="Room Type:").grid(row=1, column=0, padx=10, pady=5)
    combo_room_type = ttk.Combobox(frame_reservation, values=["Single", "Double", "Suite"])
    combo_room_type.grid(row=1, column=1, padx=10, pady=5)

    ttk.Label(frame_reservation, text="Stay Duration (nights):").grid(row=2, column=0, padx=10, pady=5)
    entry_stay_duration = ttk.Entry(frame_reservation)
    entry_stay_duration.grid(row=2, column=1, padx=10, pady=5)

    add_button = tk.Button(frame_reservation, text="Add Reservation", command=add_reservation, background='#FFA07A')
    add_button.grid(row=3, columnspan=2, pady=20)
    add_button.bind("<Enter>", on_enter)
    add_button.bind("<Leave>", on_leave)

    # About tab
    tab_about = ttk.Frame(tab_control)
    tab_control.add(tab_about, text='About')

    ttk.Label(tab_about, text="About Developers ", font=('Helvetica', 18, 'bold')).pack(pady=20)
    ttk.Label(tab_about, text="Frontend Developer ", font=('Helvetica', 12, 'bold')).pack(pady=10)
    ttk.Label(tab_about, text="Developed By: Harshit Hiranwal").pack()
    ttk.Label(tab_about, text="Contact: harshithiranwal@gmail.com").pack()

    # Load and display the first developer's profile photo
    try:
        profile_image1 = Image.open("profile.jpg")  # Ensure 'developer_photo1.jpg' is in the same directory
        profile_image1 = profile_image1.resize((200, 200), Image.LANCZOS)
        profile_photo1 = ImageTk.PhotoImage(profile_image1)
        profile_label1 = tk.Label(tab_about, image=profile_photo1)
        profile_label1.pack(pady=10)
    except Exception as e:
        messagebox.showwarning("Image Error", f"Error loading first developer's profile photo: {e}")

    ttk.Label(tab_about, text="Backend Developer ", font=('Helvetica', 12, 'bold')).pack(pady=10)
    ttk.Label(tab_about, text="Developed By: Lav raj").pack()
    ttk.Label(tab_about, text="Contact: lavraj123@gmail.com").pack()

    # Load and display the second developer's profile photo
    try:
        profile_image2 = Image.open("lav.png")  # Ensure 'developer_photo2.jpg' is in the same directory
        profile_image2 = profile_image2.resize((200, 200), Image.LANCZOS)
        profile_photo2 = ImageTk.PhotoImage(profile_image2)
        profile_label2 = tk.Label(tab_about, image=profile_photo2)
        profile_label2.pack(pady=10)
    except Exception as e:
        messagebox.showwarning("Image Error", f"Error loading second developer's profile photo: {e}")

    # Pack the tab control
    tab_control.pack(expand=True, fill='both')

    # Run the main window
    root.mainloop()

# Login function
def login():
    username = entry_username.get()
    password = entry_password.get()

    # Here you can add authentication logic (for demonstration purpose)
    if username == "admin" and password == "admin":  # Replace with actual authentication logic
        login_window.destroy()  # Close login window
        setup_main_window()  # Open main application window
    else:
        messagebox.showerror("Error", "Invalid username or password")

# Login window setup
login_window = tk.Tk()
login_window.title("Login Window")
login_window.state('zoomed')  # Open in full-screen mode

# Load background image for login window
try:
    login_bg_image = Image.open("background.jpg")
    login_bg_photo = ImageTk.PhotoImage(login_bg_image)
    login_bg_label = tk.Label(login_window, image=login_bg_photo)
    login_bg_label.place(relwidth=1, relheight=1)
except Exception as e:
    messagebox.showwarning("Image Error", f"Error loading background image: {e}")

# Frame for login form
login_frame = tk.Frame(login_window, bg='white', padx=20, pady=20)
login_frame.place(relx=0.5, rely=0.5, anchor='center')

# Username label and entry
tk.Label(login_frame, text="Username:", font=('Helvetica', 12), bg='white').grid(row=0, column=0, pady=10, padx=10)
entry_username = tk.Entry(login_frame, font=('Helvetica', 12))
entry_username.grid(row=0, column=1, pady=10, padx=10)

# Password label and entry
tk.Label(login_frame, text="Password:", font=('Helvetica', 12), bg='white').grid(row=1, column=0, pady=10, padx=10)
entry_password = tk.Entry(login_frame, font=('Helvetica', 12), show='*')
entry_password.grid(row=1, column=1, pady=10, padx=10)

# Login button
login_button = tk.Button(login_frame, text="Login", command=login, font=('Helvetica', 12), bg='lightgrey')
login_button.grid(row=2, columnspan=2, pady=20)

# Run the login window
login_window.mainloop()
