# ============================================================
# SCRIPT.RPY - Main Game File
# Game: Rumah Sandbox (Home Sandbox)
# Setting: Kamu tinggal serumah dengan cewek-cewek cantik
# ============================================================

# -- CHARACTERS --
define mc = Character("[player_name]", color="#3498db")
define s = Character("Sari", color="#e74c3c")      # Kakak tiri - mature, teasing
define m = Character("Mira", color="#f39c12")      # Teman kost - shy, cute
define d = Character("Dina", color="#9b59b6")      # Tetangga - bold, flirty

# -- IMAGES (placeholder - ganti dengan asset sendiri) --
# Taruh file gambar di game/images/bg/ dan game/images/characters/
# Ren'Py akan otomatis detect berdasarkan nama file

# image bg kamar = "bg/kamar.png"
# image bg dapur = "bg/dapur.png"
# image bg ruang_tamu = "bg/ruang_tamu.png"
# image bg kamar_mandi = "bg/kamar_mandi.png"
# image bg halaman = "bg/halaman.png"

# image sari normal = "characters/sari_normal.png"
# image sari senang = "characters/sari_senang.png"
# image sari malu = "characters/sari_malu.png"

# image mira normal = "characters/mira_normal.png"
# image mira senang = "characters/mira_senang.png"
# image mira malu = "characters/mira_malu.png"

# image dina normal = "characters/dina_normal.png"
# image dina senang = "characters/dina_senang.png"
# image dina malu = "characters/dina_malu.png"


# ============================================================
# GAME START
# ============================================================
label start:
    # Reset semua variabel
    $ reset_game()

    scene black with fade

    "Selamat datang di Rumah Sandbox..."
    "Kamu baru saja pindah ke sebuah rumah kost yang ternyata..."
    "...dihuni oleh 3 cewek cantik."

    $ player_name = renpy.input("Siapa namamu?", default="Andi")
    $ player_name = player_name.strip() or "Andi"

    mc "Oke, rumah baru... semoga betah."

    "Hari pertamamu dimulai..."

    jump sandbox_loop


# ============================================================
# SANDBOX LOOP - Inti gameplay
# ============================================================
label sandbox_loop:
    # Cek apakah hari sudah berakhir
    if waktu >= 4:
        jump tidur

    # Tampilkan info waktu
    $ waktu_text = get_waktu_text()

    # Menu utama sandbox
    call screen sandbox_menu

    return


# ============================================================
# NAVIGASI RUANGAN
# ============================================================
label goto_kamar:
    scene black with dissolve
    # scene bg kamar with dissolve  # uncomment kalau sudah ada gambar
    "Kamu di kamar sendiri."

    menu:
        "Apa yang mau kamu lakukan?"

        "Istirahat (Pulihkan energi)" if energi < 100:
            $ energi = min(energi + 30, 100)
            "Kamu istirahat sebentar. Energi pulih."
            jump sandbox_loop

        "Cek HP":
            jump cek_hp

        "Keluar kamar":
            jump sandbox_loop


label goto_dapur:
    scene black with dissolve
    # scene bg dapur with dissolve
    "Kamu di dapur."

    # Random encounter
    $ siapa_di_dapur = renpy.random.choice(["sari", "mira", "dina", "kosong"])

    if siapa_di_dapur == "sari" and sari_unlock:
        jump dapur_sari
    elif siapa_di_dapur == "mira" and mira_unlock:
        jump dapur_mira
    elif siapa_di_dapur == "dina" and dina_unlock:
        jump dapur_dina
    else:
        "Dapur kosong. Kamu bikin kopi sendiri."
        $ energi = min(energi + 10, 100)
        jump sandbox_loop


label goto_ruang_tamu:
    scene black with dissolve
    # scene bg ruang_tamu with dissolve
    "Kamu di ruang tamu."

    $ siapa_di_tamu = renpy.random.choice(["sari", "mira", "dina", "kosong"])

    if siapa_di_tamu == "sari" and sari_unlock:
        jump tamu_sari
    elif siapa_di_tamu == "mira" and mira_unlock:
        jump tamu_mira
    elif siapa_di_tamu == "dina" and dina_unlock:
        jump tamu_dina
    else:
        "Ruang tamu sepi. Kamu nonton TV sebentar."
        jump sandbox_loop


label goto_kamar_mandi:
    scene black with dissolve
    # scene bg kamar_mandi with dissolve
    "Kamu di depan kamar mandi."

    # Chance event - ada yang lagi mandi
    $ mandi_event = renpy.random.randint(1, 100)

    if mandi_event <= 20 and hari >= 3:
        jump kamar_mandi_event
    else:
        "Kamu mandi dengan tenang."
        $ energi = min(energi + 15, 100)
        jump sandbox_loop


label goto_halaman:
    scene black with dissolve
    # scene bg halaman with dissolve
    "Kamu di halaman rumah."

    menu:
        "Apa yang mau kamu lakukan?"

        "Olahraga (Butuh energi -20)" if energi >= 20:
            $ energi -= 20
            $ fitness += 1
            "Kamu push up dan jogging kecil. Badan makin fit!"
            if fitness >= 5:
                "Badanmu makin keliatan bagus..."
            jump sandbox_loop

        "Duduk santai":
            "Kamu duduk di teras, menikmati angin."
            $ siapa_lewat = renpy.random.choice(["sari", "mira", "dina", "kosong"])
            if siapa_lewat == "dina":
                jump halaman_dina
            else:
                jump sandbox_loop

        "Kembali ke dalam":
            jump sandbox_loop


# ============================================================
# SISTEM TIDUR / GANTI HARI
# ============================================================
label tidur:
    scene black with fade
    "Hari sudah malam. Waktunya tidur..."

    $ hari += 1
    $ waktu = 0
    $ energi = min(energi + 50, 100)

    "--- Hari [hari] ---"

    # Unlock karakter berdasarkan hari
    if hari == 2 and not sari_unlock:
        $ sari_unlock = True
        "Pagi ini kamu bertemu Sari di dapur untuk pertama kalinya."
        s "Oh, kamu anak baru ya? Aku Sari, kakak tingkat di sini~"
        mc "Salam kenal, kak Sari."
        s "Jangan panggil kak, bikin tua aja. Hehe~"

    elif hari == 3 and not mira_unlock:
        $ mira_unlock = True
        "Kamu mendengar suara dari kamar sebelah..."
        m "A-ah... maaf, aku berisik ya? Aku Mira..."
        mc "Nggak kok. Salam kenal, Mira."
        m "S-salam kenal juga..."

    elif hari == 5 and not dina_unlock:
        $ dina_unlock = True
        "Ada yang mengetuk pintu pagi-pagi..."
        d "Halo~ tetangga baru kan? Aku Dina dari sebelah."
        d "Kalau butuh apa-apa, tinggal ketuk aja ya~"
        mc "(Cantik banget...)"

    jump sandbox_loop


# ============================================================
# CEK HP (Status & Hubungan)
# ============================================================
label cek_hp:
    "=== STATUS ==="
    "Hari: [hari] | Waktu: [waktu_text]"
    "Energi: [energi]/100"
    "Fitness: [fitness]"
    ""
    "=== HUBUNGAN ==="
    if sari_unlock:
        "Sari: [sari_love]/100 ([sari_mood])"
    if mira_unlock:
        "Mira: [mira_love]/100 ([mira_mood])"
    if dina_unlock:
        "Dina: [dina_love]/100 ([dina_mood])"

    jump sandbox_loop
