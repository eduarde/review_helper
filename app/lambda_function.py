import json
import openai
from .variables import OPENAI_API_KEY


def generate_review(api: openai, prompt: str): 
    """ AI generates a review based on prompt """

    review_text = ""
    try:
        response = api.Completion.create(
            model="text-davinci-002",
            prompt=prompt,
            temperature=0.5,
            max_tokens=64,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        review_text = response['choices'][0]['text']
    except (IndexError, AttributeError): 
        print("Error in retrieving the review message.")

    return review_text


def create_prompt_message(tagline: str, name: str, tags: str):
    """ Generate the prompt needed for AI """ 

    return f"{tagline}:\n\nName: {name}\n{', '.join(tags)}\n\nReview:"

def lambda_handler(event, context):
    """ Handle the review generation via OpenAI

    Example:

        tagline = "Write a restaurant review based on these notes"
        name = "Pizza & Pasta Bar"
        tags = ["pizza good", "nice atmosphere", "cozy place", "long waiting"]
    
    """

    openai.api_key = OPENAI_API_KEY
    prompt = create_prompt_message(
        tagline=event['tagline'],
        name=event['name'],
        tags=event['tags']
    )
    text = generate_review(openai, prompt)
   
    return {
        'statusCode': 200,
        'body': json.dumps(text)
    }