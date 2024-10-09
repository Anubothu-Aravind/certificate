This project implements an automated certificate generation and email sending system using Django. It reads participant data from a CSV file, generates personalized certificates for an event, and sends them via email.

## Features
1. **Certificate Generation**: Uses a pre-designed certificate template and fills in participant details such as name and event name.
2. **Email Sending**: Automatically sends the generated certificate to the participant's email.
3. **CSV Integration**: Reads participant data from a CSV file to generate the certificates.

## Technologies Used
- **Django**: The web framework used for the backend.
- **Pillow**: For image processing to generate certificates.
- **pandas**: For working with CSV data.
- **Python’s CSV module**: For reading the CSV file.
- **Django’s email system**: To send emails with attachments.

## Installation

### Prerequisites
- Python 3.x
- A Gmail account with an app password set up for sending emails.

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Anubothu-Aravind/certificate/certificate-generator.git
   cd certificate-generator
   ```

2. **Install dependencies**:
   Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Gmail for sending emails**:
   - You need to set up your Gmail app password for secure email sending. Visit [this link](https://myaccount.google.com/apppasswords) for details.

4. **Set up Django**:
   - Run migrations to set up the Django project:
     ```bash
     python manage.py migrate
     ```

5. **Directory structure**:
   - Create a folder for storing certificates:
     ```bash
     mkdir -p genrator/template_certificate/Certificates
     ```

6. **CSV Data Format**:
   The `data.csv` file should be placed under `genrator/template_certificate/data/` and have the following columns:
   - `name`: The participant's name.
   - `id`: The unique ID for the participant.
   - `event_name`: The name of the event.
   - `email`: The participant's email address.

   Example:
   ```csv
   name,id,event_name,email
   John Doe,12345,AI Workshop,johndoe@example.com
   Jane Smith,54321,AI Workshop,janesmith@example.com
   ```

## Running the Application

1. **Start the Django development server**:
   ```bash
   python manage.py runserver
   ```

2. **Generate certificates**:
   - Visit `http://127.0.0.1:8000/` to start generating and sending certificates.
---
