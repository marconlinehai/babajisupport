import requests
import time
import html
from data_generator import FixedDataGenerator
from config import BOT_TOKEN, CHANNEL_ID, SEND_INTERVAL

class FixedTokenBot:
    def __init__(self, bot_token, channel_id):
        self.bot_token = bot_token
        self.channel_id = channel_id
        self.base_url = f"https://api.telegram.org/bot{bot_token}/"
        self.generator = FixedDataGenerator()
        self.message_count = 0
    
    def send_message(self, text):
        """Send message to Telegram channel"""
        url = self.base_url + "sendMessage"
        payload = {
            "chat_id": self.channel_id,
            "text": text,
            "parse_mode": "HTML"
        }
        
        try:
            response = requests.post(url, json=payload, timeout=10)
            return response.json()
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def escape_html(self, text):
        """Escape HTML special characters"""
        return html.escape(text)
    
    def format_message(self, data):
        """Format message with bold device info labels"""
        recipient = data["recipient"]
        message = self.escape_html(data["message"])
        device = data["device_info"]
        
        formatted = f"""<b>🏷️ TOKEN BABA 2.0</b>

🏷️ <b>RECIPIENT :</b> <code>{recipient}</code>
🏷️ <b>MESSAGE :</b> <code>{message}</code>

<b>⚒️ DEVICE INFO</b>

<b>MODEL :</b> {device['model']}
<b>MANUFACTURER :</b> {device['manufacturer']}
<b>BRAND :</b> {device['brand']}
<b>ANDROID VERSION :</b> {device['android_version']}
<b>SDK :</b> {device['sdk']}

<b>END ARGUMENT</b>"""
        
        return formatted
    
    def test_connection(self):
        """Test if bot can connect"""
        print("🔍 Testing bot connection...")
        url = f"{self.base_url}getMe"
        try:
            response = requests.get(url, timeout=10)
            result = response.json()
            if result.get("ok"):
                bot_name = result["result"]["first_name"]
                print(f"✅ Connected to bot: {bot_name}")
                return True
            else:
                print("❌ Bot connection failed")
                return False
        except Exception as e:
            print(f"❌ Connection error: {e}")
            return False
    
    def start_sending(self):
        """Start automated sending"""
        print("🚀 Starting TOKEN BABA 2.0 Bot")
        print("🎯 FIXED FEATURES:")
        print("   • Only 2 copy features: RECIPIENT number & MESSAGE")
        print("   • Consistent device info (manufacturer = brand)")
        print("   • Last 4 digits change every time")
        print("   • Hash parts change every time")
        
        # Test connection first
        if not self.test_connection():
            print("\n❌ Please check your configuration:")
            print("   1. BOT_TOKEN in config.py")
            print("   2. Internet connection")
            return
        
        print(f"⏰ Sending every {SEND_INTERVAL} seconds")
        print("⏹️  Press Ctrl+C to stop\n")
        
        try:
            while True:
                # Generate new random data
                random_data = self.generator.generate_complete_data()
                
                # Format with bold section
                formatted_message = self.format_message(random_data)
                
                # Send to Telegram
                result = self.send_message(formatted_message)
                
                if result and result.get("ok"):
                    self.message_count += 1
                    print(f"✅ [{self.message_count}] Sent successfully!")
                    print(f"   📞 Number: {random_data['recipient']}")
                    print(f"   📱 Device: {random_data['device_info']['model']}")
                    print(f"   🏭 Manufacturer: {random_data['device_info']['manufacturer']}")
                    print(f"   🏷️ Brand: {random_data['device_info']['brand']}")
                    print()
                else:
                    error_msg = result.get('description', 'Unknown error') if result else 'Connection failed'
                    print(f"❌ Send failed: {error_msg}")
                    break
                
                # Wait for next interval
                time.sleep(SEND_INTERVAL)
                
        except KeyboardInterrupt:
            print(f"\n🛑 Bot stopped. Total messages sent: {self.message_count}")
        except Exception as e:
            print(f"💥 Error: {e}")

def main():
    # Check if configuration is updated
    if BOT_TOKEN == "YOUR_ACTUAL_BOT_TOKEN_HERE" or CHANNEL_ID == "@YOUR_ACTUAL_CHANNEL":
        print("❌ CONFIGURATION REQUIRED")
        print("\n📝 Please update config.py with your actual details:")
        print("   1. BOT_TOKEN - Get from @BotFather on Telegram")
        print("   2. CHANNEL_ID - Your channel username")
        return
    
    # Start the bot
    bot = FixedTokenBot(BOT_TOKEN, CHANNEL_ID)
    bot.start_sending()

if __name__ == "__main__":
    main()