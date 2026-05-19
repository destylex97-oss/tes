# ============================================================
# HUD.RPY — Heads-Up Display for "House of Influence"
# ============================================================
# Upgraded UI: icons, decorative elements, animations, polish

init python:
    import math

    # Icon mappings for time slots
    def get_time_icon(slot):
        icons = {
            "morning": "☀",
            "afternoon": "🌤",
            "evening": "🌙",
            "night": "🌑"
        }
        return icons.get(slot, "⏰")

# ============================================================
# TRANSFORMS & ANIMATIONS
# ============================================================

transform hud_btn_hover:
    on hover:
        ease 0.15 zoom 1.05
    on idle:
        ease 0.15 zoom 1.0

transform hud_fade_in:
    alpha 0.0
    ease 0.3 alpha 1.0

transform hud_slide_down:
    yoffset -20 alpha 0.0
    ease 0.25 yoffset 0 alpha 1.0

transform hud_slide_up:
    yoffset 20 alpha 0.0
    ease 0.25 yoffset 0 alpha 1.0

transform hud_pulse:
    alpha 1.0
    ease 0.4 alpha 0.7
    ease 0.4 alpha 1.0
    repeat

transform hud_glow_pulse:
    matrixcolor TintMatrix("#D4A845")
    ease 1.0 matrixcolor TintMatrix("#FFD060")
    ease 1.0 matrixcolor TintMatrix("#D4A845")
    repeat

transform popup_appear:
    alpha 0.0 zoom 0.85
    ease 0.3 alpha 1.0 zoom 1.0

transform popup_disappear:
    ease 0.2 alpha 0.0 zoom 0.9

transform stat_slide_in:
    xoffset 50 alpha 0.0
    ease 0.3 xoffset 0 alpha 1.0

transform notification_bounce:
    yoffset -10
    ease 0.15 yoffset 0
    ease 0.1 yoffset -4
    ease 0.1 yoffset 0


# ============================================================
# TOP BAR
# ============================================================

screen hud_top_bar():
    zorder 100
    tag hud_top

    frame:
        at hud_slide_down
        xfill True
        ysize 72
        ypos 0
        background "gui/hud/top_bar_bg.png"
        padding (30, 0)

        # Decorative accent line at bottom
        add Solid("#D4A845", xsize=1920, ysize=2) yalign 1.0 alpha 0.4

        hbox:
            yalign 0.5
            spacing 10

            # ─── Day Counter ───
            frame:
                background Solid("#0D0D1ACC")
                xsize 120
                ysize 46
                padding (12, 6)
                at hud_btn_hover

                hbox:
                    yalign 0.5
                    xalign 0.5
                    spacing 8
                    text "📅" size 20 yalign 0.5
                    vbox:
                        yalign 0.5
                        text "DAY" size 10 color "#6A6A7A" kerning 2
                        text "[day]" size 20 color "#E8E6E3" bold True

            # Separator
            add Solid("#D4A845", xsize=1, ysize=32) yalign 0.5 alpha 0.5

            # ─── Time Slot ───
            frame:
                background Solid("#0D0D1ACC")
                xsize 160
                ysize 46
                padding (12, 6)
                at hud_btn_hover

                hbox:
                    yalign 0.5
                    xalign 0.5
                    spacing 8
                    text "[time_icon]" size 22 yalign 0.5
                    vbox:
                        yalign 0.5
                        text "TIME" size 10 color "#6A6A7A" kerning 2
                        text "[time_text]" size 18 color "#D4A845" bold True

            # Separator
            add Solid("#D4A845", xsize=1, ysize=32) yalign 0.5 alpha 0.5

            # ─── Money ───
            frame:
                background Solid("#0D0D1ACC")
                xsize 140
                ysize 46
                padding (12, 6)
                at hud_btn_hover

                hbox:
                    yalign 0.5
                    xalign 0.5
                    spacing 8
                    text "💰" size 20 yalign 0.5
                    vbox:
                        yalign 0.5
                        text "FUNDS" size 10 color "#6A6A7A" kerning 2
                        hbox:
                            spacing 2
                            text "$" size 16 color "#2ECC71" bold True yalign 0.5
                            text "[money]" size 20 color "#E8E6E3" bold True yalign 0.5

            # Separator
            add Solid("#D4A845", xsize=1, ysize=32) yalign 0.5 alpha 0.5

            # ─── Skill Level ───
            frame:
                background Solid("#0D0D1ACC")
                xsize 160
                ysize 46
                padding (12, 6)
                at hud_btn_hover

                hbox:
                    yalign 0.5
                    xalign 0.5
                    spacing 8
                    text "⚡" size 20 yalign 0.5
                    vbox:
                        yalign 0.5
                        text "SKILL" size 10 color "#6A6A7A" kerning 2
                        hbox:
                            spacing 4
                            text "Lv[skill_level]" size 18 color "#D4A845" bold True yalign 0.5
                            text "[skill_name]" size 12 color "#8A8A8A" yalign 0.5

        # ─── Right Side: Phone Button ───
        hbox:
            xalign 1.0
            yalign 0.5
            xoffset -20

            button:
                action Show("phone_screen")
                at hud_btn_hover
                background Solid("#1A1A2ECC")
                hover_background Solid("#2A2A4ECC")
                xsize 110
                ysize 46
                padding (10, 6)

                hbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 6
                    text "📱" size 18 yalign 0.5
                    text "PHONE" size 13 color "#E8E6E3" bold True yalign 0.5


# ============================================================
# BOTTOM NAV BAR
# ============================================================

screen hud_bottom_nav():
    zorder 100
    tag hud_bottom

    frame:
        at hud_slide_up
        xfill True
        ysize 80
        yalign 1.0
        background "gui/hud/bottom_bar_bg.png"
        padding (0, 0)

        # Decorative accent line at top
        add Solid("#D4A845", xsize=1920, ysize=2) yalign 0.0 alpha 0.4

        hbox:
            xalign 0.5
            yalign 0.5
            spacing 16

            # ─── MAP ───
            button:
                action Show("sandbox_map")
                style "hud_nav_btn_styled"
                at hud_btn_hover

                hbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 6
                    text "🗺" size 18 yalign 0.5
                    text "MAP" size 15 color "#E8E6E3" bold True yalign 0.5

            # ─── INTERACT ───
            button:
                action Jump("interact_menu")
                sensitive (current_room_character is not None)
                style "hud_nav_btn_styled"
                at hud_btn_hover

                hbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 6
                    text "💬" size 18 yalign 0.5
                    text "INTERACT" size 15 color "#E8E6E3" bold True yalign 0.5

            # ─── SPY ───
            button:
                action Jump("spy_menu")
                sensitive (skill_level >= 1)
                style "hud_nav_btn_styled"
                at hud_btn_hover

                hbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 6
                    text "👁" size 18 yalign 0.5
                    text "SPY" size 15 color "#E8E6E3" bold True yalign 0.5

            # ─── WORK ───
            button:
                action Jump("work_menu")
                style "hud_nav_btn_styled"
                at hud_btn_hover

                hbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 6
                    text "🔧" size 18 yalign 0.5
                    text "WORK" size 15 color "#E8E6E3" bold True yalign 0.5

            # ─── Separator before action ───
            add Solid("#D4A845", xsize=2, ysize=40) yalign 0.5 alpha 0.6

            # ─── NEXT (Action Button - highlighted) ───
            button:
                action Jump("advance_time")
                style "hud_action_btn_styled"
                at hud_btn_hover

                hbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 6
                    text "NEXT" size 16 color "#D4A845" bold True yalign 0.5
                    text "▶" size 14 color "#D4A845" yalign 0.5


# ============================================================
# STAT NOTIFICATION (slide-in from right)
# ============================================================

screen stat_notification(char_name, stat_name, amount):
    zorder 200
    timer 2.5 action Hide("stat_notification")

    frame:
        at stat_slide_in
        xalign 0.95
        yalign 0.1
        xsize 260
        ysize 70
        background Solid("#0D0D1AF0")
        padding (16, 10)

        # Accent border left
        add Solid("#D4A845", xsize=3, ysize=70) xpos 0 ypos 0

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 4

            hbox:
                xalign 0.5
                spacing 8
                if amount > 0:
                    text "▲" size 14 color "#2ECC71" bold True yalign 0.5
                    text "+[amount]" size 18 color "#2ECC71" bold True yalign 0.5
                else:
                    text "▼" size 14 color "#E74C3C" bold True yalign 0.5
                    text "[amount]" size 18 color "#E74C3C" bold True yalign 0.5
                text stat_name size 14 color "#E8E6E3" yalign 0.5

            hbox:
                xalign 0.5
                spacing 6
                text "─" size 10 color "#3A3A5E"
                text char_name size 12 color "#8A8A8A" italic True
                text "─" size 10 color "#3A3A5E"


# ============================================================
# DISCOVERY POPUP (centered modal with glow)
# ============================================================

screen discovery_popup(title, desc):
    zorder 250
    modal True

    add Solid("#000000D8")

    frame:
        at popup_appear
        xalign 0.5
        yalign 0.5
        xsize 460
        ysize 220
        background Solid("#0D0D1AF8")
        padding (30, 25)

        # Top accent bar
        add Solid("#D4A845", xsize=460, ysize=3) xpos 0 ypos 0

        # Corner decorations
        text "◆" size 12 color "#D4A845" xpos 10 ypos 8 alpha 0.6
        text "◆" size 12 color "#D4A845" xalign 1.0 xoffset -10 ypos 8 alpha 0.6

        vbox:
            spacing 14
            xalign 0.5
            yalign 0.5

            # Title with decorative elements
            hbox:
                xalign 0.5
                spacing 10
                text "✦" size 14 color "#D4A845" yalign 0.5 alpha 0.7
                text title size 22 color "#D4A845" bold True
                text "✦" size 14 color "#D4A845" yalign 0.5 alpha 0.7

            # Description
            text desc size 16 color "#C8C6C3" xalign 0.5 text_align 0.5

            null height 8

            # Buttons
            hbox:
                xalign 0.5
                spacing 16

                button:
                    action [Hide("discovery_popup"), Show("phone_screen")]
                    style "hud_popup_btn"
                    at hud_btn_hover
                    hbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 4
                        text "📱" size 14 yalign 0.5
                        text "Phone" size 14 color "#E8E6E3" bold True yalign 0.5

                button:
                    action Hide("discovery_popup")
                    style "hud_popup_btn_accent"
                    at hud_btn_hover
                    text "OK" size 14 color "#D4A845" bold True xalign 0.5 yalign 0.5


# ============================================================
# WARNING POPUP (urgent styling)
# ============================================================

screen warning_popup(message):
    zorder 300
    modal True

    add Solid("#000000E0")

    frame:
        at popup_appear
        xalign 0.5
        yalign 0.5
        xsize 520
        ysize 230
        background Solid("#0D0D1AF8")
        padding (30, 25)

        # Top accent bar (red for warning)
        add Solid("#E74C3C", xsize=520, ysize=3) xpos 0 ypos 0

        # Subtle pulsing border effect
        add Solid("#E74C3C", xsize=520, ysize=1) xpos 0 yalign 1.0 alpha 0.3

        vbox:
            spacing 16
            xalign 0.5
            yalign 0.5

            # Warning icon and title
            hbox:
                xalign 0.5
                spacing 10
                text "⚠" size 24 color "#E74C3C" yalign 0.5
                text "WARNING" size 22 color "#E74C3C" bold True kerning 3 yalign 0.5

            # Message
            text message size 17 color "#E8E6E3" xalign 0.5 text_align 0.5

            null height 6

            # Button
            button:
                action Hide("warning_popup")
                style "hud_popup_btn_warning"
                xalign 0.5
                at hud_btn_hover
                text "Understood" size 14 color "#E8E6E3" bold True xalign 0.5 yalign 0.5


# ============================================================
# TOOLTIP / HINT POPUP (for contextual hints)
# ============================================================

screen hud_tooltip(hint_text):
    zorder 180
    timer 3.0 action Hide("hud_tooltip")

    frame:
        at hud_fade_in
        xalign 0.5
        yalign 0.88
        xsize 400
        ysize 45
        background Solid("#1A1A2EE8")
        padding (16, 8)

        hbox:
            xalign 0.5
            yalign 0.5
            spacing 8
            text "💡" size 16 yalign 0.5
            text hint_text size 14 color "#C8C6C3" italic True yalign 0.5


# ============================================================
# STYLES
# ============================================================

style hud_nav_btn_styled:
    background Solid("#12122ACC")
    hover_background Solid("#1E1E3ECC")
    insensitive_background Solid("#0A0A14AA")
    xsize 160
    ysize 52
    xpadding 14
    ypadding 8

style hud_nav_btn_styled_text:
    color "#E8E6E3"
    hover_color "#D4A845"
    insensitive_color "#3A3A4A"
    size 15
    bold True
    xalign 0.5
    yalign 0.5

style hud_action_btn_styled:
    background Solid("#2A1A00DD")
    hover_background Solid("#3D2800DD")
    xsize 150
    ysize 52
    xpadding 14
    ypadding 8

style hud_action_btn_styled_text:
    color "#D4A845"
    hover_color "#FFD060"
    size 16
    bold True
    xalign 0.5
    yalign 0.5

style hud_popup_btn:
    background Solid("#1A1A2EDD")
    hover_background Solid("#2A2A4EDD")
    xsize 110
    ysize 40
    xpadding 10
    ypadding 6

style hud_popup_btn_text:
    color "#E8E6E3"
    hover_color "#D4A845"
    size 14
    bold True
    xalign 0.5
    yalign 0.5

style hud_popup_btn_accent:
    background Solid("#2A1A00DD")
    hover_background Solid("#3D2800DD")
    xsize 90
    ysize 40
    xpadding 10
    ypadding 6

style hud_popup_btn_accent_text:
    color "#D4A845"
    hover_color "#FFD060"
    size 14
    bold True
    xalign 0.5
    yalign 0.5

style hud_popup_btn_warning:
    background Solid("#3C1515DD")
    hover_background Solid("#5C2020DD")
    xsize 140
    ysize 40
    xpadding 14
    ypadding 6

style hud_popup_btn_warning_text:
    color "#E8E6E3"
    hover_color "#FF6B6B"
    size 14
    bold True
    xalign 0.5
    yalign 0.5

# Legacy styles (kept for backward compatibility)
style hud_nav_btn:
    take hud_nav_btn_styled

style hud_nav_btn_text:
    take hud_nav_btn_styled_text

style hud_action_btn:
    take hud_action_btn_styled

style hud_action_btn_text:
    take hud_action_btn_styled_text

style hud_small_btn:
    take hud_popup_btn

style hud_small_btn_text:
    take hud_popup_btn_text
