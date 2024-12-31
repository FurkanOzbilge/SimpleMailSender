# SimpleMailSender

SimpleMailSender is a simple Python application for sending emails via a graphical interface.

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/FurkanOzbilge/SimpleMailSender.git
   cd SimpleMailSender
   ```

2. **Install Dependencies:**

   ```bash
   pip install tk
   ```

3. **Configure Email Credentials:**
   Edit `main.py`:

   ```python
   EmailSender_EMail = "your_email@example.com"
   EmailSender_Email_password = "your_app_password"
   ```

   - **Gmail Users:** Enable two-factor authentication and generate an app password via [Google App Passwords](https://myaccount.google.com/apppasswords).

## Usage

Run the application:

```bash
python main.py
```

Enter the recipient's email, subject, and message, then click "Send."

## License

This project is licensed under the MIT License. For more projects, visit [Furkan Özbilge's GitHub](https://github.com/FurkanOzbilge).
