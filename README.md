# AI SQL Query Generator

This is a Streamlit application that allows users to generate SQL queries based on natural language prompts, along with an explanation of the generated queries.

## Key Concepts Used

1. **Streamlit**: Streamlit is a Python library that makes it easy to build interactive web applications. In this project, Streamlit is used to create the user interface, including the text input area and the button to generate the SQL query.

2. **Google Generative AI API**: The Google Generative AI API is used to generate the SQL queries and explanations. The `google.generativeai` library is used to interact with the API and create a `GenerativeModel` object.

3. **API Configuration**: The API key for the Google Generative AI API is configured using the `genai.configure()` function.

4. **Natural Language Processing**: The application uses a language model to generate SQL queries based on the user's natural language input. The `model.generate_content()` function takes the formatted template (which includes the user's input) and generates the SQL query and explanation.

5. **Template Formatting**: The application uses a template string to format the input text and pass it to the language model. The `template.format()` function is used to replace the `{text_input}` placeholder with the user's actual input.

6. **Spinner and Output Display**: The application uses a Streamlit spinner to indicate that the SQL query is being generated, and then displays the generated query and explanation using the `st.write()` function.

## Usage

1. Install the required dependencies:
   - `streamlit`
   - `google.generativeai`

2. Replace the `"AIzaSyDc3u4wMi-IxuGaxYy27rNjntsqYpYBEj0"` API key with your own Google Generative AI API key.

3. Run the Streamlit application: `streamlit run app.py`

4. Enter a natural language query in the text area and click the "Generate SQL Query" button.

5. The application will display the generated SQL query and an explanation of the query.

## Limitations and Future Improvements

- The current implementation uses a single language model, which may have limitations in generating complex SQL queries. Future improvements could involve using a more powerful language model or fine-tuning the existing model on a specific domain.
- The application could be further enhanced by allowing users to select from a list of pre-defined database schemas or to input their own schema information.
- Additional features could be added, such as the ability to save and load generated queries, or the option to execute the generated queries directly against a database.