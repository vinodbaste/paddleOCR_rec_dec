from detection.decmain import DecMain
from recognition.rec_main import RecMain

"""
Note: Format of the REC Ground Truth Text File

To perform OCR evaluation using the RecMain class and the provided code, it's essential to format the ground truth (GT) text file correctly. The GT text file should be in the following format:
T25166601GTD_202301181427_1 - Copy (2)_crop_0.jpg	MICHELIN
Each line of the file represents an image's GT text.
Each line contains the filename of the image, followed by a tab character (\t), and then the GT text for that image.
Ensure that the GT text file contains GT text entries for all the images present in the image folder specified in the RecMain class. The GT text should match the actual text content present in the images. This format is necessary for accurate evaluation of the OCR model's performance.
"""

"""
Note: Format of the DET Ground Truth Label File

To perform OCR evaluation using the DecMain class and the provided code, it's crucial to format the ground truth label file correctly. The label file should be in JSON format and follow the structure as shown below:

identity_T40829322TB_202212131924_1 - Copy (2).PNG [{"transcription": "215mm 18", "points": [[199, 6], [357, 6], [357, 33], [199, 33]], "difficult": False, "key_cls": "digits"}, {"transcription": "XZE SA", "points": [[15, 6], [140, 6], [140, 36], [15, 36]], "difficult": False, "key_cls": "text"}]
The label file should be in JSON format.
Each line of the file represents an image's OCR ground truth.
Each line contains the filename of the image, followed by the OCR results for that image in the form of a JSON object.
The JSON object should have the following keys:

"transcription": The ground truth text transcription of the image.
"points": A list of four points representing the bounding box coordinates of the text region in the image.
"difficult": A boolean value indicating whether the text region is difficult to recognize.
"key_cls": The class label of the OCR result, e.g., "digits" or "text".
Make sure to follow this format while creating the ground truth label file for accurate OCR evaluation."""

# Example usage: Replace with your image folder path, label file, and desired output file name
image_folder = "path/to/image_folder"
label_file = "path/to/txt_file"
output_file = "raw_output.xlsx"

# if __name__ == "__main__":
#     DecMain(image_folder_path=image_folder, label_file_path=label_file, output_file=output_file) \
#         .run_dec()

if __name__ == "__main__":
    RecMain(image_folder=image_folder, rec_file=label_file, output_file=output_file).run_rec()
