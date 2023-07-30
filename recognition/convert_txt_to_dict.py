import os


class ConvertTextToDict:
    def __init__(self, txt_file):
        self.txt_file = txt_file

    def convert_txt_to_dict(self):
        if not os.path.exists(self.txt_file):
            raise FileNotFoundError(f"The TXT file '{self.txt_file}' does not exist.")

        data_list = []
        with open(self.txt_file, 'r') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if not line:
                    continue  # Skip empty lines
                parts = line.split('\t')
                if len(parts) != 2:
                    raise ValueError(f"Invalid format at line {line_num} in '{self.txt_file}'. "
                                     f"Expected 'image_name\\tground_truth_text' format.")
                file_name, ground_truth_text = parts
                data_list.append({
                    'file_name': file_name,
                    'ground_truth_text': ground_truth_text
                })

        print(data_list)
        return data_list
