import os


class FileReader:

    @staticmethod
    def read_input_file(script_path, input_path):
        input_file_path = os.path.join(script_path, input_path)
        with open(input_file_path, 'r') as file:
            lines = file.readlines()
        return lines
