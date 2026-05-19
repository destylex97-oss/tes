# GUI / UI PLAN — "House of Influence"
## Theme, Layout, and HUD Design

---

## 1. GENERAL SPECS

| Spec | Value |
|------|-------|
| **Resolution** | 1920x1080 (16:9) |
| **Engine** | Ren'Py (Python-based screens) |
| **Theme** | Dark modern — matte black, deep navy, accent gold/amber |
| **Font** | Sans-serif for UI (Montserrat/Inter), serif for dialogue (Noto Serif) |
| **Responsive** | Scale down for 1280x720 (Android/lower-end) |
| **Orientation** | Landscape (PC primary, mobile secondary) |

---

## 2. COLOR PALETTE

| Element | Color | Hex | Usage |
|---------|-------|-----|-------|
| **Background** | Near-black | #0D0D0F | Panels, overlays |
| **Surface** | Dark navy | #1A1A2E | Cards, containers |
| **Primary** | Amber/Gold | #D4A845 | Highlights, selected items, headers |
| **Accent** | Deep red | #8B1A1A | Warnings, suspicion, NTR indicators |
| **Text Primary** | Off-white | #E8E6E3 | Body text |
| **Text Secondary** | Grey | #8A8A8A | Labels, hints |
| **Marina** | Deep purple | #6B3FA0 | Her stat bars, name color |
| **Kaori** | Burnt amber | #C17817 | Her stat bars, name color |
| **Yuki** | Soft pink | #D4789C | Her stat bars, name color |
| **Success** | Teal green | #2ECC71 | Positive stat gains |
| **Danger** | Crimson | #E74C3C | Negative events, suspicion high |

---

## 3. SCREEN FLOW (Navigation Map)

```
┌─────────────────────────────────────────────────┐
│                  MAIN MENU                        │
│  [New Game] [Continue] [Gallery] [Settings]      │
└───────────┬─────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────────┐
│              CONTENT SETTINGS                     │
│  (NTR toggles, scene toggles — first time only)  │
└───────────┬─────────────────────────────────────┘
            ↓
┌─────────────────────────────────────────────────┐
│              GAMEPLAY LOOP                        │
│                                                   │
│  ┌─────────┐   ┌──────────┐   ┌──────────────┐ │
│  │SANDBOX  │──→│  EVENT/  │──→│  DIALOGUE/   │ │
│  │  MAP    │   │  SCENE   │   │  CHOICE      │ │
│  └────┬────┘   └──────────┘   └──────────────┘ │
│       │                                          │
│       ↓                                          │
│  ┌─────────┐   ┌──────────┐   ┌──────────────┐ │
│  │  PHONE  │   │MINI-GAME │   │   H-SCENE    │ │
│  │  (HUB)  │   │          │   │  (SPECIAL UI)│ │
│  └─────────┘   └──────────┘   └──────────────┘ │
└─────────────────────────────────────────────────┘
```

---


## 4. HUD — ALWAYS VISIBLE (During Sandbox Navigation)

```
┌─────────────────────────────────────────────────────────────────┐
│ TOP BAR (Always visible during sandbox)                          │
│                                                                   │
│  ┌──────┐  ┌─────────────┐  ┌────────┐  ┌─────┐  ┌──────────┐ │
│  │ DAY  │  │  TIME SLOT  │  │ MONEY  │  │SKILL│  │  PHONE   │ │
│  │  12  │  │  ☀ Morning  │  │ $450   │  │ Lv3 │  │  [📱]    │ │
│  └──────┘  └─────────────┘  └────────┘  └─────┘  └──────────┘ │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│                    [ MAIN SCENE AREA ]                            │
│                   (Background + Sprites)                          │
│                      1920 x 880 px                                │
│                                                                   │
├─────────────────────────────────────────────────────────────────┤
│ BOTTOM BAR (Context-sensitive)                                    │
│                                                                   │
│  During Navigation:                                               │
│  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────────────┐│
│  │  MAP   │ │INTERACT│ │  SPY   │ │  WORK  │ │ ADVANCE TIME →││
│  └────────┘ └────────┘ └────────┘ └────────┘ └────────────────┘│
│                                                                   │
│  During Dialogue:                                                 │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │ [CHARACTER NAME]                                             ││
│  │ "Dialogue text goes here..."                                 ││
│  │                                              [Auto][Skip][▶]││
│  └─────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
```

### Top Bar Elements:

| Element | Display | Notes |
|---------|---------|-------|
| **Day Counter** | "Day 12" | Current in-game day |
| **Time Slot** | Icon + text: ☀ Morning / ☀ Noon / 🌅 Evening / 🌙 Night | Shows current time period |
| **Money** | "$450" | Current cash, flashes green when gained, red when spent |
| **Skill Level** | "Lv3 Manipulator" | MC's current skill tier (abbreviated) |
| **Phone Button** | 📱 icon | Tap to open phone hub (notifications badge if new content) |

---


## 5. SANDBOX MAP SCREEN

When player clicks "MAP" — fullscreen overlay shows house layout:

```
┌─────────────────────────────────────────────────────────────────┐
│                    🏠 HOUSE MAP                                   │
│                                         [Close X]                │
│  ┌─ SECOND FLOOR ──────────────────────────────────────────────┐│
│  │                                                              ││
│  │  ┌──────────┐   ┌──────────────┐   ┌──────────┐           ││
│  │  │ MC Room  │   │   Bathroom   │   │Yuki Room │           ││
│  │  │  [🛏️]   │   │    [🚿]      │   │  [🎀]   │           ││
│  │  └──────────┘   └──────────────┘   └──────────┘           ││
│  │  ┌──────────┐                       ┌──────────┐           ││
│  │  │Kaori Room│                       │Marina Rm │           ││
│  │  │  [💼]🔒 │                       │  [💜]   │           ││
│  │  └──────────┘                       └──────────┘           ││
│  └──────────────────────────────────────────────────────────────┘│
│  ┌─ FIRST FLOOR ───────────────────────────────────────────────┐│
│  │                                                              ││
│  │  ┌──────────┐   ┌──────────────┐   ┌──────────┐           ││
│  │  │ Kitchen  │   │  Living Room │   │ Entrance │           ││
│  │  │  [🍳]   │   │    [📺]      │   │  [🚪]   │           ││
│  │  └──────────┘   └──────────────┘   └──────────┘           ││
│  │  ┌──────────┐   ┌──────────────┐                           ││
│  │  │ Laundry  │   │    Study     │   [🌳 OUTSIDE →]         ││
│  │  │  [👙]   │   │    [📚]      │                           ││
│  │  └──────────┘   └──────────────┘                           ││
│  └──────────────────────────────────────────────────────────────┘│
│                                                                   │
│  ICONS ON ROOMS:                                                  │
│  👤 = Character is here    🔒 = Locked    ⚡ = Event available   │
│  💬 = New dialogue          🔥 = H-scene available               │
└─────────────────────────────────────────────────────────────────┘
```

### Map Features:
- Rooms show **character portrait thumbnails** if someone is there
- Rooms glow slightly if event is available (subtle pulse animation)
- 🔒 icon on locked rooms (Kaori's room until lock pick)
- Time-of-day affects which rooms have characters
- Click room → zooms in → shows interaction options

---


## 6. PHONE UI (Central Hub)

Phone is the MAIN HUB for all information. Accessed via 📱 button on top bar.

```
┌─────────────────────────────────────────┐
│          ┌─────────────────┐            │
│          │   📱 PHONE      │            │
│          │                 │            │
│          │  ┌───────────┐  │            │
│          │  │  12:34 PM │  │            │
│          │  │  Day 12   │  │            │
│          │  └───────────┘  │            │
│          │                 │            │
│          │ ┌──┐┌──┐┌──┐  │            │
│          │ │📊││💬││📷│  │            │
│          │ └──┘└──┘└──┘  │            │
│          │ Stats Msgs Cam │            │
│          │                 │            │
│          │ ┌──┐┌──┐┌──┐  │            │
│          │ │🛒││📓││⚙️│  │            │
│          │ └──┘└──┘└──┘  │            │
│          │ Shop Diary Set │            │
│          │                 │            │
│          │ ┌──┐┌──┐┌──┐  │            │
│          │ │🖼️││📋││🔍│  │            │
│          │ └──┘└──┘└──┘  │            │
│          │ Gal  Quest Spy │            │
│          │                 │            │
│          └─────────────────┘            │
│                                         │
│            [Close Phone]                │
└─────────────────────────────────────────┘
```

### Phone Apps:

| App | Icon | Function |
|-----|------|----------|
| **Stats** | 📊 | View all character stats (Affection, Corruption, Obedience, Desire, Suspicion) |
| **Messages** | 💬 | Phone Clone messages — read heroine chats, NTR chat progression |
| **Camera** | 📷 | Review hidden camera footage, saved photos, blackmail evidence |
| **Shop** | 🛒 | Buy items (gifts, equipment, consumables) — delivered next day |
| **Diary** | 📓 | MC's notes — hints, discovered secrets, schedule tracker |
| **Settings** | ⚙️ | Game settings, content toggles, save/load |
| **Gallery** | 🖼️ | Unlocked CGs, scene replay, completion % |
| **Quests** | 📋 | Active objectives, character progression tracker |
| **Spy Tools** | 🔍 | Manage installed cameras, phone clones, lock picks |

### Notification System:
- Red badge number on app icons when new content available
- Phone "vibrates" (screen shake) when important event discovered
- NTR chat updates show as push notifications at top of screen

---


## 7. STATS SCREEN (Phone → Stats)

```
┌─────────────────────────────────────────────────────────────────┐
│  CHARACTER STATS                                    [Close X]    │
│                                                                   │
│  ┌─── MARINA ─────────────────────────────────────────────────┐ │
│  │ [Portrait]  Affection:  ████████░░░░░░░░  52/100           │ │
│  │             Corruption: ██████░░░░░░░░░░  38/100           │ │
│  │  Age: 38    Obedience:  ████░░░░░░░░░░░░  25/100           │ │
│  │  Mood: 😊   Desire:     ███████████░░░░░  72/100           │ │
│  │             Suspicion:  ██░░░░░░░░░░░░░░  12/100   [SAFE]  │ │
│  └────────────────────────────────────────────────────────────┘ │
│                                                                   │
│  ┌─── KAORI ──────────────────────────────────────────────────┐ │
│  │ [Portrait]  Affection:  ███░░░░░░░░░░░░░  18/100           │ │
│  │             Corruption: █████░░░░░░░░░░░  30/100           │ │
│  │  Age: 23    Obedience:  ██░░░░░░░░░░░░░░  10/100           │ │
│  │  Mood: 😤   Desire:     ██████░░░░░░░░░░  40/100           │ │
│  │             Suspicion:  ████████░░░░░░░░  55/100   [⚠️]    │ │
│  └────────────────────────────────────────────────────────────┘ │
│                                                                   │
│  ┌─── YUKI ───────────────────────────────────────────────────┐ │
│  │ [Portrait]  Affection:  █████████░░░░░░░  60/100           │ │
│  │             Corruption: ████░░░░░░░░░░░░  22/100           │ │
│  │  Age: 18    Obedience:  ██████░░░░░░░░░░  35/100           │ │
│  │  Mood: 😍   Desire:     ████████████████  95/100           │ │
│  │             Suspicion:  █░░░░░░░░░░░░░░░  5/100    [SAFE]  │ │
│  │                                          Obsession: ██████░ │ │
│  └────────────────────────────────────────────────────────────┘ │
│                                                                   │
│  Legend: [SAFE] = no risk  [⚠️] = approaching danger             │
│          [🚨] = critical (>80)  [☠️] = route will fail           │
└─────────────────────────────────────────────────────────────────┘
```

### Stat Bar Design:
- Bars color-coded: Affection=green, Corruption=purple, Obedience=blue, Desire=pink, Suspicion=red
- Bars animate smoothly when values change
- "+5" or "-3" pop up briefly when stat changes (feedback)
- Yuki has extra "Obsession" bar (unique to her, shows in orange)
- Mood emoji changes based on recent interactions

---


## 8. DIALOGUE BOX

### Standard Dialogue:
```
┌─────────────────────────────────────────────────────────────────┐
│                                                                   │
│                     [Scene / Background]                          │
│                     [Character Sprite]                            │
│                                                                   │
│                                                                   │
├─────────────────────────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────────────────────────┐ │
│ │  Marina                                                      │ │
│ │  ─────────────────────────────────────────────────────────── │ │
│ │  "Good morning, sweetheart. I made breakfast — your          │ │
│ │   favorite. Come sit down."                                  │ │
│ │                                                              │ │
│ │                           [Auto] [Skip] [Log] [▶ Next]      │ │
│ └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

### Choice Menu:
```
┌─────────────────────────────────────────────────────────────────┐
│                     [Scene / Background]                          │
│                     [Character Sprite]                            │
│                                                                   │
│         ┌────────────────────────────────────────┐               │
│         │  "Compliment her cooking" [Affection+] │               │
│         ├────────────────────────────────────────┤               │
│         │  "Stare at her chest"     [Desire+]    │               │
│         ├────────────────────────────────────────┤               │
│         │  "Brush against her"      [Corruption+]│               │
│         ├────────────────────────────────────────┤               │
│         │  "Ignore her"             [—]          │               │
│         └────────────────────────────────────────┘               │
│                                                                   │
├─────────────────────────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────────────────────────┐ │
│ │  [What do you do?]                                           │ │
│ └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

### Choice Design:
- Choices show **stat hint** in brackets (which stat affected)
- Locked choices shown greyed out with requirement: "[Requires: Corruption 40+]"
- Hover effect: choice box glows with stat color (green=affection, purple=corruption, etc.)
- After choosing: brief "+5 Affection" popup near character portrait

---

## 9. H-SCENE UI (Special Mode)

During H-scenes, UI changes to minimal/cinematic:

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                   │
│                                                                   │
│                        [H-SCENE CG]                              │
│                    (Full screen artwork)                          │
│                                                                   │
│                                                                   │
│                                                                   │
│                                                                   │
├─────────────────────────────────────────────────────────────────┤
│ ┌─ H-SCENE CONTROLS ─────────────────────────────────────────┐ │
│ │                                                              │ │
│ │  [◀ Slower]  ████████████▓░░░  [Faster ▶]    PACE BAR      │ │
│ │                                                              │ │
│ │  ┌─────────────────────────────────────────────────┐        │ │
│ │  │ "Ahh... not so rough... mmm... okay, more..."  │        │ │
│ │  └─────────────────────────────────────────────────┘        │ │
│ │                                                              │ │
│ │  [Switch Position]   [Finish ▼]   [Hide UI]                 │ │
│ └──────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

### H-Scene UI Elements:
| Element | Function |
|---------|----------|
| **Pace Bar** | Player controls speed — affects dialogue & CG animation (if animated) |
| **Dialogue** | Character moans/words — changes with pace and position |
| **Switch Position** | Opens position selector mid-scene |
| **Finish Menu** | Dropdown: where to cum (inside/face/mouth/body/etc.) |
| **Hide UI** | One-click hides ALL UI — full CG view (tap to bring back) |
| **Mini-game Overlay** | If mini-game active: rhythm indicators appear above pace bar |

### Position Selector (Mid-Scene Popup):
```
┌─────────────────────────────────────────┐
│  SWITCH POSITION:                        │
│                                          │
│  ┌────────┐ ┌────────┐ ┌────────┐      │
│  │Mission-│ │ Doggy  │ │Cowgirl │      │
│  │  ary   │ │        │ │        │      │
│  │ [👆]  │ │ [🔥]  │ │ [💕]  │      │
│  └────────┘ └────────┘ └────────┘      │
│  ┌────────┐ ┌────────┐ ┌────────┐      │
│  │Standing│ │ Prone  │ │Mating  │      │
│  │        │ │  Bone  │ │ Press  │      │
│  │ [⚡]  │ │ [😈]  │ │ [🔒]  │      │
│  └────────┘ └────────┘ └────────┘      │
│                                          │
│  🔒 = Requires higher Corruption/Obed.  │
└─────────────────────────────────────────┘
```

---


## 10. MINI-GAME UI

### Money Mini-Game (Delivery — Timing):
```
┌─────────────────────────────────────────────────────────────────┐
│  DELIVERY JOB                                          $35 earned│
│                                                                   │
│                    ┌──────────────────┐                           │
│                    │   TARGET ZONE    │                           │
│        ←──────────│████ ████████│──────────→                    │
│          Moving    │  ↑ HIT HERE ↑  │   Bar                     │
│          Marker    └──────────────────┘                           │
│              ●━━━━━━━━━━━━━━━━━━━━━━━━━●                        │
│                                                                   │
│                        [TAP!]                                     │
│                                                                   │
│  Deliveries: ███░░ 3/5          Bonus: x1.5 (streak)            │
└─────────────────────────────────────────────────────────────────┘
```

### H-Scene Mini-Game (Rhythm — One-Handed):
```
┌─────────────────────────────────────────────────────────────────┐
│                        [H-SCENE CG]                              │
│                                                                   │
│                                                                   │
│                                                                   │
│                                                                   │
│  ┌─────────────────────────────────────────────────────────────┐│
│  │  RHYTHM:  ○ ○ ○ ● ○ ○ ○   ← tap when ● hits center        ││
│  │                                                              ││
│  │  STAMINA: ████████████████░░░░  80%                         ││
│  │  HER:     ██████████████████░░  90%  ← she's close!        ││
│  │                                                              ││
│  │  STREAK: 12 hits     RATING: ★★★☆☆                         ││
│  │                                              [Hold to slow] ││
│  └─────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
```

### Sleep Stealth Mini-Game:
```
┌─────────────────────────────────────────────────────────────────┐
│                    [SLEEPING CHARACTER CG]                        │
│                                                                   │
│                                                                   │
│  ┌─────────────────────────────────────────┐                    │
│  │  AWARENESS: ░░░░░░░░░░░░░░░░░░░  [ZZZ] │  ← don't fill!   │
│  │  PLEASURE:  ████████░░░░░░░░░░░░  [45%] │  ← fill this!    │
│  └─────────────────────────────────────────┘                    │
│                                                                   │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                      │
│  │  Touch   │  │  Grope   │  │ Undress  │                      │
│  │  (safe)  │  │  (risky) │  │(very risky)│                    │
│  │  +5 plea │  │ +15 plea │  │ +25 plea │                      │
│  │  +2 awar │  │ +8 awar  │  │ +15 awar │                      │
│  └──────────┘  └──────────┘  └──────────┘                      │
│                                                                   │
│  If Awareness hits 100% → SHE WAKES UP (outcome varies)         │
└─────────────────────────────────────────────────────────────────┘
```

---

## 11. MAIN MENU

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                   │
│            [Animated Background — house at night,                 │
│             dim lights, silhouettes in windows]                   │
│                                                                   │
│                                                                   │
│                   HOUSE OF INFLUENCE                              │
│                   ─────────────────                               │
│                                                                   │
│                    ┌──────────────┐                               │
│                    │   NEW GAME   │                               │
│                    ├──────────────┤                               │
│                    │   CONTINUE   │                               │
│                    ├──────────────┤                               │
│                    │   GALLERY    │                               │
│                    ├──────────────┤                               │
│                    │   SETTINGS   │                               │
│                    ├──────────────┤                               │
│                    │    QUIT      │                               │
│                    └──────────────┘                               │
│                                                                   │
│                              v0.1 — Day/Night cycle animation     │
└─────────────────────────────────────────────────────────────────┘
```

### Main Menu Design Notes:
- Background: semi-animated (particles, light flicker in windows)
- Title font: elegant serif, gold/amber color with subtle glow
- Buttons: matte black with gold border, hover = gold fill
- After first playthrough: character silhouettes appear in windows based on progress
- Music: ambient lo-fi or soft jazz (sets mood without being porn-y)

---

## 12. SAVE/LOAD SCREEN

```
┌─────────────────────────────────────────────────────────────────┐
│  SAVE / LOAD                                        [Close X]    │
│                                                                   │
│  ┌─ Page 1 ─┬─ Page 2 ─┬─ Page 3 ─┬─ Auto ─┬─ Quick ─┐       │
│                                                                   │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐            │
│  │ [Screenshot] │ │ [Screenshot] │ │ [Screenshot] │            │
│  │ Slot 1       │ │ Slot 2       │ │ Slot 3       │            │
│  │ Day 12 Night │ │ Day 8 Noon   │ │ Day 15 Eve   │            │
│  │ Marina:52    │ │ Kaori:30     │ │ Yuki:60      │            │
│  │ 2026/05/19   │ │ 2026/05/18   │ │ 2026/05/19   │            │
│  └──────────────┘ └──────────────┘ └──────────────┘            │
│                                                                   │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐            │
│  │ [Screenshot] │ │ [Screenshot] │ │   [ EMPTY ]  │            │
│  │ Slot 4       │ │ Slot 5       │ │   Slot 6     │            │
│  │ Day 20 Morn  │ │ Day 5 Night  │ │              │            │
│  │ Harem:active │ │ Fresh start  │ │   [Save Here]│            │
│  │ 2026/05/17   │ │ 2026/05/15   │ │              │            │
│  └──────────────┘ └──────────────┘ └──────────────┘            │
│                                                                   │
│  30 save slots total (6 per page x 5 pages + auto + quick)      │
└─────────────────────────────────────────────────────────────────┘
```

### Save Slot Info:
- Screenshot thumbnail of moment saved
- Day + time slot
- Highest stat character name + value (quick reference)
- Real-world date/time
- Active route indicator (if locked into path)

---

## 13. GALLERY SCREEN

```
┌─────────────────────────────────────────────────────────────────┐
│  GALLERY                                            [Close X]    │
│                                                                   │
│  ┌─MARINA─┬─KAORI─┬─YUKI─┬─HAREM─┬─NTR─┐   Total: 42/135     │
│                                                                   │
│  ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐     │
│  │ CG │ │ CG │ │ CG │ │ CG │ │ 🔒 │ │ 🔒 │ │ 🔒 │ │ 🔒 │     │
│  │ 01 │ │ 02 │ │ 03 │ │ 04 │ │ 05 │ │ 06 │ │ 07 │ │ 08 │     │
│  └────┘ └────┘ └────┘ └────┘ └────┘ └────┘ └────┘ └────┘     │
│  ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐     │
│  │ 🔒 │ │ 🔒 │ │ 🔒 │ │ 🔒 │ │ 🔒 │ │ 🔒 │ │ 🔒 │ │ 🔒 │     │
│  │ 09 │ │ 10 │ │ 11 │ │ 12 │ │ 13 │ │ 14 │ │ 15 │ │ 16 │     │
│  └────┘ └────┘ └────┘ └────┘ └────┘ └────┘ └────┘ └────┘     │
│                                                                   │
│  Unlocked: shows thumbnail (click to view full + replay scene)   │
│  Locked: shows dark silhouette + hint ("Requires: Corruption 50")│
│                                                                   │
│  ┌─────────────────────────────────────────────┐                │
│  │ Completion: ████████░░░░░░░ 31%             │                │
│  │ Reward at 50%: Outfit color variants         │                │
│  │ Reward at 75%: Director Mode                 │                │
│  └─────────────────────────────────────────────┘                │
└─────────────────────────────────────────────────────────────────┘
```

---

## 14. NOTIFICATION / POPUP SYSTEM

### Stat Change Popup (Brief — 1.5sec):
```
         ┌────────────────────┐
         │  ♥ Affection +5    │
         │  Marina             │
         └────────────────────┘
```
- Appears top-right corner
- Color-coded by stat type
- Fades in/out smoothly
- Multiple can stack

### Event Discovery Popup:
```
┌──────────────────────────────────────┐
│  🔔 NEW DISCOVERY                    │
│                                       │
│  Found: Kaori's diary entry           │
│  Blackmail Tier 1 unlocked!          │
│                                       │
│  [View in Phone] [Dismiss]           │
└──────────────────────────────────────┘
```

### Time Advance Popup:
```
┌────────────────────────────────┐
│  ☀ Morning → 🌅 Evening       │
│  Time has advanced.            │
└────────────────────────────────┘
```

---

## 15. INTERACTION MENU (When Entering a Room with Character)

```
┌─────────────────────────────────────────────────────────────────┐
│                [Background: Kitchen]                              │
│                [Marina sprite — cooking]                          │
│                                                                   │
│  ┌── INTERACTIONS ──────────────────────────────────────────┐   │
│  │                                                           │   │
│  │  💬 Talk          — Chat, compliment, ask about day       │   │
│  │  👁️ Observe       — Watch her (builds knowledge)          │   │
│  │  🤝 Help          — Assist with task (+Affection)         │   │
│  │  😈 Touch         — Physical contact (+Corruption) [Lv2+]│   │
│  │  🎁 Give Gift     — Present an item                       │   │
│  │  ⚡ Use Item      — Apply consumable (wine, etc.)         │   │
│  │  📱 Check Phone   — Read her cloned messages [FREE]       │   │
│  │  🔥 Repeat Scene  — [Unlocked: Massage Scene] [1 slot]    │   │
│  │  ← Leave          — Exit room                             │   │
│  │                                                           │   │
│  └───────────────────────────────────────────────────────────┘   │
│                                                                   │
│  Greyed options: "[Requires: Skill Lv3]" or "[Requires: item]"  │
└─────────────────────────────────────────────────────────────────┘
```

### Interaction Design Rules:
- Options color-coded by primary stat they affect
- Locked options visible but greyed (shows requirement)
- "Repeat Scene" only shows AFTER scene first unlocked
- Free actions marked [FREE] — don't consume time slot
- Maximum 3-4 visible at once without scroll (avoid overwhelm)

---

## 16. DESIGN PRINCIPLES

| Principle | Implementation |
|-----------|---------------|
| **One-handed friendly** | All critical buttons reachable from right side or bottom |
| **Don't interrupt fapping** | H-scene UI is MINIMAL. Hide UI button prominent. |
| **Information on demand** | Stats hidden in phone, not always on screen. Clean default view. |
| **Clear feedback** | Every action shows result immediately (+5 popup, sound, reaction) |
| **No confusion** | Locked content always shows WHY it's locked |
| **Dark theme** | Easy on eyes in dark room (the intended play environment) |
| **Fast navigation** | Map → Room → Interact = 2 clicks maximum |
| **Skip/Auto** | Repeat players can skip all dialogue. First-time gets full experience. |
| **Mobile-ready** | All touch targets minimum 48px. Buttons not too small. |
| **Persistent HUD** | Day/Money/Time always visible — player always knows "where they are" |

---

## 17. ANIMATION NOTES (If Budget Allows)

| Element | Animation Type |
|---------|---------------|
| Stat bars | Smooth fill/drain (0.3s ease) |
| Room hover (map) | Subtle pulse glow |
| Character portrait | Breathing idle (subtle chest movement) |
| Notification popup | Slide in from right, fade out |
| Choice hover | Box glow + slight scale up |
| Time advance | Quick day/night color shift on screen edges |
| Phone open | Slide up from bottom (like real phone) |
| H-scene CG | Optional: 2-3 frame loop animation (breathing, movement) |
| Mini-game rhythm | Smooth dot movement, hit flash effect |

---

## 18. ASSET LIST (GUI-Specific)

| Asset | Quantity | Format |
|-------|----------|--------|
| Button sprites (normal/hover/active) | ~30 sets | PNG (9-patch) |
| Stat bar frames + fills (5 colors) | 5 sets | PNG |
| Phone UI frame + app icons | 1 frame + 9 icons | PNG |
| Map room cards (normal/hover/active) | ~12 rooms | PNG |
| Dialogue box (standard + H-scene) | 2 variants | PNG |
| Save slot frame | 1 template | PNG |
| Gallery thumbnail frame (locked/unlocked) | 2 variants | PNG |
| Notification popup frame | 3 types | PNG |
| Font files | 2-3 families | TTF/OTF |
| Sound effects (UI) | ~15 (click, hover, popup, notification, etc.) | OGG |
| Mini-game elements | ~20 sprites | PNG |

---

*GUI Plan Document: v1.0*  
*Resolution: 1920x1080 (scales to 1280x720)*  
*Theme: Dark Modern (Black/Navy + Gold accent)*  
*Status: Ready for Implementation*
