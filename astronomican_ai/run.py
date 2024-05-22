import os
import sys

import vertexai
from vertexai.generative_models import GenerativeModel

try:
    PROJECT = os.environ["PROJECT"]
except KeyError:
    sys.exit("No project set")


def gemini_chat():
    vertexai.init(project=PROJECT, location="europe-north1")
    model = GenerativeModel(model_name="gemini-1.5-pro-preview-0514")

    response = model.generate_content(
        "What is Warhammer 40,000?",
    )

    print(response.text)


if __name__ == "__main__":
    gemini_chat()
