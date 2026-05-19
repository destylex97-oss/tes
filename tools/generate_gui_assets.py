#!/usr/bin/env python3
"""
GUI Asset Generator for "House of Influence"
Generates all UI/HUD placeholder assets based on gui_plan.md specs.
Uses Pillow to create PNG assets ready for Ren'Py.

Usage: python generate_gui_assets.py
Output: ../game/gui/ directory with all assets
"""

import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# === CONFIGURATION ===
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "game", "gui")
RESOLUTION = (1920, 1080)

# Color Palette (from gui_plan.md)
COLORS = {
    "bg": "#0D0D0F",
    "surface": "#1A1A2E",
    "primary": "#D4A845",
    "accent": "#8B1A1A",
    "text": "#E8E6E3",
    "text_secondary": "#8A8A8A",
    "marina": "#6B3FA0",
    "kaori": "#C17817",
    "yuki": "#D4789C",
    "success": "#2ECC71",
    "danger": "#E74C3C",
    "transparent": (0, 0, 0, 0),
    "bar_bg": "#2A2A3E",
    "button_hover": "#3A3A5E",
}


def hex_to_rgba(hex_color, alpha=255):
    """Convert hex color to RGBA tuple."""
    hex_color = hex_color.lstrip("#")
    r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
    return (r, g, b, alpha)


def ensure_dir(path):
    """Create directory if it doesn't exist."""
    os.makedirs(path, exist_ok=True)



def draw_rounded_rect(draw, xy, radius, fill=None, outline=None, width=1):
    """Draw a rounded rectangle."""
    x1, y1, x2, y2 = xy
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def create_button(width, height, text="", state="normal", corner_radius=8):
    """Create a button asset in different states."""
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    if state == "normal":
        fill = hex_to_rgba(COLORS["surface"])
        border = hex_to_rgba(COLORS["primary"], 180)
    elif state == "hover":
        fill = hex_to_rgba(COLORS["button_hover"])
        border = hex_to_rgba(COLORS["primary"])
    elif state == "active":
        fill = hex_to_rgba(COLORS["primary"], 80)
        border = hex_to_rgba(COLORS["primary"])
    elif state == "disabled":
        fill = hex_to_rgba(COLORS["surface"], 128)
        border = hex_to_rgba(COLORS["text_secondary"], 80)
    else:
        fill = hex_to_rgba(COLORS["surface"])
        border = hex_to_rgba(COLORS["primary"], 180)

    draw_rounded_rect(draw, (0, 0, width - 1, height - 1), corner_radius, fill=fill, outline=border, width=2)
    return img


# === ASSET GENERATORS ===

def generate_top_bar():
    """Generate top HUD bar background."""
    path = os.path.join(OUTPUT_DIR, "hud")
    ensure_dir(path)

    # Top bar background (full width, 60px tall)
    bar = Image.new("RGBA", (1920, 60), hex_to_rgba(COLORS["bg"], 220))
    draw = ImageDraw.Draw(bar)
    # Bottom border line
    draw.line([(0, 59), (1920, 59)], fill=hex_to_rgba(COLORS["primary"], 100), width=1)
    bar.save(os.path.join(path, "top_bar_bg.png"))

    # Bottom bar background
    bar = Image.new("RGBA", (1920, 140), hex_to_rgba(COLORS["bg"], 230))
    draw = ImageDraw.Draw(bar)
    draw.line([(0, 0), (1920, 0)], fill=hex_to_rgba(COLORS["primary"], 100), width=1)
    bar.save(os.path.join(path, "bottom_bar_bg.png"))

    print("  [OK] HUD bars")



def generate_buttons():
    """Generate all button variants."""
    path = os.path.join(OUTPUT_DIR, "buttons")
    ensure_dir(path)

    button_sizes = {
        "nav": (180, 50),       # Navigation buttons (MAP, INTERACT, SPY, WORK)
        "action": (220, 55),    # Action buttons (ADVANCE TIME)
        "menu": (280, 60),      # Main menu buttons
        "small": (100, 40),     # Small utility buttons (Auto, Skip, Log)
        "choice": (700, 55),    # Dialogue choice buttons
        "phone_app": (80, 80),  # Phone app icon buttons
        "map_room": (150, 100), # Map room buttons
    }

    states = ["normal", "hover", "active", "disabled"]

    for name, (w, h) in button_sizes.items():
        for state in states:
            btn = create_button(w, h, state=state)
            btn.save(os.path.join(path, f"btn_{name}_{state}.png"))

    print("  [OK] Buttons (all variants)")


def generate_dialogue_box():
    """Generate dialogue box assets."""
    path = os.path.join(OUTPUT_DIR, "dialogue")
    ensure_dir(path)

    # Standard dialogue box (bottom of screen)
    box = Image.new("RGBA", (1820, 200), (0, 0, 0, 0))
    draw = ImageDraw.Draw(box)
    # Main box with gradient-like opacity
    draw_rounded_rect(draw, (0, 0, 1819, 199), 12,
                      fill=hex_to_rgba(COLORS["bg"], 235),
                      outline=hex_to_rgba(COLORS["primary"], 120), width=2)
    box.save(os.path.join(path, "dialogue_box.png"))

    # Name plate
    plate = Image.new("RGBA", (250, 40), (0, 0, 0, 0))
    draw = ImageDraw.Draw(plate)
    draw_rounded_rect(draw, (0, 0, 249, 39), 6,
                      fill=hex_to_rgba(COLORS["surface"]),
                      outline=hex_to_rgba(COLORS["primary"], 150), width=2)
    plate.save(os.path.join(path, "name_plate.png"))

    # H-scene dialogue box (smaller, more transparent)
    hbox = Image.new("RGBA", (1400, 120), (0, 0, 0, 0))
    draw = ImageDraw.Draw(hbox)
    draw_rounded_rect(draw, (0, 0, 1399, 119), 10,
                      fill=hex_to_rgba(COLORS["bg"], 180),
                      outline=hex_to_rgba(COLORS["primary"], 80), width=1)
    hbox.save(os.path.join(path, "dialogue_box_hscene.png"))

    print("  [OK] Dialogue boxes")



def generate_stat_bars():
    """Generate stat bar assets (background + fill for each stat type)."""
    path = os.path.join(OUTPUT_DIR, "stats")
    ensure_dir(path)

    bar_width = 200
    bar_height = 16

    # Bar background (empty)
    bg = Image.new("RGBA", (bar_width, bar_height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(bg)
    draw_rounded_rect(draw, (0, 0, bar_width - 1, bar_height - 1), 4,
                      fill=hex_to_rgba(COLORS["bar_bg"]))
    bg.save(os.path.join(path, "bar_bg.png"))

    # Stat-specific fill bars
    stat_colors = {
        "affection": COLORS["success"],
        "corruption": COLORS["marina"],
        "obedience": "#3498DB",
        "desire": COLORS["yuki"],
        "suspicion": COLORS["danger"],
        "obsession": "#E67E22",
    }

    for stat_name, color in stat_colors.items():
        fill = Image.new("RGBA", (bar_width, bar_height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(fill)
        draw_rounded_rect(draw, (0, 0, bar_width - 1, bar_height - 1), 4,
                          fill=hex_to_rgba(color))
        fill.save(os.path.join(path, f"bar_{stat_name}.png"))

    print("  [OK] Stat bars")


def generate_phone_ui():
    """Generate phone interface assets."""
    path = os.path.join(OUTPUT_DIR, "phone")
    ensure_dir(path)

    # Phone frame (centered on screen)
    phone_w, phone_h = 400, 700
    phone = Image.new("RGBA", (phone_w, phone_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(phone)
    # Outer frame
    draw_rounded_rect(draw, (0, 0, phone_w - 1, phone_h - 1), 24,
                      fill=hex_to_rgba("#111118"),
                      outline=hex_to_rgba(COLORS["primary"], 150), width=3)
    # Inner screen area
    draw_rounded_rect(draw, (12, 50, phone_w - 13, phone_h - 50), 16,
                      fill=hex_to_rgba(COLORS["surface"]))
    # Top notch
    draw_rounded_rect(draw, (150, 10, 250, 35), 10,
                      fill=hex_to_rgba(COLORS["surface"]))
    phone.save(os.path.join(path, "phone_frame.png"))

    # App icon backgrounds (9 apps)
    app_bg = Image.new("RGBA", (70, 70), (0, 0, 0, 0))
    draw = ImageDraw.Draw(app_bg)
    draw_rounded_rect(draw, (0, 0, 69, 69), 14,
                      fill=hex_to_rgba(COLORS["surface"]),
                      outline=hex_to_rgba(COLORS["primary"], 100), width=1)
    app_bg.save(os.path.join(path, "app_icon_bg.png"))

    # Notification badge
    badge = Image.new("RGBA", (24, 24), (0, 0, 0, 0))
    draw = ImageDraw.Draw(badge)
    draw.ellipse((0, 0, 23, 23), fill=hex_to_rgba(COLORS["danger"]))
    badge.save(os.path.join(path, "notification_badge.png"))

    print("  [OK] Phone UI")



def generate_map_assets():
    """Generate sandbox map screen assets."""
    path = os.path.join(OUTPUT_DIR, "map")
    ensure_dir(path)

    # Map overlay background
    overlay = Image.new("RGBA", (1920, 1080), hex_to_rgba(COLORS["bg"], 240))
    overlay.save(os.path.join(path, "map_overlay_bg.png"))

    # Room card (normal, hover, locked, event)
    room_states = {
        "normal": (COLORS["surface"], COLORS["text_secondary"], 1),
        "hover": (COLORS["button_hover"], COLORS["primary"], 2),
        "locked": (COLORS["surface"], COLORS["accent"], 1),
        "event": (COLORS["surface"], COLORS["success"], 2),
        "hscene": (COLORS["surface"], COLORS["yuki"], 2),
    }

    for state, (fill_c, border_c, bw) in room_states.items():
        room = Image.new("RGBA", (160, 110), (0, 0, 0, 0))
        draw = ImageDraw.Draw(room)
        draw_rounded_rect(draw, (0, 0, 159, 109), 10,
                          fill=hex_to_rgba(fill_c),
                          outline=hex_to_rgba(border_c), width=bw)
        room.save(os.path.join(path, f"room_{state}.png"))

    # Floor separator line
    sep = Image.new("RGBA", (1600, 3), hex_to_rgba(COLORS["primary"], 80))
    sep.save(os.path.join(path, "floor_separator.png"))

    print("  [OK] Map assets")


def generate_choice_menu():
    """Generate choice/interaction menu assets."""
    path = os.path.join(OUTPUT_DIR, "choices")
    ensure_dir(path)

    # Choice box variants (stat-colored borders)
    stat_border_colors = {
        "neutral": COLORS["text_secondary"],
        "affection": COLORS["success"],
        "corruption": COLORS["marina"],
        "obedience": "#3498DB",
        "desire": COLORS["yuki"],
        "locked": COLORS["text_secondary"],
    }

    for stat, color in stat_border_colors.items():
        # Normal state
        choice = Image.new("RGBA", (700, 55), (0, 0, 0, 0))
        draw = ImageDraw.Draw(choice)
        draw_rounded_rect(draw, (0, 0, 699, 54), 8,
                          fill=hex_to_rgba(COLORS["surface"], 230),
                          outline=hex_to_rgba(color, 180), width=2)
        choice.save(os.path.join(path, f"choice_{stat}.png"))

        # Hover state
        choice_h = Image.new("RGBA", (700, 55), (0, 0, 0, 0))
        draw = ImageDraw.Draw(choice_h)
        draw_rounded_rect(draw, (0, 0, 699, 54), 8,
                          fill=hex_to_rgba(color, 40),
                          outline=hex_to_rgba(color), width=2)
        choice_h.save(os.path.join(path, f"choice_{stat}_hover.png"))

    print("  [OK] Choice menu assets")



def generate_hscene_ui():
    """Generate H-scene specific UI assets."""
    path = os.path.join(OUTPUT_DIR, "hscene")
    ensure_dir(path)

    # Pace bar background
    pace_bg = Image.new("RGBA", (600, 20), (0, 0, 0, 0))
    draw = ImageDraw.Draw(pace_bg)
    draw_rounded_rect(draw, (0, 0, 599, 19), 6, fill=hex_to_rgba(COLORS["bar_bg"]))
    pace_bg.save(os.path.join(path, "pace_bar_bg.png"))

    # Pace bar fill
    pace_fill = Image.new("RGBA", (600, 20), (0, 0, 0, 0))
    draw = ImageDraw.Draw(pace_fill)
    draw_rounded_rect(draw, (0, 0, 599, 19), 6, fill=hex_to_rgba(COLORS["primary"]))
    pace_fill.save(os.path.join(path, "pace_bar_fill.png"))

    # Stamina bar (green gradient)
    stam_fill = Image.new("RGBA", (400, 14), (0, 0, 0, 0))
    draw = ImageDraw.Draw(stam_fill)
    draw_rounded_rect(draw, (0, 0, 399, 13), 4, fill=hex_to_rgba(COLORS["success"]))
    stam_fill.save(os.path.join(path, "stamina_bar_fill.png"))

    # Her pleasure bar (pink)
    plea_fill = Image.new("RGBA", (400, 14), (0, 0, 0, 0))
    draw = ImageDraw.Draw(plea_fill)
    draw_rounded_rect(draw, (0, 0, 399, 13), 4, fill=hex_to_rgba(COLORS["yuki"]))
    plea_fill.save(os.path.join(path, "pleasure_bar_fill.png"))

    # H-scene control panel background
    panel = Image.new("RGBA", (1920, 180), (0, 0, 0, 0))
    draw = ImageDraw.Draw(panel)
    draw_rounded_rect(draw, (50, 10, 1870, 170), 12,
                      fill=hex_to_rgba(COLORS["bg"], 200),
                      outline=hex_to_rgba(COLORS["primary"], 60), width=1)
    panel.save(os.path.join(path, "hscene_panel_bg.png"))

    # Position selector card
    pos_card = Image.new("RGBA", (120, 90), (0, 0, 0, 0))
    draw = ImageDraw.Draw(pos_card)
    draw_rounded_rect(draw, (0, 0, 119, 89), 8,
                      fill=hex_to_rgba(COLORS["surface"]),
                      outline=hex_to_rgba(COLORS["primary"], 120), width=2)
    pos_card.save(os.path.join(path, "position_card.png"))

    # Position selector card (locked)
    pos_locked = Image.new("RGBA", (120, 90), (0, 0, 0, 0))
    draw = ImageDraw.Draw(pos_locked)
    draw_rounded_rect(draw, (0, 0, 119, 89), 8,
                      fill=hex_to_rgba(COLORS["surface"], 128),
                      outline=hex_to_rgba(COLORS["text_secondary"], 80), width=1)
    pos_locked.save(os.path.join(path, "position_card_locked.png"))

    # Finish dropdown background
    finish = Image.new("RGBA", (250, 300), (0, 0, 0, 0))
    draw = ImageDraw.Draw(finish)
    draw_rounded_rect(draw, (0, 0, 249, 299), 10,
                      fill=hex_to_rgba(COLORS["bg"], 245),
                      outline=hex_to_rgba(COLORS["primary"], 100), width=2)
    finish.save(os.path.join(path, "finish_dropdown_bg.png"))

    print("  [OK] H-scene UI")


def generate_minigame_ui():
    """Generate mini-game UI assets."""
    path = os.path.join(OUTPUT_DIR, "minigame")
    ensure_dir(path)

    # Timing target zone (delivery game)
    target = Image.new("RGBA", (120, 40), (0, 0, 0, 0))
    draw = ImageDraw.Draw(target)
    draw_rounded_rect(draw, (0, 0, 119, 39), 6,
                      fill=hex_to_rgba(COLORS["success"], 60),
                      outline=hex_to_rgba(COLORS["success"]), width=2)
    target.save(os.path.join(path, "timing_target.png"))

    # Timing marker (moving dot)
    marker = Image.new("RGBA", (20, 20), (0, 0, 0, 0))
    draw = ImageDraw.Draw(marker)
    draw.ellipse((0, 0, 19, 19), fill=hex_to_rgba(COLORS["primary"]))
    marker.save(os.path.join(path, "timing_marker.png"))

    # Rhythm hit indicator
    rhythm_dot = Image.new("RGBA", (30, 30), (0, 0, 0, 0))
    draw = ImageDraw.Draw(rhythm_dot)
    draw.ellipse((2, 2, 27, 27), fill=hex_to_rgba(COLORS["primary"]),
                 outline=hex_to_rgba(COLORS["text"], 200), width=2)
    rhythm_dot.save(os.path.join(path, "rhythm_dot.png"))

    # Rhythm dot (inactive/upcoming)
    rhythm_empty = Image.new("RGBA", (30, 30), (0, 0, 0, 0))
    draw = ImageDraw.Draw(rhythm_empty)
    draw.ellipse((2, 2, 27, 27), outline=hex_to_rgba(COLORS["text_secondary"], 150), width=2)
    rhythm_empty.save(os.path.join(path, "rhythm_dot_empty.png"))

    # Awareness bar (sleep stealth — red gradient)
    aware_fill = Image.new("RGBA", (500, 18), (0, 0, 0, 0))
    draw = ImageDraw.Draw(aware_fill)
    draw_rounded_rect(draw, (0, 0, 499, 17), 5, fill=hex_to_rgba(COLORS["danger"]))
    aware_fill.save(os.path.join(path, "awareness_bar_fill.png"))

    print("  [OK] Mini-game UI")



def generate_notification_assets():
    """Generate popup/notification assets."""
    path = os.path.join(OUTPUT_DIR, "notifications")
    ensure_dir(path)

    # Stat change popup
    popup = Image.new("RGBA", (220, 45), (0, 0, 0, 0))
    draw = ImageDraw.Draw(popup)
    draw_rounded_rect(draw, (0, 0, 219, 44), 8,
                      fill=hex_to_rgba(COLORS["surface"], 220),
                      outline=hex_to_rgba(COLORS["primary"], 100), width=1)
    popup.save(os.path.join(path, "stat_popup.png"))

    # Event discovery popup (larger)
    discovery = Image.new("RGBA", (400, 150), (0, 0, 0, 0))
    draw = ImageDraw.Draw(discovery)
    draw_rounded_rect(draw, (0, 0, 399, 149), 12,
                      fill=hex_to_rgba(COLORS["bg"], 245),
                      outline=hex_to_rgba(COLORS["primary"]), width=2)
    discovery.save(os.path.join(path, "discovery_popup.png"))

    # Warning popup (red border)
    warning = Image.new("RGBA", (500, 180), (0, 0, 0, 0))
    draw = ImageDraw.Draw(warning)
    draw_rounded_rect(draw, (0, 0, 499, 179), 12,
                      fill=hex_to_rgba(COLORS["bg"], 250),
                      outline=hex_to_rgba(COLORS["danger"]), width=3)
    warning.save(os.path.join(path, "warning_popup.png"))

    # Time advance indicator
    time_popup = Image.new("RGBA", (300, 50), (0, 0, 0, 0))
    draw = ImageDraw.Draw(time_popup)
    draw_rounded_rect(draw, (0, 0, 299, 49), 8,
                      fill=hex_to_rgba(COLORS["surface"], 200),
                      outline=hex_to_rgba(COLORS["primary"], 80), width=1)
    time_popup.save(os.path.join(path, "time_advance_popup.png"))

    print("  [OK] Notifications")


def generate_gallery_assets():
    """Generate gallery screen assets."""
    path = os.path.join(OUTPUT_DIR, "gallery")
    ensure_dir(path)

    # CG thumbnail frame (unlocked)
    thumb = Image.new("RGBA", (180, 120), (0, 0, 0, 0))
    draw = ImageDraw.Draw(thumb)
    draw_rounded_rect(draw, (0, 0, 179, 119), 6,
                      fill=hex_to_rgba(COLORS["surface"]),
                      outline=hex_to_rgba(COLORS["primary"], 120), width=2)
    thumb.save(os.path.join(path, "thumb_unlocked.png"))

    # CG thumbnail frame (locked — silhouette)
    locked = Image.new("RGBA", (180, 120), (0, 0, 0, 0))
    draw = ImageDraw.Draw(locked)
    draw_rounded_rect(draw, (0, 0, 179, 119), 6,
                      fill=hex_to_rgba("#0A0A12"),
                      outline=hex_to_rgba(COLORS["text_secondary"], 60), width=1)
    # Lock icon placeholder (simple shape)
    draw.rectangle((75, 40, 105, 70), fill=hex_to_rgba(COLORS["text_secondary"], 100))
    draw.rectangle((82, 30, 98, 45), outline=hex_to_rgba(COLORS["text_secondary"], 100), width=2)
    locked.save(os.path.join(path, "thumb_locked.png"))

    # Completion bar background
    comp_bg = Image.new("RGBA", (600, 24), (0, 0, 0, 0))
    draw = ImageDraw.Draw(comp_bg)
    draw_rounded_rect(draw, (0, 0, 599, 23), 6, fill=hex_to_rgba(COLORS["bar_bg"]))
    comp_bg.save(os.path.join(path, "completion_bar_bg.png"))

    # Completion bar fill (gold)
    comp_fill = Image.new("RGBA", (600, 24), (0, 0, 0, 0))
    draw = ImageDraw.Draw(comp_fill)
    draw_rounded_rect(draw, (0, 0, 599, 23), 6, fill=hex_to_rgba(COLORS["primary"]))
    comp_fill.save(os.path.join(path, "completion_bar_fill.png"))

    print("  [OK] Gallery assets")


def generate_save_load_assets():
    """Generate save/load screen assets."""
    path = os.path.join(OUTPUT_DIR, "saveload")
    ensure_dir(path)

    # Save slot frame (empty)
    slot = Image.new("RGBA", (280, 180), (0, 0, 0, 0))
    draw = ImageDraw.Draw(slot)
    draw_rounded_rect(draw, (0, 0, 279, 179), 10,
                      fill=hex_to_rgba(COLORS["surface"]),
                      outline=hex_to_rgba(COLORS["text_secondary"], 80), width=1)
    slot.save(os.path.join(path, "slot_empty.png"))

    # Save slot frame (filled/hover)
    slot_h = Image.new("RGBA", (280, 180), (0, 0, 0, 0))
    draw = ImageDraw.Draw(slot_h)
    draw_rounded_rect(draw, (0, 0, 279, 179), 10,
                      fill=hex_to_rgba(COLORS["surface"]),
                      outline=hex_to_rgba(COLORS["primary"]), width=2)
    slot_h.save(os.path.join(path, "slot_hover.png"))

    # Page tab
    tab = Image.new("RGBA", (100, 36), (0, 0, 0, 0))
    draw = ImageDraw.Draw(tab)
    draw_rounded_rect(draw, (0, 0, 99, 35), 6,
                      fill=hex_to_rgba(COLORS["surface"]),
                      outline=hex_to_rgba(COLORS["primary"], 100), width=1)
    tab.save(os.path.join(path, "page_tab.png"))

    # Active page tab
    tab_active = Image.new("RGBA", (100, 36), (0, 0, 0, 0))
    draw = ImageDraw.Draw(tab_active)
    draw_rounded_rect(draw, (0, 0, 99, 35), 6,
                      fill=hex_to_rgba(COLORS["primary"], 60),
                      outline=hex_to_rgba(COLORS["primary"]), width=2)
    tab_active.save(os.path.join(path, "page_tab_active.png"))

    print("  [OK] Save/Load assets")



def generate_main_menu_assets():
    """Generate main menu screen assets."""
    path = os.path.join(OUTPUT_DIR, "mainmenu")
    ensure_dir(path)

    # Dark overlay for main menu background
    overlay = Image.new("RGBA", (1920, 1080), hex_to_rgba(COLORS["bg"], 180))
    overlay.save(os.path.join(path, "menu_overlay.png"))

    # Title plate
    title_bg = Image.new("RGBA", (600, 80), (0, 0, 0, 0))
    draw = ImageDraw.Draw(title_bg)
    draw_rounded_rect(draw, (0, 0, 599, 79), 6,
                      fill=hex_to_rgba(COLORS["bg"], 200))
    # Gold underline
    draw.line([(50, 70), (550, 70)], fill=hex_to_rgba(COLORS["primary"]), width=2)
    title_bg.save(os.path.join(path, "title_plate.png"))

    # Menu button frame
    for state in ["normal", "hover"]:
        mbtn = Image.new("RGBA", (280, 55), (0, 0, 0, 0))
        draw = ImageDraw.Draw(mbtn)
        if state == "normal":
            draw_rounded_rect(draw, (0, 0, 279, 54), 6,
                              fill=hex_to_rgba(COLORS["bg"], 200),
                              outline=hex_to_rgba(COLORS["primary"], 100), width=1)
        else:
            draw_rounded_rect(draw, (0, 0, 279, 54), 6,
                              fill=hex_to_rgba(COLORS["primary"], 40),
                              outline=hex_to_rgba(COLORS["primary"]), width=2)
        mbtn.save(os.path.join(path, f"menu_btn_{state}.png"))

    print("  [OK] Main menu assets")


def generate_interaction_menu():
    """Generate room interaction menu assets."""
    path = os.path.join(OUTPUT_DIR, "interaction")
    ensure_dir(path)

    # Interaction panel background
    panel = Image.new("RGBA", (450, 500), (0, 0, 0, 0))
    draw = ImageDraw.Draw(panel)
    draw_rounded_rect(draw, (0, 0, 449, 499), 14,
                      fill=hex_to_rgba(COLORS["bg"], 240),
                      outline=hex_to_rgba(COLORS["primary"], 100), width=2)
    panel.save(os.path.join(path, "interaction_panel_bg.png"))

    # Interaction option row (normal / hover)
    for state in ["normal", "hover"]:
        row = Image.new("RGBA", (410, 45), (0, 0, 0, 0))
        draw = ImageDraw.Draw(row)
        if state == "normal":
            draw_rounded_rect(draw, (0, 0, 409, 44), 6,
                              fill=hex_to_rgba(COLORS["surface"], 180))
        else:
            draw_rounded_rect(draw, (0, 0, 409, 44), 6,
                              fill=hex_to_rgba(COLORS["primary"], 40),
                              outline=hex_to_rgba(COLORS["primary"], 150), width=1)
        row.save(os.path.join(path, f"option_row_{state}.png"))

    print("  [OK] Interaction menu")


def generate_overlay_screens():
    """Generate general overlay/modal backgrounds."""
    path = os.path.join(OUTPUT_DIR, "overlays")
    ensure_dir(path)

    # Full screen dim overlay (for modals/popups)
    dim = Image.new("RGBA", (1920, 1080), hex_to_rgba(COLORS["bg"], 200))
    dim.save(os.path.join(path, "screen_dim.png"))

    # Settings panel background
    settings = Image.new("RGBA", (900, 700), (0, 0, 0, 0))
    draw = ImageDraw.Draw(settings)
    draw_rounded_rect(draw, (0, 0, 899, 699), 16,
                      fill=hex_to_rgba(COLORS["bg"], 250),
                      outline=hex_to_rgba(COLORS["primary"], 120), width=2)
    settings.save(os.path.join(path, "settings_panel.png"))

    # Toggle switch (on/off)
    for state in ["on", "off"]:
        toggle = Image.new("RGBA", (50, 26), (0, 0, 0, 0))
        draw = ImageDraw.Draw(toggle)
        if state == "on":
            draw_rounded_rect(draw, (0, 0, 49, 25), 13, fill=hex_to_rgba(COLORS["primary"]))
            draw.ellipse((26, 2, 47, 23), fill=hex_to_rgba(COLORS["text"]))
        else:
            draw_rounded_rect(draw, (0, 0, 49, 25), 13, fill=hex_to_rgba(COLORS["bar_bg"]))
            draw.ellipse((2, 2, 23, 23), fill=hex_to_rgba(COLORS["text_secondary"]))
        toggle.save(os.path.join(path, f"toggle_{state}.png"))

    # Slider track + thumb
    track = Image.new("RGBA", (300, 8), (0, 0, 0, 0))
    draw = ImageDraw.Draw(track)
    draw_rounded_rect(draw, (0, 0, 299, 7), 4, fill=hex_to_rgba(COLORS["bar_bg"]))
    track.save(os.path.join(path, "slider_track.png"))

    thumb = Image.new("RGBA", (22, 22), (0, 0, 0, 0))
    draw = ImageDraw.Draw(thumb)
    draw.ellipse((0, 0, 21, 21), fill=hex_to_rgba(COLORS["primary"]))
    thumb.save(os.path.join(path, "slider_thumb.png"))

    print("  [OK] Overlay/modal assets")


# === MAIN EXECUTION ===

def main():
    """Generate all GUI assets."""
    print("=" * 60)
    print("  HOUSE OF INFLUENCE — GUI Asset Generator")
    print("=" * 60)
    print(f"  Output directory: {os.path.abspath(OUTPUT_DIR)}")
    print(f"  Resolution: {RESOLUTION[0]}x{RESOLUTION[1]}")
    print("-" * 60)

    ensure_dir(OUTPUT_DIR)

    generate_top_bar()
    generate_buttons()
    generate_dialogue_box()
    generate_stat_bars()
    generate_phone_ui()
    generate_map_assets()
    generate_choice_menu()
    generate_hscene_ui()
    generate_minigame_ui()
    generate_notification_assets()
    generate_gallery_assets()
    generate_save_load_assets()
    generate_main_menu_assets()
    generate_interaction_menu()
    generate_overlay_screens()

    # Count total files generated
    total = 0
    for root, dirs, files in os.walk(OUTPUT_DIR):
        total += len([f for f in files if f.endswith(".png")])

    print("-" * 60)
    print(f"  DONE! Total assets generated: {total} PNG files")
    print(f"  Location: {os.path.abspath(OUTPUT_DIR)}")
    print("=" * 60)


if __name__ == "__main__":
    main()


def generate_phone_icons():
    """Generate phone app icons with simple symbolic graphics."""
    path = os.path.join(OUTPUT_DIR, "phone", "icons")
    ensure_dir(path)

    icon_size = 48

    def make_icon(name, draw_func):
        img = Image.new("RGBA", (icon_size, icon_size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        draw_func(draw, icon_size)
        img.save(os.path.join(path, f"icon_{name}.png"))

    # Stats icon (bar chart)
    def draw_stats(draw, s):
        bar_w = 8
        draw.rectangle((8, 28, 8+bar_w, s-6), fill=hex_to_rgba(COLORS["success"]))
        draw.rectangle((20, 18, 20+bar_w, s-6), fill=hex_to_rgba(COLORS["primary"]))
        draw.rectangle((32, 10, 32+bar_w, s-6), fill=hex_to_rgba(COLORS["yuki"]))

    # Messages icon (chat bubble)
    def draw_messages(draw, s):
        draw_rounded_rect(draw, (6, 6, s-6, s-14), 8, fill=hex_to_rgba(COLORS["primary"]))
        draw.polygon([(14, s-14), (14, s-6), (22, s-14)], fill=hex_to_rgba(COLORS["primary"]))
        # dots
        for x in [16, 24, 32]:
            draw.ellipse((x, 18, x+4, 22), fill=hex_to_rgba(COLORS["bg"]))

    # Camera icon
    def draw_camera(draw, s):
        draw_rounded_rect(draw, (6, 14, s-6, s-8), 6, fill=hex_to_rgba(COLORS["text_secondary"]))
        draw.rectangle((16, 8, 32, 14), fill=hex_to_rgba(COLORS["text_secondary"]))
        draw.ellipse((16, 18, 32, 34), outline=hex_to_rgba(COLORS["text"]), width=2)
        draw.ellipse((20, 22, 28, 30), fill=hex_to_rgba(COLORS["primary"]))

    # Shop icon (cart)
    def draw_shop(draw, s):
        draw.line([(8, 12), (14, 12), (18, 32), (38, 32)], fill=hex_to_rgba(COLORS["primary"]), width=3)
        draw.line([(14, 12), (40, 12), (36, 28), (18, 28)], fill=hex_to_rgba(COLORS["primary"]), width=2)
        draw.ellipse((18, 34, 24, 40), fill=hex_to_rgba(COLORS["primary"]))
        draw.ellipse((32, 34, 38, 40), fill=hex_to_rgba(COLORS["primary"]))

    # Diary icon (notebook)
    def draw_diary(draw, s):
        draw_rounded_rect(draw, (10, 6, s-8, s-6), 4, fill=hex_to_rgba(COLORS["surface"]),
                          outline=hex_to_rgba(COLORS["primary"]), width=2)
        draw.line([(16, 6), (16, s-6)], fill=hex_to_rgba(COLORS["primary"]), width=2)
        for y in [16, 22, 28, 34]:
            draw.line([(20, y), (36, y)], fill=hex_to_rgba(COLORS["text_secondary"]), width=1)

    # Settings icon (gear)
    def draw_settings(draw, s):
        cx, cy, r = s//2, s//2, 14
        draw.ellipse((cx-r, cy-r, cx+r, cy+r), outline=hex_to_rgba(COLORS["text_secondary"]), width=3)
        draw.ellipse((cx-6, cy-6, cx+6, cy+6), fill=hex_to_rgba(COLORS["text_secondary"]))
        # gear teeth (simplified as lines)
        import math
        for angle in range(0, 360, 45):
            rad = math.radians(angle)
            x1 = cx + int((r-2) * math.cos(rad))
            y1 = cy + int((r-2) * math.sin(rad))
            x2 = cx + int((r+4) * math.cos(rad))
            y2 = cy + int((r+4) * math.sin(rad))
            draw.line([(x1, y1), (x2, y2)], fill=hex_to_rgba(COLORS["text_secondary"]), width=3)

    # Gallery icon (image frame)
    def draw_gallery(draw, s):
        draw_rounded_rect(draw, (6, 10, s-6, s-10), 4, outline=hex_to_rgba(COLORS["primary"]), width=2)
        # mountain silhouette
        draw.polygon([(10, 34), (20, 20), (28, 28), (38, 16), (42, 34)],
                     fill=hex_to_rgba(COLORS["primary"], 120))
        # sun
        draw.ellipse((12, 14, 20, 22), fill=hex_to_rgba(COLORS["primary"]))

    # Quest icon (clipboard/checklist)
    def draw_quests(draw, s):
        draw_rounded_rect(draw, (10, 6, s-10, s-6), 4, fill=hex_to_rgba(COLORS["surface"]),
                          outline=hex_to_rgba(COLORS["text_secondary"]), width=2)
        # clip
        draw.rectangle((18, 4, 30, 10), fill=hex_to_rgba(COLORS["text_secondary"]))
        # checkmarks
        for y in [16, 24, 32]:
            draw.line([(14, y+2), (17, y+5), (22, y)], fill=hex_to_rgba(COLORS["success"]), width=2)
            draw.line([(25, y+2), (34, y+2)], fill=hex_to_rgba(COLORS["text_secondary"]), width=2)

    # Spy icon (magnifying glass)
    def draw_spy(draw, s):
        draw.ellipse((8, 8, 30, 30), outline=hex_to_rgba(COLORS["danger"]), width=3)
        draw.line([(28, 28), (40, 40)], fill=hex_to_rgba(COLORS["danger"]), width=3)
        draw.ellipse((14, 14, 24, 24), fill=hex_to_rgba(COLORS["danger"], 60))

    # Generate all icons
    icons = {
        "stats": draw_stats,
        "messages": draw_messages,
        "camera": draw_camera,
        "shop": draw_shop,
        "diary": draw_diary,
        "settings": draw_settings,
        "gallery": draw_gallery,
        "quests": draw_quests,
        "spy": draw_spy,
    }

    for name, func in icons.items():
        make_icon(name, func)

    print("  [OK] Phone app icons (9 icons)")


# Update main to include icons
if __name__ == "__main__":
    generate_phone_icons()
    # Count new files
    icon_path = os.path.join(OUTPUT_DIR, "phone", "icons")
    count = len([f for f in os.listdir(icon_path) if f.endswith(".png")])
    print(f"  Generated {count} phone icons in {icon_path}")
