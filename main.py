import flet as ft
import asyncio
from groq import Groq

# --- 🔱 1. BÖLÜM: EVRENSEL YAPAY ZEKA ÇEKİRDEĞİ ---
class NewaiSuperCore:
    def __init__(self):
        self.client = Groq(api_key="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")
        self.sahip = "Samet can 88"
        self.email = "Sametsnrl5645@gmail.com"
        self.system_prompt = (
            f"Sen Newai Prime'sın. Sahibin {self.sahip}. "
            "GPT-4, Claude ve Llama3 yeteneklerine sahipsin. Siberpunk bir asistansın."
        )

    def process_ai(self, user_input):
        try:
            completion = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": user_input},
                ],
                model="llama3-70b-8192",
                temperature=0.6,
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"Çekirdek Hatası: {str(e)}"

# --- 🔱 2. BÖLÜM: ANA UYGULAMA MOTORU ---
async def main(page: ft.Page):
    core = NewaiSuperCore()
    
    page.title = "Newai Prime v2.0.1"
    page.bgcolor = "#0b0014"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.AUTO

    # Bileşenler
    chat_display = ft.Column(spacing=15, scroll=ft.ScrollMode.ALWAYS, expand=True)
    status_msg = ft.Text("SİSTEM KİLİTLİ: KİMLİK DOĞRULAYIN", color="purple", weight="bold")

    async def handle_action(e):
        if login_container.visible:
            if email_field.value.lower() == core.email.lower():
                login_container.visible = False
                chat_interface.visible = True
                status_msg.value = f"SİSTEM AKTİF: HOŞ GELDİN SAHİP"
                page.update()
            else:
                status_msg.value = "ERİŞİM REDDEDİLDİ!"
                status_msg.color = "red"
                page.update()
        
        elif chat_input.value:
            user_msg = chat_input.value
            chat_input.value = ""
            chat_display.controls.append(
                ft.Container(content=ft.Text(f"S: {user_msg}", color="white"), 
                             padding=10, bgcolor="#1a1a2e", border_radius=15)
            )
            page.update()

            response = await asyncio.to_thread(core.process_ai, user_msg)
            chat_display.controls.append(
                ft.Container(content=ft.Text(f"N: {response}", color="gold"), 
                             padding=10, bgcolor="#050505", border_radius=15, border=ft.border.all(1, "cyan"))
            )
            page.update()

    # --- ARAYÜZ KATMANLARI ---
    email_field = ft.TextField(label="Sahip Email", border_radius=25, border_color="#d500f9", width=320)
    
    login_container = ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Icon(ft.icons.SHIELD_MOON, color="cyan", size=100),
            ft.Text("NEWAI PRIME", size=35, weight="bold"),
            status_msg,
            email_field,
            ft.Container(
                content=ft.Text("SİSTEMİ BAŞLAT", weight="bold"),
                alignment=ft.alignment.center,
                width=320, height=55, border_radius=25,
                gradient=ft.LinearGradient(colors=["#00d4ff", "#d500f9"]),
                on_click=handle_action
            )
        ]
    )

    chat_input = ft.TextField(hint_text="Emriniz nedir?", expand=True, on_submit=handle_action)
    chat_interface = ft.Column(
        visible=False,
        expand=True,
        controls=[
            ft.Container(content=chat_display, height=500, padding=10),
            ft.Row([chat_input, ft.IconButton(ft.icons.SEND, icon_color="cyan", on_click=handle_action)])
        ]
    )

    page.add(
        ft.Container(
            content=ft.Column([login_container, chat_interface]),
            alignment=ft.alignment.center,
            expand=True
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
