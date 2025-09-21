# 🤖 Telegram GPT Bot

A Telegram bot powered by **OpenAI GPT** models, deployed 24/7 on **Render**.

---

## 📌 Features
- Responds to user messages using GPT (`gpt-3.5-turbo` or `gpt-4`)
- Deployed on **Render** (always online)
- Uses environment variables for security
- Easy setup with `.env` locally, or Render Dashboard in production

---

## 🔧 Local Setup

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/telegram_gpt_bot.git
cd telegram_gpt_bot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create `.env`
Inside project folder, create a `.env` file:
```
TELEGRAM_BOT_TOKEN=your_real_telegram_bot_token
OPENAI_API_KEY=your_real_openai_key
```

### 4. Run the bot
```bash
python bot.py
```

---

## 🚀 Deploy on Render

### 1. Push to GitHub
```bash
git init
git add .
git commit -m "Telegram GPT bot"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/telegram_gpt_bot.git
git push -u origin main
```

### 2. Create Render Service
1. Go to [https://dashboard.render.com](https://dashboard.render.com)
2. Click **New → Web Service**
3. Connect your GitHub repo
4. Fill in:
   - **Environment**: `Python 3`
   - **Build Command**:
     ```bash
     pip install -r requirements.txt
     ```
   - **Start Command**:
     ```bash
     python bot.py
     ```

### 3. Add Environment Variables
On Render, go to **Environment → Add Environment Variable**, then add:

| Key                | Value (example)                                      |
|--------------------|------------------------------------------------------|
| `TELEGRAM_BOT_TOKEN` | `1234567890:ABC-your-telegram-bot-token`             |
| `OPENAI_API_KEY`     | `sk-your-openai-api-key`                            |

⚠️ **Important**: No quotes, no spaces, copy the tokens exactly.

### 4. Deploy
- Click **Save**
- Render will redeploy automatically
- Check **Logs** — you should see:
  ```
  🤖 Bot is running...
  ```

---

## 🧪 Usage
- Open Telegram
- Start your bot (`/start`)
- Ask any question — GPT will reply 🎉

---

## 📜 Requirements
- `python-telegram-bot==20.3`
- `openai==0.28`
- `python-dotenv`

(Already included in `requirements.txt`)

---

## ✅ Notes
- Locally, use `.env`
- On Render, **don’t upload `.env`** — instead use Render’s Environment tab
- Keep your keys secret 🔑

