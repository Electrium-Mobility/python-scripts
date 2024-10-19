import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
from tkinter import filedialog, messagebox
from src.on_drop import onDrop

file_path = ''
# Function to handle file selection
def open_file():
    global file_path
    file_path= filedialog.askopenfilename(
        title="Select a CSV file",
        filetypes=[("CSV files", "*.csv")]
    )
    if file_path:
        label.config(text="Select a folder")
        button.config(text="Select a folder", command = save_file)
        
def save_file():
    folder_path = filedialog.askdirectory(
        title="Select a folder to save the result",
    )
    onDrop(file_path,folder_path)
    
# Create the main window (now inheriting from TkinterDnD)
root = TkinterDnD.Tk()
root.title("CSV File Processor")
root.geometry("400x200")

# Create a label with instructions
textVariable = "Drag and drop a CSV file or click 'Open File'"
label = tk.Label(root, text=  'Select a CSV file', pady=20)
label.pack()

# Create a button to open file dialog
button = tk.Button(root, text= 'Open a file', command=open_file)
button.pack(pady=10)


# # Enable dragging and dropping files onto the window
# def on_drop(event):
#     file_path = event.data.strip()  # File path
#     if file_path.endswith(".csv"):
#         onDrop(file_path)
#     else:
#         messagebox.showerror("Invalid File", "Please select a valid CSV file.")


# # Bind drag and drop event using tkinterdnd2's DND_FILES
# root.drop_target_register(DND_FILES)
# root.dnd_bind('<<Drop>>', on_drop)

# Start the GUI loop
root.mainloop()