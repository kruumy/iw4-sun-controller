import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from pymem import Pymem
import win32api
import pywintypes
import sys
import webbrowser

# gui setup stuff
root = Tk()
root.title("IW4x Sun Controller")
root.geometry('311x115')
root.resizable(False, False)

tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Color')
tab_control.add(tab2, text='Position')
tab_control.add(tab3, text='Presets')
tab_control.add(tab4, text='Misc')
tab_control.add(tab5, text='About')
tab_control.pack(expand=1, fill='both')
try:
    root.iconbitmap("icon.ico")
except:
    print("count not find icon.ico")

# pymem start stuff
try:
    pm = Pymem("iw4m.exe")
except:
    try:
        pm = Pymem("iw4x.exe")
    except:
        print("Could Not Find iw4m.exe")
        messagebox.showerror('Error',
                             'Could Not Find iw4m.exe or iw4x.exe\nPlease make sure it is running and in game/demo.')
        sys.exit()

# setting addresses
sunRedAdd = 0x0085B878
sunGreenAdd = 0x0085B87C
sunBlueAdd = 0x0085B880
sunXAdd = 0x0085B884
sunYAdd = 0x0085B888
sunZAdd = 0x0085B88C
fovAdd = 0x63FC560

# setting defaults
dred = pm.read_float(sunRedAdd)
dgreen = pm.read_float(sunGreenAdd)
dblue = pm.read_float(sunBlueAdd)
dx = pm.read_float(sunXAdd)
dy = pm.read_float(sunYAdd)
dz = pm.read_float(sunZAdd)


def wrpFloat(address, value):
    pm.write_float(address, float(value))
    # a = pm.read_float(address)
    # print("Value: " + str(a))


# gui stuff cont
# About me tab
def callback(url):
    webbrowser.open_new(url)


lbl1 = Label(tab5, text="v2.00")
lbl1.grid(column=0, row=0)
lbl2 = Label(tab5, text="Made By Kruumy")
lbl2.grid(column=0, row=1)
link = Label(tab5, text="Github Page", fg="blue", cursor="hand2")
link.grid(column=0, row=2)
link.bind("<Button-1>", lambda e: callback("https://github.com/kruumy/iw4-sun-controller"))


def brightDisplay():
    pass
    # brightness = pm.read_float(sunRedAdd) + pm.read_float(sunGreenAdd) + pm.read_float(sunBlueAdd)
    # brightnessPercent = "{:.1%}".format(brightness / 3)
    # brightLabel = Label(tab1, text="Brightness: " + str(brightnessPercent))
    # brightLabel.grid(column=4, row=1)


# open current action

def openAction():
    action = pm.read_string(0x01ABF8A0)
    messagebox.showinfo('Current Action', action)


btn1 = Button(tab4, text='Current Action', command=openAction)
btn1.grid(column=0, row=1)

# Slider FOV

current_value_fov = DoubleVar()


def get_current_value_fov():
    current_value_fov.set(pm.read_float(fovAdd))
    return '{: .2f}'.format(current_value_fov.get())


def slider_changed_fov(event):
    wrpFloat(fovAdd, event)
    value_label_fov.configure(text=get_current_value_fov())


slider_label_fov = ttk.Label(
    tab4,
    text='FOV:'
)
slider_label_fov.grid(
    column=0,
    row=0,
    sticky='w'
)
slider_fov = ttk.Scale(
    tab4,
    from_=0,
    to=180,
    orient='horizontal',
    command=slider_changed_fov,
    variable=current_value_fov
)
slider_fov.grid(
    column=1,
    row=0,
    sticky='we'
)
value_label_fov = ttk.Label(
    tab4,
    text=get_current_value_fov()
)
value_label_fov.grid(
    column=2,
    row=0,
    sticky='n'
)

# Slider Color Red

current_value_red = DoubleVar()


def get_current_value_red():
    current_value_red.set(pm.read_float(sunRedAdd))
    return '{: .2f}'.format(current_value_red.get())


def slider_changed_red(event):
    wrpFloat(sunRedAdd, event)
    brightDisplay()
    value_label_red.configure(text=get_current_value_red())


slider_label_red = ttk.Label(
    tab1,
    text='Red:'
)
slider_label_red.grid(
    column=0,
    row=0,
    sticky='w'
)
slider_red = ttk.Scale(
    tab1,
    from_=0,
    to=2,
    orient='horizontal',
    command=slider_changed_red,
    variable=current_value_red
)
slider_red.grid(
    column=1,
    row=0,
    sticky='we'
)
value_label_red = ttk.Label(
    tab1,
    text=get_current_value_red()
)
value_label_red.grid(
    column=2,
    row=0,
    sticky='n'
)

# Slider Color Blue

current_value_blue = DoubleVar()


def get_current_value_blue():
    current_value_blue.set(pm.read_float(sunBlueAdd))
    return '{: .2f}'.format(current_value_blue.get())


def slider_changed_blue(event):
    wrpFloat(sunBlueAdd, event)
    brightDisplay()
    value_label_blue.configure(text=get_current_value_blue())


slider_label_blue = ttk.Label(
    tab1,
    text='Blue:'
)
slider_label_blue.grid(
    column=0,
    row=1,
    sticky='w'
)
slider_blue = ttk.Scale(
    tab1,
    from_=0,
    to=2,
    orient='horizontal',
    command=slider_changed_blue,
    variable=current_value_blue
)
slider_blue.grid(
    column=1,
    row=1,
    sticky='we'
)
value_label_blue = ttk.Label(
    tab1,
    text=get_current_value_blue()
)
value_label_blue.grid(
    column=2,
    row=1,
    sticky='n'
)

# Slider Color Green

current_value_green = DoubleVar()


def get_current_value_green():
    current_value_green.set(pm.read_float(sunGreenAdd))
    return '{: .2f}'.format(current_value_green.get())


def slider_changed_green(event):
    wrpFloat(sunGreenAdd, event)
    brightDisplay()
    value_label_green.configure(text=get_current_value_green())


slider_label_green = ttk.Label(
    tab1,
    text='Green:'
)
slider_label_green.grid(
    column=0,
    row=2,
    sticky='w'
)
slider_green = ttk.Scale(
    tab1,
    from_=0,
    to=2,
    orient='horizontal',
    command=slider_changed_green,
    variable=current_value_green
)
slider_green.grid(
    column=1,
    row=2,
    sticky='we'
)
value_label_green = ttk.Label(
    tab1,
    text=get_current_value_green()
)
value_label_green.grid(
    column=2,
    row=2,
    sticky='n'
)

# Slider Color X

current_value_x = DoubleVar()


def get_current_value_x():
    current_value_x.set(pm.read_float(sunXAdd))
    return '{: .2f}'.format(current_value_x.get())


def slider_changed_x(event):
    wrpFloat(sunXAdd, event)
    value_label_x.configure(text=get_current_value_x())


slider_label_x = ttk.Label(
    tab2,
    text='x:'
)
slider_label_x.grid(
    column=0,
    row=0,
    sticky='w'
)
slider_x = ttk.Scale(
    tab2,
    from_=-10,
    to=20,
    orient='horizontal',
    command=slider_changed_x,
    variable=current_value_x
)
slider_x.grid(
    column=1,
    row=0,
    sticky='we'
)
value_label_x = ttk.Label(
    tab2,
    text=get_current_value_x()
)
value_label_x.grid(
    column=2,
    row=0,
    sticky='n'
)

# Slider Color X

current_value_x = DoubleVar()


def get_current_value_x():
    current_value_x.set(pm.read_float(sunXAdd))
    return '{: .2f}'.format(current_value_x.get())


def slider_changed_x(event):
    wrpFloat(sunXAdd, event)
    value_label_x.configure(text=get_current_value_x())


slider_label_x = ttk.Label(
    tab2,
    text='Sun X:'
)
slider_label_x.grid(
    column=0,
    row=0,
    sticky='w'
)
slider_x = ttk.Scale(
    tab2,
    from_=-5,
    to=5,
    orient='horizontal',
    command=slider_changed_x,
    variable=current_value_x
)
slider_x.grid(
    column=1,
    row=0,
    sticky='we'
)
value_label_x = ttk.Label(
    tab2,
    text=get_current_value_x()
)
value_label_x.grid(
    column=2,
    row=0,
    sticky='n'
)

# Slider Color Y

current_value_y = DoubleVar()


def get_current_value_y():
    current_value_y.set(pm.read_float(sunYAdd))
    return '{: .2f}'.format(current_value_y.get())


def slider_changed_y(event):
    wrpFloat(sunYAdd, event)
    value_label_y.configure(text=get_current_value_y())


slider_label_y = ttk.Label(
    tab2,
    text='Sun Y:'
)
slider_label_y.grid(
    column=0,
    row=1,
    sticky='w'
)
slider_y = ttk.Scale(
    tab2,
    from_=-5,
    to=5,
    orient='horizontal',
    command=slider_changed_y,
    variable=current_value_y
)
slider_y.grid(
    column=1,
    row=1,
    sticky='we'
)
value_label_y = ttk.Label(
    tab2,
    text=get_current_value_x()
)
value_label_y.grid(
    column=2,
    row=1,
    sticky='n'
)

# Slider Color Z

current_value_z = DoubleVar()


def get_current_value_z():
    current_value_z.set(pm.read_float(sunZAdd))
    return '{: .2f}'.format(current_value_z.get())


def slider_changed_z(event):
    wrpFloat(sunZAdd, event)
    value_label_z.configure(text=get_current_value_z())


slider_label_z = ttk.Label(
    tab2,
    text='Sun Z:'
)
slider_label_z.grid(
    column=0,
    row=2,
    sticky='w'
)
slider_z = ttk.Scale(
    tab2,
    from_=-5,
    to=5,
    orient='horizontal',
    command=slider_changed_z,
    variable=current_value_z
)
slider_z.grid(
    column=1,
    row=2,
    sticky='we'
)
value_label_z = ttk.Label(
    tab2,
    text=get_current_value_z()
)
value_label_z.grid(
    column=2,
    row=2,
    sticky='n'
)


# preset stuff
def setPreset(red, green, blue, x, y, z):
    slider_changed_red(float(red))
    slider_changed_green(float(green))
    slider_changed_blue(float(blue))
    slider_changed_x(float(x))
    slider_changed_y(float(y))
    slider_changed_z(float(z))
    messagebox.showinfo('Notification', 'Preset Applied')


def setDefaults():
    slider_changed_red(float(dred))
    slider_changed_green(float(dgreen))
    slider_changed_blue(float(dblue))
    slider_changed_x(float(dx))
    slider_changed_y(float(dy))
    slider_changed_z(float(dz))
    messagebox.showinfo('Notification', 'Default Preset Applied')


defaultbtn = Button(tab3, text="Defaults", command=setDefaults)
defaultbtn.grid(column=2, row=0)


def openPreset():
    open1 = filedialog.askopenfilename(filetypes=[("Sun file", ".sun")], defaultextension=".sun", title="Open Config")
    try:
        fob = open(open1, "r")
        fobi = fob.readlines()
        setPreset(fobi[0], fobi[1], fobi[2], fobi[3], fobi[4], fobi[5])
        fob.close()
    except:
        print("no text file (OPEN)")


def savePreset():
    save1 = filedialog.asksaveasfilename(
        filetypes=[("Sun file", ".sun")],
        defaultextension=".sun", title="Save Config")
    try:
        valueList = str(get_current_value_red()) + "\n" + str(get_current_value_green()) + "\n" + str(
            get_current_value_blue()) + "\n" + str(get_current_value_x()) + "\n" + str(
            get_current_value_y()) + "\n" + str(get_current_value_z())
        fobo = open(save1, 'w')
        fobo.write(str(valueList))
        fobo.close()
    except:
        print("no text file (CLOSE)")


openpresetbtn = Button(tab3, text='Open', command=openPreset)
openpresetbtn.grid(column=0, row=0)

savepresetbtn = Button(tab3, text='Save As', command=savePreset)
savepresetbtn.grid(column=1, row=0)

root.mainloop()