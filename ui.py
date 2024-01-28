import tkinter as tk
import lights
from tkinter import font as tkFont

#Function for toggle switches, var = tracked status of the light, light = light status from lights.py
def toggle_switch(var, light, label_widget, bslider_widget, wslider_widget):
    if var.get():
        #Change the button text to On
        label_widget.config(text="ON")
        #Turn the light on
        light.turn_on(switch=20)
        #Enable the sliders
        bslider_widget.config(state="normal")
        wslider_widget.config(state="normal")
    else:
        #Change the button text to Off
        label_widget.config(text="OFF")
        #Turn the light off
        light.turn_off(switch=20)
        #Disable the sliders
        bslider_widget.config(state="disabled")
        wslider_widget.config(state="disabled")
        

#Function for brightness sliders
def brightness_slider(value, light):
    #Change brightness
    light.set_brightness(int(value))

#Function for wartmh sliders
def warmth_slider(value, light):
    light.set_colourtemp(int(value))


def main():
    #Check that all devices are connected, and add them to active lights list
    active_lights = []

    for light in lights.light_list:
        response = light.receive()
        if response is None:
            active_lights.append(light)
            continue
        if "Error" in response:
            print("Have you turned on the physical light switch?")
            

    #First set version for all lights
    lights.init_status(active_lights)

    #Main window
    menu = tk.Tk()
    menu.title("Smart Light Control")

    #Bold font variable
    bold_font = tkFont.Font(family="TkDefaultFont", weight=tkFont.BOLD)


    #Give all active lights a custom attribute to track on/off status, and initialize in the UI to show the current status when app starts
    if lights.lroom1_light in active_lights: lights.lroom1_light.switch_var = tk.BooleanVar(value=lights.lroom1_light.status()["dps"]["20"])
    if lights.lroom2_light in active_lights: lights.lroom2_light.switch_var = tk.BooleanVar(value=lights.lroom2_light.status()["dps"]["20"])
    if lights.lroom3_light in active_lights: lights.lroom3_light.switch_var = tk.BooleanVar(value=lights.lroom3_light.status()["dps"]["20"])
    if lights.lroom4_light in active_lights: lights.lroom4_light.switch_var = tk.BooleanVar(value=lights.lroom4_light.status()["dps"]["20"])
    if lights.office1_light in active_lights: lights.office1_light.switch_var = tk.BooleanVar(value=lights.office1_light.status()["dps"]["20"])
    if lights.office2_light in active_lights: lights.office2_light.switch_var = tk.BooleanVar(value=lights.office2_light.status()["dps"]["20"])
    if lights.office3_light in active_lights: lights.office3_light.switch_var = tk.BooleanVar(value=lights.office3_light.status()["dps"]["20"])

    #Initiate value for grid row
    grid_row = 0

    #Loop through the light list, and add UI elements to each
    for light in active_lights:
        #Create frame
        frame = tk.Frame(master=menu)
        frame.grid(row=grid_row, column=0)
        #Variable which tracks the status of the light (on/off)
        switch_var = light.switch_var
        label = tk.Label(master=frame, text=light.name, font=bold_font)
        label.grid(row=0, column=0, columnspan=3, pady=10)
        switch_label = tk.Label(frame, text="ON" if switch_var.get() else "OFF")
        switch_label.grid(row=1, column=0, padx=10)
        #Brightness slider
        bslider_label = tk.Label(frame, text="Brightness")
        bslider_label.grid(row=1, column=1, padx=10)
        #Get the starting brightness value of the light
        bslider_initial_value = light.status()["dps"]["22"]
        bslider_var = tk.IntVar(value=bslider_initial_value)
        #Create brightness slider, which will be disabled if light is off
        bslider_button = tk.Scale(frame, variable=bslider_var, from_=0, to=1000, orient=tk.HORIZONTAL, length=300, state="normal" if switch_var.get() else "disabled", command=lambda value, lt=light: brightness_slider(value, lt))
        bslider_button.grid(row=2, column=1, padx=10, pady=10)
        #Warmth slider
        wslider_label = tk.Label(frame, text="Warmth")
        wslider_label.grid(row=1, column=2, padx=10)
        #Get the starting warmth value of the light
        wslider_initial_value = light.status()["dps"]["23"]
        wslider_var = tk.IntVar(value=wslider_initial_value)
        #Create warmth slider, which will be disabled if light is off
        wslider_button = tk.Scale(frame, variable=wslider_var, from_=0, to=1000, orient=tk.HORIZONTAL, length=300, state="normal" if switch_var.get() else "disabled", command=lambda value, lt=light: warmth_slider(value, lt))
        wslider_button.grid(row=2, column=2, padx=10, pady=10)        
        #Switch button, the command uses toggle_switch function and passes the tracked status of the light, and passes in the light data from lights.py
        switch_button = tk.Checkbutton(frame, variable=switch_var, command=lambda var=switch_var, lt=light, lbl=switch_label, bslider=bslider_button, wslider=wslider_button: toggle_switch(var, lt, lbl, bslider, wslider))
        switch_button.grid(row=2, column=0, padx=5)
        #Increment grid_row, so next frame goes to the next row
        grid_row += 1

    #Start UI
    menu.mainloop()
