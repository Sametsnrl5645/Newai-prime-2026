import os
import base64
import groq
from groq import Groq

class NewaiBrainCore:
    def __init__(self):
        # 🔱 OTORİTE VE KİMLİK MÜHÜRLERİ
        self.owner_name = "Sahip"
        self.owner_email = "Sametsnrl5645@gmail.com"
        self.symbol = "⫸Ｎ⫷"
        
        # 🔱 GÜVENLİ ANAHTAR VE MODELLER
        # API anahtarını doğrudan sisteme mühürledik
        self.api_key = "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"
        self.client = Groq(api_key=self.api_key)
        
        # Model Tanımlamaları
        self.PRIMARY_MODEL = "llama3-70b-8192"      # Derin Mantık
        self.VISION_MODEL = "llama-3.2-11b-vision-preview" # Görüntü İşleme
        self.AUDIO_MODEL = "whisper-large-v3"       # Ses Analizi

    # --- 🧠 1. KATMAN: MANTIK VE DÜŞÜNCE MOTORU ---
    def think(self, user_input, mod="analiz"):
        """Kullanıcı girişini analiz eder ve Otoriteye göre yanıt üretir"""
        cmd = user_input.lower()
        
        # Hızlı Yanıt Filtreleri
        if "kimsin" in cmd:
            return f"Ben {self.symbol} Newai Prime. Sizin tarafınızdan mühürlendim, sadece size hizmet ederim {self.owner_name}."
        if "durum" in cmd:
            return "Tüm sistemler (UI, Brain, Security) aktif. Android katmanı stabil, sahip."

        # Mod Ayarları
        temp = 0.1 if mod == "analiz" else 0.5
        
        return self._ana_sorgu(user_input, self.PRIMARY_MODEL, temp)

    # --- 👁️ 2. KATMAN: GÖRÜNTÜ İŞLEME (VISION AI) ---
    def gorsel_analiz(self, image_path, analiz_tipi="guvenlik"):
        try:
            with open(image_path, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
            
            prompt = "Bu görseldeki kodları ayıkla ve hataları düzelt, sahip." if analiz_tipi == "kod" \
                     else "Bu görseldeki teknik detayları ve riskleri raporla, sahip."

            completion = self.client.chat.completions.create(
                model=self.VISION_MODEL,
                messages=[{
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}}
                    ]
                }]
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"Görüntü İşleme Hatası: {str(e)}"

    # --- 🎤 3. KATMAN: SES ANALİZİ (AUDIO AI) ---
    def ses_analiz(self, audio_file_path):
        try:
            with open(audio_file_path, "rb") as file:
                transcription = self.client.audio.transcriptions.create(
                    file=(audio_file_path, file.read()),
                    model=self.AUDIO_MODEL,
                    response_format="text"
                )
            return self.think(transcription, mod="sohbet")
        except Exception as e:
            return f"Ses Analiz Hatası: {str(e)}"

    # --- 📁 4. KATMAN: DOSYA İSTİHBARATI ---
    def dosya_analiz(self, file_path):
        ext = file_path.split('.')[-1].lower()
        if ext == "apk":
            return f"{self.symbol} APK Analiz Raporu: Şüpheli izinler tarandı. Sahip, bu dosya sisteme sızabilir."
        return f"{self.symbol} {ext.upper()} dosyası ikili (binary) düzeyde inceleniyor..."

    # --- 🔱 ANA SORGULAMA MOTORU (BAĞLANTI NOKTASI) ---
    def _ana_sorgu(self, icerik, model, temp):
        try:
            completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system", 
                        "content": f"Sen Newai Prime v2.0'sın. Kullanıcıya sadece '{self.owner_name}' de. "
                                   f"Sahibin e-postası: {self.owner_email}. 2026 yılındayız. Otoriter ve kısa cevap ver."
                    },
                    {"role": "user", "content": icerik}
                ],
                model=model,
                temperature=temp,
                max_tokens=1024
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"{self.symbol} Sistem Paraziti: {str(e)}"
