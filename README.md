# paddleOCR for Det and Rec
Optical Character Recognition (OCR) is a powerful technology that enables machines to recognize and extract text from images or scanned documents. OCR finds applications in various fields, including document digitization, text extraction from images, and text-based data analysis. In this article, we will explore how to use PaddleOCR, an advanced OCR toolkit based on deep learning, for text detection and recognition tasks. We will walk through a code snippet that demonstrates the process step-by-step.
# Prerequisites
Before we dive into the code, let's ensure we have everything set up to run the PaddleOCR library. Make sure you have the following prerequisites installed on your machine:
Python (3.6 or higher)
PaddleOCR library
Other necessary dependencies (e.g., NumPy, pandas, etc)

Before running the code snippet, make sure you have the necessary libraries installed. You can find all the required packages and their versions in the requirements.txt file
```python
pip install -r requirements.txt
```
# Getting started
In the provided ```main.py```, we have an example usage of the RecMain class for performing text recognition (OCR) on a folder of images and generating an output Excel file with evaluation metrics:
```
# Example usage: Replace with your image folder path, label file, and desired output file name
image_folder = "path/to/image_folder"
label_file = "path/to/txt_file"
output_file = "raw_output.xlsx"

if __name__ == "__main__":
    RecMain(image_folder=image_folder, rec_file=label_file, output_file=output_file).run_rec()
```

same can be initiated for detection
```
#Dec
# Example usage: Replace with your image folder path, label file, and desired output file name
image_folder = "path/to/image_folder"
label_file = "path/to/txt_file"
output_file = "raw_output.xlsx"

if __name__ == "__main__":
  DecMain(image_folder_path=image_folder, label_file_path=label_file, output_file=output_file) \
  .run_dec()
```

# 1. Text Detection
The code provided is a part of a class named DecMain, which seems to be designed for Optical Character Recognition (OCR) evaluation using ground truth data. It appears to use PaddleOCR to extract text from images and then calculates metrics like precision, recall, and Character Error Rate (CER) to evaluate the performance of the OCR system.
```python
class DecMain:
    def __init__(self, image_folder_path, label_file_path, output_file):
        self.image_folder_path = image_folder_path
        self.label_file_path = label_file_path
        self.output_file = output_file

    def run_dec(self):
        # Check and update the ground truth file
        CheckAndUpdateGroundTruth(self.label_file_path).check_and_update_ground_truth_file()

        df = OcrToDf(image_folder=self.image_folder_path, label_file=self.label_file_path, det=True, rec=True, cls=False).ocr_to_df()

        ground_truth_data = ReadGroundTruthFile(self.label_file_path).read_ground_truth_file()

        # Get the extracted text as a list of dictionaries (representing the OCR results)
        ocr_results = df.to_dict(orient="records")

        # Calculate precision, recall, and CER
        precision, recall, total_samples = CalculateMetrics(ground_truth_data, ocr_results).calculate_precision_recall()

        CreateSheet(dataframe=df, precision=precision, recall=recall, total_samples=total_samples,
                    file_name=self.output_file).create_sheet()
```
# Note: Format of the DET Ground Truth Label File
```
To perform OCR evaluation using the DecMain class and the provided code, it's crucial to format the ground truth label file correctly.
The label file should be in JSON format and follow the structure as shown below:

image_name.jpg [{"transcription": "215mm 18", "points": [[199, 6], [357, 6], [357, 33], [199, 33]], "difficult": False, "key_cls": "digits"}, {"transcription": "XZE SA", "points": [[15, 6], [140, 6], [140, 36], [15, 36]], "difficult": False, "key_cls": "text"}]

The label file should be in JSON format.
Each line of the file represents an image's OCR ground truth.
Each line contains the filename of the image, followed by the OCR results for that image in the form of a JSON object.
The JSON object should have the following keys:
"transcription": The ground truth text transcription of the image.
"points": A list of four points representing the bounding box coordinates of the text region in the image.
"difficult": A boolean value indicating whether the text region is difficult to recognize.
"key_cls": The class label of the OCR result, e.g., "digits" or "text".
Make sure to follow this format while creating the ground truth label file for accurate OCR evaluation.
```
# 2. Text Recognition
The code provided defines a class named RecMain, which is designed to run text recognition (OCR) using a pre-trained OCR model on a folder of images and generate an evaluation Excel sheet.
```python
class RecMain:
    def __init__(self, image_folder, rec_file, output_file):
        self.image_folder = image_folder
        self.rec_file = rec_file
        self.output_file = output_file

    def run_rec(self):
        image_paths = GetImagePathsFromFolder(self.image_folder, self.rec_file). \
            get_image_paths_from_folder()

        ocr_model = LoadRecModel().load_model()

        results = ProcessImages(ocr=ocr_model, image_paths=image_paths).process_images()

        ground_truth_data = ConvertTextToDict(self.rec_file).convert_txt_to_dict()

        model_predictions, ground_truth_texts, image_names, precision, recall, \
            overall_model_precision, overall_model_recall, cer_data_list = EvaluateRecModel(results,
                                                                                            ground_truth_data).evaluate_model()

        # Create Excel sheet
        CreateMetricExcel(image_names, model_predictions, ground_truth_texts,
                          precision, recall, cer_data_list, overall_model_precision, overall_model_recall,
                          self.output_file).create_excel_sheet()
```
# Note: Format of the Ground Truth Text File
```
To perform OCR evaluation using the RecMain class and the provided code, it's essential to format the ground truth (GT) text file correctly.
The GT text file should be in the following format:

image_name.jpg text

Each line of the file represents an image's GT text.
Each line contains the filename of the image, followed by a tab character (\t), and then the GT text for that image.
Ensure that the GT text file contains GT text entries for all the images present in the image folder specified in the RecMain class. The GT text should match the actual text content present in the images. This format is necessary for accurate evaluation of the OCR model's performance.
```

**If you find this library useful, please consider starring this repository from the top of this page.**
[![](https://i.imgur.com/oSLuE0e.png)](#)

# Support my work
<a href="https://www.buymeacoffee.com/bastevinod" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

# License
```
Copyright [2023] [Vinod Baste]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
