# ============================================================
# EVENTS.RPY - Event & Scene untuk setiap karakter
# ============================================================

# ============================================================
# SARI EVENTS (Kakak tiri - mature, teasing, suka godain)
# ============================================================

label dapur_sari:
    # scene bg dapur
    # show sari normal

    s "Oh, pagi~ mau sarapan bareng?"

    menu:
        "Boleh, masak bareng yuk":
            $ tambah_love("sari", 5)
            $ maju_waktu()
            s "Wah rajin~ sini aku ajarin."
            "Kamu masak bareng Sari. Sesekali tangannya menyentuh tanganmu."
            s "Ups, maaf~ hehe~"
            mc "(Jantung deg-degan...)"

            if sari_love >= 30 and not sari_event_1:
                jump sari_event_apron

            jump sandbox_loop

        "Nggak, makasih":
            s "Yah~ padahal aku masak banyak lho."
            jump sandbox_loop

        "Godain Sari" if sari_love >= 20:
            $ tambah_lust("sari", 5)
            mc "Masakanmu selalu enak, kayak orangnya~"
            s "Ih, gombal! ...tapi makasih~"
            $ set_mood("sari", "senang")
            jump sandbox_loop


label sari_event_apron:
    $ sari_event_1 = True
    "Saat masak, Sari tiba-tiba..."
    s "Eh, celemekku kotor. Minjem bajumu dong buat lap?"
    s "Bercanda~ tapi celemekku emang kotor nih."

    menu:
        "Pinjemin baju":
            $ tambah_love("sari", 10)
            s "Makasih~ kamu baik banget."
            "Sari memakai bajumu yang kebesaran. Terlihat... menggoda."
            mc "(Gila... keliatan banget lekuknya...)"
            jump sandbox_loop

        "Biar aja, seksi kok":
            $ tambah_lust("sari", 10)
            s "H-hah?! Dasar mesum..."
            s "...tapi makasih udah jujur~ hehe."
            $ set_mood("sari", "senang")
            jump sandbox_loop


label tamu_sari:
    # scene bg ruang_tamu
    # show sari normal

    "Sari sedang nonton TV di sofa."
    s "Eh, sini duduk~ lagi seru nih filmnya."

    menu:
        "Duduk di sebelahnya":
            $ tambah_love("sari", 3)
            "Kamu duduk di sebelah Sari. Bahu kalian bersentuhan."

            if sari_love >= 50 and not sari_event_2:
                jump sari_event_sofa

            s "Filmnya bagus kan~"
            jump sandbox_loop

        "Duduk di kursi lain":
            s "Kok jauh sih~ nggak gigit kok."
            jump sandbox_loop


label sari_event_sofa:
    $ sari_event_2 = True
    "Film horror mulai menegangkan..."
    s "Kyaa~!"
    "Sari refleks memeluk lenganmu."
    s "M-maaf... aku takut..."
    mc "(Dadanya nempel...)"

    menu:
        "Tenangkan dia (peluk balik)":
            $ tambah_love("sari", 15)
            $ tambah_lust("sari", 10)
            mc "Nggak apa-apa, aku di sini."
            s "...makasih. Kamu hangat~"
            "Sari tidak melepaskan pelukannya sampai film selesai."
            $ set_mood("sari", "senang")
            jump sandbox_loop

        "Diam aja":
            $ tambah_love("sari", 5)
            "Kamu membiarkan Sari memeluk lenganmu."
            s "...maaf ya, aku penakut."
            jump sandbox_loop

        "Goda dia":
            $ tambah_lust("sari", 15)
            mc "Kalau takut, peluknya yang lebih erat dong~"
            s "D-dasar...!"
            "Wajah Sari memerah, tapi dia tidak menjauh."
            $ set_mood("sari", "terangsang")
            jump sandbox_loop


# ============================================================
# MIRA EVENTS (Teman kost - shy, cute, gampang malu)
# ============================================================

label dapur_mira:
    # show mira normal

    "Mira sedang membuat teh dengan gugup."
    m "A-ah! K-kamu... mau teh juga?"

    menu:
        "Boleh, makasih Mira":
            $ tambah_love("mira", 5)
            m "I-ini... semoga enak."
            "Mira memberikan secangkir teh dengan tangan gemetar."
            mc "Enak kok, makasih."
            m "S-syukurlah..."
            jump sandbox_loop

        "Aku buatin kamu aja":
            $ tambah_love("mira", 8)
            m "E-eh?! Nggak usah repot-repot..."
            "Kamu tetap membuatkan teh untuk Mira."
            m "...makasih. Kamu baik banget."
            $ set_mood("mira", "senang")

            if mira_love >= 25 and not mira_event_1:
                jump mira_event_dapur

            jump sandbox_loop

        "Kamu manis kalau gugup gitu" if mira_love >= 15:
            $ tambah_lust("mira", 5)
            $ tambah_love("mira", 3)
            m "H-HAAAH?! J-jangan ngomong gitu...!"
            "Wajah Mira merah padam. Dia hampir menjatuhkan gelasnya."
            mc "(Cute banget...)"
            jump sandbox_loop


label mira_event_dapur:
    $ mira_event_1 = True
    "Saat kamu memberikan teh, jari kalian bersentuhan."
    m "...!"
    "Mira menjatuhkan gelas, teh tumpah ke bajunya."
    m "A-aduh...!"

    menu:
        "Ambilkan handuk":
            $ tambah_love("mira", 10)
            "Kamu cepat mengambil handuk."
            mc "Ini, keringkan dulu."
            m "M-makasih... maaf aku ceroboh."
            "Bajunya basah dan... agak transparan."
            mc "(Jangan lihat... jangan lihat...)"
            m "K-kenapa mukamu merah...?"
            jump sandbox_loop

        "Bantu keringkan langsung":
            $ tambah_lust("mira", 10)
            $ tambah_love("mira", 5)
            "Kamu refleks mengelap baju Mira dengan tangan."
            m "T-TUNGGU!! I-itu...!!"
            "Kamu baru sadar tanganmu menyentuh area yang... sensitif."
            mc "M-MAAF!!"
            m "............"
            "Mira diam dengan wajah sangat merah."
            $ set_mood("mira", "terangsang")
            jump sandbox_loop


label tamu_mira:
    # show mira normal
    "Mira sedang membaca buku di pojok ruang tamu."

    menu:
        "Duduk di dekatnya":
            $ tambah_love("mira", 3)
            "Kamu duduk tidak jauh dari Mira."
            m "...kamu mau baca juga?"
            mc "Boleh, baca apa?"
            m "I-ini... novel romansa..."
            mc "(Ternyata suka yang romantis ya...)"
            jump sandbox_loop

        "Tanya soal bukunya" if mira_love >= 20:
            $ tambah_love("mira", 5)
            mc "Ceritanya tentang apa?"
            m "I-ini... tentang... c-cewek yang suka sama temen kostnya..."
            "Mira langsung menutup buku dengan panik."
            m "B-BUKAN AKU!! Ini cuma novel!!"
            mc "(Hmm... suspicious~)"
            jump sandbox_loop

        "Biarkan dia sendiri":
            "Kamu membiarkan Mira membaca dengan tenang."
            jump sandbox_loop


# ============================================================
# DINA EVENTS (Tetangga - bold, flirty, agresif)
# ============================================================

label dapur_dina:
    # show dina normal
    d "Yo~ pinjam gula dong, tetangga~"

    menu:
        "Boleh, ambil aja":
            $ tambah_love("dina", 3)
            d "Makasih~ kamu emang yang paling baik di sini."
            jump sandbox_loop

        "Tuker sama apa nih?":
            $ tambah_lust("dina", 5)
            d "Hmm~ mau dituker apa? Pelukan? Ciuman?"
            d "Bercanda~ ...atau nggak? Hehe~"
            mc "(Cewek ini bahaya...)"

            if dina_love >= 20 and not dina_event_1:
                jump dina_event_dapur

            jump sandbox_loop

        "Mahal tuh gula":
            d "Pelit banget sih~ aku balikin nanti deh, plus bonus~"
            $ tambah_love("dina", 2)
            jump sandbox_loop


label dina_event_dapur:
    $ dina_event_1 = True
    d "Beneran mau dituker?"
    "Dina mendekat dengan senyum nakal."

    menu:
        "Pelukan boleh":
            $ tambah_love("dina", 10)
            $ tambah_lust("dina", 10)
            d "Deal~!"
            "Dina langsung memelukmu erat. Tubuhnya menempel."
            d "Mmm~ hangat. Boleh lebih lama nggak?"
            mc "(Wangi banget... dan bodynya...)"
            $ set_mood("dina", "senang")
            jump sandbox_loop

        "Ciuman? Serius?":
            $ tambah_lust("dina", 15)
            d "Kenapa? Mau?"
            "Dina mendekatkan wajahnya..."
            d "...bercanda~ belum saatnya. Hehe~"
            d "Tapi kalau kamu mau... next time ya~"
            $ set_mood("dina", "terangsang")
            jump sandbox_loop

        "Nggak jadi deh, gratis aja":
            $ tambah_love("dina", 5)
            d "Ah~ gentleman ya. Aku suka tipe kayak gitu~"
            jump sandbox_loop


label tamu_dina:
    # show dina normal
    "Dina sedang duduk santai di sofa."
    d "Eh~ mampir sini dong. Bosen nih."

    menu:
        "Duduk bareng":
            $ tambah_love("dina", 3)
            d "Sini-sini~ cerita dong, ada gossip nggak?"
            "Kamu ngobrol santai dengan Dina."
            jump sandbox_loop

        "Nggak ah, sibuk":
            d "Yah~ padahal aku kesepian~"
            d "Next time ya~"
            jump sandbox_loop

        "Flirt balik" if dina_love >= 30:
            $ tambah_lust("dina", 8)
            mc "Sama siapa aja bosen, yang penting sama aku kan?"
            d "Wah wah~ udah berani ya sekarang~"
            d "Aku suka~ lanjutin dong~"

            if dina_love >= 50 and not dina_event_2:
                jump dina_event_sofa

            jump sandbox_loop


label dina_event_sofa:
    $ dina_event_2 = True
    d "Kamu tau nggak..."
    "Dina bergeser sangat dekat."
    d "Aku suka cowok yang berani~"

    menu:
        "Pegang tangannya":
            $ tambah_love("dina", 15)
            $ tambah_lust("dina", 10)
            "Kamu menggenggam tangan Dina."
            d "...finally. Aku udah nunggu kamu berani dari kemarin."
            "Dina meletakkan kepalanya di bahumu."
            $ set_mood("dina", "senang")
            jump sandbox_loop

        "Cium dia":
            $ tambah_lust("dina", 20)
            $ tambah_love("dina", 10)
            "Kamu mencium Dina."
            d "...!!"
            d "...wow. Langsung tembak ya~"
            d "Aku nggak keberatan sih... malah suka~"
            $ set_mood("dina", "terangsang")
            jump sandbox_loop

        "Belum waktunya":
            $ tambah_love("dina", 5)
            d "Hmm~ playing hard to get ya? Oke, aku sabar~"
            jump sandbox_loop


# ============================================================
# HALAMAN EVENTS
# ============================================================
label halaman_dina:
    "Kamu melihat Dina lewat depan rumah."
    d "Eh~ lagi santai? Sendirian?"

    menu:
        "Iya, gabung sini":
            $ tambah_love("dina", 5)
            d "Boleh~ cuaca bagus ya hari ini."
            "Dina duduk di sebelahmu."
            jump sandbox_loop

        "Mau kemana?":
            d "Jalan-jalan aja~ mau ikut?"
            $ tambah_love("dina", 3)
            jump sandbox_loop


# ============================================================
# KAMAR MANDI EVENT (Random encounter)
# ============================================================
label kamar_mandi_event:
    "Kamu membuka pintu kamar mandi dan..."

    $ siapa_mandi = renpy.random.choice(["sari", "mira", "dina"])

    if siapa_mandi == "sari" and sari_unlock:
        s "Kyaa~! ...eh, kamu toh."
        s "Ketuk dulu dong~ ...atau emang sengaja?"

        menu:
            "MAAF!! (Tutup pintu)":
                $ tambah_love("sari", 2)
                mc "Maaf maaf maaf!!"
                s "Haha~ nggak apa-apa kok~"
                jump sandbox_loop

            "...sorry, tapi nggak bisa nggak lihat":
                $ tambah_lust("sari", 10)
                s "Dasar mesum~"
                s "...tapi reaksimu lucu. Hehe~"
                $ set_mood("sari", "terangsang")
                jump sandbox_loop

    elif siapa_mandi == "mira" and mira_unlock:
        m "KYAAAA!!!"
        "Mira melempar botol shampoo ke arahmu!"

        menu:
            "MAAF!! (Kabur)":
                mc "MAAF MIRA!!"
                "Kamu langsung menutup pintu dan kabur."
                m "H-HENTAI...!!"
                "...tapi kamu sempat melihat sekilas."
                $ tambah_lust("mira", 5)
                jump sandbox_loop

            "Mira, aku nggak sengaja!":
                m "K-KELUAR!! SEKARANG!!"
                "Kamu menutup pintu."
                "...nanti malam, Mira mengetuk kamarmu."
                m "...a-aku... maaf sudah teriak. Kamu nggak sengaja kan?"
                $ tambah_love("mira", 5)
                mc "Iya, maaf banget."
                m "...k-kamu lihat banyak?"
                mc "N-nggak kok!"
                m "...bohong."
                jump sandbox_loop

    elif siapa_mandi == "dina" and dina_unlock:
        d "Oh~? Mau ikut mandi~?"
        "Dina bahkan tidak mencoba menutupi tubuhnya."

        menu:
            "MAAF! (Tutup pintu)":
                d "Haha~ nggak perlu malu. Aku nggak keberatan kok~"
                $ tambah_lust("dina", 5)
                jump sandbox_loop

            "...kamu nggak malu?":
                $ tambah_lust("dina", 15)
                d "Kenapa harus malu? Badanku bagus kan~?"
                d "Tapi lain kali... ketuk dulu ya. Atau jangan. Hehe~"
                $ set_mood("dina", "terangsang")
                jump sandbox_loop

    else:
        "Kamar mandi kosong. Kamu mandi dengan tenang."
        $ energi = min(energi + 15, 100)

    jump sandbox_loop
