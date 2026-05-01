# Student Dashboard

A simple web dashboard built with [Streamlit](https://streamlit.io/) for students to enter their information (Name, College, and Number), securely saving this data to a Google Sheet.

## 🚀 Features

- **Password Protection**: Uses simple password authentication to restrict access to the form.
- **Modern Aesthetic**: Aesthetically pleasing premium Dark UI.
- **Google Sheets Integration**: Automatically appends new student entries to a Google Sheet using `st-gsheets-connection`.

## 🛠️ Setup Instructions

### 1. Initialize Git and Push to GitHub

To deploy for free on Streamlit Community Cloud, your code must be hosted on GitHub.

```bash
git init
git add .
git commit -m "Initial commit for Student Dashboard"
git branch -M main
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME.git
git push -u origin main
```

*(Ensure you create a repository on GitHub first and substitute the above URL)*

### 2. Set Up Google Sheets API 

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new Google Cloud Project.
3. Enable the **Google Sheets API** and **Google Drive API** in your project's "Library" section.
4. Go to **Credentials**, click on **Create Credentials** -> **Service Account**. Give it any name, then generate the Service Account.
5. Once created, click on the Service Account edit icon, go to **Keys** -> **Add Key** -> **Create New Key** -> **JSON**. This will download your `credentials.json` file.
6. Open your `credentials.json` file. You will need its contents for Streamlit's Secret settings.
7. Note down the `client_email` found inside the `credentials.json`. 

### 3. Create a Google Sheet

1. Go to [Google Sheets](https://docs.google.com/spreadsheets/) and create a new blank spreadsheet.
2. In the top right, click **Share**.
3. **Important**: Paste the `client_email` you obtained from the Service Account JSON and give it "Editor" access.
4. Note your Google Sheet's URL.

### 4. Deploy to Streamlit Community Cloud (100% Free)

1. Sign up/Log in to [Streamlit Community Cloud](https://share.streamlit.io/).
2. Click **New app**. 
3. Select the GitHub repository you created, the branch (`main`), and the main file path (`app.py`).
4. **Before clicking Deploy**, click on **Advanced settings**.
5. You will see a "Secrets" text box. Paste the following structure, substituting the dummy attributes with the ones from your downloaded `credentials.json` file and your Google Sheet URL:

```toml
[connections.gsheets]
spreadsheet = "YOUR_GOOGLE_SHEET_URL"

[connections.gsheets.service_account]
type = "service_account"
project_id = "your-project-id"
private_key_id = "your-private-key-id"
private_key = "-----BEGIN PRIVATE KEY-----\nYOUR_PRIVATE_KEY_HERE\n-----END PRIVATE KEY-----\n"
client_email = "your-service-account@your-project-id.iam.gserviceaccount.com"
client_id = "your-client-id"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "your-cert-url"
```

6. Click **Save** on the secrets page.
7. Click **Deploy!**

Your beautiful student dashboard is now live, password protected, and seamlessly integrating form data directly into a Google Spreadsheet!
