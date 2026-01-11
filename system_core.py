import os
import time

class SystemCore:
    def __init__(self):
        self.cloud_path = r"C:\Newai\Bulut"
        if not os.path.exists(self.cloud_path):
            os.makedirs(self.cloud_path)

    def get_cloud_files(self):
        return os.listdir(self.cloud_path) if os.path.exists(self.cloud_path) else []

    def ses_yönetimi(self, mesaj):
        """app.py içindeki akıllı ses kontrolü"""
        mesaj = mesaj.lower()
        if "ver bakayım" in mesaj:
            os.system("nircmd.exe changesysvolume 2000")
            return "Ses %2 artırıldı Sahip. Otorite yükseliyor."
        elif "al sesi" in mesaj:
            os.system("nircmd.exe changesysvolume -2620")
            return "Ses seviyesi düşürüldü Sahip."
        return None

    def guvenlik_kalkani_testi(self, dosya_adi):
        """Newai_Eternal_Security_Shield.py içindeki test özelliği"""
        # Burada simülasyon yapıyoruz
        time.sleep(1)
        return f"🛡️ {dosya_adi} için güvenlik taraması tamamlandı."
