class ReadGroundTruthFile:
    def __init__(self, ground_truth_file):
        self.ground_truth_file = ground_truth_file

    def read_ground_truth_file(self):
        with open(self.ground_truth_file, 'r') as f:
            lines = f.readlines()

        ground_truth_data_value = []
        for line in lines:
            image_path, regions = line.strip().split('\t')
            regions = eval(regions)  # Convert the string representation of the list to a Python list
            ground_truth_data_value.append({"Image_Path": image_path, "Regions": regions})

        return ground_truth_data_value
