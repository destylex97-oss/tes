# ============================================================
# VARIABLES.RPY - Semua variabel game
# ============================================================

# -- Player --
default player_name = "Andi"
default energi = 100
default fitness = 0
default uang = 50

# -- Waktu --
default hari = 1
default waktu = 0  # 0=pagi, 1=siang, 2=sore, 3=malam, 4=tidur

# -- Karakter Unlock --
default sari_unlock = False
default mira_unlock = False
default dina_unlock = False

# -- SARI Stats (Kakak tiri - mature, teasing) --
default sari_love = 0       # 0-100 hubungan
default sari_lust = 0       # 0-100 nafsu
default sari_mood = "biasa" # biasa, senang, terangsang, marah
default sari_event_1 = False
default sari_event_2 = False
default sari_event_3 = False
default sari_h_scene_1 = False
default sari_h_scene_2 = False

# -- MIRA Stats (Teman kost - shy, cute) --
default mira_love = 0
default mira_lust = 0
default mira_mood = "biasa"
default mira_event_1 = False
default mira_event_2 = False
default mira_event_3 = False
default mira_h_scene_1 = False
default mira_h_scene_2 = False

# -- DINA Stats (Tetangga - bold, flirty) --
default dina_love = 0
default dina_lust = 0
default dina_mood = "biasa"
default dina_event_1 = False
default dina_event_2 = False
default dina_event_3 = False
default dina_h_scene_1 = False
default dina_h_scene_2 = False


# ============================================================
# FUNGSI HELPER
# ============================================================
init python:

    def reset_game():
        """Reset semua variabel ke default"""
        store.energi = 100
        store.fitness = 0
        store.uang = 50
        store.hari = 1
        store.waktu = 0
        store.sari_unlock = False
        store.mira_unlock = False
        store.dina_unlock = False
        store.sari_love = 0
        store.sari_lust = 0
        store.sari_mood = "biasa"
        store.mira_love = 0
        store.mira_lust = 0
        store.mira_mood = "biasa"
        store.dina_love = 0
        store.dina_lust = 0
        store.dina_mood = "biasa"

    def get_waktu_text():
        """Konversi angka waktu ke teks"""
        waktu_map = {
            0: "Pagi",
            1: "Siang",
            2: "Sore",
            3: "Malam",
            4: "Larut Malam"
        }
        return waktu_map.get(store.waktu, "???")

    def tambah_love(chara, jumlah):
        """Tambah love point karakter"""
        if chara == "sari":
            store.sari_love = min(store.sari_love + jumlah, 100)
        elif chara == "mira":
            store.mira_love = min(store.mira_love + jumlah, 100)
        elif chara == "dina":
            store.dina_love = min(store.dina_love + jumlah, 100)

    def tambah_lust(chara, jumlah):
        """Tambah lust point karakter"""
        if chara == "sari":
            store.sari_lust = min(store.sari_lust + jumlah, 100)
        elif chara == "mira":
            store.mira_lust = min(store.mira_lust + jumlah, 100)
        elif chara == "dina":
            store.dina_lust = min(store.dina_lust + jumlah, 100)

    def set_mood(chara, mood):
        """Set mood karakter"""
        if chara == "sari":
            store.sari_mood = mood
        elif chara == "mira":
            store.mira_mood = mood
        elif chara == "dina":
            store.dina_mood = mood

    def cek_love(chara):
        """Cek love level karakter"""
        if chara == "sari":
            return store.sari_love
        elif chara == "mira":
            return store.mira_love
        elif chara == "dina":
            return store.dina_love
        return 0

    def cek_lust(chara):
        """Cek lust level karakter"""
        if chara == "sari":
            return store.sari_lust
        elif chara == "mira":
            return store.mira_lust
        elif chara == "dina":
            return store.dina_lust
        return 0

    def maju_waktu():
        """Majukan waktu 1 step"""
        store.waktu += 1
