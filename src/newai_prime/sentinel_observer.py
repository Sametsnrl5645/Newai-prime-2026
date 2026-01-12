import subprocess
import sys
import os
import requests

class SentinelObserver:
    def __init__(self, file_list, page=None):
        self.file_list = file_list
        self.page = page # Bildirimler için page objesi
        self.backup_url = "https://raw.githubusercontent.com/Sametsnrl5645/Newai-Prime-2026/main/"
        self.symbol = "⫸Ｎ⫷"

    def full_system_check(self):
        """Kütüphaneleri ve dosyaları sırayla onarır."""
        self._resolve_dependencies()
        self._scan_and_fix_files()

    def _resolve_dependencies(self):
        """Eksik kütüphaneleri (flet, requests vb.) otomatik yükler."""
        required = ["flet", "requests"]
        for lib in required:
            try:
                __import__(lib)
            except ImportError:
                print(f"{self.symbol} {lib} eksik! Akıllı Çözücü yükleme başlatıyor...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
                self.show_repair_toast(f"{lib} Kütüphanesi Onarıldı")

    def _scan_and_fix_files(self):
        """Dosyaları denetler ve bozuk olanları GitHub'dan çeker."""
        for file in self.file_list:
            if not os.path.exists(file) or os.path.getsize(file) == 0:
                print(f"{self.symbol} {file} bozuk veya kayıp! Onarılıyor...")
                self._recover_from_cloud(file)
                self.show_repair_toast(f"{file} Dosyası Onarıldı")

    def _recover_from_cloud(self, file_path):
        try:
            r = requests.get(self.backup_url + file_path)
            if r.status_code == 200:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(r.text)
        except: pass

    def show_repair_toast(self, message):
        """Ekranın köşesinde mühürlü onarım bildirimi çıkarır."""
        if self.page:
            self.page.snack_bar = ft.SnackBar(
                content=ft.Text(f"{self.symbol} {message}", color="white"),
                bgcolor="#B8860B", # Altın/Kahve tonu
                duration=3000
            )
            self.page.snack_bar.open = True
            self.page.update()
