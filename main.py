import tkinter as tk
import pandas as pd
import time as time
from Vehicle import Vehicle

#new_car = Vehicle("Make", "Model", "1990", "2020", "Mileage", "Horsepower", "Sedan")

# Variables to track:
# Make
# Model
# Trim
# Horsepower
# Year From and Year to
# Body Type



# Breakdown:
# Two different search algorithm's  the large dataset into a smaller list
# Then Linear search the smaller list to narrow it down further
# Display data to user (first 9 results)


# Tests for convenience:
# 1. AC, ACE, 1997, 4.9 AT, 260, Cabriolet - Returns 1 car (can remove element to see other results)
# 2. AC, ACE - Returns 9 cars
# 3. AC, Cobra - Returns 9 cars
# 4. Audi R8 - Not a recognized make and model
# 5. AC, ACE, 2003, 5.2 AT, 235, Sedan - Returns no cars



def ternary_search(dataset, make, model):
    vehicle_list = []
    low, high = 0, len(dataset) - 1

    while high >= 1 and dataset["Make"].iloc[low] <= make <= dataset["Make"].iloc[high]:
        middle1 = low + (high - low) // 3
        middle2 = high - (high - low) // 3

        if dataset["Make"].iloc[middle1] == make and dataset["Model"].iloc[middle1] == model:
            # Create a Vehicle object and append it to the list
            vehicle = Vehicle(
                make=dataset["Make"].iloc[middle1],
                model=dataset["Model"].iloc[middle1],
                yearFrom=dataset["Year_from"].iloc[middle1],
                yearTo=dataset["Year_to"].iloc[middle1],
                trim=dataset["Trim"].iloc[middle1],
                horsepower=dataset["engine_hp"].iloc[middle1],
                body_type=dataset["Body_type"].iloc[middle1]
            )
            vehicle_list.append(vehicle)

            # Explore left side
            left = middle1 - 1
            while left >= low and dataset["Make"].iloc[left] == make and dataset["Model"].iloc[left] == model:
                vehicle_left = Vehicle(
                    make=dataset["Make"].iloc[left],
                    model=dataset["Model"].iloc[left],
                    yearFrom=dataset["Year_from"].iloc[left],
                    yearTo=dataset["Year_to"].iloc[left],
                    trim=dataset["Trim"].iloc[left],
                    horsepower=dataset["engine_hp"].iloc[left],
                    body_type=dataset["Body_type"].iloc[left]
                )
                vehicle_list.append(vehicle_left)
                left -= 1

            # Explore right side
            right = middle1 + 1
            while right <= high and dataset["Make"].iloc[right] == make and dataset["Model"].iloc[right] == model:
                vehicle_right = Vehicle(
                    make=dataset["Make"].iloc[right],
                    model=dataset["Model"].iloc[right],
                    yearFrom=dataset["Year_from"].iloc[right],
                    yearTo=dataset["Year_to"].iloc[right],
                    trim=dataset["Trim"].iloc[right],
                    horsepower=dataset["engine_hp"].iloc[right],
                    body_type=dataset["Body_type"].iloc[right]
                )
                vehicle_list.append(vehicle_right)
                right += 1

            return vehicle_list  # All occurrences found
        elif dataset["Make"].iloc[middle2] == make and dataset["Model"].iloc[middle2] == model:
            # Create a Vehicle object and append it to the list
            vehicle = Vehicle(
                make=dataset["Make"].iloc[middle2],
                model=dataset["Model"].iloc[middle2],
                yearFrom=dataset["Year_from"].iloc[middle2],
                yearTo=dataset["Year_to"].iloc[middle2],
                trim=dataset["Trim"].iloc[middle2],
                horsepower=dataset["engine_hp"].iloc[middle2],
                body_type=dataset["Body_type"].iloc[middle2]
            )
            vehicle_list.append(vehicle)

            # Explore left side
            left = middle2 - 1
            while left >= low and dataset["Make"].iloc[left] == make and dataset["Model"].iloc[left] == model:
                vehicle_left = Vehicle(
                    make=dataset["Make"].iloc[left],
                    model=dataset["Model"].iloc[left],
                    yearFrom=dataset["Year_from"].iloc[left],
                    yearTo=dataset["Year_to"].iloc[left],
                    trim=dataset["Trim"].iloc[left],
                    horsepower=dataset["engine_hp"].iloc[left],
                    body_type=dataset["Body_type"].iloc[left]
                )
                vehicle_list.append(vehicle_left)
                left -= 1

            # Explore right side
            right = middle2 + 1
            while right <= high and dataset["Make"].iloc[right] == make and dataset["Model"].iloc[right] == model:
                vehicle_right = Vehicle(
                    make=dataset["Make"].iloc[right],
                    model=dataset["Model"].iloc[right],
                    yearFrom=dataset["Year_from"].iloc[right],
                    yearTo=dataset["Year_to"].iloc[right],
                    trim=dataset["Trim"].iloc[right],
                    horsepower=dataset["engine_hp"].iloc[right],
                    body_type=dataset["Body_type"].iloc[right]
                )
                vehicle_list.append(vehicle_right)
                right += 1

            return vehicle_list  # All occurrences found

        elif dataset["Make"].iloc[middle1] < make or (dataset["Make"].iloc[middle1] == make and dataset["Model"].iloc[middle1] < model):
            low = middle2 + 1
        elif dataset["Make"].iloc[middle1] > make or (dataset["Make"].iloc[middle1] == make and dataset["Model"].iloc[middle1] > model):
            high = middle1 - 1
        else:
            low = middle1 + 1
            high = middle2 - 1

    return None  # Make and model not found

def interpolation_search(dataset, make, model):
    vehicle_list = []
    low, high = 0, len(dataset) - 1

    while low <= high and dataset["Make"].iloc[low] <= make <= dataset["Make"].iloc[high]:
        # Estimate the position based on the position of the make relative to the range
        pos = low + int((high - low) * (dataset["Make"].tolist().index(make) - dataset["Make"].tolist().index(dataset["Make"].iloc[low])) / (dataset["Make"].tolist().index(dataset["Make"].iloc[high]) - dataset["Make"].tolist().index(dataset["Make"].iloc[low])))

        if dataset["Make"].iloc[pos] == make and dataset["Model"].iloc[pos] == model:
            # Create a Vehicle object and append it to the list
            vehicle = Vehicle(
                make=dataset["Make"].iloc[pos],
                model=dataset["Model"].iloc[pos],
                yearFrom=dataset["Year_from"].iloc[pos],
                yearTo=dataset["Year_to"].iloc[pos],
                trim=dataset["Trim"].iloc[pos],
                horsepower=dataset["engine_hp"].iloc[pos],
                body_type=dataset["Body_type"].iloc[pos]
            )
            vehicle_list.append(vehicle)

            # Explore left side
            left = pos - 1
            while left >= low and dataset["Make"].iloc[left] == make and dataset["Model"].iloc[left] == model:
                vehicle_left = Vehicle(
                    make=dataset["Make"].iloc[left],
                    model=dataset["Model"].iloc[left],
                    yearFrom=dataset["Year_from"].iloc[left],
                    yearTo=dataset["Year_to"].iloc[left],
                    trim=dataset["Trim"].iloc[left],
                    horsepower=dataset["engine_hp"].iloc[left],
                    body_type=dataset["Body_type"].iloc[left]
                )
                vehicle_list.append(vehicle_left)
                left -= 1

            # Explore right side
            right = pos + 1
            while right <= high and dataset["Make"].iloc[right] == make and dataset["Model"].iloc[right] == model:
                vehicle_right = Vehicle(
                    make=dataset["Make"].iloc[right],
                    model=dataset["Model"].iloc[right],
                    yearFrom=dataset["Year_from"].iloc[right],
                    yearTo=dataset["Year_to"].iloc[right],
                    trim=dataset["Trim"].iloc[right],
                    horsepower=dataset["engine_hp"].iloc[right],
                    body_type=dataset["Body_type"].iloc[right]
                )
                vehicle_list.append(vehicle_right)
                right += 1

            return vehicle_list  # All occurrences found

        elif dataset["Make"].iloc[pos] < make or (dataset["Make"].iloc[pos] == make and dataset["Model"].iloc[pos] < model):
            low = pos + 1
        else:
            high = pos - 1

    return None  # Make and model not found

def linear_scrub(vehicles, user_input):
    filtered_vehicles = []

    for vehicle in vehicles:
        #print(vehicle.trim)
        # Check if the vehicle matches the user's input criteria
        if (
            (user_input["year"] == "" or (user_input["year"] == "" or int(user_input["year"]) >= vehicle.yearFrom and int(user_input["year"]) <= vehicle.yearTo)) and
            (user_input["trim"] == "" or (user_input["trim"] == "" or user_input["trim"] == vehicle.trim)) and
            (user_input["horsepower"] == "" or (user_input["horsepower"] != "" and int(user_input["horsepower"]) == vehicle.horsepower)) and
            (user_input["body type"] == "Unknown" or user_input["body type"] == "" or user_input["body type"] == vehicle.body_type) and (len(filtered_vehicles) < 9)
            # Add other criteria as needed
        ):
            # append the vehicle to list
            filtered_vehicles.append(vehicle)

    return filtered_vehicles




def search_button_click(year_entry, model_entry, make_entry, trim_entry, hp_entry, body_type_var, algorithm_var, time_label, result_frame):
    user_input = {
        "year": year_entry.get(),
        "make": make_entry.get(),
        "model": model_entry.get(),
        "trim": trim_entry.get(),
        "horsepower": hp_entry.get(),
        "body type": body_type_var.get(),
        # Add other specifications
    }
    if user_input["make"] == "" and user_input["model"] == "":
        # Clear previous results in result_frame
        clear_result_frame(result_frame)
        result_label = tk.Label(result_frame, text="Please enter a make and model")
        result_label.grid(row=0, column=0, padx=5, pady=5, stick="w")
        return
    elif user_input["make"] == "":
        # Clear previous results in result_frame
        clear_result_frame(result_frame)
        result_label = tk.Label(result_frame, text="Please enter a make")
        result_label.grid(row=0, column=0, padx=5, pady=5, stick="w")
        return
    elif user_input["model"] == "":
        # Clear previous results in result_frame
        clear_result_frame(result_frame)
        result_label = tk.Label(result_frame, text="Please enter a model")
        result_label.grid(row=0, column=0, padx=5, pady=5, stick="w")
        return


    dataset = pd.read_csv("cars.csv", low_memory=False)
    # Determine the selected searching algorithm
    selected_algorithm = algorithm_var.get()

    if selected_algorithm == "Interpolation Search":
        # Setup timer
        start = time.time()

        # Perform interpolation search to find cars of the specified make and model
        interpolated_cars = interpolation_search(dataset, user_input["make"], user_input["model"])

        if not interpolated_cars:
            # Clear previous results in result_frame
            clear_result_frame(result_frame)
            result_label = tk.Label(result_frame, text="No cars found for the given make and model.")
            result_label.grid(row=0, column=0, padx=5, pady=5, stick="w")
            return

        # Perform linear search within the interpolated cars for matching attributes
        result = linear_scrub(interpolated_cars, user_input)
        #print(result)
        # End timer
        end = time.time()


    if selected_algorithm == "Ternary Search":
        # Start Timer
        start = time.time()
        # Perform ternary search to find cars of the specified make and model
        ternary_cars = ternary_search(dataset, user_input["make"], user_input["model"])

        if not ternary_cars:
            # Clear previous results in result_frame
            clear_result_frame(result_frame)
            result_label = tk.Label(result_frame, text="No cars found for the given make and model.")
            result_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
            return

        # Perform linear search within the ternary cars for matching attributes
        result = linear_scrub(ternary_cars, user_input)
        #print(result)
        # End Timer
        end = time.time()

    # Clear previous results in result_frame
    clear_result_frame(result_frame)

    # Display the first 9 results in a 3x3 grid
    for idx, vehicle in enumerate(result[:9]):
        row_num = idx // 3
        col_num = idx % 3
        label_text = vehicle.display_info()
        result_label = tk.Label(result_frame, text=label_text)
        result_label.grid(row=row_num, column=col_num, padx=5, pady=5, sticky="w")

    if not result:
        result_label = tk.Label(result_frame, text="No matching cars found.")
        result_label.grid(row=0, column=0, padx=5, pady=5,sticky="w")

    # Print execution time
    time_elapsed = end - start
    time_elapsed = round(time_elapsed, 6)
    time_label.config(text=f"Execution Time: {time_elapsed} seconds")


def clear_result_frame(result_frame):
    # Destroy all widgets inside result_frame
    for widget in result_frame.winfo_children():
        widget.destroy()

def print_vehicle_data(vehicles):
    for vehicle in vehicles:
        print(vehicle.display_info())
        print("=" * 30)  # Separator for better readability

def print_test(results):
    for car in results:
        print(car.trim)


def main():
    # Load the dataset
    dataset = pd.read_csv("cars.csv", low_memory=False)

    # Create the main application window
    app = tk.Tk()
    app.title("DSA Project 3")
    app.geometry("800x1400")



    title_label = tk.Label(app, text="Enter Information on Desired Vehicle")
    title_label.grid(row=0, column=1, padx=10, pady=10)

    # Define Entry widgets for vehicle variables

    # Make
    make_label = tk.Label(app, text="Make (Required):")
    make_label.grid(row=1, column=0, padx=10, pady=10)
    make_entry = tk.Entry(app)
    make_entry.grid(row=1, column=1, padx=10, pady=10)

    # Model
    model_label = tk.Label(app, text="Model (Required):")
    model_label.grid(row=2, column=0, padx=10, pady=10)
    model_entry = tk.Entry(app)
    model_entry.grid(row=2, column=1, padx=10, pady=10)

    # Year
    year_label = tk.Label(app, text="Year:")
    year_label.grid(row=3, column=0, padx=10, pady=10)
    year_entry = tk.Entry(app)
    year_entry.grid(row=3, column=1, padx=10, pady=10)

    # Trim
    trim_label = tk.Label(app, text="Trim:")
    trim_label.grid(row=4, column=0, padx=10, pady=10)
    trim_entry = tk.Entry(app)
    trim_entry.grid(row=4, column=1, padx=10, pady=10)

    # Horsepower
    hp_label = tk.Label(app, text="Horsepower:")
    hp_label.grid(row=5, column=0, padx=10, pady=10)
    hp_entry = tk.Entry(app)
    hp_entry.grid(row=5, column=1, padx=10, pady=10)

    # Body type
    body_type_label = tk.Label(app, text="Body Type:")
    body_type_label.grid(row=6, column=0, padx=10, pady=10)
    body_type_options = ["Unknown", "Cabriolet", "Coupe", "Roadster", "Sedan", "Crossover", "Hatchback", "SUV", "Liftback", "Wagon", "Minivan"]
    body_type_var = tk.StringVar(app)
    body_type_var.set("Unknown")  # Default value
    body_type_menu = tk.OptionMenu(app, body_type_var, *body_type_options)
    body_type_menu.grid(row=6, column=1, padx=10, pady=10)

    # Define OptionMenu for selecting the algorithm
    algorithm_label = tk.Label(app, text="Search Algorithm")
    algorithm_label.grid(row=7, column=0, padx=10, pady=10)
    algorithm_var = tk.StringVar(app)
    algorithm_var.set("Ternary Search")  # Default value
    algorithm_menu = tk.OptionMenu(app, algorithm_var, "Ternary Search", "Interpolation Search")
    algorithm_menu.grid(row=7, column=1, padx=10, pady=10)

    # Define label for time
    time_label = tk.Label(app, text="")
    time_label.grid(row=5, column=6, columnspan=2, pady=10)

    result_frame = tk.Frame(app)
    result_frame.grid(row=8, column=0, columnspan=3, padx=10, pady=10)

    # Create and place the Search button
    search_button = tk.Button(app, text="Search", command=lambda: search_button_click(year_entry, model_entry, make_entry, trim_entry, hp_entry, body_type_var, algorithm_var, time_label, result_frame))
    search_button.grid(row=4, column=6, columnspan=2, pady=10)




    '''
    user_input = {
        "year": "1997",
        "make": "AC",
        "model": "ACE",
        "trim": "",
        "horsepower": "",
        "body type": "Cabriolet",
        
    }

    make = "AC"
    model ="ACE"
    results = interpolation_search(dataset, make, model)
    results = ternary_search(dataset, make, model);
    print_vehicle_data(results)
    final = linear_scrub(results, user_input)
    print_test(final)

    '''


    # Start the Tkinter event loop
    app.mainloop()

if __name__ == "__main__":
    main()
