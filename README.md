**Project: Email Automation**

This project automates emails using the OpenAI API and Streamlit.
![image](https://github.com/user-attachments/assets/fa19b6e0-b7cb-4d21-b4c4-9db8e1fb717d)


**Requirements**

* Python 3.6 or later
* OpenAI API Key ([https://platform.openai.com/login?launch](https://platform.openai.com/login?launch))
* Streamlit (`pip install streamlit`)
* python-dotenv (`pip install python-dotenv`)

**Installation**

1. Clone this repository.
2. Create a virtual environment (recommended)
3. Activate the virtual environment
4. Install the required dependencies:
   ```bash
   pip install streamlit python-dotenv
   ```
5. Create a file named `.env` in the project's root directory. Populate it with your OpenAI API key, email password, and sender email address following the format:

   ```
   OPENAI_API_KEY=your_api_key
   EMAIL_PASSWORD=your_email_password
   SENDER_EMAIL=your_sender_email
   ```

   **Important:**  **Do not commit the .env file to version control**  as it contains sensitive information.  Add the `.env` file to your `.gitignore` file.

**Usage**

1. Make sure your CSV file contains headers named `recipient_email`, `subject`, `description`, and `company_name`.
2. Place your CSV file in the same directory as your Python script (`main.py`).
3. Run the script using Streamlit:

   ```bash
   streamlit run main.py
   ```

**Explanation**

The project leverages the OpenAI API and Streamlit to automate emails. Here's a general breakdown of the functionalities:

* The `.env` file stores sensitive information like your OpenAI API key, email password, and sender email address securely.
* The script utilizes the `python-dotenv` library to load environment variables from the `.env` file.
* The script retrieves email data (recipient email, subject, description, and company name) from the CSV file.
* It leverages the OpenAI API to potentially craft email content or personalize it based on your requirements. 
* Streamlit creates a user interface to potentially preview and send the emails.


 
