# Course-Inquiry-Chatbot-with-Rasa-Telegram-Deployment

This is a Rasa-powered conversational AI chatbot designed for **Luminar Technolab**. The chatbot provides course information and is deployed on **Telegram** for user interaction.

## Features
- Provides detailed information about Luminar Technolab's courses.
- Offers contact details after sharing course information.
- Handles common conversation flows like greetings, goodbyes, and mood responses.
- Efficient entity recognition using Rasa's **DIETClassifier** for identifying course names.
- Deployed on **Telegram** for seamless user experience.

## Tech Stack
- **Rasa** (NLP Framework)
- **Python** (Core Logic)
- **Telegram Bot API** (Deployment)

## Setup Instructions

### Prerequisites
- Python 3.8 or above
- Rasa 3.1 or above

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install dependencies:
   ```bash
   pip install rasa
   ```
3. Train the Rasa model:
   ```bash
   rasa train
   ```
4. Run the Rasa actions server:
   ```bash
   rasa run actions
   ```
5. Run the chatbot:
   ```bash
   rasa run
   ```

## Telegram Integration
1. Create a bot on Telegram via **BotFather**.
2. Copy the bot token.
3. Add your Telegram credentials in `credentials.yml`:
   ```yaml
   telegram:
     access_token: '<YOUR_BOT_TOKEN>'
     verify: '<YOUR_BOT_USERNAME>'
     webhook_url: '<YOUR_WEBHOOK_URL>'
   ```
4. Set the webhook URL:
   ```bash
   curl -X POST https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook?url=<YOUR_WEBHOOK_URL>/webhooks/telegram/webhook
   ```

## Usage
- Start the bot by initiating a conversation on Telegram.
- Use prompts like:
  - "Tell me about Data Science."
  - "What courses do you offer?"
  - "I'm interested in Python Django."
- After receiving course information, replying with **'ok'** or similar confirms the interaction and displays contact information.

## Project Structure
```
├── actions
│   └── actions.py
├── data
│   ├── nlu.yml
│   ├── rules.yml
│   └── stories.yml
├── domain.yml
├── config.yml
├── credentials.yml
├── endpoints.yml
├── README.md
```

## Future Improvements
- Enhance dialogue flows with more dynamic responses.
- Integrate additional features like FAQs, scheduling assistance, and payment support.
- Improve model accuracy with more training data.



