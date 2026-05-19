# Rumah Sandbox - Ren'Py Hentai Game

Game sandbox sederhana berlatar di rumah kost. Kamu tinggal serumah dengan 3 cewek cantik.

## Karakter

| Nama | Tipe | Deskripsi |
|------|------|-----------|
| **Sari** | Kakak tiri | Mature, suka godain, teasing |
| **Mira** | Teman kost | Shy, cute, gampang malu |
| **Dina** | Tetangga | Bold, flirty, agresif |

## Gameplay

- **Sandbox loop**: Pilih ruangan -> Event random/triggered -> Naikkan stat -> Unlock scene
- **Waktu**: Pagi > Siang > Sore > Malam > Tidur (ganti hari)
- **Stats**: Love (hubungan), Lust (nafsu), Mood (biasa/senang/terangsang/marah)
- **Unlock**: Karakter muncul bertahap (Hari 2, 3, 5)

## Lokasi

- Kamar (istirahat, cek status)
- Dapur (encounter random)
- Ruang Tamu (encounter random)
- Kamar Mandi (random spicy event)
- Halaman (olahraga, encounter Dina)

## Setup / Cara Install

### 1. Download Ren'Py
- Download dari: https://www.renpy.org/latest.html
- Extract ke folder mana aja

### 2. Setup Project
- Buka Ren'Py Launcher
- Klik "preferences" -> set Projects Directory ke folder parent dari game ini
- ATAU copy folder `game/` ke project Ren'Py baru

### 3. Struktur File

```
game/
├── scripts/
│   ├── script.rpy      # Main game, karakter, navigasi
│   ├── variables.rpy   # Variabel & fungsi helper
│   ├── screens.rpy     # UI / menu sandbox
│   └── events.rpy      # Event & scene tiap karakter
├── images/
│   ├── bg/             # Background (kamar.png, dapur.png, dll)
│   ├── characters/     # Sprite karakter (sari_normal.png, dll)
│   └── ui/             # UI elements
└── audio/
    ├── bgm/            # Background music
    └── sfx/            # Sound effects
```

### 4. Tambah Asset (Gambar & Audio)
- Taruh background di `game/images/bg/` dengan nama: `kamar.png`, `dapur.png`, `ruang_tamu.png`, `kamar_mandi.png`, `halaman.png`
- Taruh sprite karakter di `game/images/characters/` dengan nama: `sari_normal.png`, `sari_senang.png`, `mira_normal.png`, dll
- Uncomment baris `image` dan `scene` di script.rpy

### 5. Run Game
- Di Ren'Py Launcher, pilih project -> "Launch Project"

## Cara Develop / Extend

### Tambah Event Baru:
1. Buka `events.rpy`
2. Tambah label baru, contoh:
```renpy
label sari_event_baru:
    s "Dialog Sari..."
    menu:
        "Pilihan 1":
            $ tambah_love("sari", 10)
            jump sandbox_loop
        "Pilihan 2":
            $ tambah_lust("sari", 10)
            jump sandbox_loop
```

### Tambah Karakter Baru:
1. Define di `script.rpy`: `define x = Character("Nama", color="#hex")`
2. Tambah variabel di `variables.rpy`
3. Tambah event di `events.rpy`

### Tambah Lokasi Baru:
1. Tambah tombol di `screens.rpy` (di screen sandbox_menu)
2. Tambah label `goto_lokasi_baru` di `script.rpy`

## Tips Development

- Gunakan `{b}bold{/b}` dan `{i}italic{/i}` di dialog untuk emphasis
- Test pakai Ren'Py developer mode (Shift+D in-game)
- Pakai `renpy.random.choice()` untuk randomisasi
- Love >= 30 = event ringan unlock, Love >= 50 = event berat unlock, Love >= 80 = H-scene unlock

## Asset Resources (Free/Paid)

- **Background**: Lemma Soft Forums, itch.io (search "visual novel background")
- **Character Sprites**: Koikatsu, DAZ3D, commission artist
- **Music**: freesound.org, itch.io game assets
- **AI Generated**: Stable Diffusion, NovelAI (untuk prototype)

## License

Private project - for personal use only.
