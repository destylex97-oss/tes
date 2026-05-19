# ============================================================
# OPTIONS.RPY — Game Config for "House of Influence"
# ============================================================

define config.name = _("House of Influence")
define config.version = "0.1.0"
define build.name = "HouseOfInfluence"

define config.screen_width = 1920
define config.screen_height = 1080
define config.window = "auto"
define config.save_directory = "HouseOfInfluence-saves"

define config.has_sound = True
define config.has_music = True
define config.has_voice = False

define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = dissolve
define config.end_game_transition = dissolve

define config.default_text_cps = 40
define config.default_afm_time = 15
define config.default_afm_enable = False

define config.allow_skipping = True
define config.fast_skipping = False
define config.skip_indicator = True

define config.rollback_enabled = True
define config.hard_rollback_limit = 100

define config.developer = True

init python:
    build.classify("**~", None)
    build.classify("**.bak", None)
    build.classify("**/.**", None)
    build.classify("**/#**", None)
    build.classify("**/thumbs.db", None)
    build.classify("**.rpy", None)
    build.classify("**.psd", None)
    build.classify("**", "archive")
    build.documentation("README.md")
