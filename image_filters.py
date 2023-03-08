"""Image Filters v0.3.0"""
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from multiprocessing import Pool, cpu_count
from threading import Thread
from PIL import ImageTk

from image import PILImage
from filters import (grayscale_filter, invert_filter, black_and_white_filter, sepia_filter,
    cold_filter, warm_filter, colorful_filter, lighter_filter, darker_filter)

def update_image_label(new_image):
    """Updates the image label to a new image."""
    global image_tk
    image_tk = ImageTk.PhotoImage(new_image)
    image_label.config(image=image_tk)

def change_filter():
    """Changes the current filter to the selected one in the listbox."""
    global current_filter

    intensity_slider.set(1)
    apply_filter_button.config(state='active')

    match filter_list.selection():
        case ('I001',):
            current_filter = grayscale_filter
            intensity_slider.config(state='disabled')
        case ('I002',):
            current_filter = invert_filter
            intensity_slider.config(state='disabled')
        case ('I003',):
            current_filter = black_and_white_filter
            intensity_slider.config(state='disabled')
        case ('I004',):
            current_filter = sepia_filter
            intensity_slider.config(state='disabled')
        case ('I005',):
            current_filter = cold_filter
            intensity_slider.config(state='disabled')
        case ('I006',):
            current_filter = warm_filter
            intensity_slider.config(state='disabled')
        case ('I007',):
            current_filter = colorful_filter
            intensity_slider.config(state='disabled')
        case ('I008',):
            current_filter = lighter_filter
            intensity_slider.config(state='active')
        case ('I009',):
            current_filter = darker_filter
            intensity_slider.config(state='active')

def change_intensity(event):
    """Limits the intensity slider to integer values."""
    value = int(float(event))
    intensity_slider.config(value=value)
    intensity_text.config(text=f'Intensity ({value})')

def apply_filter_button_click():
    """Configures buttons and applies filter in a new thread."""
    filter_list.config(selectmode='none')
    apply_filter_button.config(state='disabled')
    apply_filter_button.config(text='Applying filter...')
    revert_one_step_button.config(state='disabled')
    revert_to_original_button.config(state='disabled')
    open_image_button.config(state='disabled')
    save_image_button.config(state='disabled')
    save_image_as_button.config(state='disabled')
    status_bar.start(10)

    # Runs filter application in a new thread to allow changes to the GUI
    thread = Thread(target=apply_filter)
    thread.start()

def apply_filter():
    """Applies the selected filter to the current image."""
    image_sections = []
    for section in image.current_sections:
        image_sections.append((section, intensity_slider.get()))

    with Pool(image.section_count) as pool:
        image.current_sections = pool.starmap(current_filter, image_sections)

    image.merge()
    image.resize()
    update_image_label(image.resized)

    filter_list.config(selectmode='browse')
    apply_filter_button.config(text='Apply filter')
    apply_filter_button.config(state='active')
    revert_one_step_button.config(state='active')
    revert_to_original_button.config(state='active')
    open_image_button.config(state='active')
    save_image_button.config(state='active')
    save_image_as_button.config(state='active')
    status_bar.stop()

def revert_one_step_button_click():
    """Reverts the current image to the last image."""
    if len(image.list) >= 1:
        image.list.pop()
        image.crop()
        image.resize()
        update_image_label(image.resized)

        if len(image.list) == 1:
            revert_one_step_button.config(state='disabled')
            revert_to_original_button.config(state='disabled')

def revert_to_original_button_click():
    """Reverts the current image to the original image."""
    image.list = [image.list[0]]

    image.crop()
    image.resize()
    update_image_label(image.resized)

    revert_one_step_button.config(state='disabled')
    revert_to_original_button.config(state='disabled')

def open_image_button_click():
    """Opens an image and sets it as the current image."""
    file_path = filedialog.askopenfilename(filetypes = (
        ('PNG (transparency support)', '*.png'),
            ('JPG (no transparency support)', '*.jpg')))

    if file_path != '':
        global image

        try:
            image = PILImage()
            image.open(file_path)
        except IOError:
            messagebox.showerror(
                'File error', f'The selected file ({file_path}) is not an image.')
        else:
            # CPU count is used to determine the number of sections to split the image into
            if image.list[-1].width >= cpu_count():
                image.section_count = cpu_count()
            else:
                image.section_count = image.list[-1].width

            image.crop()
            image.resize()
            update_image_label(image.resized)

            window.title(f'Image Filters v0.3.0 • {file_path}')
            image_label.place(relx=0.5, rely=0.5, anchor='center')
            save_image_button.config(state='active')
            save_image_as_button.config(state='active')
            filter_list.config(selectmode='browse')

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
    file_path = filedialog.asksaveasfilename(
        filetypes = (('PNG (transparency support)', '*.png'),
            ('JPG (no transparency support)', '*.jpg'),
                ('All', '*')), defaultextension='.png')

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

if __name__ == '__main__':
    image = PILImage()
    image_tk = None
    current_filter = None

    # Window
    window = tk.Tk()
    window.minsize(width=960, height=720)
    window.title('Image Filters v0.3.0')
    window.wm_iconphoto(False, tk.PhotoImage(file='icon.png'))

    # Top frame
    top_frame = tk.Frame(window, bg='white')
    top_frame.pack(side='top', fill='both', expand=True)

    top_frame_separator = ttk.Separator(top_frame, orient='horizontal')
    top_frame_separator.pack(side='bottom', fill='x')

    image_label = ttk.Label(top_frame, relief='solid')

    # Bottom frame
    bottom_frame = tk.Frame(window, bg='white')
    bottom_frame.pack(side='bottom', fill='x')

    # Bottom left frame
    bottom_left_frame = tk.Frame(bottom_frame, bg='white')
    bottom_left_frame.pack(side='left', fill='both', expand=True)

    filter_list = ttk.Treeview(bottom_left_frame, selectmode='none', height=8)
    filter_list.heading('#0', text='Filters (9)')
    filter_list.insert('', 'end', text='Grayscale')
    filter_list.insert('', 'end', text='Invert')
    filter_list.insert('', 'end', text='Black and white')
    filter_list.insert('', 'end', text='Sepia')
    filter_list.insert('', 'end', text='Cold')
    filter_list.insert('', 'end', text='Warm')
    filter_list.insert('', 'end', text='Colorful')
    filter_list.insert('', 'end', text='Lighter (1-10)')
    filter_list.insert('', 'end', text='Darker (1-10)')
    filter_list.bind('<<TreeviewSelect>>', lambda event: change_filter())

    filter_list.pack()

    # Bottom center frame
    bottom_center_frame = tk.Frame(bottom_frame, height=150, bg='white')
    bottom_center_frame.pack(side='left', fill='both', expand=True)

    bottom_center_frame_separator_1 = ttk.Separator(bottom_center_frame, orient='vertical')
    bottom_center_frame_separator_1.pack(side='left', fill='y')

    intensity_text = tk.Label(bottom_center_frame, text='Intensity (1)', bg='white')
    intensity_text.pack()

    style = ttk.Style()
    style.configure('TScale', background='white')

    intensity_slider = ttk.Scale(bottom_center_frame, from_=1, to=10, orient='horizontal',
        state='disabled', value=1, style='TScale', command=change_intensity)
    intensity_slider.place(relx=0.5, rely=0.5, anchor='center')

    bottom_center_frame_separator_2 = ttk.Separator(bottom_center_frame, orient='vertical')
    bottom_center_frame_separator_2.pack(side='right', fill='y')

    # Bottom right frame
    bottom_right_frame = tk.Frame(bottom_frame)
    bottom_right_frame.pack(side='right', fill='both', expand=True)

    bottom_right_top_frame = tk.Frame(bottom_right_frame, bg='white')
    bottom_right_top_frame.pack(side='top', fill='both', expand=True)

    bottom_right_bottom_frame = tk.Frame(bottom_right_frame, bg='white')
    bottom_right_bottom_frame.pack(side='bottom', fill='both')

    options_text = tk.Label(bottom_right_top_frame, text='Options', bg='white')
    options_text.pack()

    bottom_right_top_left_frame = tk.Frame(bottom_right_top_frame, bg='white')
    bottom_right_top_left_frame.place(relx=0.15, rely=0.5, anchor='w')

    style.configure('Custom.TButton', background='white')

    apply_filter_button = ttk.Button(bottom_right_top_left_frame, text='Apply filter',
        command=apply_filter_button_click, style='Custom.TButton', state='disabled')
    apply_filter_button.pack()

    revert_one_step_button = ttk.Button(bottom_right_top_left_frame, text='Revert one step',
        command=revert_one_step_button_click, style='Custom.TButton', state='disabled')
    revert_one_step_button.pack()

    revert_to_original_button = ttk.Button(bottom_right_top_left_frame, text='Revert to original',
        command=revert_to_original_button_click, style='Custom.TButton', state='disabled')
    revert_to_original_button.pack()

    bottom_rigth_top_right_frame = tk.Frame(bottom_right_top_frame, bg='white')
    bottom_rigth_top_right_frame.place(relx=0.85, rely=0.5, anchor='e')

    open_image_button = ttk.Button(bottom_rigth_top_right_frame, text='Open image',
        command=open_image_button_click, style='Custom.TButton', state='active')
    open_image_button.pack()

    save_image_button = ttk.Button(bottom_rigth_top_right_frame, text='Save image',
        command=save_image_button_click, style='Custom.TButton', state='disabled')
    save_image_button.pack()

    save_image_as_button = ttk.Button(bottom_rigth_top_right_frame, text='Save image as...',
        command=save_image_as_button_click, style='Custom.TButton', state='disabled')
    save_image_as_button.pack()

    status_text = tk.Label(bottom_right_bottom_frame, text='Status', bg='white')
    status_text.pack()

    status_bar = ttk.Progressbar(bottom_right_bottom_frame, orient='horizontal',
        mode='indeterminate', length=300)
    status_bar.pack(pady=10)

    window.mainloop()
