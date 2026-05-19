# ============================================================
# GUI.RPY — GUI Configuration for "House of Influence"
# Theme: Dark Modern (Black/Navy + Gold Accent)
# Resolution: 1920x1080
# ============================================================

init -2:

    # --- RESOLUTION ---
    define gui.text_size = 24
    define gui.name_text_size = 28
    define gui.interface_text_size = 22
    define gui.label_text_size = 30
    define gui.notify_text_size = 20
    define gui.title_text_size = 52

    # --- COLORS (from gui_plan.md) ---
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

    # Character name colors
    define gui.marina_color = "#6B3FA0"
    define gui.kaori_color = "#C17817"
    define gui.yuki_color = "#D4789C"

    # --- FONTS ---
    define gui.text_font = "gui/fonts/Inter-Regular.ttf"
    define gui.name_text_font = "gui/fonts/Inter-SemiBold.ttf"
    define gui.interface_text_font = "gui/fonts/Inter-Regular.ttf"

    # Fallback to default if custom fonts not found
    define gui.default_font = gui.text_font

    # --- DIALOGUE BOX ---
    define gui.textbox_height = 200
    define gui.textbox_yalign = 1.0

    # Dialogue text positioning within the box
    define gui.dialogue_xpos = 340
    define gui.dialogue_ypos = 60
    define gui.dialogue_width = 1200
    define gui.dialogue_text_xalign = 0.0

    # Character name positioning
    define gui.name_xpos = 80
    define gui.name_ypos = 10
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
    define gui.choice_button_text_idle_color = "#E8E6E3"
    define gui.choice_button_text_hover_color = "#D4A845"

    # --- BUTTONS (General) ---
    define gui.button_width = None
    define gui.button_height = 50
    define gui.button_borders = Borders(8, 5, 8, 5)
    define gui.button_tile = False
    define gui.button_text_xalign = 0.5

    define gui.navigation_button_width = 280

    # --- BARS ---
    define gui.bar_size = 16
    define gui.scrollbar_size = 8
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

    # --- WINDOW ---
    define config.window_icon = None

    # --- SAVE/LOAD ---
    define gui.file_slot_cols = 3
    define gui.file_slot_rows = 2
    define config.thumbnail_width = 280
    define config.thumbnail_height = 158

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

    # --- NVL ---
    define gui.nvl_borders = Borders(0, 10, 0, 20)
    define gui.nvl_height = 115
    define gui.nvl_spacing = 10
    define gui.nvl_name_xpos = 430
    define gui.nvl_name_ypos = 0
    define gui.nvl_name_width = 150
    define gui.nvl_name_xalign = 1.0
    define gui.nvl_text_xpos = 450
    define gui.nvl_text_ypos = 8
    define gui.nvl_text_width = 590
    define gui.nvl_text_xalign = 0.0
    define gui.nvl_thought_xpos = 240
    define gui.nvl_thought_ypos = 0
    define gui.nvl_thought_width = 780
    define gui.nvl_thought_xalign = 0.0
    define gui.nvl_button_xpos = 450
    define gui.nvl_button_xalign = 0.0

    # --- QUICK MENU ---
    define gui.quick_button_text_size = 16

    # --- SKIP INDICATOR ---
    define gui.skip_ypos = 10
    define gui.notify_ypos = 45

    # --- MOBILE OVERRIDES ---
    if renpy.variant("small"):
        define gui.text_size = 28
        define gui.name_text_size = 32
        define gui.notify_text_size = 24
        define gui.interface_text_size = 26
        define gui.choice_button_width = int(config.screen_width * 0.9)
        define gui.navigation_button_width = 340
        define gui.file_slot_cols = 2
        define gui.file_slot_rows = 2

