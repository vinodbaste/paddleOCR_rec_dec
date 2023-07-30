import pandas as pd


class CreateSheet:
    def __init__(self, dataframe, precision, recall, total_samples, file_name="output_file.xlsx",
                 extracted_text_sheet="Extracted_Texts_Metrics", model_metrics_sheet="Model_Metrics"):
        self.precision = precision
        self.recall = recall
        self.total_samples = total_samples
        self.df = dataframe
        self.file_name = file_name
        self.extracted_text_sheet = extracted_text_sheet
        self.model_metrics_sheet = model_metrics_sheet

    def create_sheet(self):
        # Create a DataFrame for the entire model's metrics
        df_model_metrics = pd.DataFrame(
            {"Model": "en_PP-OCRv3_det", "Precision": [self.precision], "Recall": [self.recall],
             "Total Samples": [self.total_samples]})

        # Create a Pandas Excel writer object
        with pd.ExcelWriter(self.file_name, engine="xlsxwriter") as writer:
            # Save the DataFrame with extracted texts to the first sheet
            self.df.to_excel(writer, sheet_name=self.extracted_text_sheet, index=False)
            worksheet = writer.sheets[self.extracted_text_sheet]
            # Set the column width
            worksheet.set_column("A:C", 50)  # Adjust the width as needed
            # Freeze the first row
            worksheet.freeze_panes(1, 0)

            # Save the DataFrame with model metrics to the second sheet
            df_model_metrics.to_excel(writer, sheet_name=self.model_metrics_sheet, index=False)
            worksheet = writer.sheets[self.model_metrics_sheet]
            # Set the column width
            worksheet.set_column("A:D", 20)  # Adjust the width as needed
            # Freeze the first row
            worksheet.freeze_panes(1, 0)
