# hayy-media

كل الملفات اللي بيحمّلها تطبيق «حيّ» للصلاة على موبايل المستخدم لما يطلبها، متقسّمة بالنوع.
Every file the Hayy prayer app downloads to the user's phone on request, sorted by kind.
The app checks each file against its sha256 before it keeps it.

| Folder | What | Source | Terms |
|---|---|---|---|
| `quran/pages/` | The Mushaf's 604 pages (`p001.png` … `p604.png`) + `pages.tsv` (size and sha256 of each) | King Fahd Glorious Qur'an Printing Complex — Madinah Mushaf (Hafs), green edition 1441 AH, PDF; each page cut from it without any change | © King Fahd Complex, under the Complex's terms |
| `quran/fonts/` | King Fahd Complex QCF v2 fonts, one per page (`QCF2001.ttf` … `QCF2604.ttf`) + `QCF2BSML.ttf` (sura heads and basmala) | As published in `nuqayah/qpc-fonts` | © King Fahd Complex — free use in software per the Complex's copyright page; not modified |
| `tafsir/` | Tafsir al-Muyassar and Tafsir Ibn Kathir, one file per sura (`<book>/<sura>.json`) | `spa5k/tafsir_api` at commit `eb82bb6` | MIT (the repository) |
| `hadith/` | Sahih al-Bukhari, Sahih Muslim, the Forty Nawawi, the Forty Qudsi — one file per book section (`<book>/<n>.min.json`) | `fawazahmed0/hadith-api` at commit `df57907` | Unlicense |
| `asr/` | The listening model for the voice search and «follow me» (`whisper-base-ar-quran-q5_1.bin`) + its NOTICE | `tarteel-ai/whisper-base-ar-quran`, converted to ggml q5_1 with whisper.cpp (details in the NOTICE) | Apache License 2.0 |
| `video/intro/` | Short opening clips (Dhuhr, Isha, Jumuah) | Made by the app's owner | The owner's |
| `images/prayer_bg/` | Background pictures | The app's own | The owner's |
| `hayy_media.json` | The list the app reads: each file's path, size, sha256, source and rights | — | — |

The files are kept exactly as received: no change to the Qur'an text, the page drawing, the fonts, the tafsir or the hadith.
