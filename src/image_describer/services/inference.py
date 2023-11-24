import uuid

from transformers import pipeline


class InferenceService:
    def __init__(self, model="microsoft/git-base-textcaps"):
        self.default_model = model
        self.captioner = None

    def load_model(self, model=None):
        self.captioner = pipeline("image-to-text", model=model or self.default_model)

    def predict(self, image_content):
        if not self.captioner:
            self.load_model(self.default_model)

        return self.captioner(image_content)


inference_service = InferenceService()
