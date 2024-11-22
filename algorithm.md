# Algorithm Document



Purpose: read data from file to a table, 
Name: read_data_to_table    
Parameter: none
Return: table  
Algorithm:
1. make an empty list for the table
2. make error_loop = 0
3. while error_loop = 0
   2. try
      3. Prompt the user to enter the name of the file they want to use
      4. open the file for reading
      2. for each line in the file
         1. set a row list to the line split by commas
         2. set the numbers in the row to integers
      4. set error_loop to 1
      5. return table
   2. except
      3. output "file not found"

Purpose:  update table by adding 1 element at each row to hold profit
Name: calculate_profit  
Parameter: table  
Return: table  
Algorithm:  
1. for each row in the table
   2. subtract the cost of the film from the worldwide gross
   3. append this difference to the row
2. return the table


Purpose: Ask the user for a new output file name  
Name: output_name  
Parameter: none  
Return: filename 
Algorithm:  
1. Prompt the user to input the new output files name
2. remove punctuation 
3. display the new file name
2. return the new name

Purpose:  write each the new table onto output file
Name: write_table_to_file  
Parameter: table, output_filename   
Return: none  
Algorithm:  
1. open the output file for writing
2. for each row in the table
   1. write each row onto the file sepa1 rated with commas
3. close the file

Purpose: Find and display the movie with the highest profit
Name: display_highest_profit_movie
Parameter: table
Return: None
Algorithm:
1. make an empty list
2. set value to 0
3. for each row in the table
   1. if the profit is greater than the value
      1. set the highest profit movie to the row
      2. set the value to the profit