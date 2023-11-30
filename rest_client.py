import json
import requests
import os
import warnings

warnings.simplefilter("ignore")


def send_question(question):

    url = 'http://127.0.0.1:8000/parse_query'

    got_key = os.getenv("OPENAI_API_KEY")

    query_dict = {'question': question,
                  'key': got_key
                  }
    response = requests.post(url, json=query_dict)
#    response = requests.post(url, json={"question": question})

    if response.status_code == 200:        
        return response.json()
    else:
        return 'Error: Unable to connect to the API'


if __name__ == '__main__':
    
    # Get input from the user, use a static question string for now
    question = input('Please ask your question here!')
#    question = 'What is the volume for AAPL?'
#    question = 'What is the close for AAIN?'

    result = send_question(question)
    print(f'Your question: {question}')
#    print(f'Your answer: {result}')
    ticker = result['ticker']
    metric = result['metric']
    value  = result['value']
    print('Based on your question {0}s {1} is {2} shares.'.format(result['ticker'], result['metric'], result['value']))


