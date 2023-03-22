# P.Blueberry

This is a Python-based tool for managing AWS access keys.

## Features

* Supports both existing and new AWS access keys
* Validates the provided access keys by attempting to list AWS regions
* Provides a simple UI for selecting options once authenticated and validated

## Requirements

To use this tool, you will need:

* Python 3.x
* PySimpleGUI package (`pip install PySimpleGUI`)
* Boto3 package (`pip install boto3`)

You can install the required packages by running the following command in your project directory:

`pip3 install -r requirements.txt`


You will also need valid AWS access keys to use the tool. If you do not have access keys, you can generate them in the AWS Management Console.

## Usage

To use the tool, simply run the `main.py` file with Python:

`python main.py`

Follow the prompts to enter your AWS access key ID and secret access key, or use existing keys if you already have them. Once authenticated and validated, you will be presented with a UI for selecting options.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
