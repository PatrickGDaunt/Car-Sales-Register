'''
    File name: Assignment1.py
    Author: Patrick D
    Date created: 2020-08-10
    Date last modified: 2020-08-10
    Python Version: 3.7.4
    Purpose: Record details of a car onto a local sql database
'''

# Importing pymysql
import pymysql

# Importing tkinter
import tkinter as tk


# Declare functions
def submit(carMake: str, carModel: str, carYear: str, salesPerson: str, salesPrice: str):
    """Function for submit button action. Submits entries into sql database
    :param carMake: Make of car
    :param carModel: Model of car
    :param carYear: Year of manufacture
    :param salesPerson: Who sold the car
    :param salesPrice: The price sold
    """
    # Connect to local database c4v
    connection = pymysql.connect('localhost', 'root', '', 'c4v')

    # Create cursor object
    cursor = connection.cursor()

    # SQL insert statement into assignment4 table
    sql = "INSERT INTO assignment4 (carMake, carModel, carYear, salesPerson, salesPrice) VALUES " \
          "(%s, %s, %s, %s, %s)"

    # Execute sql statement
    cursor.execute(sql, (carMake, carModel, carYear, salesPerson, salesPrice))

    # Commit insert change to database
    connection.commit()

    # Close connection
    connection.close()

    # Response text
    responseLabel["text"] = "The %s %s %s, sold by %s, for $%s has been saved to the database" % (carYear, carMake, carModel, salesPerson, salesPrice)


# Declare constants
HEIGHT = 500
WIDTH = 600

# Initialize the root object. All the widget will go within this root object.
root = tk.Tk()

# Set canvas size
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# Tkinter window label
root.wm_title("Car Sales Register")

# Create background image
background_image = tk.PhotoImage(file="yellowcar.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Car Make
# Create frame
carMakeFrame = tk.Frame(root, bg="#80c1ff", bd=5)
carMakeFrame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

# Create entry
carMakeEntry = tk.Entry(carMakeFrame, font=40)
carMakeEntry.place(relwidth=0.65, relheight=1)

# Label
carMakeLabel = tk.Label(carMakeFrame, text="Car Make", bd=5)
carMakeLabel.place(relx=0.8, relwidth=0.2, relheight=1)

# Car Model
# Create frame
carModelFrame = tk.Frame(root, bg="#80c1ff", bd=5)
carModelFrame.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.1, anchor="n")

# Create entry
carModelEntry = tk.Entry(carModelFrame, font=40)
carModelEntry.place(relwidth=0.65, relheight=1)

# Label
carModelLabel = tk.Label(carModelFrame, text="Car Model", bd=5)
carModelLabel.place(relx=0.8, relwidth=0.2, relheight=1)

# Car Year
# Create frame
carYearFrame = tk.Frame(root, bg="#80c1ff", bd=5)
carYearFrame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.1, anchor="n")

# Create entry
carYearEntry = tk.Entry(carYearFrame, font=40)
carYearEntry.place(relwidth=0.65, relheight=1)

# Label
carYearLabel = tk.Label(carYearFrame, text="Sales Person", bd=5)
carYearLabel.place(relx=0.8, relwidth=0.2, relheight=1)

# Sales Person
# Create frame
salesPersonFrame = tk.Frame(root, bg="#80c1ff", bd=5)
salesPersonFrame.place(relx=0.5, rely=0.4, relwidth=0.75, relheight=0.1, anchor="n")

# Create entry
salesPersonEntry = tk.Entry(salesPersonFrame, font=40)
salesPersonEntry.place(relwidth=0.65, relheight=1)

# Label
salesPersonLabel = tk.Label(salesPersonFrame, text="Car Year", bd=5)
salesPersonLabel.place(relx=0.8, relwidth=0.2, relheight=1)

# Sales Price
# Create frame
salesPriceFrame = tk.Frame(root, bg="#80c1ff", bd=5)
salesPriceFrame.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.1, anchor="n")

# Create entry
salesPriceEntry = tk.Entry(salesPriceFrame, font=40)
salesPriceEntry.place(relwidth=0.65, relheight=1)

# Label
salesPriceLabel = tk.Label(salesPriceFrame, text="Sale Price", bd=5)
salesPriceLabel.place(relx=0.8, relwidth=0.2, relheight=1)


# Add a button
# Create Frame
buttonFrame = tk.Frame(root, bg="black", bd=5)
buttonFrame.place(relx=0.5, rely=0.6, relwidth=0.75, relheight=0.1, anchor="n")
button = tk.Button(buttonFrame, text="Submit", font=40, command=lambda: submit(carMakeEntry.get(),
                                                                               carModelEntry.get(),
                                                                               salesPersonEntry.get(),
                                                                               carYearEntry.get(),
                                                                               salesPriceEntry.get()))
button.place(relwidth=1, relheight=1)

# Add response frame
responseFrame = tk.Frame(root, bg="#80c1ff", bd=5)
responseFrame.place(relx=0.5, rely=0.7, relwidth=0.75, relheight=0.1, anchor="n")
responseLabel = tk.Label(responseFrame)
responseLabel.place(relwidth=1, relheight=1)

# Initialize the main root.
root.mainloop()