import random

class FixedDataGenerator:
    def __init__(self):
        self.setup_data()
        self.available_devices = self.devices.copy()
        random.shuffle(self.available_devices)  # randomize start order

    def setup_data(self):
        # Large and varied device list (A–Z coverage)
        self.devices = [

            # Oppo
            {"model": "CPH2385", "manufacturer": "oppo", "brand": "oppo"},
            {"model": "CPH2205", "manufacturer": "oppo", "brand": "oppo"},
            {"model": "CPH2211", "manufacturer": "oppo", "brand": "oppo"},
            {"model": "CPH2123", "manufacturer": "oppo", "brand": "oppo"},
            
            ]

    def generate_hash_part(self, length):
        """Generate random hexadecimal part"""
        chars = "abcdef0123456789"
        return ''.join(random.choices(chars, k=length))
    
    def generate_dynamic_hash(self):
        """Generate hash with changing parts"""
        part1 = "2eb0f9cc"
        part2 = self.generate_hash_part(4)
        part3 = self.generate_hash_part(4)
        part4 = self.generate_hash_part(4)
        part5 = self.generate_hash_part(11)
        return f"{part1}&{part2}&{part3}&{part4}&{part5}"
    
    def generate_phone_number(self):
        """Generate phone number with only last 4 digits changing"""
        from config import BASE_PHONE
        last_four = ''.join(random.choices("0123456789", k=4))
        return f"{BASE_PHONE}{last_four}"
    
    def generate_message_content(self):
        """Generate exact DO NOT COPY message format"""
        hash_value = self.generate_dynamic_hash()
        return f"DO NOT COPY, FORWARD or SHARE THIS MESSAGE under any circumstance. USE UPI PIN ONLY on UPI PIN page of the app <{hash_value}>"
    
    def get_next_device(self):
        """Get next unique device, reshuffle when list is empty"""
        if not self.available_devices:
            self.available_devices = self.devices.copy()
            random.shuffle(self.available_devices)
        return self.available_devices.pop()
    
    def generate_device_info(self):
        """Generate consistent device info"""
        device = self.get_next_device()
        return {
            "model": device["model"],
            "manufacturer": device["manufacturer"],
            "brand": device["brand"],
            "android_version": str(random.randint(11, 15)),
            "sdk": str(random.randint(30, 35))
        }
    
    def generate_complete_data(self):
        """Generate full dataset"""
        return {
            "recipient": self.generate_phone_number(),
            "message": self.generate_message_content(),
            "device_info": self.generate_device_info()
        }
