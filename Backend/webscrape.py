
from typing import Any, Dict, List

from hume import HumeBatchClient
from hume.models.config import NerConfig
from hume.models.config import LanguageConfig

def print_sentiment(sentiment: List[Dict[str, Any]]) -> None:
    sentiment_map = {e["name"]: e["score"] for e in sentiment}
    for rating in range(1, 10):
        print(f"- Sentiment {rating}: {sentiment_map[str(rating)]:4f}")

def print_emotions(emotions: List[Dict[str, Any]]) -> None:
    emotion_map = {e["name"]: e["score"] for e in emotions}
    for emotion in ["Joy", "Sadness", "Anger"]:
        print(f"- {emotion}: {emotion_map[emotion]:4f}")

client = HumeBatchClient("G5vVjRWYoVM4WtNKzI5PJ0XsSOFnan8VYYucHMeFxaCvbhjJ")

file_path = "test.txt"

with open(file_path, 'w') as file:
    # Write data to the file
    file.write("President Obama called Wednesday on Congress to extend a tax break for students included in last year's economic stimulus package, arguing that the policy provides more generous assistance. The American Opportunity Tax Credit program, which will cost $58 billion over a decade, is due to expire at the end of this year. In a statement to reporters in the White House Rose Garden, Obama said the tax breaks help make a college education more affordable for Americans. 'I am calling on Congress to make this tax credit permanent,' Obama said, using the occasion to campaign for Democratic policies on education in the upcoming congressional elections on November 2. After touting his administration's steps to expand student loans and reform public school education in the country, Obama said Republicans want to cut government spending that could include a 20 percent reduction in education funding.\n")

# Submit the obama.txt file from the local disk
files = ["test.txt"]
config = LanguageConfig(sentiment={})
job = client.submit_job([], [config], files=files)

print("Running...", job)

job.await_complete()
print("Job completed with status: ", job.get_status())

full_predictions = job.get_predictions()
for source in full_predictions:
    predictions = source["results"]["predictions"]
    for prediction in predictions:
        ner_predictions = prediction["models"]["ner"]["grouped_predictions"]
        for ner_prediction in ner_predictions:
            for entity_data in ner_prediction["predictions"]:
                print(entity_data["entity"])
                print_emotions(entity_data["emotions"])
                print()