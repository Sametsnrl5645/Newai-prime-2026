import flet as ft

async def main(page: ft.Page):
    # 🔱 SİSTEM KİMLİĞİ VE SAYFA AYARLARI
    page.title = "Newai Prime"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0b0014" 
    page.padding = 0
    page.spacing = 0
    
    # Ekranın tam ortasına her şeyi kilitleyen ana kapsayıcı
    def create_input(hint, is_pass=False):
        return ft.Container(
            width=320,
            height=50,
            content=ft.TextField(
                hint_text=hint,
                password=is_pass,
                border_radius=25,
                border_color="#d500f9",
                bgcolor="#1a1225",
                content_padding=15,
                hint_style=ft.TextStyle(color="#888888"),
                cursor_color="cyan",
            )
        )

    # 🔱 AKILLI BUTON TASARIMI (SABİT)
    def action_button(text, colors):
        return ft.Container(
            content=ft.Text(text, size=16, weight="bold", color="white"),
            alignment=ft.alignment.center,
            width=320,
            height=55,
            border_radius=25,
            gradient=ft.LinearGradient(begin=ft.alignment.center_left, end=ft.alignment.center_right, colors=colors),
            on_click=lambda _: print(f"{text} tetiklendi"),
            animate=ft.animation.Animation(300, "decelerate"),
        )

    # 🔱 ARAYÜZÜN MERKEZİNE KİLİTLENMİŞ YAPI
    layout = ft.Container(
        expand=True,
        alignment=ft.alignment.center,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
            controls=[
                # Logo ve Başlık
                ft.Icon(ft.icons.AUTO_AWESOME_MOTION, color="cyan", size=60),
                ft.Text("NEWAI PRIME", size=32, weight="bold", color="white", letter_spacing=2),
                ft.Divider(height=20, color="transparent"),
                
                # Giriş Alanları
                create_input("Ad Soyad"),
                create_input("Email"),
                create_input("Şifre", True),
                
                ft.Divider(height=10, color="transparent"),
                
                # Sabit Duran Butonlar
                action_button("GİRİŞ YAP", ["#00d4ff", "#d500f9"]),
                action_button("ÜYE OL", ["#00f2fe", "#fff000"]),
                
                ft.TextButton("Şifremi Unuttum?", style=ft.ButtonStyle(color="cyan")),
            ]
        )
    )

    await page.add_async(layout)

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.FLET_APP)
    login_btn = ft.Container(
        content=ft.Text("Giriş Yap", size=18, weight="bold", color="white"),
        alignment=ft.alignment.center,
        width=300,
        height=55,
        border_radius=30,
        gradient=ft.LinearGradient(
            begin=ft.alignment.center_left,
            end=ft.alignment.center_right,
            colors=["#00d4ff", "#d500f9"], # Mavi - Mor gradyan
        ),
        on_click=lambda _: print("Giriş yapılıyor...")
    )

    register_btn = ft.Container(
        content=ft.Text("Üye Ol", size=18, weight="bold", color="black"),
        alignment=ft.alignment.center,
        width=300,
        height=55,
        border_radius=30,
        gradient=ft.LinearGradient(
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
