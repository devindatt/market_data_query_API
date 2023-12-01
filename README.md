# Flask Stock Data API

![screenshot_example](https://github.com/devindatt/market_data_query_API/assets/42626142/99227db0-f1a4-4512-8ef3-148bf6b5a230)

## Overview
Created a REST API in Python service that allows a user to query market data with a question. It uses a LLM natural language capability to extract info and performs a look in a static preloaded market data csv.

This Flask-based API runs LOCALLY on your machine and provides an interface to parse user questions about stock metrics and retrieve specific data points from a preloaded dataset. Utilizing LangChain for natural language understanding, it extracts key information (ticker symbol and metric) from a user's query and looks up the corresponding value in a locally preloaded Pandas DataFrame loaded from a CSV file.

## Features
- **Natural Language Query Parsing**: Leverages LangChain to interpret user questions.
- **Stock Data Lookup**: Searches a preloaded dataset for specific stock metrics.
- **RESTful API**: Easy-to-use REST API for sending queries and receiving responses.


## Getting Started

### Installation
Clone the repository:
```
git clone https://github.com/devindatt/market_data_query_API
cd market_data_query_API
```

### Prerequisites from File
- Python 3.x
- Flask
- Pandas
- LangChain
- Requests (for the client script)

Run the 'Requirement.txt file to load all the prerequisties
<img width="916" alt="requirements_install" src="https://github.com/devindatt/market_data_query_API/assets/42626142/8fffee96-0a49-4d7f-afea-75beba42551f">

Or alternatively, install the packages separately:

### Install the required packages:
![pip install](https://github.com/devindatt/market_data_query_API/assets/42626142/788fc0d7-4679-4b61-91e6-909dd47e59fe)

```
pip install flask pandas langchain requests
```

### Prepare Your OpenAI Key
Please update your own OpenAI key in the provide empty .env file.
<img width="664" alt="openai_key" src="https://github.com/devindatt/market_data_query_API/assets/42626142/418f9dde-5df7-469b-b381-bfcae7516b1e">



### Usage

1) **Start the Server:**
Navigate to the server script directory and run:
![start_server](https://github.com/devindatt/market_data_query_API/assets/42626142/4d2ca54f-c70f-41e9-bb80-a97fb2ee2e62)

```
python llm_rest_service.py
This will start the Flask server on localhost at port 8000.
```


2) **Using the Client:**
In a separate terminal, run the client script to send requests:
![start_client](https://github.com/devindatt/market_data_query_API/assets/42626142/fe3ad41f-a567-4089-be32-bc8f95595e07)

```
python rest_client.py
```

Modify the rest_client.py script to send different questions as needed.
Note: the current script will ask you to enter your question at the prompt. Please have a question handy to type in.

Alternatively, you can uncomment out one of the static examples provided in the script:
<img width="573" alt="question_input" src="https://github.com/devindatt/market_data_query_API/assets/42626142/0e21464a-45ae-4847-8f36-85bf0b1637b5">

### API Endpoints

- **POST /parse_question**
Description: Parses the user's question and retrieves the stock data.
Payload:
  {"question": "What is the volume of AAPL today?"}

Response: 
  >Your question:  What is the volume of AAPL?
  >Based on your question AAPLs volume is 55964401 shares.

## Example

Here's an example of how to use the API:

1) **Send a Question:**
```
> Please ask your question here! What is the volume of AAPL?
```
2) **Receive a Response:**
```
Based on your question AAPLs volume is 55964401 shares.
```

## Data Format

Ensure your CSV file follows the required format. Example:

![csv_columns](https://github.com/devindatt/market_data_query_API/assets/42626142/1ad939c5-cef2-4269-bd41-6c32cb18fb2b)


## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your proposed changes.

## License

This project is licensed under the MIT License.

## Contact

For any queries or further assistance, please contact Devin Datt by message.
