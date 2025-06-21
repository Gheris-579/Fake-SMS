# SMS Sender Tool

 
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue) ![License](https://img.shields.io/badge/license-Unlicensed-lightgrey) ![Build Status](https://img.shields.io/github/actions/workflow/status/Gheris-579/sms-sender-tool/ci.yml?branch=main) ![GitHub Issues](https://img.shields.io/github/issues/Gheris-579/sms-sender-tool)

## Table of Contents
- [What’s This Project About?](#whats-this-project-about)
- [What Can It Do?](#what-can-it-do)
- [What Do You Need to Run It?](#what-do-you-need-to-run-it)
- [How to Set It Up](#how-to-set-it-up)
- [How to Use It](#how-to-use-it)
- [API Limits](#api-limits)
- [Running Into Issues?](#running-into-issues)
- [Want to Help Out?](#want-to-help-out)
- [Code of Conduct](#code-of-conduct)
- [Security](#security)
- [What’s New?](#whats-new)
- [Project Status](#project-status)
- [Author](#author)
- [License](#license)
- [Important Disclaimer](#important-disclaimer)

## What’s This Project About?
The **SMS Sender Tool** is a neat little Python script that lets you send SMS messages to a phone number using the Textbelt API. It’s got a colorful command-line interface that’s super easy to use, making it great for anyone curious about APIs or wanting to send messages programmatically. Think of it as a fun way to learn Python and API stuff, but use it responsibly!

## What Can It Do?
- **Cool Interface**: Uses colors to make prompts and outputs pop (thanks to `pystyle` and `colorama`).
- **Sends SMS**: Fires off text messages with a single command via Textbelt’s API.
- **Clear Feedback**: Shows you if the message went through or if something went wrong.
- **Works Everywhere**: Runs smoothly on Windows, macOS, or Linux.

## What Do You Need to Run It?
- A computer with **Python 3.6** or newer.
- A few Python libraries:
  - `pystyle` (for the fancy colors)
  - `requests` (to talk to the API)
  - `colorama` (to make colors work on Windows)
- A solid internet connection.
- The Textbelt API key (the free one is just `textbelt`).

## How to Set It Up
1. **Grab the Code**:
   ```bash
   git clone https://github.com/Gheris-579/Fake-SMS.git
   ```
2. **Jump Into the Folder**:
   ```bash
   cd Fake-sms
   ```
3. **Set Up a Virtual Environment** (keeps things tidy):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install the Libraries**:
   ```bash
   pip install pystyle requests colorama
   ```
5. **Check It’s All Good**:
   ```bash
   python3 -c "import pystyle, requests, colorama"
   ```
   No errors? You’re ready to roll!

## How to Use It
1. **Start the Script**:
   ```bash
   python3 fake.py
   ```
2. **Follow the Prompts**:
   - Type in the phone number (like `+12025550123` with the country code).
   - Enter the message you want to send (up to 160 characters for the free version).
3. **Check the Result**: You’ll see a green message if it worked, or an error if something’s off.

**Example**:
```plaintext
[*] Enter number of the victim: +12025550123
>>> +12025550123
[*] ENTER YOUR MSG: Hey, this is a test!
>>> Hey, this is a test!

{
  "success": true,
  "textId": "123456789",
  "quotaRemaining": 0
}
```

## API Limits
- The free `textbelt` key lets you send **only one SMS per day**.
- Phone numbers need the country code (like `+1` for the US).
- You’ll need an internet connection to make it work.
- If you mess up the number or hit the limit, the API will throw an error.

## Running Into Issues?
- **“Module not found”**:
  - Double-check you installed the libraries: `pip install -r requirements.txt`.
  - Make sure your virtual environment is active.
- **“API didn’t work”**:
  - Check the phone number format (needs `+1` or similar).
  - Visit [textbelt.com](https://textbelt.com) to see if the API’s down or you hit the quota.
- **“Nothing happens or it crashes”**:
  - Confirm Python 3.6+ is installed: `python3 --version`.
  - Try a different terminal (like PowerShell or Bash).
- **“Colors look weird”**:
  - Reinstall `colorama`: `pip install colorama`.

## Want to Help Out?
Awesome! Here’s how you can pitch in:
1. Fork the repo.
2. Create a new branch: `git checkout -b my-cool-feature`.
3. Make your changes and commit: `git commit -m "Added something awesome"`.
4. Push it up: `git push origin my-cool-feature`.
5. Open a Pull Request and tell us what you did.

Try to keep your code clean (check out [PEP 8](https://peps.python.org/pep-0008/)) and add tests if you can.

## Code of Conduct
We want everyone to feel welcome. Please follow the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/0/code_of_conduct/). Be kind and respectful!

## Security
Found a security issue? Please contact me directly (see [Author](#author)) instead of posting it publicly. We’ll fix it ASAP. Also, never leave API keys in your code where others can see them!

## What’s New?
- **v1.0.0** (June 21, 2025):
  - First release with Textbelt API support.
  - Colorful CLI and basic error handling.

Check [CHANGELOG.md](CHANGELOG.md) for the full scoop.

## Project Status
- **Version**: 1.0.0
- **Status**: Solid for basic use with Textbelt’s free API.
- **What’s Next**:
  - Support for premium Textbelt API keys.
  - Better phone number validation.
  - Automated tests to catch bugs.
  - Translations for non-English users.

## Author
- **Name**: Gheris (Akmenrah)
- **Contact**:
  - Instagram: [gheris__579_](https://www.instagram.com/gheris__579_)
  - GitHub: [Gheris-579](https://github.com/Gheris-579)

