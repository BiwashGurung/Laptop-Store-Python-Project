# Open the text file for reading

def read_data():
        file=open("laptops.txt", "r")
 

    # Initialize an empty list to store the data
        data = []

    # Loop through each line in the file
        for line in file:

        # Split the line into individual pieces of data
            row = line.strip().split(',')

        # Append the data to the list as a row in the 2D array
            data.append(row)

# Print the resulting 2D array
        file.close()
        return data
      