import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
from tkinter import filedialog, messagebox, font as font
from src.gui_functions.on_drop import onDrop

file_path = ''

# Function to handle file selection
def restart_app():
    label.config(text= "Drag and drop a CSV file or click 'Open File'")
    button.config(text="Open a file", command = open_file)
    newbutton.pack_forget()
def open_file():
    global file_path # referring to the top-level variable
    file_path= filedialog.askopenfilename(
        title="Select a CSV file to run the algorithm",
        filetypes=[("CSV files", "*.csv")]
    )
    if file_path:
        label.config(text="Select a folder you want to store the resulting csv file")
        button.config(text="Select a folder", command = save_file)
        newbutton.pack(pady=10)


        
def save_file():
    folder_path = filedialog.askdirectory(
        title="Select a folder to save the result",
    )
    onDrop(file_path,folder_path)
    
# Create the main window (now inheriting from TkinterDnD)
root = TkinterDnD.Tk()
root.title("CSV File Processor")
root.geometry("600x400")

# Styles for the window
my_font = font.Font(family = "Helvetica", size = 22, weight = 'normal')

# Create a label with instructions
label = tk.Label(root, text = "Drag and drop a CSV file or click 'Open File'", pady=20, font = my_font)
label.pack()

# Create a button to open file dialog
button = tk.Button(root, text= 'Open a file', command=open_file, font = my_font)
newbutton = tk.Button(root, text= 'Restart', command=restart_app, font = my_font)
button.pack(pady=10)


# Enable dragging and dropping files onto the window
def on_drop(event):
    global file_path
    file_path = event.data.strip()  # File path
    if file_path.endswith(".csv"):
        label.config(text="Select a folder you want to store the resulting csv file")
        button.config(text="Select a folder", command = save_file)
        newbutton.pack(pady=10)
    else:
        messagebox.showerror("Invalid File", "Please select a valid CSV file.")


# Bind drag and drop event using tkinterdnd2's DND_FILES
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', on_drop)

# Start the GUI loop
root.mainloop()