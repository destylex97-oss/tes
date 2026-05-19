# ============================================================
# HUD.RPY — Heads-Up Display for "House of Influence"
# ============================================================

# --- TOP BAR ---
screen hud_top_bar():
    zorder 100

    frame:
        xfill True
        ysize 60
        ypos 0
        background "gui/hud/top_bar_bg.png"
        padding (30, 0)

        hbox:
            yalign 0.5
            spacing 50

            # Day
            hbox:
                spacing 6
                text "DAY" size 14 color "#8A8A8A" yalign 0.5
                text "[day]" size 22 color "#E8E6E3" bold True yalign 0.5

            # Time slot
            hbox:
                spacing 8
                text "[time_icon]" size 20 yalign 0.5
                text "[time_text]" size 20 color "#D4A845" yalign 0.5

            # Money
            hbox:
                spacing 4
                text "$" size 18 color "#2ECC71" yalign 0.5
                text "[money]" size 22 color "#E8E6E3" bold True yalign 0.5

            # Skill
            hbox:
                spacing 6
                text "Lv[skill_level]" size 18 color "#D4A845" yalign 0.5
                text "[skill_name]" size 14 color "#8A8A8A" yalign 0.5

        # Phone button (right side)
        hbox:
            xalign 1.0
            yalign 0.5
            xoffset -30

            textbutton "PHONE":
                action Show("phone_screen")
                text_size 16
                text_color "#E8E6E3"
                text_hover_color "#D4A845"


# --- BOTTOM BAR ---
screen hud_bottom_nav():
    zorder 100

    frame:
        xfill True
        ysize 70
        yalign 1.0
        background "gui/hud/bottom_bar_bg.png"
        padding (0, 0)

        hbox:
            xalign 0.5
            yalign 0.5
            spacing 20

            textbutton "MAP" action Show("sandbox_map") style "hud_nav_btn"
            textbutton "INTERACT" action Jump("interact_menu") style "hud_nav_btn" sensitive (current_room_character is not None)
            textbutton "SPY" action Jump("spy_menu") style "hud_nav_btn" sensitive (skill_level >= 1)
            textbutton "WORK" action Jump("work_menu") style "hud_nav_btn"
            textbutton "NEXT \u25B6" action Jump("advance_time") style "hud_action_btn"


# --- STAT NOTIFICATION ---
screen stat_notification(char_name, stat_name, amount):
    zorder 200
    timer 2.0 action Hide("stat_notification")

    frame:
        xalign 0.9
        yalign 0.08
        xsize 220
        ysize 50
        background "gui/notifications/stat_popup.png"
        padding (15, 8)

        vbox:
            xalign 0.5
            yalign 0.5
            hbox:
                xalign 0.5
                spacing 6
                if amount > 0:
                    text "+[amount]" size 16 color "#2ECC71" bold True
                else:
                    text "[amount]" size 16 color "#E74C3C" bold True
                text "[stat_name]" size 14 color "#E8E6E3"
            text "[char_name]" size 12 color "#8A8A8A" xalign 0.5


# --- DISCOVERY POPUP ---
screen discovery_popup(title, desc):
    zorder 250
    modal True

    add Solid("#000000C8")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 420
        ysize 180
        background "gui/notifications/discovery_popup.png"
        padding (25, 25)

        vbox:
            spacing 12
            xalign 0.5
            text title size 20 color "#D4A845" bold True xalign 0.5
            text desc size 16 color "#E8E6E3" xalign 0.5 text_align 0.5
            null height 5
            hbox:
                xalign 0.5
                spacing 20
                textbutton "Phone" action [Hide("discovery_popup"), Show("phone_screen")] style "hud_small_btn"
                textbutton "OK" action Hide("discovery_popup") style "hud_small_btn"


# --- WARNING POPUP ---
screen warning_popup(message):
    zorder 300
    modal True

    add Solid("#000000D0")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 500
        ysize 200
        background "gui/notifications/warning_popup.png"
        padding (30, 25)

        vbox:
            spacing 15
            xalign 0.5
            text "⚠ WARNING" size 22 color "#E74C3C" bold True xalign 0.5
            text message size 18 color "#E8E6E3" xalign 0.5 text_align 0.5
            textbutton "Understood" action Hide("warning_popup") xalign 0.5 style "hud_nav_btn"


# ============================================================
# HUD STYLES
# ============================================================

style hud_nav_btn:
    background Solid("#1A1A2E")
    hover_background Solid("#3A3A5E")
    insensitive_background Solid("#111118")
    xsize 160
    ysize 45
    xpadding 10

style hud_nav_btn_text:
    color "#E8E6E3"
    hover_color "#D4A845"
    insensitive_color "#4A4A5A"
    size 16
    bold True
    xalign 0.5
    yalign 0.5

style hud_action_btn:
    background Solid("#2A1A00")
    hover_background Solid("#4A3000")
    xsize 140
    ysize 45
    xpadding 10

style hud_action_btn_text:
    color "#D4A845"
    hover_color "#FFD060"
    size 16
    bold True
    xalign 0.5
    yalign 0.5

style hud_small_btn:
    background Solid("#1A1A2E")
    hover_background Solid("#3A3A5E")
    xsize 90
    ysize 35
    xpadding 8

style hud_small_btn_text:
    color "#E8E6E3"
    hover_color "#D4A845"
    size 14
    xalign 0.5
    yalign 0.5
