import flet as ft

def main(page: ft.Page):
    page.title = "Newai Prime"
    page.bgcolor = "#0b0014" # Görseldeki koyu mor/siyah ton
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 40

    # --- TASARIM BİLEŞENLERİ ---
    
    # Newai Logo ve Halka (Görselin üst kısmı)
    logo_section = ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Icon(ft.icons.PENTAGON_OUTLINED, color="purple", size=100),
            ft.Text("NewAI", size=45, weight="bold", color="white"),
        ]
    )

    # Giriş Alanları (Görseldeki gibi oval ve şeffafımsı)
    def custom_input(hint, is_password=False):
        return ft.TextField(
            hint_text=hint,
            password=is_password,
            can_reveal_password=is_password,
            bgcolor="#1a1225",
            border_radius=30,
            border_color="purple",
            focused_border_color="cyan",
            color="white",
            height=55
        )

    # Butonlar (Görseldeki gradyan efektine yakın)
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
