"""Image Filters v0.1.0"""
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk

from image import PILImage

window = tk.Tk()
window.minsize(width=960, height=720)
window.title("Image Filters v0.1.0")

image = PILImage()

def update_image_label(image):
    """Updates the image label to a new image."""
    global image_tk
    image_tk = ImageTk.PhotoImage(image)
    image_label.config(image=image_tk)

def change_filter(event):
    """Changes the current filter to the selected one in the listbox."""
    global current_filter

    intensity_slider.set(1)
    apply_filter_button.config(state="active")

    match event.widget.curselection():
        case (0,):
            current_filter = 'grayscale'
            intensity_slider.config(state="disabled")
        case (1,):
            current_filter = 'invert'
            intensity_slider.config(state="disabled")
        case (2,):
            current_filter = 'black_and_white'
            intensity_slider.config(state="disabled")
        case (3,):
            current_filter = 'sepia'
            intensity_slider.config(state="disabled")
        case (4,):
            current_filter = 'cold'
            intensity_slider.config(state="disabled")
        case (5,):
            current_filter = 'warm'
            intensity_slider.config(state="disabled")
        case (6,):
            current_filter = 'colorful'
            intensity_slider.config(state="disabled")
        case (7,):
            current_filter = 'lighter'
            intensity_slider.config(state="active")
        case (8,):
            current_filter = 'darker'
            intensity_slider.config(state="active")

def intensity_slider_change(event):
    print('intensity slider ' + event)

def apply_filter_button_click():
    print('apply filter')

def revert_one_step_button_click():
    print('revert step')

def revert_to_original_button_click():
    print('revert original')

def open_image_button_click():
    """Opens an image and sets it as the current image."""
    file_path = filedialog.askopenfilename()

    if file_path != '':
        global image

        try:
            image = PILImage()
            image.open(file_path)
        except IOError:
            messagebox.showerror(
                "File error", f"The selected file ({file_path}) is not an image.")
        else:
            image.resized = image.resize(image.current)
            update_image_label(image.resized)

            save_image_button.config(state="active")
            save_image_as_button.config(state="active")
            filter_list.config(state="normal")

def save_image_button_click():
    """Saves the image to the path it was opened from."""
    try:
        image.save(image.path)
    except IOError:
        messagebox.showerror('Image save error',
                             f'The image could not be saved at path: {image.path}.')
    except ValueError:
        messagebox.showerror('Image save error',
                             'The image could not be saved since \
                                 it does not have a valid filename.')

def save_image_as_button_click():
    """Saves the image to a new path."""
    file_path = filedialog.asksaveasfilename()

    if file_path != '':
        try:
            image.save(file_path)
        except IOError:
            messagebox.showerror('Image save error',
                                 f'The image could not be saved at path: {file_path}.')
        except ValueError:
            messagebox.showerror('Image save error',
                                 'The image could not be saved since \
                                     it does not have a valid filename.')

# Top frame
top_frame = tk.Frame(window)
top_frame.pack(side="top", fill="both", expand=True)

image_label = tk.Label(top_frame)
image_label.place(relx=0.5, rely=0.5, anchor='center')

# Bottom frame
bottom_frame = tk.Frame(window)
bottom_frame.pack(side="bottom", fill="x")

# Bottom left frame
bottom_left_frame = tk.Frame(bottom_frame, height=150)
bottom_left_frame.pack(side="left", fill="both", expand=True)

filter_text = tk.Label(bottom_left_frame, text="Filters (9)")
filter_text.pack()

filter_list = tk.Listbox(bottom_left_frame)
filter_list.insert(tk.END, "Grayscale")
filter_list.insert(tk.END, "Invert")
filter_list.insert(tk.END, "Black and white")
filter_list.insert(tk.END, "Sepia")
filter_list.insert(tk.END, "Cold")
filter_list.insert(tk.END, "Warm")
filter_list.insert(tk.END, "Colorful")
filter_list.insert(tk.END, "Lighter (1-10)")
filter_list.insert(tk.END, "Darker (1-10)")
filter_list.bind("<<ListboxSelect>>", change_filter)
filter_list.pack()
filter_list.config(state="disabled")

# Bottom center frame
bottom_center_frame = tk.Frame(bottom_frame, height=150)
bottom_center_frame.pack(side="left", fill="both", expand=True)

intensity_text = tk.Label(bottom_center_frame, text="Intensity (1-10)")
intensity_text.pack()

intensity_slider = tk.Scale(bottom_center_frame, from_=1, to=10, orient="horizontal",
                            command=intensity_slider_change, state="disabled")
intensity_slider.place(relx=0.5, rely=0.5, anchor="center")

# Bottom right frame
bottom_right_frame = tk.Frame(bottom_frame, height=150)
bottom_right_frame.pack(side="right", fill="both", expand=True)

options_text = tk.Label(bottom_right_frame, text="Options")
options_text.pack()

bottom_right_top_frame = tk.Frame(bottom_right_frame)
bottom_right_top_frame.place(relx=0.15, rely=0.5, anchor="w")

apply_filter_button = tk.Button(bottom_right_top_frame, text="Apply filter",
                                command=apply_filter_button_click, state="disabled")
apply_filter_button.pack()

revert_one_step_button = tk.Button(bottom_right_top_frame, text="Revert one step",
                                   command=revert_one_step_button_click, state="disabled")
revert_one_step_button.pack()

revert_to_original_button = tk.Button(bottom_right_top_frame, text="Revert to original",
                                      command=revert_to_original_button_click, state="disabled")
revert_to_original_button.pack()

bottom_right_bottom_frame = tk.Frame(bottom_right_frame)
bottom_right_bottom_frame.place(relx=0.85, rely=0.5, anchor="e")

open_image_button = tk.Button(bottom_right_bottom_frame, text="Open image",
                              command=open_image_button_click, state="active")
open_image_button.pack()

save_image_button = tk.Button(bottom_right_bottom_frame, text="Save image",
                              command=save_image_button_click, state="disabled")
save_image_button.pack()

save_image_as_button = tk.Button(bottom_right_bottom_frame, text="Save image as...",
                                 command=save_image_as_button_click, state="disabled")
save_image_as_button.pack()

window.mainloop()
