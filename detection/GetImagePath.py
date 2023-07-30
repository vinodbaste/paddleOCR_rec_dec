import os


class GetImagePath:

    def __init__(self, image_name, image_folder_path):
        self.image_name = image_name
        self.image_folder_path = image_folder_path

    def get_image_path_by_name(self):
        image_path = os.path.join(self.image_folder_path, self.image_name)
        if os.path.exists(image_path) and os.path.isfile(image_path):
            return image_path
        else:
            print(f"Image with name '{self.image_name}' not found in the folder '{self.image_folder_path}'.")
            return None
