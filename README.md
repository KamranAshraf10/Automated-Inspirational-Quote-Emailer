# Automated Inspirational Quote Emailer

## Overview
Automated Inspirational Quote Emailer delivers daily motivational quotes to your inbox using Python, API integration, and scheduled cron jobs. Brighten your day or boost team morale with seamless, uplifting messages.

## Features
- **Daily Inspirational Quotes**: Start your day with positive energy.
- **API Integration**: Fetches quotes from a reputable source.
- **Cron Job Scheduling**: Ensures timely delivery of your daily dose of inspiration.
- **Easy Configuration**: Customize delivery times and recipients to fit your needs.

## Getting Started

### Prerequisites
- Python 3.x
- Access to a command-line interface
- A virtual environment (optional but recommended)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/inspiremail.git
   ```

2. Navigate to the project directory:
   ```bash
   cd inspiremail
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration
- Update the `params` in `automation.py` to include your desired email recipients and sender details.
- Set up your cron job or scheduled task to run `auto_email.bat` at your chosen time.

## Usage
Run the script manually to send an email immediately:
```bash
python automation.py
```

Or schedule `auto_email.bat` for automatic daily emails.

## Contributing
Contributions are welcome! Please feel free to submit pull requests or open issues to suggest improvements or add new features.

## License
This project is licensed under the MIT License - see the LICENSE file for details.