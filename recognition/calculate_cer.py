
class CalculateCER:
    def __init__(self, model_texts, ground_truth_texts_data):
        self.model_texts = model_texts
        self.ground_truth_texts_data = ground_truth_texts_data

    def calculate_cer(self):
        cer_scores = []

        for model_text, ground_truth_text in zip(self.model_texts, self.ground_truth_texts_data):
            # Obtain Sentence-Level Character Error Rate (CER)
            cer_score = fastwer.score_sent(model_text, ground_truth_text, char_level=True)
            cer_scores.append(cer_score)

        return cer_scores
