# ============================================================
# GUI.RPY — GUI Configuration for "House of Influence"
# Theme: Dark Modern (Black/Navy + Gold Accent)
# Resolution: 1920x1080
# ============================================================

init python:
    gui.init(1920, 1080)

# --- TEXT SIZES ---
define gui.text_size = 24
define gui.name_text_size = 28
define gui.interface_text_size = 22
define gui.label_text_size = 30
define gui.notify_text_size = 20
define gui.title_text_size = 52
define gui.quick_button_text_size = 16

# --- COLORS ---
define gui.accent_color = "#D4A845"
define gui.idle_color = "#8A8A8A"
define gui.idle_small_color = "#6A6A7A"
define gui.hover_color = "#D4A845"
define gui.selected_color = "#D4A845"
define gui.insensitive_color = "#4A4A5A"
define gui.muted_color = "#3A3A4E"
define gui.hover_muted_color = "#5A5A7E"
define gui.text_color = "#E8E6E3"
define gui.interface_text_color = "#E8E6E3"
define gui.choice_text_color = "#E8E6E3"

# --- FONTS (fallback to DejaVuSans if custom not found) ---
define gui.text_font = gui.preference("font", "DejaVuSans.ttf")
define gui.name_text_font = gui.preference("font", "DejaVuSans.ttf")
define gui.interface_text_font = gui.preference("font", "DejaVuSans.ttf")

# --- DIALOGUE BOX ---
define gui.textbox_height = 200
define gui.textbox_yalign = 1.0
define gui.dialogue_xpos = 50
define gui.dialogue_ypos = 50
define gui.dialogue_width = 1700
define gui.dialogue_text_xalign = 0.0

# --- CHARACTER NAME ---
define gui.name_xpos = 30
define gui.name_ypos = 5
define gui.name_xalign = 0.0
define gui.namebox_width = 250
define gui.namebox_height = 40
define gui.namebox_borders = Borders(5, 5, 5, 5)

# --- CHOICE BUTTONS ---
define gui.choice_button_width = 700
define gui.choice_button_height = 55
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(20, 8, 20, 8)
define gui.choice_button_text_xalign = 0.5

# --- BUTTONS ---
define gui.button_width = None
define gui.button_height = 50
define gui.button_borders = Borders(8, 5, 8, 5)
define gui.button_tile = False
define gui.button_text_xalign = 0.5
define gui.navigation_button_width = 280

# --- BARS ---
define gui.bar_size = 16
define gui.scrollbar_size = 12
define gui.slider_size = 20
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False
define gui.bar_borders = Borders(4, 4, 4, 4)
define gui.scrollbar_borders = Borders(4, 4, 4, 4)
define gui.slider_borders = Borders(4, 4, 4, 4)

# --- FRAMES ---
define gui.frame_borders = Borders(8, 8, 8, 8)
define gui.confirm_frame_borders = Borders(30, 30, 30, 30)
define gui.skip_frame_borders = Borders(12, 6, 40, 6)

# --- SAVE/LOAD ---
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2
define config.thumbnail_width = 256
define config.thumbnail_height = 144

# --- HISTORY ---
define config.history_length = 250
define gui.history_height = 140
define gui.history_name_xpos = 160
define gui.history_name_ypos = 0
define gui.history_name_width = 160
define gui.history_name_xalign = 1.0
define gui.history_text_xpos = 180
define gui.history_text_ypos = 2
define gui.history_text_width = 700
define gui.history_text_xalign = 0.0

# --- SKIP / NOTIFY ---
define gui.skip_ypos = 10
define gui.notify_ypos = 45

# --- MOBILE ---
init python:
    if renpy.variant("small"):
        gui.text_size = 28
        gui.name_text_size = 32
        gui.notify_text_size = 24
        gui.interface_text_size = 26
        gui.choice_button_width = 900
        gui.navigation_button_width = 340
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2
