# ============================================================
# HUD.RPY — Heads-Up Display for "House of Influence"
# Always-visible elements during sandbox gameplay
# ============================================================

# --- TOP BAR ---
screen hud_top_bar():
    tag hud
    zorder 100
    layer "hud"

    frame:
        xfill True
        ysize 60
        ypos 0
        background "gui/hud/top_bar_bg.png"

        hbox:
            yalign 0.5
            xalign 0.5
            spacing 40

            # Day counter
            frame:
                background None
                padding (10, 5)
                hbox:
                    spacing 6
                    text "DAY" size 14 color "#8A8A8A" yalign 0.5
                    text "[day]" size 22 color "#E8E6E3" bold True yalign 0.5

            # Time slot
            frame:
                background None
                padding (10, 5)
                hbox:
                    spacing 8
                    text "[time_icon]" size 20 yalign 0.5
                    text "[time_text]" size 20 color "#D4A845" yalign 0.5

            # Money
            frame:
                background None
                padding (10, 5)
                hbox:
                    spacing 4
                    text "$" size 18 color "#2ECC71" yalign 0.5
                    text "[money]" size 22 color "#E8E6E3" bold True yalign 0.5

            # Skill level
            frame:
                background None
                padding (10, 5)
                hbox:
                    spacing 6
                    text "Lv[skill_level]" size 18 color "#D4A845" yalign 0.5
                    text "[skill_name]" size 16 color "#8A8A8A" yalign 0.5

            # Phone button
            imagebutton:
                idle "gui/buttons/btn_small_normal.png"
                hover "gui/buttons/btn_small_hover.png"
                action Show("phone_screen")
                yalign 0.5
                tooltip "Phone"

            # Notification badge (if any)
            if phone_notifications > 0:
                frame:
                    xpos -30
                    ypos 5
                    background "gui/phone/notification_badge.png"
                    xsize 24
                    ysize 24
                    text "[phone_notifications]" size 12 color "#FFFFFF" xalign 0.5 yalign 0.5


# --- BOTTOM BAR (Navigation Mode) ---
screen hud_bottom_nav():
    tag hud_bottom
    zorder 100
    layer "hud"

    frame:
        xfill True
        ysize 70
        yalign 1.0
        background "gui/hud/bottom_bar_bg.png"

        hbox:
            xalign 0.5
            yalign 0.5
            spacing 15

            # Map button
            textbutton "MAP":
                style "nav_button"
                action Show("sandbox_map")
                tooltip "Open house map"

            # Interact button
            textbutton "INTERACT":
                style "nav_button"
                action Jump("interact_menu")
                tooltip "Interact with character"
                sensitive (current_room_character is not None)

            # Spy button
            textbutton "SPY":
                style "nav_button"
                action Jump("spy_menu")
                tooltip "Spy/observe"
                sensitive (skill_level >= 1)

            # Work button
            textbutton "WORK":
                style "nav_button"
                action Jump("work_menu")
                tooltip "Part-time job"

            # Advance time
            textbutton "ADVANCE TIME {image=gui/buttons/btn_small_normal.png}":
                style "action_button"
                action Jump("advance_time")
                tooltip "Move to next time slot"


# --- STAT CHANGE NOTIFICATION ---
screen stat_notification(character_name, stat_name, amount):
    tag stat_notif
    zorder 200
    layer "hud"

    timer 2.0 action Hide("stat_notification")

    frame:
        xalign 0.95
        yalign 0.1
        xsize 220
        ysize 45
        background "gui/notifications/stat_popup.png"

        hbox:
            xalign 0.5
            yalign 0.5
            spacing 8

            if amount > 0:
                text "+" + str(amount) size 18 color "#2ECC71"
            else:
                text str(amount) size 18 color "#E74C3C"

            text stat_name.capitalize() size 16 color "#E8E6E3"

        text character_name size 12 color "#8A8A8A" xalign 0.5 yalign 0.9


# --- TIME ADVANCE NOTIFICATION ---
screen time_notification(old_time, new_time):
    tag time_notif
    zorder 200
    layer "hud"

    timer 1.5 action Hide("time_notification")

    frame:
        xalign 0.5
        yalign 0.1
        background "gui/notifications/time_advance_popup.png"
        xsize 300
        ysize 50

        hbox:
            xalign 0.5
            yalign 0.5
            spacing 10
            text old_time size 18 color "#8A8A8A"
            text "{image=gui/buttons/btn_small_normal.png}" yalign 0.5
            text new_time size 18 color "#D4A845"


# --- DISCOVERY POPUP ---
screen discovery_popup(title, description):
    tag discovery
    zorder 250
    modal True

    add "gui/overlays/screen_dim.png"

    frame:
        xalign 0.5
        yalign 0.5
        background "gui/notifications/discovery_popup.png"
        xsize 400
        ysize 150
        padding (20, 20)

        vbox:
            spacing 10
            text title size 20 color "#D4A845" bold True xalign 0.5
            text description size 16 color "#E8E6E3" xalign 0.5

            hbox:
                xalign 0.5
                spacing 20
                textbutton "View in Phone" action [Hide("discovery_popup"), Show("phone_screen")] style "small_button"
                textbutton "Dismiss" action Hide("discovery_popup") style "small_button"


# --- WARNING POPUP ---
screen warning_popup(message):
    tag warning
    zorder 300
    modal True

    add "gui/overlays/screen_dim.png"

    frame:
        xalign 0.5
        yalign 0.5
        background "gui/notifications/warning_popup.png"
        xsize 500
        ysize 180
        padding (30, 30)

        vbox:
            spacing 15
            text "WARNING" size 22 color "#E74C3C" bold True xalign 0.5
            text message size 18 color "#E8E6E3" xalign 0.5 text_align 0.5
            textbutton "Understood" action Hide("warning_popup") xalign 0.5 style "nav_button"


# ============================================================
# HUD STYLES
# ============================================================

style nav_button:
    background "gui/buttons/btn_nav_normal.png"
    hover_background "gui/buttons/btn_nav_hover.png"
    selected_background "gui/buttons/btn_nav_active.png"
    insensitive_background "gui/buttons/btn_nav_disabled.png"
    xsize 180
    ysize 50

style nav_button_text:
    color "#E8E6E3"
    hover_color "#D4A845"
    insensitive_color "#4A4A5A"
    size 18
    xalign 0.5
    yalign 0.5
    bold True

style action_button:
    background "gui/buttons/btn_action_normal.png"
    hover_background "gui/buttons/btn_action_hover.png"
    xsize 220
    ysize 55

style action_button_text:
    color "#E8E6E3"
    hover_color "#D4A845"
    size 18
    xalign 0.5
    yalign 0.5
    bold True

style small_button:
    background "gui/buttons/btn_small_normal.png"
    hover_background "gui/buttons/btn_small_hover.png"
    xsize 100
    ysize 40

style small_button_text:
    color "#E8E6E3"
    hover_color "#D4A845"
    size 14
    xalign 0.5
    yalign 0.5
