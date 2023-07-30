import os

from detection.CalculateMetrics import CalculateMetrics
from detection.OcrToDf import OcrToDf
from detection.ReadGroundTruthFile import ReadGroundTruthFile
from detection.check_update_ground_truth import CheckAndUpdateGroundTruth
from detection.create_sheet import CreateSheet

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


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
