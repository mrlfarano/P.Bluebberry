import PySimpleGUI as sg
import datetime
import boto3

# Get current time
now = datetime.datetime.now()

# Determine greeting based on time of day
if now.hour < 12:
    greeting = "Good morning!"
elif now.hour < 18:
    greeting = "Good afternoon!"
else:
    greeting = "Good evening!"

# Define the layout of the window
layout = [
    [sg.Text(greeting, font=("Helvetica", 36), justification="center", relief="raised", border_width=2)],
    [sg.Text("Please enter your AWS Access Key ID:", font=("Helvetica", 24)), sg.InputText(size=(30, 1), key="-ACCESS_KEY-")],
    [sg.Text("Please enter your AWS Secret Access Key:", font=("Helvetica", 24)), sg.InputText(password_char="*", size=(30, 1), key="-SECRET_KEY-")],
    [sg.Checkbox("Use existing keys", key="-USE_EXISTING-", font=("Helvetica", 24), default=False)],
    [sg.Submit(button_text="Connect", size=(10, 1)), sg.Cancel(button_text="Exit", size=(10, 1))]
]

# Create the window
window = sg.Window("Project Blueberry", layout)

# Event loop
while True:
    event, values = window.read()
    if event in (None, "Exit"):
        break
    elif event == "Connect":
        use_existing_keys = values["-USE_EXISTING-"]
        access_key = values["-ACCESS_KEY-"]
        secret_key = values["-SECRET_KEY-"]
        
        # Create a Boto3 session using the provided authentication objects
        session = boto3.Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key
        )
        
        # Check the validity of the authentication objects by attempting to list AWS regions
        try:
            regions = session.client("ec2").describe_regions()
            sg.popup("AWS Access Key ID and Secret Access Key are valid.")
        except:
            sg.popup("AWS Access Key ID and Secret Access Key are invalid.")
        
        if use_existing_keys:
            # Do something with the existing access_key and secret_key, such as using them to connect to AWS
            sg.popup("Using existing AWS Access Key ID and Secret Access Key.")
        else:
            # Do something with the new access_key and secret_key, such as storing them in a file or using them to connect to AWS
            sg.popup("AWS Access Key ID and Secret Access Key have been saved.")
            
# Close the window
window.close()
