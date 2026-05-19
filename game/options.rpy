# ============================================================
# OPTIONS.RPY — Game Configuration for "House of Influence"
# ============================================================

define config.name = _("House of Influence")
define config.version = "0.1.0"
define build.name = "HouseOfInfluence"

# Resolution
define config.screen_width = 1920
define config.screen_height = 1080

# Window settings
define config.window = "auto"
define config.window_title = "House of Influence v0.1"

# Save directory
define config.save_directory = "HouseOfInfluence-saves"

# Sound
define config.has_sound = True
define config.has_music = True
define config.has_voice = False

define config.default_music_volume = 0.7
define config.default_sfx_volume = 0.8

# Transitions
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = dissolve
define config.end_game_transition = dissolve

# Text speed
define config.default_text_cps = 40

# Auto-forward
define config.default_afm_time = 15
define config.default_afm_enable = False

# Skip
define config.allow_skipping = True
define config.fast_skipping = False
define config.skip_indicator = True

# Layers
define config.layers = ['master', 'transient', 'screens', 'overlay', 'hud']

# Mouse
define config.mouse = None

# Rollback
define config.rollback_enabled = True
define config.hard_rollback_limit = 100

# Developer mode (disable for release)
define config.developer = True

# Garbage collection
define config.predict_statements = 50

# ============================================================
# BUILD CONFIGURATION
# ============================================================

init python:
    # File patterns for build
    build.classify("**~", None)
    build.classify("**.bak", None)
    build.classify("**/.**", None)
    build.classify("**/#**", None)
    build.classify("**/thumbs.db", None)
    build.classify("**.rpy", None)
    build.classify("**.psd", None)
    build.classify("game/**.rpyc", "archive")
    build.classify("game/images/**", "archive")
    build.classify("game/gui/**", "archive")
    build.classify("game/audio/**", "archive")
    build.classify("**", "archive")

    # Platforms
    build.archive("archive", "all")

    # Documentation
    build.documentation("README.md")
