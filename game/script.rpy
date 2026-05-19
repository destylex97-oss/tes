# ============================================================
# SCRIPT.RPY — Main script (Layout/GUI Test)
# ============================================================

define mc = Character("You", color="#E8E6E3")
define marina_char = Character("Marina", color="#6B3FA0")
define kaori_char = Character("Kaori", color="#C17817")
define yuki_char = Character("Yuki", color="#D4789C")

default day = 1
default time_slot = 0
default time_text = "Morning"
default time_icon = "☀"
default money = 100
default skill_level = 1
default skill_name = "Observer"
default phone_notifications = 2
default current_room_character = None
default marina_unlocked = True
default kaori_unlocked = True
default yuki_unlocked = True
default kaori_room_unlocked = False
default outside_unlocked = False
default marina_affection = 15
default marina_corruption = 5
default marina_obedience = 0
default marina_desire = 30
default marina_suspicion = 0
default kaori_affection = 5
default kaori_corruption = 10
default kaori_obedience = 0
default kaori_desire = 20
default kaori_suspicion = 15
default yuki_affection = 40
default yuki_corruption = 8
default yuki_obedience = 10
default yuki_desire = 55
default yuki_suspicion = 0

label start:
    scene black with fade
    "Welcome to {b}House of Influence{/b} — GUI Test Build"
    jump sandbox_test

label sandbox_test:
    scene black
    show screen hud_top_bar
    show screen hud_bottom_nav
    menu:
        "What do you want to test?"
        "Open Phone":
            call screen phone_screen
            jump sandbox_test
        "Open Map":
            call screen sandbox_map
            jump sandbox_test
        "Open Stats":
            call screen stats_screen
            jump sandbox_test
        "Test Dialogue":
            jump test_dialogue
        "Test Notifications":
            jump test_notif
        "Advance Time":
            jump advance_time
        "Work (+$30)":
            $ money += 30
            jump sandbox_test
        "Quit":
            jump test_end

label test_dialogue:
    hide screen hud_bottom_nav
    marina_char "Good morning, sweetheart. Did you sleep well?"
    mc "Yeah... thanks."
    kaori_char "Tch. Move. You're in my way."
    yuki_char "Onii-chan~! Good morning!"
    "Each of them hides something behind their smile."
    show screen hud_bottom_nav
    jump sandbox_test

label test_notif:
    show screen stat_notification("Marina", "Affection", 5)
    $ marina_affection += 5
    "Stat notification shown (top-right)."
    show screen discovery_popup("Secret Found", "Marina's diary in locked drawer.")
    "Discovery popup shown."
    jump sandbox_test

label advance_time:
    $ time_slot += 1
    if time_slot == 1:
        $ time_text = "Noon"
        $ time_icon = "☀"
    elif time_slot == 2:
        $ time_text = "Evening"
        $ time_icon = "🌅"
    elif time_slot == 3:
        $ time_text = "Night"
        $ time_icon = "🌙"
    else:
        $ time_slot = 0
        $ time_text = "Morning"
        $ time_icon = "☀"
        $ day += 1
    "Time: [time_text] (Day [day])"
    jump sandbox_test

label goto_mc_room:
    "MC's room."
    jump sandbox_test
label goto_bathroom:
    "Bathroom."
    jump sandbox_test
label goto_yuki_room:
    $ current_room_character = "Yuki"
    "Yuki's room."
    jump sandbox_test
label goto_kaori_room:
    "Locked!"
    jump sandbox_test
label goto_marina_room:
    $ current_room_character = "Marina"
    "Marina's room."
    jump sandbox_test
label goto_kitchen:
    $ current_room_character = "Marina"
    "Kitchen. Marina cooking."
    jump sandbox_test
label goto_living_room:
    $ current_room_character = "Kaori"
    "Living room. Kaori on couch."
    jump sandbox_test
label goto_laundry:
    "Laundry room."
    jump sandbox_test
label goto_study:
    "Study."
    jump sandbox_test
label goto_entrance:
    "Entrance."
    jump sandbox_test
label goto_mall:
    "Mall."
    jump sandbox_test
label goto_park:
    "Park."
    jump sandbox_test

label interact_menu:
    "[current_room_character] is here."
    jump sandbox_test
label spy_menu:
    "You observe..."
    jump sandbox_test
label work_menu:
    $ money += 30
    "Earned $30."
    jump sandbox_test

label test_end:
    hide screen hud_top_bar
    hide screen hud_bottom_nav
    scene black with fade
    "Test complete."
    return
