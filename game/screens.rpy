# ============================================================
# SCREENS.RPY — All Screens for "House of Influence"
# ============================================================

# --- MAIN MENU ---
screen main_menu():
    tag menu

    add "gui/mainmenu/menu_overlay.png"

    vbox:
        xalign 0.5
        yalign 0.3
        spacing 8
        text "HOUSE OF INFLUENCE" size 52 color "#D4A845" xalign 0.5 bold True
        text "v0.1.0" size 16 color "#8A8A8A" xalign 0.5

    vbox:
        xalign 0.5
        yalign 0.65
        spacing 14
        textbutton _("New Game") action Start() style "mmenu_btn"
        textbutton _("Continue") action ShowMenu("load") style "mmenu_btn"
        textbutton _("Gallery") action ShowMenu("gallery") style "mmenu_btn"
        textbutton _("Settings") action ShowMenu("preferences") style "mmenu_btn"
        textbutton _("Quit") action Quit(confirm=True) style "mmenu_btn"

style mmenu_btn:
    xsize 280
    ysize 50
    xalign 0.5
    background Solid("#1A1A2E")
    hover_background Solid("#3A3A5E")

style mmenu_btn_text:
    color "#E8E6E3"
    hover_color "#D4A845"
    size 22
    xalign 0.5
    yalign 0.5

# --- SAY / DIALOGUE ---
screen say(who, what):
    style_prefix "say"

    window id "window":
        if who is not None:
            window id "namebox" style "say_namebox":
                text who id "who" size gui.name_text_size color "#D4A845" bold True

        text what id "what" size gui.text_size color "#E8E6E3"

    use quick_menu

style say_window is default:
    background "gui/dialogue/dialogue_box.png"
    xsize 1820
    ysize gui.textbox_height
    xalign 0.5
    yalign 1.0
    padding (60, 60, 60, 30)

style say_namebox is default:
    background "gui/dialogue/name_plate.png"
    xpos gui.name_xpos
    ypos gui.name_ypos
    xsize gui.namebox_width
    ysize gui.namebox_height
    padding (15, 5, 15, 5)

# --- QUICK MENU ---
screen quick_menu():
    zorder 100
    hbox:
        xalign 0.95
        yalign 0.955
        spacing 12
        textbutton "Auto" action Preference("auto-forward", "toggle") style "qm_btn"
        textbutton "Skip" action Skip() alternate Skip(fast=True, confirm=True) style "qm_btn"
        textbutton "Log" action ShowMenu("history") style "qm_btn"
        textbutton "Save" action ShowMenu("save") style "qm_btn"

style qm_btn is default:
    background None

style qm_btn_text:
    color "#6A6A7A"
    hover_color "#D4A845"
    size 15

# --- CHOICE ---
screen choice(items):
    vbox:
        xalign 0.5
        yalign 0.4
        spacing 12
        for i in items:
            textbutton i.caption action i.action style "ch_btn"

style ch_btn:
    xsize 700
    ysize 55
    xalign 0.5
    background "gui/choices/choice_neutral.png"
    hover_background "gui/choices/choice_neutral_hover.png"

style ch_btn_text:
    color "#E8E6E3"
    hover_color "#D4A845"
    size 20
    xalign 0.5
    yalign 0.5

# --- SAVE / LOAD ---
screen save():
    tag menu
    use file_slots(_("Save"))

screen load():
    tag menu
    use file_slots(_("Load"))

screen file_slots(title):
    add Solid("#000000CC")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1100
        ysize 650
        background Solid("#1A1A2E")
        padding (40, 30)

        vbox:
            spacing 20
            hbox:
                text title size 26 color "#D4A845" bold True
                null width 700
                textbutton "Close" action Return() text_color "#8A8A8A" text_hover_color "#D4A845"

            hbox:
                spacing 8
                for pg in range(1, 6):
                    textbutton str(pg) action FilePage(pg) style "pg_tab"

            grid 3 2:
                xalign 0.5
                spacing 20
                for i in range(6):
                    $ slot = i + 1
                    button:
                        action FileAction(slot)
                        xsize 300
                        ysize 180
                        background Solid("#0D0D0F")
                        hover_background Solid("#2A2A3E")
                        padding (10, 10)
                        vbox:
                            spacing 5
                            add FileScreenshot(slot) xsize 280 ysize 130
                            text FileTime(slot, format=_("%b %d %H:%M"), empty=_("Empty")) size 13 color "#8A8A8A"

style pg_tab:
    xsize 60
    ysize 30
    background Solid("#0D0D0F")
    hover_background Solid("#2A2A3E")

style pg_tab_text:
    color "#8A8A8A"
    hover_color "#D4A845"
    selected_color "#D4A845"
    size 14
    xalign 0.5
    yalign 0.5

# --- PREFERENCES ---
screen preferences():
    tag menu

    add Solid("#000000CC")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 800
        ysize 550
        background Solid("#1A1A2E")
        padding (40, 30)

        vbox:
            spacing 20
            hbox:
                text "Settings" size 26 color "#D4A845" bold True
                null width 480
                textbutton "Close" action Return() text_color "#8A8A8A" text_hover_color "#D4A845"

            vbox:
                spacing 12
                text "Audio" size 18 color "#D4A845"
                hbox:
                    spacing 20
                    text "Music" size 16 color "#E8E6E3" yalign 0.5 xsize 80
                    bar value Preference("music volume") xsize 300 ysize 16 left_bar Solid("#D4A845") right_bar Solid("#2A2A3E")
                hbox:
                    spacing 20
                    text "SFX" size 16 color "#E8E6E3" yalign 0.5 xsize 80
                    bar value Preference("sound volume") xsize 300 ysize 16 left_bar Solid("#D4A845") right_bar Solid("#2A2A3E")

            vbox:
                spacing 12
                text "Text" size 18 color "#D4A845"
                hbox:
                    spacing 20
                    text "Speed" size 16 color "#E8E6E3" yalign 0.5 xsize 80
                    bar value Preference("text speed") xsize 300 ysize 16 left_bar Solid("#2ECC71") right_bar Solid("#2A2A3E")
                hbox:
                    spacing 20
                    text "Auto" size 16 color "#E8E6E3" yalign 0.5 xsize 80
                    bar value Preference("auto-forward time") xsize 300 ysize 16 left_bar Solid("#D4789C") right_bar Solid("#2A2A3E")

            vbox:
                spacing 12
                text "Display" size 18 color "#D4A845"
                hbox:
                    spacing 15
                    textbutton "Windowed" action Preference("display", "any window") style "pg_tab"
                    textbutton "Fullscreen" action Preference("display", "fullscreen") style "pg_tab"

# --- PHONE ---
screen phone_screen():
    zorder 150
    modal True

    add Solid("#000000CC")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 380
        ysize 620
        background Solid("#111118")
        padding (30, 40)

        vbox:
            spacing 12
            xalign 0.5

            text "[time_text]" size 20 color "#E8E6E3" xalign 0.5
            text "Day [day]" size 14 color "#8A8A8A" xalign 0.5
            null height 15

            grid 3 3:
                xalign 0.5
                spacing 18
                use _phone_icon("Stats", "gui/phone/icons/icon_stats.png", Show("stats_screen"))
                use _phone_icon("Msgs", "gui/phone/icons/icon_messages.png", Show("messages_screen"))
                use _phone_icon("Cam", "gui/phone/icons/icon_camera.png", Show("camera_screen"))
                use _phone_icon("Shop", "gui/phone/icons/icon_shop.png", Show("shop_screen"))
                use _phone_icon("Diary", "gui/phone/icons/icon_diary.png", Show("diary_screen"))
                use _phone_icon("Set", "gui/phone/icons/icon_settings.png", ShowMenu("preferences"))
                use _phone_icon("Gallery", "gui/phone/icons/icon_gallery.png", ShowMenu("gallery"))
                use _phone_icon("Quest", "gui/phone/icons/icon_quests.png", Show("quests_screen"))
                use _phone_icon("Spy", "gui/phone/icons/icon_spy.png", Show("spy_tools_screen"))

            null height 15
            textbutton "Close" action Hide("phone_screen") xalign 0.5 text_color "#8A8A8A" text_hover_color "#D4A845"

screen _phone_icon(label, icon, act):
    vbox:
        spacing 3
        xsize 80
        imagebutton idle icon hover icon action act xalign 0.5
        text label size 11 color "#8A8A8A" xalign 0.5

# --- STATS ---
screen stats_screen():
    zorder 160
    modal True

    add Solid("#000000CC")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 750
        ysize 520
        background Solid("#1A1A2E")
        padding (30, 25)

        vbox:
            spacing 12
            hbox:
                text "Stats" size 24 color "#D4A845" bold True
                null width 500
                textbutton "X" action Hide("stats_screen") text_color "#8A8A8A" text_hover_color "#E74C3C"

            if marina_unlocked:
                use _stat_card("Marina", marina_affection, marina_corruption, marina_obedience, marina_desire, marina_suspicion, "#6B3FA0")
            if kaori_unlocked:
                use _stat_card("Kaori", kaori_affection, kaori_corruption, kaori_obedience, kaori_desire, kaori_suspicion, "#C17817")
            if yuki_unlocked:
                use _stat_card("Yuki", yuki_affection, yuki_corruption, yuki_obedience, yuki_desire, yuki_suspicion, "#D4789C")

screen _stat_card(name, aff, cor, obe, des, sus, col):
    frame:
        xfill True
        background Solid("#0D0D0F")
        padding (15, 10)
        vbox:
            spacing 5
            text name size 16 color col bold True
            grid 2 3:
                spacing 5
                xsize 320
                use _bar("Aff", aff, "#2ECC71")
                use _bar("Des", des, "#D4789C")
                use _bar("Cor", cor, "#6B3FA0")
                use _bar("Sus", sus, "#E74C3C")
                use _bar("Obe", obe, "#3498DB")
                null

screen _bar(label, val, col):
    hbox:
        spacing 6
        text label size 12 color "#8A8A8A" yalign 0.5 xsize 30
        bar value val range 100 xsize 100 ysize 10 left_bar Solid(col) right_bar Solid("#2A2A3E")
        text "[val]" size 12 color "#E8E6E3" yalign 0.5

# --- SANDBOX MAP ---
screen sandbox_map():
    zorder 120
    modal True

    add "gui/map/map_overlay_bg.png"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1200
        ysize 750
        background None
        padding (50, 30)

        vbox:
            spacing 15
            hbox:
                text "House Map" size 26 color "#D4A845" bold True
                null width 800
                textbutton "X" action Hide("sandbox_map") text_color "#8A8A8A" text_hover_color "#E74C3C"

            text "2F" size 14 color "#8A8A8A"
            hbox:
                spacing 15
                use _room("MC Room", "mc_room", True)
                use _room("Bath", "bathroom", True)
                use _room("Yuki", "yuki_room", yuki_unlocked)
                use _room("Kaori", "kaori_room", kaori_room_unlocked)
                use _room("Marina", "marina_room", marina_unlocked)

            add Solid("#D4A84530") xsize 1000 ysize 2 xalign 0.5

            text "1F" size 14 color "#8A8A8A"
            hbox:
                spacing 15
                use _room("Kitchen", "kitchen", True)
                use _room("Living", "living_room", True)
                use _room("Laundry", "laundry", True)
                use _room("Study", "study", True)
                use _room("Exit", "entrance", True)

screen _room(label, rid, ok):
    vbox:
        spacing 3
        if ok:
            imagebutton idle "gui/map/room_normal.png" hover "gui/map/room_hover.png" action [Hide("sandbox_map"), Jump("goto_" + rid)]
        else:
            imagebutton idle "gui/map/room_locked.png" action NullAction()
        text label size 12 color "#E8E6E3" xalign 0.5

# --- GALLERY (placeholder) ---
screen gallery():
    tag menu
    add Solid("#000000CC")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 800
        ysize 500
        background Solid("#1A1A2E")
        padding (30, 30)
        vbox:
            hbox:
                text "Gallery" size 24 color "#D4A845" bold True
                null width 500
                textbutton "Close" action Return() text_color "#8A8A8A" text_hover_color "#D4A845"
            null height 30
            text "Coming soon..." size 18 color "#8A8A8A" xalign 0.5

# --- HISTORY ---
screen history():
    tag menu
    add Solid("#000000CC")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 600
        background Solid("#1A1A2E")
        padding (30, 30)
        vbox:
            spacing 10
            hbox:
                text "History" size 24 color "#D4A845" bold True
                null width 550
                textbutton "Close" action Return() text_color "#8A8A8A" text_hover_color "#D4A845"
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                ysize 480
                vbox:
                    for h in _history_list:
                        vbox:
                            spacing 2
                            if h.who:
                                text h.who size 14 color "#D4A845"
                            text h.what size 16 color "#E8E6E3"
                        null height 8

# --- CONFIRM ---
screen confirm(message, yes_action, no_action):
    zorder 300
    modal True
    add Solid("#000000D0")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 450
        ysize 180
        background Solid("#1A1A2E")
        padding (30, 25)
        vbox:
            spacing 20
            text message size 18 color "#E8E6E3" xalign 0.5 text_align 0.5
            hbox:
                xalign 0.5
                spacing 30
                textbutton "Yes" action yes_action style "hud_nav_btn"
                textbutton "No" action no_action style "hud_nav_btn"

# --- PLACEHOLDER PHONE SCREENS ---
screen messages_screen():
    zorder 160
    modal True
    add Solid("#000000CC")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 550
        ysize 400
        background Solid("#1A1A2E")
        padding (25, 20)
        vbox:
            hbox:
                text "Messages" size 22 color "#D4A845" bold True
                null width 280
                textbutton "X" action Hide("messages_screen") text_color "#8A8A8A" text_hover_color "#E74C3C"
            null height 20
            text "No messages." size 16 color "#8A8A8A" xalign 0.5

screen camera_screen():
    zorder 160
    modal True
    add Solid("#000000CC")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 550
        ysize 400
        background Solid("#1A1A2E")
        padding (25, 20)
        vbox:
            hbox:
                text "Camera" size 22 color "#D4A845" bold True
                null width 310
                textbutton "X" action Hide("camera_screen") text_color "#8A8A8A" text_hover_color "#E74C3C"
            null height 20
            text "No cameras installed." size 16 color "#8A8A8A" xalign 0.5

screen shop_screen():
    zorder 160
    modal True
    add Solid("#000000CC")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 550
        ysize 400
        background Solid("#1A1A2E")
        padding (25, 20)
        vbox:
            hbox:
                text "Shop" size 22 color "#D4A845" bold True
                null width 330
                textbutton "X" action Hide("shop_screen") text_color "#8A8A8A" text_hover_color "#E74C3C"
            null height 20
            text "Coming soon." size 16 color "#8A8A8A" xalign 0.5

screen diary_screen():
    zorder 160
    modal True
    add Solid("#000000CC")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 550
        ysize 400
        background Solid("#1A1A2E")
        padding (25, 20)
        vbox:
            hbox:
                text "Diary" size 22 color "#D4A845" bold True
                null width 320
                textbutton "X" action Hide("diary_screen") text_color "#8A8A8A" text_hover_color "#E74C3C"
            null height 20
            text "No notes." size 16 color "#8A8A8A" xalign 0.5

screen quests_screen():
    zorder 160
    modal True
    add Solid("#000000CC")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 550
        ysize 400
        background Solid("#1A1A2E")
        padding (25, 20)
        vbox:
            hbox:
                text "Quests" size 22 color "#D4A845" bold True
                null width 310
                textbutton "X" action Hide("quests_screen") text_color "#8A8A8A" text_hover_color "#E74C3C"
            null height 20
            text "No quests." size 16 color "#8A8A8A" xalign 0.5

screen spy_tools_screen():
    zorder 160
    modal True
    add Solid("#000000CC")
    frame:
        xalign 0.5
        yalign 0.5
        xsize 550
        ysize 400
        background Solid("#1A1A2E")
        padding (25, 20)
        vbox:
            hbox:
                text "Spy Tools" size 22 color "#D4A845" bold True
                null width 270
                textbutton "X" action Hide("spy_tools_screen") text_color "#8A8A8A" text_hover_color "#E74C3C"
            null height 20
            text "No tools." size 16 color "#8A8A8A" xalign 0.5
