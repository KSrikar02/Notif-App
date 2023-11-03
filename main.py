# Import necessary libraries
from tkinter import *
from plyer import notification
from tkinter import messagebox
import time
# Create a Tkinter window
notification_window = Tk()
notification_window.title('Notification')
notification_window.geometry("500x300")

# Function to get notification details and set the notification
def set_notification():
    # Get user input for title, message, and time
    title = title_entry.get()
    message = message_entry.get()
    time_minutes = time_entry.get()

    # Check if any of the fields are empty
    if title == "" or message == "" or time_minutes == "":
        messagebox.showerror("Alert", "All fields are required!")
    else:
        # Convert time from minutes to seconds
        time_seconds = int(float(time_minutes) * 60)

        # Show a confirmation message and close the window
        messagebox.showinfo("Notification set", "Notification set!")
        notification_window.destroy()

        # Delay for the specified time and then show the notification
        time.sleep(time_seconds)
        notification.notify(
            title=title,
            message=message,
            app_name="Notification",
            app_icon="icon.ico",
            toast=True,
            timeout=10
        )

# Label for Title
title_label = Label(notification_window, text="Title to Notify", font=("poppins", 10))
title_label.place(x=12, y=70)

# Entry for Title
title_entry = Entry(notification_window, width="25", font=("poppins", 13))
title_entry.place(x=123, y=70)

# Label for Message
message_label = Label(notification_window, text="Display Message", font=("poppins", 10))
message_label.place(x=12, y=120)

# Entry for Message
message_entry = Entry(notification_window, width="40", font=("poppins", 13))
message_entry.place(x=123, height=30, y=120)

# Label for Time
time_label = Label(notification_window, text="Set Time (minutes)", font=("poppins", 10))
time_label.place(x=12, y=175)

# Entry for Time
time_entry = Entry(notification_window, width="5", font=("poppins", 13))
time_entry.place(x=123, y=175)

# Label for "min"
time_min_label = Label(notification_window, text="min", font=("poppins", 10))
time_min_label.place(x=175, y=180)

# Button to set the notification
set_notification_button = Button(notification_window, text="SET NOTIFICATION", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20, relief="raised", command=set_notification)
set_notification_button.place(x=170, y=230)

# Disable window resizing
notification_window.resizable(0, 0)

# Start the Tkinter main loop
notification_window.mainloop()


