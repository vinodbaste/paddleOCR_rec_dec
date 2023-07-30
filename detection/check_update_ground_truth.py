class CheckAndUpdateGroundTruth:
    def __init__(self, ground_truth_file):
        self.ground_truth_file = ground_truth_file

    def check_and_update_ground_truth_file(self):
        # Read the contents of the ground truth file
        with open(self.ground_truth_file, 'r') as f:
            content = f.read()

        # Replace all occurrences of 'false' with 'False'
        content = content.replace('false', 'False')

        # Write the modified content back to the ground truth file
        with open(self.ground_truth_file, 'w') as f:
            f.write(content)
