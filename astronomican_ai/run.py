import os
import sys

import vertexai
from vertexai.generative_models import GenerativeModel, Tool
from vertexai.preview.generative_models import grounding

try:
    PROJECT = os.environ["PROJECT"]
    DS = os.environ["DS"]
except KeyError:
    sys.exit("Required variables unset")


def gemini_chat():
    vertexai.init(project=PROJECT, location="europe-north1")
    model = GenerativeModel(model_name="gemini-1.0-pro")

    tool = Tool.from_retrieval(
        grounding.Retrieval(
            grounding.VertexAISearch(
                datastore=f"projects/{PROJECT}/locations/eu/collections/default_collection/dataStores/{DS}",
            ),
        ),
    )

    response = model.generate_content(
        "What is Warhammer 40,000?",
        tools=[tool],
    )

    print(response.text)


if __name__ == "__main__":
    gemini_chat()
