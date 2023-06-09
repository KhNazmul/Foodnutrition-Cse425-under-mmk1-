import tkinter as tk
import requests

def search_food():
    # Call the API to retrieve the list of food names
    response = requests.get("https://psyduck3773.pythonanywhere.com/foodsList")
    data = response.json()["data"]

    # Create a new window to display the food names
    search_food_window = tk.Toplevel(homeWindow)
    search_food_window.title("Food Names")
    search_food_window.geometry("400x300")

    # Create a scrollable frame
    scroll_frame = tk.Frame(search_food_window)
    scroll_frame.pack(fill=tk.BOTH, expand=True)

    # Create a canvas and attach a scrollbar to it
    canvas = tk.Canvas(scroll_frame)
    scrollbar = tk.Scrollbar(scroll_frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame inside the canvas to hold the food names
    food_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=food_frame, anchor=tk.NW)

    # Populate the food names in buttons
    for food in data:
        name = food["name"]
        button = tk.Button(food_frame, text=name, command=lambda f=food: show_nutritional_facts(f))
        button.pack(pady=5)

    # Configure the canvas scroll region
    food_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

def compare_foods():
    # Create a new window to compare foods
    compare_food_window = tk.Toplevel(homeWindow)
    compare_food_window.title("Compare Foods")
    compare_food_window.geometry("400x300")

    # Add code to customize the compare food window and implement the comparison logic

def show_nutritional_facts(food):
    # Create a new window to display the nutritional facts of a specific food
    nutrition_window = tk.Toplevel(homeWindow)
    nutrition_window.title("Nutritional Facts")
    nutrition_window.geometry("400x300")

    # Add code to customize the nutrition window and display the nutritional facts of the selected food

homeWindow = tk.Tk()
homeWindow.geometry("640x480")
homeWindow.configure(bg="yellow")

search_food_button = tk.Button(homeWindow, text="Search food by name", command=search_food,
                              font=("Arial", 14), relief="raised", highlightbackground="white", padx=10, pady=10)
search_food_button.pack(pady=10)

compare_food_button = tk.Button(homeWindow, text="Compare Foods", command=compare_foods,
                               font=("Arial", 14), relief="raised", highlightbackground="white", padx=10, pady=10)
compare_food_button.pack(pady=10)

homeWindow.mainloop()
