from paddleocr import PaddleOCR


class ProcessImages:

    def __init__(self, ocr, image_paths, cls=False, det=False, rec=True):
        self.ocr = ocr
        self.image_paths = image_paths
        self.cls = cls
        self.det = det
        self.rec = rec

    def process_images(self):
        results = []

        for image_path in self.image_paths:
            result = self.ocr.ocr(image_path, cls=self.cls, det=True, rec=self.rec)  # No need for the detection model
            results.append(result)

        return results
