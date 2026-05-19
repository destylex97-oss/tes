# ============================================================
# SCREENS.RPY — All Game Screens for "House of Influence"
# Main menu, save/load, preferences, phone, map, etc.
# ============================================================


# ============================================================
# MAIN MENU
# ============================================================

screen main_menu():
    tag menu
    style_prefix "main_menu"

    add "gui/mainmenu/menu_overlay.png"

    frame:
        xalign 0.5
        yalign 0.3
        background None
        # Title
        text "HOUSE OF INFLUENCE" size 52 color "#D4A845" xalign 0.5 bold True
        # Subtitle/version
        text "v0.1.0" size 16 color "#8A8A8A" xalign 0.5 ypos 60

    vbox:
        xalign 0.5
        yalign 0.65
        spacing 12

        textbutton _("New Game") action Start() style "menu_button"
        textbutton _("Continue") action ShowMenu("load") style "menu_button"
        textbutton _("Gallery") action ShowMenu("gallery") style "menu_button"
        textbutton _("Settings") action ShowMenu("preferences") style "menu_button"
        textbutton _("Quit") action Quit(confirm=True) style "menu_button"

    # Version info
    text "v[config.version]" xalign 0.98 yalign 0.98 size 14 color "#4A4A5A"


style menu_button:
    background "gui/mainmenu/menu_btn_normal.png"
    hover_background "gui/mainmenu/menu_btn_hover.png"
    xsize 280
    ysize 55
    xalign 0.5

style menu_button_text:
    color "#E8E6E3"
    hover_color "#D4A845"
    size 22
    xalign 0.5
    yalign 0.5


# ============================================================
# DIALOGUE / SAY SCREEN
# ============================================================

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who" style "say_who_text"

        text what id "what" style "say_dialogue_text"

    # Quick menu (Auto, Skip, Log)
    use quick_menu


style window:
    background "gui/dialogue/dialogue_box.png"
    xfill True
    ysize gui.textbox_height
    yalign gui.textbox_yalign
    padding (50, 50, 50, 30)

style namebox:
    background "gui/dialogue/name_plate.png"
    xsize gui.namebox_width
    ysize gui.namebox_height
    xpos gui.name_xpos
    ypos gui.name_ypos
    padding (10, 5, 10, 5)

style say_who_text:
    color "#D4A845"
    size gui.name_text_size
    bold True
    xalign 0.5
    yalign 0.5

style say_dialogue_text:
    color "#E8E6E3"
    size gui.text_size
    xpos gui.dialogue_xpos
    ypos gui.dialogue_ypos
    xsize gui.dialogue_width
    text_align gui.dialogue_text_xalign


# ============================================================
# QUICK MENU (During Dialogue)
# ============================================================

screen quick_menu():
    zorder 100

    hbox:
        xalign 0.95
        yalign 0.96
        spacing 10

        textbutton _("Auto") action Preference("auto-forward", "toggle") style "quick_btn"
        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True) style "quick_btn"
        textbutton _("Log") action ShowMenu("history") style "quick_btn"
        textbutton _("Save") action ShowMenu("save") style "quick_btn"

style quick_btn:
    background None
    xsize 60
    ysize 30

style quick_btn_text:
    color "#8A8A8A"
    hover_color "#D4A845"
    size gui.quick_button_text_size
    xalign 0.5


# ============================================================
# CHOICE SCREEN
# ============================================================

screen choice(items):
    style_prefix "choice"

    vbox:
        xalign 0.5
        yalign 0.4
        spacing 12

        for i in items:
            textbutton i.caption action i.action style "choice_button"


style choice_button:
    background "gui/choices/choice_neutral.png"
    hover_background "gui/choices/choice_neutral_hover.png"
    insensitive_background "gui/choices/choice_locked.png"
    xsize gui.choice_button_width
    ysize gui.choice_button_height
    xalign 0.5

style choice_button_text:
    color gui.choice_text_color
    hover_color "#D4A845"
    insensitive_color "#4A4A5A"
    size 20
    xalign 0.5
    yalign 0.5


# ============================================================
# SAVE / LOAD SCREENS
# ============================================================

screen save():
    tag menu
    use file_slots(_("Save"))

screen load():
    tag menu
    use file_slots(_("Load"))

screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Auto"), quick=_("Quick"))

    frame:
        xfill True
        yfill True
        background "gui/overlays/screen_dim.png"

        frame:
            xalign 0.5
            yalign 0.5
            xsize 1200
            ysize 700
            background "gui/overlays/settings_panel.png"
            padding (40, 40)

            vbox:
                spacing 20

                # Title
                hbox:
                    text title size 28 color "#D4A845" bold True
                    null width 600
                    textbutton _("Return") action Return() style "small_button"

                # Page tabs
                hbox:
                    spacing 10
                    for pg in range(1, 6):
                        textbutton str(pg):
                            action FilePage(pg)
                            style "page_tab"
                            selected_background "gui/saveload/page_tab_active.png"

                # Slots grid
                grid gui.file_slot_cols gui.file_slot_rows:
                    xalign 0.5
                    spacing 20

                    for i in range(gui.file_slot_cols * gui.file_slot_rows):
                        $ slot = i + 1
                        button:
                            action FileAction(slot)
                            style "save_slot"

                            vbox:
                                spacing 5
                                add FileScreenshot(slot) xsize config.thumbnail_width ysize config.thumbnail_height
                                text FileTime(slot, format=_("{#file_time}%b %d, %H:%M"), empty=_("Empty Slot")) size 14 color "#8A8A8A"
                                text FileSaveName(slot) size 14 color "#E8E6E3"

style save_slot:
    background "gui/saveload/slot_empty.png"
    hover_background "gui/saveload/slot_hover.png"
    xsize 280
    ysize 180
    padding (10, 10)

style page_tab:
    background "gui/saveload/page_tab.png"
    xsize 100
    ysize 36

style page_tab_text:
    color "#8A8A8A"
    hover_color "#D4A845"
    selected_color "#D4A845"
    size 16
    xalign 0.5
    yalign 0.5


# ============================================================
# PREFERENCES / SETTINGS
# ============================================================

screen preferences():
    tag menu

    frame:
        xfill True
        yfill True
        background "gui/overlays/screen_dim.png"

        frame:
            xalign 0.5
            yalign 0.5
            xsize 900
            ysize 700
            background "gui/overlays/settings_panel.png"
            padding (40, 40)

            vbox:
                spacing 20

                hbox:
                    text _("Settings") size 28 color "#D4A845" bold True
                    null width 500
                    textbutton _("Return") action Return() style "small_button"

                # Volume controls
                vbox:
                    spacing 15
                    text _("Audio") size 20 color "#D4A845"

                    hbox:
                        spacing 20
                        text _("Music") size 18 color "#E8E6E3" xsize 120
                        bar value Preference("music volume") xsize 300 ysize 20 style "pref_bar"

                    hbox:
                        spacing 20
                        text _("Sound") size 18 color "#E8E6E3" xsize 120
                        bar value Preference("sound volume") xsize 300 ysize 20 style "pref_bar"

                null height 10

                # Display settings
                vbox:
                    spacing 15
                    text _("Display") size 20 color "#D4A845"

                    hbox:
                        spacing 20
                        text _("Fullscreen") size 18 color "#E8E6E3" xsize 120
                        textbutton _("Window") action Preference("display", "any window") style "pref_toggle"
                        textbutton _("Full") action Preference("display", "fullscreen") style "pref_toggle"

                null height 10

                # Text settings
                vbox:
                    spacing 15
                    text _("Text") size 20 color "#D4A845"

                    hbox:
                        spacing 20
                        text _("Speed") size 18 color "#E8E6E3" xsize 120
                        bar value Preference("text speed") xsize 300 ysize 20 style "pref_bar"

                    hbox:
                        spacing 20
                        text _("Auto") size 18 color "#E8E6E3" xsize 120
                        bar value Preference("auto-forward time") xsize 300 ysize 20 style "pref_bar"

                null height 10

                # Skip settings
                vbox:
                    spacing 15
                    text _("Skip") size 20 color "#D4A845"

                    hbox:
                        spacing 20
                        text _("Unseen") size 18 color "#E8E6E3" xsize 120
                        textbutton _("Skip") action Preference("skip", "all") style "pref_toggle"
                        textbutton _("Stop") action Preference("skip", "seen") style "pref_toggle"


style pref_bar:
    left_bar "gui/overlays/slider_track.png"
    right_bar "gui/overlays/slider_track.png"
    thumb "gui/overlays/slider_thumb.png"
    ysize 20

style pref_toggle:
    background "gui/saveload/page_tab.png"
    hover_background "gui/saveload/page_tab_active.png"
    selected_background "gui/saveload/page_tab_active.png"
    xsize 80
    ysize 36

style pref_toggle_text:
    color "#8A8A8A"
    hover_color "#D4A845"
    selected_color "#D4A845"
    size 16
    xalign 0.5
    yalign 0.5


# ============================================================
# PHONE SCREEN (Central Hub)
# ============================================================

screen phone_screen():
    tag phone
    zorder 150
    modal True

    add "gui/overlays/screen_dim.png"

    frame:
        xalign 0.5
        yalign 0.5
        background "gui/phone/phone_frame.png"
        xsize 400
        ysize 700
        padding (30, 70, 30, 60)

        vbox:
            spacing 15

            # Clock/date header
            frame:
                background None
                xalign 0.5
                vbox:
                    xalign 0.5
                    text "[time_text]" size 22 color "#E8E6E3" xalign 0.5
                    text "Day [day]" size 14 color "#8A8A8A" xalign 0.5

            null height 10

            # App grid (3x3)
            grid 3 3:
                xalign 0.5
                spacing 20

                # Row 1
                use phone_app_btn("Stats", "gui/phone/icons/icon_stats.png", Show("stats_screen"))
                use phone_app_btn("Messages", "gui/phone/icons/icon_messages.png", Show("messages_screen"))
                use phone_app_btn("Camera", "gui/phone/icons/icon_camera.png", Show("camera_screen"))

                # Row 2
                use phone_app_btn("Shop", "gui/phone/icons/icon_shop.png", Show("shop_screen"))
                use phone_app_btn("Diary", "gui/phone/icons/icon_diary.png", Show("diary_screen"))
                use phone_app_btn("Settings", "gui/phone/icons/icon_settings.png", ShowMenu("preferences"))

                # Row 3
                use phone_app_btn("Gallery", "gui/phone/icons/icon_gallery.png", ShowMenu("gallery"))
                use phone_app_btn("Quests", "gui/phone/icons/icon_quests.png", Show("quests_screen"))
                use phone_app_btn("Spy", "gui/phone/icons/icon_spy.png", Show("spy_tools_screen"))

            null height 20

            # Close button
            textbutton "Close" action Hide("phone_screen") xalign 0.5 style "small_button"


# Phone app button helper
screen phone_app_btn(label, icon, act):
    vbox:
        spacing 4
        imagebutton:
            idle icon
            hover icon
            action act
            xalign 0.5
        text label size 12 color "#8A8A8A" xalign 0.5


# ============================================================
# STATS SCREEN (Phone -> Stats)
# ============================================================

screen stats_screen():
    tag phone_sub
    zorder 160
    modal True

    add "gui/overlays/screen_dim.png"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 800
        ysize 600
        background "gui/overlays/settings_panel.png"
        padding (30, 30)

        vbox:
            spacing 15

            hbox:
                text "Character Stats" size 24 color "#D4A845" bold True
                null width 400
                textbutton "X" action Hide("stats_screen") style "small_button"

            # Marina stats
            if marina_unlocked:
                use char_stat_block("Marina", marina_affection, marina_corruption, marina_obedience, marina_desire, marina_suspicion, "#6B3FA0")

            # Kaori stats
            if kaori_unlocked:
                use char_stat_block("Kaori", kaori_affection, kaori_corruption, kaori_obedience, kaori_desire, kaori_suspicion, "#C17817")

            # Yuki stats
            if yuki_unlocked:
                use char_stat_block("Yuki", yuki_affection, yuki_corruption, yuki_obedience, yuki_desire, yuki_suspicion, "#D4789C")


# Character stat block helper
screen char_stat_block(name, affection, corruption, obedience, desire, suspicion, name_color):
    frame:
        background "gui/buttons/btn_map_room_normal.png"
        xfill True
        padding (15, 10)

        vbox:
            spacing 4
            text name size 18 color name_color bold True

            hbox:
                spacing 30
                vbox:
                    spacing 3
                    use stat_bar_row("Affection", affection, "#2ECC71")
                    use stat_bar_row("Corruption", corruption, "#6B3FA0")
                    use stat_bar_row("Obedience", obedience, "#3498DB")
                vbox:
                    spacing 3
                    use stat_bar_row("Desire", desire, "#D4789C")
                    use stat_bar_row("Suspicion", suspicion, "#E74C3C")


# Individual stat bar row
screen stat_bar_row(label, value, color):
    hbox:
        spacing 8
        text label size 13 color "#8A8A8A" xsize 80
        bar:
            value value
            range 100
            xsize 120
            ysize 12
            left_bar Solid(color)
            right_bar Solid("#2A2A3E")
        text "[value]" size 13 color "#E8E6E3"


# ============================================================
# SANDBOX MAP SCREEN
# ============================================================

screen sandbox_map():
    tag map
    zorder 120
    modal True

    add "gui/map/map_overlay_bg.png"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1400
        ysize 900
        background None
        padding (50, 50)

        vbox:
            spacing 20

            hbox:
                text "House Map" size 28 color "#D4A845" bold True
                null width 900
                textbutton "X" action Hide("sandbox_map") style "small_button"

            # Second floor
            text "SECOND FLOOR" size 16 color "#8A8A8A"
            hbox:
                spacing 20
                use map_room_btn("MC Room", "mc_room", True, False)
                use map_room_btn("Bathroom", "bathroom", True, False)
                use map_room_btn("Yuki's Room", "yuki_room", yuki_unlocked, False)
                use map_room_btn("Kaori's Room", "kaori_room", kaori_room_unlocked, not kaori_room_unlocked)
                use map_room_btn("Marina's Room", "marina_room", marina_unlocked, False)

            add "gui/map/floor_separator.png" xalign 0.5

            # First floor
            text "FIRST FLOOR" size 16 color "#8A8A8A"
            hbox:
                spacing 20
                use map_room_btn("Kitchen", "kitchen", True, False)
                use map_room_btn("Living Room", "living_room", True, False)
                use map_room_btn("Laundry", "laundry", True, False)
                use map_room_btn("Study", "study", True, False)
                use map_room_btn("Entrance", "entrance", True, False)

            null height 20

            # Outside (if unlocked)
            if outside_unlocked:
                text "OUTSIDE" size 16 color "#8A8A8A"
                hbox:
                    spacing 20
                    use map_room_btn("Mall", "mall", True, False)
                    use map_room_btn("Park", "park", True, False)


# Map room button helper
screen map_room_btn(label, room_id, accessible, locked):
    vbox:
        spacing 4
        if locked:
            imagebutton:
                idle "gui/map/room_locked.png"
                action NullAction()
                tooltip "Locked"
        elif accessible:
            imagebutton:
                idle "gui/map/room_normal.png"
                hover "gui/map/room_hover.png"
                action [Hide("sandbox_map"), Jump("goto_" + room_id)]
        else:
            imagebutton:
                idle "gui/map/room_normal.png"
                action NullAction()

        text label size 13 color "#E8E6E3" xalign 0.5


# ============================================================
# GALLERY SCREEN
# ============================================================

screen gallery():
    tag menu

    frame:
        xfill True
        yfill True
        background "gui/overlays/screen_dim.png"

        frame:
            xalign 0.5
            yalign 0.5
            xsize 1400
            ysize 800
            background "gui/overlays/settings_panel.png"
            padding (40, 40)

            vbox:
                spacing 20

                hbox:
                    text _("Gallery") size 28 color "#D4A845" bold True
                    null width 900
                    textbutton _("Return") action Return() style "small_button"

                # Tabs
                hbox:
                    spacing 10
                    textbutton "Marina" action SetScreenVariable("gallery_tab", "marina") style "page_tab"
                    textbutton "Kaori" action SetScreenVariable("gallery_tab", "kaori") style "page_tab"
                    textbutton "Yuki" action SetScreenVariable("gallery_tab", "yuki") style "page_tab"
                    textbutton "Harem" action SetScreenVariable("gallery_tab", "harem") style "page_tab"

                # Placeholder grid
                text "CG Gallery - Coming Soon" size 20 color "#8A8A8A" xalign 0.5 yalign 0.5


# ============================================================
# HISTORY / LOG SCREEN
# ============================================================

screen history():
    tag menu

    frame:
        xfill True
        yfill True
        background "gui/overlays/screen_dim.png"

        frame:
            xalign 0.5
            yalign 0.5
            xsize 1000
            ysize 700
            background "gui/overlays/settings_panel.png"
            padding (40, 40)

            vbox:
                spacing 10

                hbox:
                    text _("History") size 28 color "#D4A845" bold True
                    null width 600
                    textbutton _("Return") action Return() style "small_button"

                viewport:
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    ysize 580

                    vbox:
                        for h in _history_list:
                            frame:
                                background None
                                xfill True
                                padding (0, 5)

                                vbox:
                                    if h.who:
                                        text h.who size 16 color "#D4A845" bold True
                                    text h.what size 18 color "#E8E6E3"


# ============================================================
# CONFIRM SCREEN
# ============================================================

screen confirm(message, yes_action, no_action):
    zorder 300
    modal True

    add "gui/overlays/screen_dim.png"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 500
        ysize 200
        background "gui/overlays/settings_panel.png"
        padding (30, 30)

        vbox:
            spacing 20
            text message size 20 color "#E8E6E3" xalign 0.5 text_align 0.5

            hbox:
                xalign 0.5
                spacing 30
                textbutton _("Yes") action yes_action style "nav_button"
                textbutton _("No") action no_action style "nav_button"


# ============================================================
# PLACEHOLDER SCREENS (Phone sub-screens)
# ============================================================

screen messages_screen():
    tag phone_sub
    zorder 160
    modal True
    add "gui/overlays/screen_dim.png"
    frame:
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 500
        background "gui/overlays/settings_panel.png"
        padding (30, 30)
        vbox:
            hbox:
                text "Messages" size 24 color "#D4A845" bold True
                null width 350
                textbutton "X" action Hide("messages_screen") style "small_button"
            null height 20
            text "No messages yet." size 18 color "#8A8A8A" xalign 0.5

screen camera_screen():
    tag phone_sub
    zorder 160
    modal True
    add "gui/overlays/screen_dim.png"
    frame:
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 500
        background "gui/overlays/settings_panel.png"
        padding (30, 30)
        vbox:
            hbox:
                text "Camera Footage" size 24 color "#D4A845" bold True
                null width 280
                textbutton "X" action Hide("camera_screen") style "small_button"
            null height 20
            text "No cameras installed." size 18 color "#8A8A8A" xalign 0.5

screen shop_screen():
    tag phone_sub
    zorder 160
    modal True
    add "gui/overlays/screen_dim.png"
    frame:
        xalign 0.5
        yalign 0.5
        xsize 700
        ysize 600
        background "gui/overlays/settings_panel.png"
        padding (30, 30)
        vbox:
            hbox:
                text "Shop" size 24 color "#D4A845" bold True
                null width 470
                textbutton "X" action Hide("shop_screen") style "small_button"
            null height 20
            text "Shop coming in next update." size 18 color "#8A8A8A" xalign 0.5

screen diary_screen():
    tag phone_sub
    zorder 160
    modal True
    add "gui/overlays/screen_dim.png"
    frame:
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 500
        background "gui/overlays/settings_panel.png"
        padding (30, 30)
        vbox:
            hbox:
                text "Diary" size 24 color "#D4A845" bold True
                null width 380
                textbutton "X" action Hide("diary_screen") style "small_button"
            null height 20
            text "No notes yet." size 18 color "#8A8A8A" xalign 0.5

screen quests_screen():
    tag phone_sub
    zorder 160
    modal True
    add "gui/overlays/screen_dim.png"
    frame:
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 500
        background "gui/overlays/settings_panel.png"
        padding (30, 30)
        vbox:
            hbox:
                text "Quests" size 24 color "#D4A845" bold True
                null width 370
                textbutton "X" action Hide("quests_screen") style "small_button"
            null height 20
            text "No active quests." size 18 color "#8A8A8A" xalign 0.5

screen spy_tools_screen():
    tag phone_sub
    zorder 160
    modal True
    add "gui/overlays/screen_dim.png"
    frame:
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 500
        background "gui/overlays/settings_panel.png"
        padding (30, 30)
        vbox:
            hbox:
                text "Spy Tools" size 24 color "#D4A845" bold True
                null width 340
                textbutton "X" action Hide("spy_tools_screen") style "small_button"
            null height 20
            text "No tools purchased." size 18 color "#8A8A8A" xalign 0.5
