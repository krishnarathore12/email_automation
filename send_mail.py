import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import openai
import pandas as pd
from utils import get_placeholders
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Access the API key and SMTP credentials
api_key = os.getenv('OPENAI_API_KEY')

# OpenAI API key setup
openai.api_key = api_key

def generate_email_content(description, company_name):
    prompt = f"Write a formal email to a client from {company_name}. The email should include the following details: {description}. Make the tone professional."
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant that writes professional emails."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error generating email content: {e}")
        return None

def send_email(smtp_server, port, sender_email, password, recipient_email, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)

        print(f"Email sent successfully to {recipient_email}.")
    except smtplib.SMTPRecipientsRefused as e:
        print(f"Recipient refused: {e}")
    except smtplib.SMTPAuthenticationError as e:
        print(f"Authentication error: {e}")
    except Exception as e:
        print(f"Error sending email to {recipient_email}: {e}")

def process_and_send_emails(sender_email, password, csv_path, smtp_server, port):
    try:
        # Read CSV file
        df = pd.read_csv(csv_path)

        # Process each row in the CSV
        for _, row in df.iterrows():
            recipient_email = row['recipient_email']
            subject = row['subject']
            description = row['description']
            company_name = row['company_name']

            # Generate email content
            email_body = generate_email_content(description, company_name)
            if email_body:
                print(f"Generated Email Content for {recipient_email}:\n{email_body}")

                # Send the email
                send_email(smtp_server, port, sender_email, password, recipient_email, subject, email_body)
    except FileNotFoundError as e:
        print(f"CSV file not found: {e}")
    except KeyError as e:
        print(f"Missing column in the CSV: {e}")
    except Exception as e:
        print(f"An error occurred while processing emails: {e}")

# Example usage

