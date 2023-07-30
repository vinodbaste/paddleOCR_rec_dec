import os

import pandas as pd
from paddleocr import PaddleOCR

from detection.GetImagePath import GetImagePath


class OcrToDf:
    def __init__(self,
                 image_folder,
                 label_file,
                 lang='en',
                 use_gpu=False,
                 rec_path=None,
                 det_db_thresh=0.5,
                 rec_thresh=0.5,
                 image_shape=(640, 640),
                 cls=False,
                 det=True,
                 rec=True
                 ):
        self.image_folder_path = image_folder
        self.label_file_path = label_file
        self.lang = lang
        self.use_gpu = use_gpu
        self.rec_path = rec_path
        self.det_db_thresh = det_db_thresh
        self.rec_thresh = rec_thresh
        self.image_shape = image_shape
        self.cls = cls
        self.det = det,
        self.rec = rec

    def ocr_to_df(self):
        # Initialize PaddleOCR with the text detection_poc model
        ocr = PaddleOCR(
            lang=self.lang,
            use_gpu=self.use_gpu,
            rec_path=self.rec_path,
            det_db_thresh=self.det_db_thresh,
            rec_thresh=self.rec_thresh,
            image_shape=self.image_shape,
        )

        results = []

        with open(self.label_file_path, 'r') as f:
            ground_truth_labels = f.readlines()

        for ground_truth in ground_truth_labels:

            image_path = GetImagePath(image_name=ground_truth.strip().split('\t')[0],
                                      image_folder_path=self.image_folder_path).get_image_path_by_name()

            if not image_path or image_path is None:
                continue

            # Perform text detection_poc and recognition (OCR) on the image
            result = ocr.ocr(image_path, cls=self.cls, det=self.det, rec=self.rec)
            if result[0]:
                print(result[0])
            extracted_text = []

            # Extract the text from OCR results
            for line in result[0]:
                for word_info in line[1]:
                    extracted_text.append(str(word_info))
                    break

            regions = eval(ground_truth.strip().split('\t')[1])

            # Combine all ground truth transcriptions into one string for comparison
            gt_text = " ".join(region["transcription"] for region in regions)

            # Calculate precision and recall
            true_positives = sum(1 for ocr_char, gt_char in zip(extracted_text, gt_text) if ocr_char == gt_char)
            false_positives = len(extracted_text) - true_positives
            false_negatives = len(gt_text) - true_positives

            # Check for division by zero
            if (true_positives + false_positives) == 0:
                precision_value = 0.0
            else:
                precision_value = true_positives / (true_positives + false_positives)

            if (true_positives + false_negatives) == 0:
                recall_value = 0.0
            else:
                recall_value = true_positives / (true_positives + false_negatives)

            # Append the extracted text and ground truth label to the results list
            results.append({"Image_Path": str(os.path.basename(image_path)),
                            "Extracted_Text": " ".join(extracted_text),
                            "Ground_Truth": gt_text,
                            "Precision": precision_value,
                            "Recall": recall_value
                            })

        # Create a DataFrame from the results list
        dataframe = pd.DataFrame(results)

        return dataframe
