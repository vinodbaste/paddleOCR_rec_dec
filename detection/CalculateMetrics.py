class CalculateMetrics:
    def __init__(self, ground_truth_data_value, ocr_results_value):
        self.ground_truth_data_value = ground_truth_data_value
        self.ocr_results_value = ocr_results_value

    def calculate_precision_recall(self):
        total_image_samples = len(self.ground_truth_data_value)
        true_positives = 0
        false_positives = 0
        false_negatives = 0

        for gt_entry, ocr_entry in zip(self.ground_truth_data_value, self.ocr_results_value):
            gt_regions = gt_entry["Regions"]
            ocr_text = ocr_entry.get("Extracted_Text", "")  # Replace "Extracted_Text" with the correct key name

            if not ocr_text:  # Handle empty or None "Extracted_Text" as a special case
                ocr_text = ""

            # Combine all ground truth transcriptions into one string for comparison
            gt_text = " ".join(region["transcription"] for region in gt_regions)

            # Print the ground truth and detected text for each image
            print(f"Image: {gt_entry['Image_Path']}")
            print(f"Ground Truth: {gt_text}")
            print(f"Detected Text: {ocr_text}\n")

            # Calculate precision and recall
            true_positives_img = sum(1 for ocr_char, gt_char in zip(ocr_text, gt_text) if ocr_char == gt_char)
            false_positives_img = len(ocr_text) - true_positives_img
            false_negatives_img = len(gt_text) - true_positives_img

            # Update overall metrics
            true_positives += true_positives_img
            false_positives += false_positives_img
            false_negatives += false_negatives_img

        # Check for zero true positives to avoid division by zero
        if true_positives == 0:
            precision_value = 0.0
            recall_value = 0.0
        else:
            precision_value = true_positives / (true_positives + false_positives)
            recall_value = true_positives / (true_positives + false_negatives)

        return precision_value, recall_value, total_image_samples
