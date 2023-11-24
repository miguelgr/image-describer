import uuid
import logging

from transformers import pipeline


class InferenceService:
    def __init__(self, model="microsoft/git-base-textcaps"):
        self.default_model = model
        self.captioner = None

    def load_model(self, model=None):
        self.captioner = pipeline("image-to-text", model=model or self.default_model)

    def predict(self, image_content):
        if not self.captioner:
            logging.warn("Model not previously loaded")
            self.load_model(self.default_model)

        try:
            logging.info("Attempting image caption")
            result = self.captioner(image_content)
            title = result[0]["generated_text"]
        except Exception:
            logging.error("Error describing an image", exc_info=True)
            title = ""
        return title


inference_service = InferenceService()
