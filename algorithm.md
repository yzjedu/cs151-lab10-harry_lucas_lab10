# Algorithm Document


Purpose: Get the file name from the user.  
Name: get_file_name  
Parameter: none  
Return: filename  
Algorithm:  
1. Prompt the user to enter the name of the file they want to use
2. while the filename is not a file
   1. output "file not found"   
   2. prompt the user to enter the name of the file they want to use
3. return the filename

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

Purpose:  write each the new table onto output file
Name: write_table_to_file  
Parameter: table   
Return: file  
Algorithm:  

Purpose:  
Name:  
Parameter:  
Return:  
Algorithm:  