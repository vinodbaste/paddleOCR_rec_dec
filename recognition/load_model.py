from paddleocr import PaddleOCR


class LoadRecModel:
    def __init__(self, use_gpu=False, rec_path=None, lang='en', rec_thresh=0.5, image_shape=(640, 640)):
        self.rec_thresh = rec_thresh
        self.image_shape = image_shape
        self.lang = lang
        self.use_gpu = use_gpu
        self.rec_path = rec_path

    def load_model(self):
        ocr = PaddleOCR(lang=self.lang,
                        use_gpu=self.use_gpu,
                        rec_path=self.rec_path,
                        image_shape=self.image_shape,
                        rec_thresh=self.rec_thresh)

        return ocr
