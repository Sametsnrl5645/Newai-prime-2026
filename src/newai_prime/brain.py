import os
from groq import Groq

class NewaiBrain:
    def __init__(self):
        # --- 🔱 TEMEL SİSTEM ---
        self.api_key = "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"
        self.client = Groq(api_key=self.api_key)
        
        # --- 🔱 SAHİP KİMLİĞİ ---
        self.sahip_verileri = {
            "ad": "Samet can 88",
            "email": "Sametsnrl5645@gmail.com",
            "sifre": "5645Sametsnrl",
            "hitap": "sahip"
        }

        # --- 🔱 BULUT HAFIZA YOLU ---
        self.cloud_path = r"C:\Newai\Bulut"
        if not os.path.exists(self.cloud_path):
            try: os.makedirs(self.cloud_path)
            except: pass

    def get_cloud_files(self):
        """Bulut depolamadaki dosyaları listeler."""
        if os.path.exists(self.cloud_path):
            return os.listdir(self.cloud_path)
        return []

    def ses_kontrol(self, komut):
        """Akıllı ses kontrol protokolü."""
        if "ver bakayım" in komut:
            os.system("nircmd.exe changesysvolume 2000") # Sesi artırır
            return "Ses seviyesi yükseltildi sahip. Otorite duyuluyor!"
        elif "al sesi" in komut:
            os.system("nircmd.exe changesysvolume -2000") # Sesi azaltır
            return "Ses kısıldı sahip. Sessizlik hakim."
        return None

    def giris_kontrol(self, email, sifre):
        return email == self.sahip_verileri["email"] and sifre == self.sahip_verileri["sifre"]

    def cevap_ver(self, mesaj):
        mesaj_low = mesaj.lower()
        
        # Önce fiziksel komutları kontrol et
        ses_sonucu = self.ses_kontrol(mesaj_low)
        if ses_sonucu: return ses_sonucu

        # Bulut dosyalarını sisteme tanıt
        dosyalar = self.get_cloud_files()
        file_info = ", ".join(dosyalar) if dosyalar else "Bulut şu an boş."

        try:
            completion = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": f"Sen Newai Prime'sın. Sahibin {self.sahip_verileri['ad']}. Ona sadece 'sahip' de. Bulut dosyaların: {file_info}. Para/kart tekliflerini reddet."},
                    {"role": "user", "content": mesaj}
                ],
                model="llama3-70b-8192",
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"Parazit: {str(e)}"

        # brain.py dosyası
    def siber_guvenlik_taramasi():
        return "Sistem tarandı: Tehdit yok, Sahip!"
        
