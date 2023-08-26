import csv
class Data:
    """
    The class Data represents the read data from a CSV file.
    """
    def __init__(self) -> None:
        pass
    def read_csv(self, csv_file_name: str) -> dict:
        """
        Read CSV file into dictionary, this takes the first line of the data as the header element.

        :param csv_file_name: The name of the CSV file to be read.
        """
        with open(csv_file_name, 'r') as file:
            lines = file.readlines()
            # Take first line as header and remove it from read lines
            header  = lines[0].strip.split(',')
            for line_num, line in enumerate(lines[1:], start=1):  # Start index from 1
                values = line.strip().split(',')  # Split the line into values
                
                # Create a dictionary entry where keys are from the header and values are from the current line
                data_entry = {header[j]: values[j] for j in range(len(header))}
                
                data_dict[line_num] = data_entry
                
        return data_dict  # Return the dictionary containing the data

# Create an instance of the Data class
data_handler = Data()

# Call the read_csv method to read the CSV file and get the data dictionary
csv_data = data_handler.read_csv('param.csv')
print(csv_data)

            
        
