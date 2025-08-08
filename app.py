# First I installed the tkinter (tk) and pillow (pillow) libraries
# tkinter is used for creating the GUI
# pillow is used for image processing
import tkinter as tk  # `tkinter` is the standard GUI toolkit for Python
from tkinter import filedialog  # for opening file dialog
import os  # for file path operations

# A class is a blueprint for creating objects
# In this case, we are creating a class to convert images to PDF


class ImageToPDFConverter:
    # Initialize the class with a root window, this is the main window of the application on which all widgets will be placed
    def __init__(self, root):
        self.root = root  # Assign the root window to an instance variable
        self.image_path = []  # This will hold the paths of selected images
        # This will hold the name of the output PDF file
        self.output_pdf_name = tk.StringVar()  # Initialize the output PDF name variable
        self.selected_images_listbox = tk.Listbox(
            root, slectmode=tk.MULTIPLE)  # Create a listbox to display selected images
        self.intialize_ui()  # Call the method to set up the user interface

    # Method to initialize the user interface
    def intialize_ui(self):
        title_label = tk.Label(
            self.root, text="Image to PDF Converter", font=("Helvetica", 24, "bold"))  # Create a label for the title
        title_label.pack(pady=10)


def main():
    root = tk.Tk()  # Create the main window
    root.title("Iamge to PDF Converter")
    root.geometry("400x600")  # Set the size of the window
    root.mainloop()  # Start the main event loop


if __name__ == "__main__":
    main()  # Call the main function to run the application
