# Project Name: NL2SQL ✨

## Overview
Welcome to the Speech-to-SQL Query Converter project! This Python script combines ChatGPT, MySQL, and various libraries to create a voice and text interface for generating SQL queries based on user input. The script makes use of speech recognition, text-to-speech conversion, and ChatGPT natural language processing to simplify the process of formulating SQL queries.

## Features
- **Speech Recognition:** Converts spoken words into text.
- **Text-to-Speech:** Reads out responses and information.
- **Voice and Text Interface:** Allows users to choose between voice and text input for query generation.
- **Interactive Prompt:** Guides users through the process of asking for information.
- **Dynamic SQL Query Generation:** Utilizes FreeGPT to convert user input into valid SQL queries.
- **MySQL Database Interaction:** Executes the generated SQL query against a MySQL database.
- **Error Handling:** Catches exceptions and provides informative messages in case of errors.

## Prerequisites
- [FreeGPT](https://pypi.org/project/freeGPT/)
- [MySQL Connector](https://pypi.org/project/mysql-connector-python/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [winsound](https://docs.python.org/3/library/winsound.html)

## Configuration
Update the MySQL connection details in the `main()` function:
```python
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="sakila"
)
```
## User Input
The script utilizes the speechrecognition library to create instances of the recognizer and microphone classes. It accepts input either through voice or text. In the case of voice input, a prompt is signaled to the user with an accompanying sound, indicating that they can speak their command.

## Data Retrieval
The Table and attribute names of the database is retrieved and stored in the form of a dictionary where the table name is the key and the attribute names are the values.

## LLM Interpretation
The LLM(Large Language Model) interprets the user input and generates an SQL command based on the dictionary given to it.

## Command Execution
The generated query is executed and the result is displayed in the terminal.

## Exception Handling
If the Language Model cannot generate a query based on the provided data, the script will display an error message.



