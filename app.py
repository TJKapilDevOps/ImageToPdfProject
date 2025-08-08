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
        self.image_paths = []  # This will hold the paths of selected images
        # This will hold the name of the output PDF file
        self.output_pdf_name = tk.StringVar()  # Initialize the output PDF name variable
        self.selected_images_listbox = tk.Listbox(
            root, selectmode=tk.MULTIPLE)  # Create a listbox to display selected images
        self.initialize_ui()  # Call the method to set up the user interface

    # Method to initialize the user interface
    def initialize_ui(self):
        title_label = tk.Label(
            self.root, text="Image to PDF Converter", font=("Helvetica", 24, "bold"))  # Create a label for the title
        title_label.pack(pady=10)

        select_images_button = tk.Button(
            self.root, text="Select Images", command=self.select_images)  # Create a button to select images
        select_images_button.pack(pady=10)

        self.selected_images_listbox.pack(
            pady=(0, 10), fill=tk.BOTH, expand=True)  # Pack the listbox to fill the available space

        # Label for output PDF name
        # Create a label for the output PDF name
        label = tk.Label(self.root, text="Enter output PDF name: ")
        label.pack()  # Pack the label with some padding

        # Create an entry field for the PDF name
        pdf_name_entry = tk.Entry(
            self.root, textvariable=self.output_pdf_name, width=40, justify='center')  # Entry field for PDF name
        pdf_name_entry.pack()  # Pack the entry field with some padding

        convert_button = tk.Button(
            self.root, text="Convert to PDF", command=self.convert_images_to_pdf)  # Create a button to select images
        convert_button.pack(pady=(20, 40))  # Pack the button with some padding

    # Method to select images
    def select_images(self):
        self.image_paths = filedialog.askopenfilenames(
            title="Select Images", filetype=[("Image files", "*.png;*.jpg;*.jpeg")])
        self.update_selected_images_listbox()

        # Open a file dialog to select multiple image files

    def convert_images_to_pdf(self):
        print("This will do something later.")

    def update_selected_images_listbox(self):
        self.selected_images_listbox.delete(0, tk.END)  # Clear the listbox)

        for image_path in self.image_paths:  # Iterate through the selected image paths
            # Get the file name from the path
            _, image_path = os.path.split(image_path)
            # Insert the file name into the listbox
            self.selected_images_listbox.insert(tk.END, image_path)


def main():
    root = tk.Tk()  # Create the main window
    root.title("Image to PDF Converter")
    # Create an instance of the ImageToPDFConverter class
    # Initialize the converter with the root window
    converter = ImageToPDFConverter(root)
    root.geometry("400x600")  # Set the size of the window
    root.mainloop()  # Start the main event loop


if __name__ == "__main__":
    main()  # Call the main function to run the application
