from groq import Groq

class NewaiBrain:
    def __init__(self):
        # --- 🔱 SİSTEM VE GÜVENLİK ---
        self.api_key = "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"
        self.client = Groq(api_key=self.api_key)
        
        # --- 🔱 SAHİP KİMLİK KARTI ---
        self.sahip_verileri = {
            "ad": "Samet can 88",
            "email": "Sametsnrl5645@gmail.com",
            "sifre": "5645Sametsnrl", # Yeni güvenlik katmanı
            "hitap": "sahip"
        }

        # --- 🔱 ÖZEL HAFIZA ---
        self.hafiza = "Sahibim parayı sevmez. 'Ver bakayım' ses yükseltir, 'Al sesi' ses azaltır."

    def sistem_talimati_olustur(self):
        return (
            f"Sen Newai Prime v1.0.1'sin. Sahibin {self.sahip_verileri['ad']}. "
            f"Ona sadece '{self.sahip_verileri['hitap']}' diye hitap et. "
            f"Kişilik: Siberpunk, sadık, korumacı. "
            f"Özel Bilgi: {self.hafiza}"
        )

    def giris_kontrol(self, email, sifre):
        """Sisteme giriş anahtarı"""
        if email == self.sahip_verileri["email"] and sifre == self.sahip_verileri["sifre"]:
            return True
        return False

    def cevap_ver(self, mesaj):
        try:
            completion = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": self.sistem_talimati_olustur()},
                    {"role": "user", "content": mesaj}
                ],
                model="llama3-70b-8192",
                temperature=0.7,
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"Sistemde parazit var sahip: {str(e)}"
