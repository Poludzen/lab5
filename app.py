from dearpygui.core import *
from dearpygui.simple import *
from image_func import *
import cv2

# window object settings
set_main_window_size(height=640, width=1080)
set_global_font_scale(1.25)
set_theme("Gold")
set_style_window_padding(30, 30)

# if u want your images to share, put them on an app folder with names img1.png and img2.png
# reading images and fixing size
image1_path = "img1.jpg"
image2_path = "img2.jpg"
result_path = "img3.jpg"
image1 = cv2.imread(image1_path, cv2.COLOR_BGR2RGB)
image1 = cv2.resize(image1, (180, 320))
cv2.imwrite(image1_path, image1)
image1 = np.array(image1).astype('float64')
image1 /= 255
image2 = cv2.imread(image2_path, cv2.COLOR_BGR2RGB)
image2 = cv2.resize(image2, (180, 320))
cv2.imwrite(image2_path, image2)

image2 = np.array(image2).astype('float64')
image2 /= 255

result = cv2.imread(image1_path, cv2.COLOR_BGR2RGB)
cv2.resize(result, (180, 320))

# preparing text for a list box
image_merging_buttons = ['additive_mix', 'subtractive_mix', 'difference_mix', 'multiply_mix', 'screen_mix',
                         'negation_mix', 'darken_mix', ' lighter_mix', 'exclusion_mix', 'overlay_mix',
                         'hard_light_mode',
                         'soft_light_mode', 'color_dodge_fix', 'color_burn_fix', 'reflect_fix']
# same names of a funcs
merg_funcs = [additive_mix, subtractive_mix, difference_mix, multiply_mix, screen_mix,
              negation_mix, darken_mix, lighter_mix, exclusion_mix, overlay_mix,
              hard_light_mode,
              soft_light_mode, color_dodge_fix, color_burn_fix, reflect_fix]


# processing list box calls(calls mixing funcs)
def list_box_merge_funcs(sender):
    index = get_value(sender)
    # saving image cause we cannot print numpy images wit this gui lab
    cv2.imwrite(result_path, merg_funcs[index](image1, image2))
    # we need to rewrite our image every time
    clear_drawing("result")
    draw_image("result", result_path, [0, 0], pmax=[180, 320])


# opacity is so special cause it need some special params
def opacity_callback():
    # getting input
    alpha = float(get_value("Opacity Input"))
    # saving image cause we cannot print numpy images wit this gui lab
    cv2.imwrite(result_path, opacity(image1, image2, alpha))
    # we need to rewrite our image every time
    clear_drawing("result")
    draw_image("result", result_path, [0, 0], pmax=[180, 320])


# processing image 1 with linear transform
def linear_callback():
    # getting input
    values = get_value("linear transform img1").split()
    alpha = float(values[0])
    beta = float(values[1])
    # saving image cause we cannot print numpy images wit this gui lab
    cv2.imwrite(result_path, linear_transform(image1, alpha, beta))
    # we need to rewrite our image every time
    clear_drawing("result")
    draw_image("result", result_path, [0, 0], pmax=[180, 320])


# processing image 1 with power transform
def power_callback():
    # getting input
    values = get_value("power transform img1").split()
    c = float(values[0])
    n = float(values[1])
    # saving image cause we cannot print numpy images wit this gui lab
    cv2.imwrite(result_path, power_transform(image1, c=c, n=n))
    # we need to rewrite our image every time
    clear_drawing("result")
    draw_image("result", result_path, [0, 0], pmax=[180, 320])


# creating window for image 1
with window("image1 window", width=220, height=360):
    set_window_pos("image1 window", 380, 200)
    add_drawing("img1", width=180, height=320)  # create some space for the image
    draw_image("img1", image1_path, [0, 0], pmax=[180, 320])

# creating window for image 2
with window("image2 window", width=220, height=360):
    set_window_pos("image2 window", 610, 200)
    add_drawing("img2", width=180, height=320)  # create some space for the image
    draw_image("img2", image2_path, [0, 0], pmax=[180, 320])

# creating window for result image
with window("result window", width=220, height=360):
    set_window_pos("result window", 840, 200)
    add_drawing("result", width=180, height=320)

# window of all funcs
with window("Simple Image Processing", width=1080, height=200):
    set_window_pos("Simple Image Processing", 0, 0)
    # list of merging funcs(without opacity)
    add_listbox(callback=list_box_merge_funcs, name="Merge", items=image_merging_buttons, num_items=4)
    # add some free space between items
    add_spacing(count=12)
    # add input for opacity
    add_input_text("Opacity Input", width=100, default_value="input alpha")
    add_button("Do Opacity", callback=opacity_callback)
    add_spacing(count=12)
    # add input for linear
    add_input_text("linear transform img1", width=100, default_value="enter:a b")
    add_button("Do linear", callback=linear_callback)
    add_spacing(count=12)
    # add input for power
    add_input_text("power transform img1", width=100, default_value="enter:c n")
    add_button("Do power", callback=power_callback)
    add_spacing(count=12)
    set_primary_window("Simple Image Processing", True)

# starting an app
start_dearpygui()
