# Programmers:  Lucas Podowski, Harry Li
# Course:  CS151, Dr. Zee
# Due Date: 11/20/24
# Lab Assignment:  10
# Problem Statement:  In this lab assignment you will analyze data on movies, their budgets, and their profits
# Data In: file name and output file name
# Data Out:  The highest profit returning movie
# Credits: Dr. Zee's fantastic lectures
# Input Files: .csv files

#Purpose: Ask the user for a new output file name
#Parameter: none
#Return: filename
def read_data_to_table():
    table = []
    error_loop = 0

    while error_loop == 0:
        try:
            # Prompt the user to enter the file name
            filename = input("Please enter the name of the file to read from: ").strip()
            with open(filename, 'r') as file:
                for line in file:
                    # Split line by commas to create a row
                    row = line.strip().split(',')

                    # Convert numeric values in row to integers (budget, domestic gross, worldwide gross)
                    row[2] = int(row[2])  # Movie Budget
                    row[3] = int(row[3])  # Domestic Gross
                    row[4] = int(row[4])  # Worldwide Gross

                    # Append row to the table
                    table.append(row)

            error_loop = 1  # Exit the loop if file is read successfully
        except FileNotFoundError:
            print("File not found. Please try again.")

    return table

'''Purpose:  update table by adding 1 element at each row to hold profit
Name: calculate_profit  
Parameter: table  
Return: table '''
def calculate_profit(table):
    for row in table:
        # Profit = Worldwide Gross - Budget
        profit = row[4] - row[2]
        row.append(profit)  # Append profit to the row

    return table


'''Purpose: Ask the user for a new output file name  
Parameter: none  
Return: filename '''
def output_name():
    filename = input("Please enter the name of the output file: ").strip()
    print(f"The new file name will be called: {filename}")
    return filename

'''Purpose:  write each the new table onto output file
Parameter: table, output_filename   
Return: none  '''
def write_table_to_file(table, output_filename):
    with open(output_filename, 'w') as file:
        for row in table:
            # Convert each element in row to string and join with commas
            line = ','.join(map(str, row))
            file.write(line + '\n')


'''Purpose: Find and display the movie with the highest profit
Parameter: table
Return: None'''
def display_highest_profit_movie(table):
    # Find the row with the maximum profit
    highest_profit_movie = []
    value = 0
    for row in table:
        if row[5] > value:
            highest_profit_movie = row
            value = row[5]

    # Display all information related to the movie with the highest profit
    print("\nMovie with the Highest Profit:")
    print(f"Release Date: {highest_profit_movie[0]}")
    print(f"Title: {highest_profit_movie[1]}")
    print(f"Budget: ${highest_profit_movie[2]}")
    print(f"Domestic Gross: ${highest_profit_movie[3]}")
    print(f"Worldwide Gross: ${highest_profit_movie[4]}")
    print(f"Profit: ${highest_profit_movie[5]}")

'''Purpose: be the main function
Parameters: none
return: none'''
def main():
    print('Given the name of the file, this program will calculate the the overall profit of movies'
          ' and add the profit into another file.')
    # Step 1: Read data from file to a table
    table = read_data_to_table()

    # Step 2: Calculate profit and update table
    table = calculate_profit(table)

    # Step 3: Ask user for output file name
    output_filename = output_name()

    # Step 4: Write the updated table to the output file
    write_table_to_file(table, output_filename)

    # Step 5: Display movie with highest or lowest profit (choosing highest for this example)
    display_highest_profit_movie(table)

    print("Thank you for using the program :)")

main()