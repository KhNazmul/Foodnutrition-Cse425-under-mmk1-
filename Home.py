import tkinter as tk
import requests

root = tk.Tk()
root.geometry("1000x800")
root.title("Home")
root.configure(bg="wheat")
pad_x = 50
pad_y = 50
button_width = 30
button_height = 10

def goHome():
    for widget in root.winfo_children():
        widget.destroy()
    find_food_button = tk.Button(root, text="Find Food", command=lambda: find_food("foodsList"), width=button_width, height=button_height)
    find_food_button.grid(row=0, column=0, padx=pad_x, pady=pad_y)

    compare_button = tk.Button(root, text="Compare", command=compare_foods, width=button_width, height=button_height)
    compare_button.grid(row=1, column=0, padx=pad_x, pady=pad_y)

    sort_by_highest_button = tk.Button(root, text="Sort by Highest", command=sort_by_highest, width=button_width, height=button_height)
    sort_by_highest_button.grid(row=2, column=0, padx=pad_x, pady=pad_y)

    root.mainloop()

def find_food(b):

    for widget in root.winfo_children():
        widget.destroy()


    def search_food():
        global data

        url = f"https://psyduck3773.pythonanywhere.com/{b}"

        try:
            response = requests.get(url)
            data = response.json()

            food_listbox.delete(0, tk.END)

            for food in data["data"]:
                food_listbox.insert(tk.END, food["name"])

        except requests.exceptions.RequestException as e:
            print("Error occurred:", str(e))

    def show_food_info(event):
        selected_food = food_listbox.get(food_listbox.curselection())
        global data

        for food in data["data"]:
            if food["name"] == selected_food:
                food_info_text.config(state=tk.NORMAL)
                food_info_text.delete("1.0", tk.END)
                if b=="Protein":
                    food_info_text.insert(tk.END, f"Food Name: {food['name']}\n")
                    food_info_text.insert(tk.END, f"Protein: {food['Protein']}\n")

                elif b=="calorie":
                    food_info_text.insert(tk.END, f"Food Name: {food['name']}\n")
                    food_info_text.insert(tk.END, f"calories: {food['calories']}\n")

                elif b == "Vitamin_A":
                    food_info_text.insert(tk.END, f"Food Name: {food['name']}\n")
                    food_info_text.insert(tk.END, f"Vitamin_A: {food['Vitamin_A']}\n")
                elif b == "Vitamin_C":
                    food_info_text.insert(tk.END, f"Food Name: {food['name']}\n")
                    food_info_text.insert(tk.END, f"Vitamin_C: {food['Vitamin_C']}\n")


                elif b == "Vitamin_E":
                    food_info_text.insert(tk.END, f"Food Name: {food['name']}\n")
                    food_info_text.insert(tk.END, f"Vitamin_E: {food['Vitamin_E']}\n")

                elif b == "Vitamin_D":
                    food_info_text.insert(tk.END, f"Food Name: {food['name']}\n")
                    food_info_text.insert(tk.END, f"Vitamin_D: {food['Vitamin_D']}\n")
                elif b == "foodsList":

                    food_info_text.insert(tk.END, f"Food Name: {food['name']}\n")
                    food_info_text.insert(tk.END, f"Calories: {food['Calories']}\n")
                    food_info_text.insert(tk.END, f"Carbohydrates: {food['Carbohydrates']}\n")
                    food_info_text.insert(tk.END, f"Protein: {food['Protein']}\n")
                    food_info_text.insert(tk.END, f"Fat: {food['Fat']}\n")
                    food_info_text.insert(tk.END, f"Vitamin_A: {food['Vitamin_A']}\n")
                    food_info_text.insert(tk.END, f"Vitamin_K: {food['Vitamin_K']}\n")
                    food_info_text.insert(tk.END, f"Vitamin_D: {food['Vitamin_D']}\n")
                    food_info_text.insert(tk.END, f"Vitamin_E: {food['Vitamin_E']}\n")
                    food_info_text.insert(tk.END, f"Alcohol: {food['Alcohol']}\n")
                    food_info_text.insert(tk.END, f"Fiber: {food['Fiber']}\n")
                    food_info_text.insert(tk.END, f"Sugar: {food['Sugar']}\n")
                    food_info_text.insert(tk.END, f"Saturated Fat: {food['Saturated_Fat']}\n")
                    food_info_text.insert(tk.END, f"Cholesterol: {food['Cholesterol']}\n")
                    food_info_text.insert(tk.END, f"Sodium: {food['Sodium']}\n")
                    food_info_text.insert(tk.END, f"Potassium: {food['Potassium']}\n")
                    food_info_text.insert(tk.END, f"Sugar: {food['Sugar']}\n")
                    food_info_text.insert(tk.END, f"Iron: {food['Iron']}\n")
                    food_info_text.insert(tk.END, f"Vitamin_A: {food['Vitamin_A']}\n")
                    food_info_text.insert(tk.END, f"Vitamin_C: {food['Vitamin_C']}\n")

                food_info_text.config(state=tk.DISABLED)
                break

    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


    food_listbox = tk.Listbox(root, font=("Arial", 12), width=30, yscrollcommand=scrollbar.set)
    food_listbox.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH)

    food_listbox.bind("<<ListboxSelect>>", show_food_info)

    scrollbar.config(command=food_listbox.yview)
    info_frame = tk.Frame(root)

    info_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    food_info_text = tk.Text(info_frame, font=("Arial", 12), state=tk.DISABLED)
    food_info_text.pack(fill=tk.BOTH, expand=True)
    home_button = tk.Button(root, text="Home", command=goHome, width=6, height=3)
    home_button.pack()


    search_food()



def compare_foods():
    for widget in root.winfo_children():
        widget.destroy()

    url = "https://psyduck3773.pythonanywhere.com/NameList"
    response = requests.get(url)
    name_list = response.json()["data"]
    name_list = [item['name'] for item in name_list]


    def get_selected_foods():
        selected_food_1 = food_var_1.get()
        selected_food_2 = food_var_2.get()
        print(selected_food_1)
        print(selected_food_2)

        api1 = f"https://psyduck3773.pythonanywhere.com/SearchByName/\"{selected_food_1}\""
        api2 = f"https://psyduck3773.pythonanywhere.com/SearchByName/\"{selected_food_2}\""
        response1 = requests.get(api1)
        response2 = requests.get(api2)

        food_info_1 = response1.json()["data"][0]
        food_info_2 = response2.json()["data"][0]

        food_info_text1= tk.Text(root, font=("Arial", 14), state=tk.DISABLED,width=30)
        food_info_text1.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

        food_info_text_2 = tk.Text(root, font=("Arial", 14), state=tk.DISABLED,width=30)
        food_info_text_2.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

        food_info_text1.config(state=tk.NORMAL)
        food_info_text1.delete("1.0", tk.END)
        food_info_text1.insert(tk.END, f"Food Name: {food_info_1['name']}\n")
        food_info_text1.insert(tk.END, f"Calories: {food_info_1['Calories']}\n")
        food_info_text1.insert(tk.END, f"Vitamin_A: {food_info_1['Vitamin_A']}\n")
        food_info_text1.insert(tk.END, f"Vitamin_C: {food_info_1['Vitamin_C']}\n")
        food_info_text1.insert(tk.END, f"Vitamin_D: {food_info_1['Vitamin_D']}\n")
        food_info_text1.insert(tk.END, f"Vitamin_K: {food_info_1['Vitamin_K']}\n")
        food_info_text1.insert(tk.END, f"Vitamin_E: {food_info_1['Vitamin_E']}\n")
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
        food_info_text_2.insert(tk.END, f"Vitamin_A: {food_info_2['Vitamin_A']}\n")
        food_info_text_2.insert(tk.END, f"Vitamin_C: {food_info_2['Vitamin_C']}\n")
        food_info_text_2.insert(tk.END, f"Vitamin_D: {food_info_2['Vitamin_D']}\n")
        food_info_text_2.insert(tk.END, f"Vitamin_E: {food_info_2['Vitamin_E']}\n")
        food_info_text_2.insert(tk.END, f"Vitamin_K: {food_info_2['Vitamin_K']}\n")

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












    food_label_1 = tk.Label(root, text="Select Food 1:", font=("Arial", 12))
    food_label_1.pack(pady=10)

    food_var_1 = tk.StringVar(root)
    food_dropdown_1 = tk.OptionMenu(root, food_var_1, *name_list)
    food_dropdown_1.pack(pady=10)

    food_label_2 = tk.Label(root, text="Select Food 2:", font=("Arial", 12))
    food_label_2.pack(pady=10)

    food_var_2 = tk.StringVar(root)
    food_dropdown_2 = tk.OptionMenu(root, food_var_2, *name_list)
    food_dropdown_2.pack(pady=10)

    compare_button = tk.Button(root, text="Compare", command=get_selected_foods,
                              font=("Arial", 14), relief="raised", highlightbackground="white", padx=10, pady=10)
    compare_button.pack(pady=10)

    home_button = tk.Button(root, text="Home", command=goHome, width=4, height=3)
    home_button.pack()



def sort_by_highest():

    for widget in root.winfo_children():
        widget.destroy()
    home_button = tk.Button(root, text="Home", command=goHome, width=4, height=3)
    home_button.grid(row=1, column=3, padx=pad_x, pady=pad_y, columnspan=2)

    Protein = tk.Button(root, text="Protein", command=lambda: find_food("Protein"), width=button_width, height=button_height)
    Protein.grid(row=0, column=0, padx=pad_x, pady=pad_y)

    Vitamin_A = tk.Button(root, text="Vitamin_A", command=lambda: find_food("Vitamin_A"), width=button_width, height=button_height)
    Vitamin_A.grid(row=0, column=1, padx=pad_x, pady=pad_y)

    Calorie = tk.Button(root, text="Calorie", command=lambda: find_food("calories"), width=button_width,
                                         height=button_height)
    Calorie.grid(row=1, column=0, padx=pad_x, pady=pad_y)

    Vitamin_C = tk.Button(root, text="Vitamin_C", command=lambda: find_food("Vitamin_C"), width=button_width,
                                       height=button_height)
    Vitamin_C.grid(row=1, column=1, padx=pad_x, pady=pad_y)

    Vitamin_E = tk.Button(root, text="Vitamin_E", command=lambda: find_food("Vitamin_E"), width=button_width,
                                       height=button_height)
    Vitamin_E.grid(row=2, column=0, padx=pad_x, pady=pad_y)

    Vitamin_D = tk.Button(root, text="Vitamin_D", command=lambda: find_food("Vitamin_D"), width=button_width,
                                       height=button_height)
    Vitamin_D.grid(row=2, column=1, padx=pad_x, pady=pad_y)


find_food_button = tk.Button(root, text="Find Food", command=lambda: find_food("foodsList"), width=button_width,
                             height=button_height)
find_food_button.grid(row=0, column=0, padx=pad_x, pady=pad_y)

compare_button = tk.Button(root, text="Compare", command=compare_foods, width=button_width, height=button_height)
compare_button.grid(row=1, column=0, padx=pad_x, pady=pad_y)

sort_by_highest_button = tk.Button(root, text="Sort by Highest", command=sort_by_highest, width=button_width,
                                   height=button_height)
sort_by_highest_button.grid(row=2, column=0, padx=pad_x, pady=pad_y)

root.mainloop()






