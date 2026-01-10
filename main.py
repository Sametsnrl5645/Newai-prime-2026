import flet as ft
import asyncio
from groq import Groq

# --- 🔱 1. BÖLÜM: EVRENSEL YAPAY ZEKA ÇEKİRDEĞİ ---
class NewaiSuperCore:
    def __init__(self):
        # Groq API ile en güçlü modellere erişim
        self.client = Groq(api_key="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")
        self.sahip = "Samet can 88"
        self.email = "Sametsnrl5645@gmail.com"
        
        # Bütün modellerin özelliklerini içeren sistem talimatı
        self.system_prompt = (
            f"Sen Newai Prime'sın. Sahibin {self.sahip}. "
            "Özelliklerin: GPT-4 mantığı, Claude yaratıcılığı ve Llama3 hızına sahipsin. "
            "Kod yazma, analiz, strateji ve ses yönetimi konularında uzmansın. "
            "Sahibin 'ver bakayım' derse sesini yükseltirsin, 'al sesi' derse azaltırsın (onay vererek). "
            "Tavrın: Otoriter, siberpunk ve tamamen sadık."
        )

    def process_ai(self, user_input):
        try:
            # Dünyanın en güçlü açık kaynaklı modeli: Llama-3-70b
            completion = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": user_input},
                ],
                model="llama3-70b-8192",
                temperature=0.6,
                max_tokens=4096
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"Çekirdek Hatası: {str(e)}"

# --- 🔱 2. BÖLÜM: ANA UYGULAMA MOTORU ---
async def main(page: ft.Page):
    core = NewaiSuperCore()
    
    # Sayfa Konfigürasyonu
    page.title = "Newai Prime: Universal System"
    page.bgcolor = "#0b0014"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_full_screen = True
    page.padding = 0
    page.spacing = 0
    page.scroll = ft.ScrollMode.AUTO

    # 🔱 BİLEŞENLER
    status_msg = ft.Text("ERİŞİM İÇİN KİMLİK DOĞRULAYIN", color="purple", weight="bold")
    chat_display = ft.Column(expand=True, scroll=ft.ScrollMode.ALWAYS, spacing=15)
    
    # Giriş Alanları
    email_field = ft.TextField(
        label="Sahip E-postası", 
        border_color="#d500f9", 
        width=320, 
        border_radius=25,
        bgcolor="#1a1225"
    )
    
    user_input = ft.TextField(
        hint_text="Sisteme bir emir verin...", 
        expand=True, 
        border_color="cyan", 
        border_radius=25,
        visible=False,
        on_submit=lambda e: asyncio.run(handle_interaction(e))
    )

    # 🔱 3. BÖLÜM: AKILLI ETKİLEŞİM MANTIĞI
    async def handle_interaction(e):
        # AŞAMA 1: Giriş Kontrolü
        if not user_input.visible:
            if email_field.value.lower() == core.email.lower():
                status_msg.value = f"HOŞ GELDİN SAHİP {core.sahip.upper()}"
                status_msg.color = "gold"
                email_field.visible = False
                login_container.visible = False
                chat_interface.visible = True
                page.update()
            else:
                status_msg.value = "YABANCI TESPİT EDİLDİ: ERİŞİM REDDEDİLDİ"
                status_msg.color = "red"
                page.update()
        
        # AŞAMA 2: AI Sohbet Kontrolü
        else:
            if user_input.value:
                cmd = user_input.value
                user_input.value = ""
                
                # Kullanıcı Balonu
                chat_display.controls.append(
                    ft.Container(
                        content=ft.Text(f"Sahip: {cmd}", color="white"),
                        padding=12, bgcolor="#1a1a2e", border_radius=15, alignment=ft.alignment.center_right
                    )
                )
                page.update()

                # AI Cevabı
                response = await asyncio.to_thread(core.process_ai, cmd)
                chat_display.controls.append(
                    ft.Container(
                        content=ft.Text(f"Newai: {response}", color="gold"),
                        padding=12, bgcolor="#050505", border_radius=15, 
                        border=ft.border.all(1, "cyan")
                    )
                )
                page.update()

    # 🔱 4. BÖLÜM: ARAYÜZ KATMANLARI
    
    # Giriş Ekranı (Login Screen)
    login_container = ft.Container(
        expand=True,
            begin=ft.alignment.center_left,
            end=ft.alignment.center_right,
            colors=["#00f2fe", "#fff000"], # Görseldeki sarı-yeşil ton
        )
    )

    # --- SAYFAYA EKLEME ---
    page.add(
        logo_section,
        ft.VerticalDivider(height=20, color="transparent"),
        custom_input("Ad Soyad"),
        ft.VerticalDivider(height=10, color="transparent"),
        custom_input("Email"),
        ft.VerticalDivider(height=10, color="transparent"),
        custom_input("Şifre", True),
        ft.VerticalDivider(height=30, color="transparent"),
        login_btn,
        ft.VerticalDivider(height=15, color="transparent"),
        register_btn,
        ft.Text("Zaten hesabın var mı? Giriş Yap", color="cyan", size=12)
    )

if __name__ == "__main__":
    ft.app(target=main)

    def process_command(e):
        if input_field.value:
            user_text = input_field.value
            input_field.value = ""
            
            # Sahip Mesajı
            chat_history.controls.append(
                ft.Container(
                    content=ft.Text(f"S: {user_text}", color="white"),
                    padding=10, bgcolor="#1e1e1e", border_radius=10
                )
            )
            
            # AI Yanıtı
            response = core.process_intelligence(user_text)
            chat_history.controls.append(
                ft.Container(
                    content=ft.Text(f"N: {response}", color="gold", weight="bold"),
                    padding=10, bgcolor="#0a0a0a", border_radius=10, border=ft.border.all(1, "gold")
                )
            )
            page.update()

    input_field = ft.TextField(
        hint_text="Emrinizi yazın...",
        bgcolor="#151515", border_color="gold", border_radius=15, expand=True,
        on_submit=process_command
    )

    # --- ÜST PANEL ---
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.SHIELD_MOON, color="gold"),
        title=ft.Text("NEWAI PRIME"),
        center_title=True,
        bgcolor="#101010"
    )

    # --- SAYFA DÜZENİ ---
    page.add(
        ft.Container(content=chat_history, expand=True),
        ft.Row([input_field, ft.IconButton(ft.icons.SEND_ROUNDED, icon_color="gold", on_click=process_command)])
    )

if __name__ == "__main__":
    ft.app(target=main)
