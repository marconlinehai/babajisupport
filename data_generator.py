import random

class FixedDataGenerator:
    def __init__(self):
        self.setup_data()
        self.available_devices = self.devices.copy()
        random.shuffle(self.available_devices)  # randomize start order

    def setup_data(self):
        # Large and varied device list (A–Z coverage)
        self.devices = [
            # Samsung
            {"model": "SM-A146B", "manufacturer": "samsung", "brand": "samsung"},
            {"model": "SM-A235F", "manufacturer": "samsung", "brand": "samsung"},
            {"model": "SM-G998B", "manufacturer": "samsung", "brand": "samsung"},
            {"model": "SM-F936B", "manufacturer": "samsung", "brand": "samsung"},
            {"model": "SM-M536B", "manufacturer": "samsung", "brand": "samsung"},
            {"model": "SM-S901E", "manufacturer": "samsung", "brand": "samsung"},
            {"model": "SM-A556E", "manufacturer": "samsung", "brand": "samsung"},
            
            # Realme
            {"model": "RMX3081", "manufacturer": "realme", "brand": "realme"},
            {"model": "RMX2156", "manufacturer": "realme", "brand": "realme"},
            {"model": "RMX2185", "manufacturer": "realme", "brand": "realme"},
            {"model": "RMX2061", "manufacturer": "realme", "brand": "realme"},
            {"model": "RMX3381", "manufacturer": "realme", "brand": "realme"},
            {"model": "RMX3821", "manufacturer": "realme", "brand": "realme"},
            
            # Xiaomi / Redmi
            {"model": "M2010J19SI", "manufacturer": "xiaomi", "brand": "xiaomi"},
            {"model": "M2007J20CI", "manufacturer": "xiaomi", "brand": "xiaomi"},
            {"model": "22021211RI", "manufacturer": "xiaomi", "brand": "xiaomi"},
            {"model": "21091116UI", "manufacturer": "xiaomi", "brand": "xiaomi"},
            {"model": "Redmi Note 11", "manufacturer": "xiaomi", "brand": "redmi"},
            {"model": "Redmi Note 12", "manufacturer": "xiaomi", "brand": "redmi"},
            {"model": "Mi 11 Lite", "manufacturer": "xiaomi", "brand": "xiaomi"},
            {"model": "Poco X5", "manufacturer": "xiaomi", "brand": "poco"},
            
            # Oppo
            {"model": "CPH2385", "manufacturer": "oppo", "brand": "oppo"},
            {"model": "CPH2205", "manufacturer": "oppo", "brand": "oppo"},
            {"model": "CPH2211", "manufacturer": "oppo", "brand": "oppo"},
            {"model": "CPH2123", "manufacturer": "oppo", "brand": "oppo"},
            
            # OnePlus
            {"model": "2107113SG", "manufacturer": "oneplus", "brand": "oneplus"},
            {"model": "220333QAG", "manufacturer": "oneplus", "brand": "oneplus"},
            {"model": "21091116AG", "manufacturer": "oneplus", "brand": "oneplus"},
            {"model": "2201123G", "manufacturer": "oneplus", "brand": "oneplus"},
            {"model": "OnePlus 10R", "manufacturer": "oneplus", "brand": "oneplus"},
            {"model": "OnePlus Nord CE3", "manufacturer": "oneplus", "brand": "oneplus"},
            
            # Motorola
            {"model": "Moto G82", "manufacturer": "motorola", "brand": "motorola"},
            {"model": "Moto G72", "manufacturer": "motorola", "brand": "motorola"},
            {"model": "Moto Edge 40", "manufacturer": "motorola", "brand": "motorola"},
            {"model": "XT2175-2", "manufacturer": "motorola", "brand": "motorola"},
            
            # Vivo
            {"model": "Vivo 2006", "manufacturer": "vivo", "brand": "vivo"},
            {"model": "Vivo 2025", "manufacturer": "vivo", "brand": "vivo"},
            {"model": "Vivo 1919", "manufacturer": "vivo", "brand": "vivo"},
            {"model": "Vivo 2104", "manufacturer": "vivo", "brand": "vivo"},
            {"model": "Vivo Y36", "manufacturer": "vivo", "brand": "vivo"},
            
            # Nothing / Pixel / iQOO / Asus (added variety)
            {"model": "A059", "manufacturer": "Nothing", "brand": "Nothing"},
            {"model": "Pixel 7a", "manufacturer": "Google", "brand": "Pixel"},
            {"model": "iQOO Z9", "manufacturer": "iQOO", "brand": "iQOO"},
            {"model": "Asus ROG 8", "manufacturer": "asus", "brand": "asus"},
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