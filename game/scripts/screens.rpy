# ============================================================
# SCREENS.RPY - UI / Menu Sandbox
# ============================================================

# -- SANDBOX MENU (Menu utama navigasi) --
screen sandbox_menu():
    tag menu

    # Background overlay
    add Solid("#1a1a2e") alpha 0.8

    # Header info
    frame:
        xalign 0.5
        yalign 0.05
        padding (20, 10)
        background Solid("#16213e")

        hbox:
            spacing 30
            text "Hari [hari]" size 18 color "#ecf0f1"
            text "[waktu_text]" size 18 color "#f39c12"
            text "Energi: [energi]/100" size 18 color "#2ecc71"

    # Judul
    text "Mau kemana?" xalign 0.5 yalign 0.2 size 32 color "#ecf0f1"

    # Grid tombol lokasi
    vbox:
        xalign 0.5
        yalign 0.55
        spacing 15

        hbox:
            spacing 15
            xalign 0.5

            # Kamar
            textbutton "Kamarku":
                action [SetVariable("waktu", waktu + 1), Jump("goto_kamar")]
                style "lokasi_button"

            # Dapur
            textbutton "Dapur":
                action [SetVariable("waktu", waktu + 1), Jump("goto_dapur")]
                style "lokasi_button"

        hbox:
            spacing 15
            xalign 0.5

            # Ruang Tamu
            textbutton "Ruang Tamu":
                action [SetVariable("waktu", waktu + 1), Jump("goto_ruang_tamu")]
                style "lokasi_button"

            # Kamar Mandi
            textbutton "Kamar Mandi":
                action [SetVariable("waktu", waktu + 1), Jump("goto_kamar_mandi")]
                style "lokasi_button"

        hbox:
            spacing 15
            xalign 0.5

            # Halaman
            textbutton "Halaman":
                action [SetVariable("waktu", waktu + 1), Jump("goto_halaman")]
                style "lokasi_button"

            # Tidur (hanya malam)
            if waktu >= 3:
                textbutton "Tidur":
                    action Jump("tidur")
                    style "lokasi_button_sleep"

    # Footer - HP/Status button
    hbox:
        xalign 0.5
        yalign 0.9
        spacing 20

        textbutton "Status":
            action Jump("cek_hp")
            style "small_button"

        textbutton "Save":
            action ShowMenu("save")
            style "small_button"

        textbutton "Load":
            action ShowMenu("load")
            style "small_button"


# ============================================================
# STYLES
# ============================================================
style lokasi_button:
    background Solid("#2c3e50")
    hover_background Solid("#3498db")
    padding (30, 15)
    minimum (180, 50)

style lokasi_button_text:
    color "#ecf0f1"
    size 20
    xalign 0.5

style lokasi_button_sleep:
    background Solid("#8e44ad")
    hover_background Solid("#9b59b6")
    padding (30, 15)
    minimum (180, 50)

style lokasi_button_sleep_text:
    color "#ecf0f1"
    size 20
    xalign 0.5

style small_button:
    background Solid("#34495e")
    hover_background Solid("#5d6d7e")
    padding (15, 8)

style small_button_text:
    color "#bdc3c7"
    size 14
    xalign 0.5
