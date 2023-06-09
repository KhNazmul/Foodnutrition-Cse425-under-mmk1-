import tkinter as tk
from tkinter import ttk
import requests

def compare_foods():
    # Destroy all widgets
    for widget in root.winfo_children():
        widget.destroy()

    # Call the API to get the list of available food names
    url = "https://psyduck3773.pythonanywhere.com/NameList"
    response = requests.get(url)
    name_list = response.json()["data"]
    name_list = [item['name'] for item in name_list]

    # Create a new window for food selection
    # compare_window = tk.Toplevel(root)

    def get_selected_foods():
        selected_food_1 = food_var_1.get()
        selected_food_2 = food_var_2.get()
        print(selected_food_1)
        print(selected_food_2)

        # Call the API to get nutritional information of the selected foods
        api1 = f"https://psyduck3773.pythonanywhere.com/SearchByName/\"{selected_food_1}\""
        api2 = f"https://psyduck3773.pythonanywhere.com/SearchByName/\"{selected_food_2}\""
        response1 = requests.get(api1)
        response2 = requests.get(api2)

        food_info_1 = response1.json()["data"][0]
        food_info_2 = response2.json()["data"][0]

        # Create a new window to display the comparison
        # comparison_window = tk.Toplevel(compare_window)
        # comparison_window.configure(bg="yellow")


        # Display the nutritional information of the selected foods side by side
        food_info_text1= tk.Text(root, font=("Arial", 14), state=tk.DISABLED,width=30)
        food_info_text1.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

        food_info_text_2 = tk.Text(root, font=("Arial", 14), state=tk.DISABLED,width=30)
        food_info_text_2.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

        food_info_text1.config(state=tk.NORMAL)
        food_info_text1.delete("1.0", tk.END)
        food_info_text1.insert(tk.END, f"Food Name: {food_info_1['name']}\n")
        food_info_text1.insert(tk.END, f"Calories: {food_info_1['Calories']}\n")
        food_info_text1.insert(tk.END, f"Carbohydrates: {food_info_1['Carbohydrates']}\n")
        food_info_text1.insert(tk.END, f"Protein: {food_info_1['Protein']}\n")
        food_info_text1.insert(tk.END, f"Fat: {food_info_1['Fat']}\n")
        food_info_text1.insert(tk.END, f"Alcohol: {food_info_1['Alcohol']}\n")
        food_info_text1.insert(tk.END, f"Fiber: {food_info_1['Fiber']}\n")
        food_info_text1.insert(tk.END, f"Sugar: {food_info_1['Sugar']}\n")
        food_info_text1.insert(tk.END, f"Saturated Fat: {food_info_1['Saturated_Fat']}\n")
        food_info_text1.insert(tk.END, f"Cholesterol: {food_info_1['Cholesterol']}\n")
        food_info_text1.insert(tk.END, f"Sodium: {food_info_1['Sodium']}\n")
        food_info_text1.insert(tk.END, f"Potassium: {food_info_1['Potassium']}\n")
        food_info_text1.insert(tk.END, f"Sugar: {food_info_1['Sugar']}\n")
        food_info_text1.insert(tk.END, f"Iron: {food_info_1['Iron']}\n")
        food_info_text1.config(state=tk.DISABLED)

        food_info_text_2.config(state=tk.NORMAL)
        food_info_text_2.delete("1.0", tk.END)
        food_info_text_2.insert(tk.END, f"Food Name: {food_info_2['name']}\n")
        food_info_text_2.insert(tk.END, f"Calories: {food_info_2['Calories']}\n")
        food_info_text_2.insert(tk.END, f"Carbohydrates: {food_info_2['Carbohydrates']}\n")
        food_info_text_2.insert(tk.END, f"Protein: {food_info_2['Protein']}\n")
        food_info_text_2.insert(tk.END, f"Fat: {food_info_2['Fat']}\n")
        food_info_text_2.insert(tk.END, f"Alcohol: {food_info_2['Alcohol']}\n")
        food_info_text_2.insert(tk.END, f"Fiber: {food_info_2['Fiber']}\n")
        food_info_text_2.insert(tk.END, f"Sugar: {food_info_2['Sugar']}\n")
        food_info_text_2.insert(tk.END, f"Saturated Fat: {food_info_2['Saturated_Fat']}\n")
        food_info_text_2.insert(tk.END, f"Cholesterol: {food_info_2['Cholesterol']}\n")
        food_info_text_2.insert(tk.END, f"Sodium: {food_info_2['Sodium']}\n")
        food_info_text_2.insert(tk.END, f"Potassium: {food_info_2['Potassium']}\n")
        food_info_text_2.insert(tk.END, f"Sugar: {food_info_2['Sugar']}\n")
        food_info_text_2.insert(tk.END, f"Iron: {food_info_2['Iron']}\n")
        food_info_text_2.config(state=tk.DISABLED)












    # Create a label for the first food selection
    food_label_1 = tk.Label(root, text="Select Food 1:", font=("Arial", 12))
    food_label_1.pack(pady=10)

    # Create a dropdown menu for the first food selection
    food_var_1 = tk.StringVar(root)
    food_dropdown_1 = ttk.OptionMenu(root, food_var_1, *name_list)
    food_dropdown_1.pack(pady=10)

    # Create a label for the second food selection
    food_label_2 = tk.Label(root, text="Select Food 2:", font=("Arial", 12))
    food_label_2.pack(pady=10)

    # Create a dropdown menu for the second food selection
    food_var_2 = tk.StringVar(root)
    food_dropdown_2 = ttk.OptionMenu(root, food_var_2, *name_list)
    food_dropdown_2.pack(pady=10)

    # Create a button to compare the selected foods
    compare_button = tk.Button(root, text="Compare", command=get_selected_foods,
                              font=("Arial", 14), relief="raised", highlightbackground="white", padx=10, pady=10)
    compare_button.pack(pady=10)

# Create the main window


# Create the main window
root = tk.Tk()
root.geometry("1280x720")
root.configure(bg="yellow")

# Create a button to invoke the compare function
compare_button = tk.Button(root, text="Compare Foods", command=compare_foods,
                           font=("Arial", 14), relief="raised", highlightbackground="white", padx=10, pady=10)
compare_button.pack(pady=10)

root.mainloop()
