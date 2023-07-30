from recognition.convert_txt_to_dict import ConvertTextToDict
from recognition.create_excel_sheet import CreateMetricExcel
from recognition.evaluate_model import EvaluateRecModel
from recognition.get_image_paths import GetImagePathsFromFolder
from recognition.load_model import LoadRecModel
from recognition.process_images import ProcessImages


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
