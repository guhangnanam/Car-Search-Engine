import tkinter as tk
import pandas as pd

# Variables to track:
# Make
# Model
# Mileage
# Horsepower
# Year From and Year to
# Body Type
# Drive Wheels
# Engine Type


# Breakdown:
# Two different search algorithm's narrow the large dataset into a smaller list
#



def ternary_search(dataset, user_input):
    # Implement ternary search algorithm
    pass

def interpolation_search(dataset, user_input):
    # Implement interpolation search algorithm
    pass


def search_cars(dataset, user_input):
    # Search algorithm to find cars that match the user input
    matching_cars = []

    for index, row in dataset.iterrows():
        match = True

        # Check each attribute for a match
        for key, value in user_input.items():
            if value and str(row[key]).lower() != value.lower():  # Ignore blank values
                match = False
                break

        if match:
            matching_cars.append(row)
            if len(matching_cars) == 5:
                break  # Stop when 5 matches are found

    return matching_cars


def search_button_click(year_entry, model_entry, mileage_entry, horsepower_entry, body_type_var, algorithm_var,  result_label, dataset):
    '''
    user_input = {
        "year": year_entry.get(),
        "model": model_entry.get(),
        "mileage": mileage_entry.get(),
        "horsepower": horsepower_entry.get(),
        "body type": body_type_var.get(),
        # Add other specifications
    }

    # Determine the selected searching algorithm
    selected_algorithm = algorithm_var.get()
    #print("Called")
    result_text = "Name"  # Initialize result_text with a default value

    if selected_algorithm == "Ternary Search":
        result = ternary_search(dataset, user_input)
    elif selected_algorithm == "Interpolation Search":
        result = interpolation_search(dataset, user_input)
    else:
        result = "Invalid algorithm selected."

    result_text = result  # Update result_text with the actual result

    result_label.config(text=result_text)  # Update the text of the result_label
    '''

def main():
    # Load the dataset
    dataset = pd.read_csv("cars.csv", low_memory=False)

    # Create the main application window
    app = tk.Tk()
    app.title("DSA Project 3")
    app.geometry("500x500")

    title_label = tk.Label(app, text="Enter Information on Desired Vehicle")
    title_label.grid(row=0, column=1, padx=10, pady=10)

    # Define Entry widgets for vehicle variables

    # Enter desired year
    year_label = tk.Label(app, text="Year:")
    year_label.grid(row=1, column=0, padx=10, pady=10)
    year_entry = tk.Entry(app)
    year_entry.grid(row=1, column=1, padx=10, pady=10)

    # Make
    make_label = tk.Label(app, text="Make:")
    make_label.grid(row=2, column=0, padx=10, pady=10)
    make_entry = tk.Entry(app)
    make_entry.grid(row=2, column=1, padx=10, pady=10)

    # Model
    model_label = tk.Label(app, text="Model:")
    model_label.grid(row=3, column=0, padx=10, pady=10)
    model_entry = tk.Entry(app)
    model_entry.grid(row=3, column=1, padx=10, pady=10)

    # Mileage
    mileage_label = tk.Label(app, text="Mileage:")
    mileage_label.grid(row=4, column=0, padx=10, pady=10)
    mileage_entry = tk.Entry(app)
    mileage_entry.grid(row=4, column=1, padx=10, pady=10)

    # Horsepower
    hp_label = tk.Label(app, text="Horsepower:")
    hp_label.grid(row=5, column=0, padx=10, pady=10)
    hp_entry = tk.Entry(app)
    hp_entry.grid(row=5, column=1, padx=10, pady=10)

    # Body type
    body_type_label = tk.Label(app, text="Body Type:")
    body_type_label.grid(row=6, column=0, padx=10, pady=10)
    body_type_options = ["Cabriolet", "Coupe", "Roadster", "Sedan", "Crossover", "Hatchback", "SUV", "Liftback", "Wagon", "Minivan"]
    body_type_var = tk.StringVar(app)
    body_type_var.set(body_type_options[0])  # Default value
    body_type_menu = tk.OptionMenu(app, body_type_var, *body_type_options)
    body_type_menu.grid(row=6, column=1, padx=10, pady=10)

    # Define OptionMenu for selecting the algorithm
    algorithm_label = tk.Label(app, text="Search Algorithm")
    algorithm_label.grid(row=7, column=0, padx=10, pady=10)
    algorithm_var = tk.StringVar(app)
    algorithm_var.set("Ternary Search")  # Default value
    algorithm_menu = tk.OptionMenu(app, algorithm_var, "Ternary Search", "Interpolation Search")
    algorithm_menu.grid(row=7, column=1, columnspan=2, pady=10)

    # Create and place the Search button
    search_button = tk.Button(app, text="Search", command=lambda: search_button_click(year_entry, model_entry, mileage_entry, hp_entry, body_type_var, algorithm_var, result_label, dataset))
    search_button.grid(row=8, column=0, columnspan=2, pady=10)

    # Define the result label
    result_label = tk.Label(app, text="Blank")
    result_label.grid(row=9, column=0, columnspan=2, pady=10)



    # Start the Tkinter event loop
    app.mainloop()

if __name__ == "__main__":
    main()
