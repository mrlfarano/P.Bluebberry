# P.Bluebberry
The tool is designed to simplify the process of running specific actions against AWS services.

## Getting Started

### Prerequisites

To use this tool, you'll need to have the following:

- Python 3.6 or later installed
- Boto3 library installed (`pip install boto3`)
- PySimpleGUI library installed (`pip install PySimpleGUI`)

### Installation

To install the tool, simply clone the repository and navigate to the project directory:

git clone https://github.com/mrlfarano/P.Blueberry.git
cd P.Blueberry/

### Usage

To use the tool, run the `main.py` file:

python main.py

You'll be prompted to enter your AWS Access Key ID and Secret Access Key, and optionally indicate whether you want to use existing keys. Upon clicking the "Connect" button, the tool will attempt to validate the entered authentication objects by attempting to list the available AWS regions using Boto3. If the authentication objects are valid, a success message will be displayed. If the authentication objects are invalid, an error message will be displayed.

## Contributing

Contributions to the AWS Access Key Tool are welcome and encouraged! To contribute, simply fork the repository, create a new branch for your changes, and submit a pull request. For major changes, please open an issue first to discuss your proposed changes.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- [PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI)
- [Boto3](https://github.com/boto/boto3)
