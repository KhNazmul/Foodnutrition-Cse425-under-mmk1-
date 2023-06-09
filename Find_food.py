import tkinter as tk
from tkinter import ttk
import requests


def search_food(food_listbox):
    global data

    url = "https://psyduck3773.pythonanywhere.com/foodsList"

    try:
        response = requests.get(url)
        data = response.json()

        # Clear the listbox before updating with new data
        food_listbox.delete(0, tk.END)

        # Update the listbox with food names
        for food in data["data"]:
            food_listbox.insert(tk.END, food["name"])

    except requests.exceptions.RequestException as e:
        print("Error occurred:", str(e))

def show_food_info(food_info_text,food_listbox):
    selected_food = food_listbox.get(food_listbox.curselection())
    global data

    for food in data["data"]:
        if food["name"] == selected_food:
            food_info_text.config(state=tk.NORMAL)
            food_info_text.delete("1.0", tk.END)
            food_info_text.insert(tk.END, f"Food Name: {food['name']}\n")
            food_info_text.insert(tk.END, f"Calories: {food['Calories']}\n")
            food_info_text.insert(tk.END, f"Carbohydrates: {food['Carbohydrates']}\n")
            food_info_text.insert(tk.END, f"Protein: {food['Protein']}\n")
            food_info_text.insert(tk.END, f"Fat: {food['Fat']}\n")
            food_info_text.insert(tk.END, f"Alcohol: {food['Alcohol']}\n")
            food_info_text.insert(tk.END, f"Fiber: {food['Fiber']}\n")
            food_info_text.insert(tk.END, f"Sugar: {food['Sugar']}\n")
            food_info_text.insert(tk.END, f"Saturated Fat: {food['Saturated_Fat']}\n")
            food_info_text.insert(tk.END, f"Cholesterol: {food['Cholesterol']}\n")
            food_info_text.insert(tk.END, f"Sodium: {food['Sodium']}\n")
            food_info_text.insert(tk.END, f"Potassium: {food['Potassium']}\n")
            food_info_text.insert(tk.END, f"Sugar: {food['Sugar']}\n")
            food_info_text.insert(tk.END, f"Iron: {food['Iron']}\n")
            food_info_text.config(state=tk.DISABLED)
            break

def Food_main(root):

    root.geometry("1280x720")
    root.configure(bg="wheat")

# Scrollbar for the food listbox
    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    info_frame = ttk.Frame(root)
    info_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    food_info_text = tk.Text(info_frame, font=("Arial", 12), state=tk.DISABLED)
    food_info_text.pack(fill=tk.BOTH, expand=True)

# Listbox to display food names
    food_listbox = tk.Listbox(root, font=("Arial", 12), width=30, yscrollcommand=scrollbar.set)
    food_listbox.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH)
    food_listbox.bind("<<ListboxSelect>>", show_food_info(food_info_text,food_listbox))

    scrollbar.config(command=food_listbox.yview)

# Frame to hold the food information

# Text widget to display food information

# Button to search food
    search_food(food_listbox)

    root.mainloop()
