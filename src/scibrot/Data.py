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
        