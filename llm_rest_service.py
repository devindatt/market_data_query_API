from flask import Flask, request, jsonify
import pandas as pd
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import ChatPromptTemplate
from langchain.output_parsers import ResponseSchema, StructuredOutputParser

# Create Flask application
app = Flask(__name__)

# Load in static csv file locally for this application
market_df = pd.read_csv('EndOfDayData_2023-05-30.csv')

# Instantiate an OpenAI llm model in Langchain


def engage_llm(question):
    
    # Establish the returned schema for later lookup
    ticker = ResponseSchema(
            name="ticker",
            description="The company stock ticker symbol found in the users question, as a unique string.",
        )
    metric = ResponseSchema(
            name="metric",
            description="The company financial metric found in the users question, as a unique string.",
        )

    output_parser = StructuredOutputParser.from_response_schemas(
        [ticker, metric]
    )

    response_format = output_parser.get_format_instructions()

    # Establish a well formed prompt to extract the info from the users question
    prompt = ChatPromptTemplate.from_template('''Extract the stock ticker symbol and financial metric from this users question {question}? Return the metric and stock ticker symbol separately. \n {format_instructions}''')    
    
    llm_openai = OpenAI()
    question = question

    formated_prompt = prompt.format(**{"question":question, "format_instructions":output_parser.get_format_instructions()})
    
    # Get a reply back from the llm
    response_openai = llm_openai(formated_prompt)
    
    # Parse our the data into a dictionary    
    data = output_parser.parse(response_openai)
    
    
    return data


def parse_query(question):
    
    data = engage_llm(question)

    ticker_symbol = data['ticker']
    metric  = data['metric']
          
#    ticker_symbol = 'AAL'
#    metric = 'close'
    
    return ticker_symbol, metric
    
    
@app.route('/parse_query', methods=['POST'])

def handle_question():
    
#    user_input = request.get_json(force=True)
    user_input = request.json
    
#    user_question = user_input.get('question', '') 
    user_question = user_input['question'] 
    
    ticker_symbol, metric = parse_query(user_question)
    
    # Check if we got the items to proceed
    if ticker_symbol and metric:
        try:
            value = str(round(((market_df.loc[market_df['symbol'] == ticker_symbol, metric].values[0])),1))   
            return jsonify({'ticker': ticker_symbol, 'metric': metric, 'value':value})
        except Exception as e:
            return jsonify({'error': str(e)})

    else:
        return jsonify({'error': 'Unable to parse the question to get the ticker symbol and metric'})
    
    
if __name__ == '__main__':
    app.run(port=8000, debug=True)
    