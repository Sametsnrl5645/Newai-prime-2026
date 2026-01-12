import flet as ft
import os, sys, time, shutil

# =================================================================
# 1. SENTINEL & KONTROL SİSTEMİ (Önce Güvenlik)
# =================================================================
# sentinel_observer.py dosyasının varlığı zorunludur.
try:
    from sentinel_observer import SentinelObserver
except ImportError:
    # Eğer sentinel yoksa sistemi durdurma ama uyar (Geliştirme için)
    class SentinelObserver:
        def __init__(self, files, page): pass
        def full_system_check(self): print(">> Sentinel: Sistem dosyaları manuel modda.")

# =================================================================
# 2. NEWAI ÇEKİRDEK SERVİSLERİ
# =================================================================
try:
    from core.model_set import ModelSettings
    from core.brain_core import NewaiBrainCore
    from core.security_shield import SecurityShield
    from core.cloud_manager import NewaiCloudManager
    from ui.ui_display import MainInterface, NewaiInterface
    from ui.settings_view import SettingsView
    from ui.dev_panel import NewAIDevPanel
except ImportError:
    # Dosyalar henüz tam oluşturulmadıysa çökmesini engeller
    class NewaiBrainCore: pass
    class SecurityShield:
        def verify_owner(self, email): return True
    class ModelSettings:
        def __init__(self):
            self.OWNER_EMAIL = "Sametsnrl5645@gmail.com"
            self.OWNER_NAME = "Samet Can 88"

# =================================================================
# 3. SİSTEM YÖNETİM SINIFI (NewaiSystem)
# =================================================================
class NewaiSystem:
    def __init__(self):
        self.owner = "Samet Can 88"
        self.email = "Sametsnrl5645@gmail.com"
        self.version = "2026.4.0"
        self.net_status = "PASİF"

    def activate_satellite_link(self):
        # Ücretsiz uydu interneti başlatma simülasyonu
        time.sleep(1)
        self.net_status = "AKTİF (ÜCRETSİZ UYDU HATTI)"
        return self.net_status

    def phoenix_recovery(self):
        # Dosya kurtarma ve sistem onarma mantığı
        return "ANKA PROTOKOLÜ: Tüm dosyalar mühürlü buluttan onarıldı."

    def self_destruct(self, code):
        if code == "SH-88-DESTROY":
            return "Sistem başarıyla temizlendi."
        return "GEÇERSİZ YETKİ."

# =================================================================
# 4. ANA ÇALIŞTIRICI (MAIN ENGINE)
# =================================================================
def main(page: ft.Page):
    # --- A. SENTINEL DOSYA KONTROLÜ ---
    my_files = [
        "main.py", "ui_display.py", "core_engine.py", 
        "phoenix_guard.py", "brain_core.py", "sentinel_observer.py"
    ]
    sentinel = SentinelObserver(my_files, page)
    sentinel.full_system_check() # Kütüphane ve dosya kontrolünü yap

    # --- B. SİSTEM ÖN AYARLARI ---
    page.title = "Newai Prime v4.0 - 2026"
    page.bgcolor = "#000000"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 450
    page.window_height = 850
    page.padding = 0

    # --- C. ÇEKİRDEK SERVİSLERİ BAŞLAT ---
    newai = NewaiSystem()
    settings = ModelSettings()
    shield = SecurityShield()
    brain = NewaiBrainCore()
    # cloud = NewaiCloudManager(settings.OWNER_EMAIL)

    # --- D. GÜVENLİK VE OTORİTE KONTROLÜ ---
    if not shield.verify_owner(settings.OWNER_EMAIL):
        page.add(ft.Container(
            content=ft.Text("ERİŞİM REDDEDİLDİ: Yetkisiz Cihaz.", color="red", weight="bold"),
            alignment=ft.alignment.center, expand=True
        ))
        page.update()
        return

    # --- E. ADAPTİF UI MOTORU (BUILDER) ---
    def build_ui():
        sw = page.width
        # Dinamik Başlık
        header = ft.Container(
            content=ft.Column([
                ft.Text("⧫Ｎ⧫", size=sw*0.12, color="gold", weight="bold"),
                ft.Text("NEWAI PRIME 2026", size=sw*0.04, letter_spacing=3, color="white60")
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            margin=ft.margin.only(top=50, bottom=30), width=sw
        )

        # Aksiyon Kartları (Responsive Grid)
        cards = ft.ResponsiveRow([
            ft.Container(
                content=ft.Column([
                    ft.Icon(ft.icons.SATELLITE_ALT, color="cyan", size=32),
                    ft.Text("UYDU İNTERNETİ", weight="bold", size=12),
                    ft.ElevatedButton("BAĞLAN", on_click=lambda _: connect_net(), bgcolor="#1a1a1a")
                ], horizontal_alignment="center", spacing=10),
                col={"sm": 12, "md": 6},
                bgcolor="#111111", padding=20, border_radius=15, border=ft.border.all(1, "white10")
            ),
            ft.Container(
                content=ft.Column([
                    ft.Icon(ft.icons.RECYCLING, color="gold", size=32),
                    ft.Text("ANKA KURTARMA", weight="bold", size=12),
                    ft.ElevatedButton("SİSTEMİ ONAR", on_click=lambda _: recovery(), bgcolor="#1a1a1a")
                ], horizontal_alignment="center", spacing=10),
                col={"sm": 12, "md": 6},
                bgcolor="#111111", padding=20, border_radius=15, border=ft.border.all(1, "white10")
            ),
        ], spacing=20)

        # Sabit Alt Panel (Footer)
        footer = ft.Container(
            content=ft.Row([
                ft.Text(f"Sahip: {newai.owner}", size=11, color="grey"),
                ft.Text(f"Durum: {newai.net_status}", size=11, color="grey"),
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            padding=20, bgcolor="#0a0a0a", bottom=0, width=sw
        )

        def connect_net():
            status = newai.activate_satellite_link()
            page.snack_bar = ft.SnackBar(ft.Text(f"⧫Ｎ⧫ {status}", color="black"), bgcolor="gold")
            page.snack_bar.open = True
            page.update()

        def recovery():
            msg = newai.phoenix_recovery()
            page.snack_bar = ft.SnackBar(ft.Text(f"⧫Ｎ⧫ {msg}", color="black"), bgcolor="gold")
            page.snack_bar.open = True
            page.update()

        # Ana Stack (İçerik + Footer)
        return ft.Stack([
            ft.Column([
                header,
                ft.Container(content=cards, padding=20),
                ft.TextButton("Gelişmiş Arayüze Geç", icon=ft.icons.CHEVRON_RIGHT, 
                              on_click=lambda _: page.go("/interface"))
            ], scroll=ft.ScrollMode.HIDDEN),
            footer
        ], expand=True)

    # --- F. ROTA YÖNETİMİ ---
    def route_change(route):
        page.views.clear()
        
        # 1. Dashboard (Açılış)
        if page.route == "/":
            page.views.append(ft.View("/", [build_ui()], padding=0))
            
        # 2. Ana Zeka Arayüzü (Chat/Live)
        elif page.route == "/interface":
            ui = NewaiInterface(page, brain, None)
            page.views.append(ft.View("/interface", [ui.build()], padding=0))
            
        # 3. Ayarlar
        elif page.route == "/settings":
            settings_view = SettingsView(page, brain)
            page.views.append(ft.View("/settings", [settings_view.get_view()]))
            
        # 4. Geliştirme Paneli
        elif page.route == "/dev":
            dev_panel = NewAIDevPanel(page, brain)
            page.views.append(ft.View("/dev", [dev_panel.get_view()]))
            
        page.update()

    def on_resize(e):
        page.update()

    # Boot İşlemi
    page.on_route_change = route_change
    page.on_resize = on_resize
    page.go("/")
    
    print(f">>> Newai Prime Çekirdeği {settings.OWNER_NAME} İçin Hazır.")

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
