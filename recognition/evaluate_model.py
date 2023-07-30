from sklearn.metrics import precision_recall_fscore_support, precision_score, recall_score, accuracy_score

from recognition.calculate_cer import CalculateCER


class EvaluateRecModel:
    def __init__(self, ocr_results, rec_ground_truth_data):
        self.ocr_results = ocr_results
        self.rec_ground_truth_data = rec_ground_truth_data

    def evaluate_model(self):
        model_predictions_data = []
        ground_truth_texts_data = []
        image_names_data = []
        precision_list = []
        recall_list = []

        for result, annotation in zip(self.ocr_results, self.rec_ground_truth_data):
            model_text = [word_info[0] for line in result for word_info in line]
            model_text = ' '.join(model_text).strip()
            model_predictions_data.append(model_text)
            # Handle missing ground truth text
            ground_truth_text = annotation.get('ground_truth_text', 'NILL').replace(' ', '')
            ground_truth_texts_data.append(ground_truth_text)
            image_names_data.append(annotation.get('file_name', 'NILL'))  # Handle missing image names

            # Calculate precision and recall for the current image
            precision_value, recall_value, f_score, true_sum = \
                precision_recall_fscore_support([ground_truth_text], [model_text], average='weighted')
            precision_list.append(precision_value)
            recall_list.append(recall_value)

        overall_model_precision = precision_score(ground_truth_texts_data, model_predictions_data, average='weighted')
        overall_model_recall = recall_score(ground_truth_texts_data, model_predictions_data, average='weighted')

        cer_data_list = CalculateCER(model_predictions_data, ground_truth_texts_data).calculate_cer()

        return model_predictions_data, ground_truth_texts_data, \
            image_names_data, precision_list, recall_list, overall_model_precision, overall_model_recall, cer_data_list
