import pandas as pd


class CreateMetricExcel:
    def __init__(self, image_names, model_predictions, ground_truth_texts, precision_list,
                 recall_list, cer_list, overall_model_precision, overall_model_recall,
                 file_name="output_file.xlsx",
                 extracted_text_sheet="Extracted_Texts_Metrics", model_metrics_sheet="Model_Metrics"):
        self.image_names = image_names
        self.model_predictions = model_predictions
        self.ground_truth_texts = ground_truth_texts
        self.precision_list = precision_list
        self.recall_list = recall_list
        self.cer_list = cer_list
        self.overall_model_precision = overall_model_precision
        self.overall_model_recall = overall_model_recall
        self.file_name = file_name
        self.extracted_text_sheet = extracted_text_sheet
        self.model_metrics_sheet = model_metrics_sheet

    def create_excel_sheet(self):
        df_metrics = pd.DataFrame({"Image": str(self.image_names),
                                   "Extracted_Text": self.model_predictions,
                                   "Ground_Truth": self.ground_truth_texts,
                                   "Precision": self.precision_list,
                                   "Recall": self.recall_list,
                                   "CER": self.cer_list
                                   })

        df_model_metrics = pd.DataFrame(
            {"Model": "en_PP-OCRv3_rec", "Precision": [self.overall_model_precision],
             "Recall": [self.overall_model_recall], "Total Samples": [len(self.image_names)]})

        # Create a Pandas Excel writer object
        with pd.ExcelWriter(self.file_name, engine="xlsxwriter") as writer:
            # Save the DataFrame with extracted texts to the first sheet
            df_metrics.to_excel(writer, sheet_name=self.extracted_text_sheet, index=False)
            worksheet = writer.sheets[self.extracted_text_sheet]
            # Set the column width
            worksheet.set_column("A:F", 50)  # Adjust the width as needed
            # Freeze the first row
            worksheet.freeze_panes(1, 0)

            # Save the DataFrame with model metrics to the second sheet
            df_model_metrics.to_excel(writer, sheet_name=self.model_metrics_sheet, index=False)
            worksheet = writer.sheets[self.model_metrics_sheet]
            # Set the column width
            worksheet.set_column("A:D", 20)  # Adjust the width as needed
            # Freeze the first row
            worksheet.freeze_panes(1, 0)
