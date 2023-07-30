import os

from detection.GetImagePath import GetImagePath


class GetImagePathsFromFolder:
    def __init__(self, image_folder, txt_file):
        self.image_folder = image_folder
        self.txt_file = txt_file

    def get_image_paths_from_folder(self):
        if not os.path.exists(self.image_folder):
            raise FileNotFoundError(f"The image folder '{self.image_folder}' does not exist.")

        image_paths = []

        with open(self.txt_file, 'r') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if not line:
                    continue  # Skip empty lines

                image_path = GetImagePath(image_name=line.split('\t')[0],
                                          image_folder_path=self.image_folder).get_image_path_by_name()
                image_paths.append(os.path.join(self.image_folder, image_path))

        return image_paths
