# Age of Claude 🏰⚔️ — Novempos Fork

*Wololo! İmparatorluk küçük adımlarla başlar!*

## Genel Bakış

Age of Claude, Age of Empires'ın ikonik seslerini Claude Code oturumlarına taşır. Claude bir şey yaptıkça AoE ses efektleri çalar; kodlama seansı bir RTS deneyimine döner.

Bu, [aliparoya/age-of-claude](https://github.com/aliparoya/age-of-claude) reposunun **Novempos fork'udur**. Orijinalden farkı:

- Sesler `.claude/settings.json` içinde **inline python** yerine tek bir yardımcı script (`play.py`) üzerinden çalınır.
- Yüzlerce kullanılmayan ses temizlendi; sadece **kullandığımız 7 ses** bırakıldı.
- Hook eşleşmeleri bizim kurulumumuza göre sadeleştirildi.

Python kurulu olması gerekir; ses çalma tüm büyük işletim sistemlerinde `play.py` üzerinden çalışır.

## Hook Ses Eşleşmeleri

```
📁 Oturum Yaşam Döngüsü
├── UserPromptSubmit ──────── 5814.wav
├── Stop ──────────────────── villager_train1.wav
├── SubagentStop ──────────── 6298.wav
├── Notification ──────────── 6294.wav
└── SessionEnd
    ├── exit ───────────────── 6301.wav
    └── clear ──────────────── 6300.wav

📁 Bağlam Yönetimi
└── PreCompact
    ├── auto ───────────────── 5809.wav
    └── manual ─────────────── 6294.wav
```

Kalan sesler (`.claude/sounds/`):

```
5809.wav  5814.wav  6294.wav  6298.wav  6300.wav  6301.wav  villager_train1.wav
```

## Kurulum

1. Repoyu klonla:
```bash
git clone https://github.com/Novempos/age-of-claude.git
cd age-of-claude
```

2. Ya:
   - `.claude` klasörünü proje kök dizinine kopyala, ya da
   - Bu repo dizinine `cd` yapıp Claude Code'u doğrudan kullanmaya başla
3. Hook'lar Claude Code oturumları sırasında otomatik tetiklenir.

> Not: `.claude/settings.json` içindeki hook komutları `play.py`'ye **mutlak yol** ile referans verir
> (`C:/Users/Osman/.claude/age-of-claude/play.py`). Başka bir makinede kullanacaksan bu yolu kendi
> ortamına göre güncelle.

## Gereksinimler

- Python 3.x (çapraz platform ses çalma için)
- Ses çalma desteği:
  - **Windows**: Python `winsound` kütüphanesi
  - **macOS**: Yerleşik `afplay`
  - **Linux**: `aplay`

## Özelleştirme

- Ses eşleşmelerini `.claude/settings.json` içinden değiştir.
- Yeni ses eklemek istersen `.claude/sounds/` klasörüne `.wav` dosyanı koy ve ilgili hook komutunda dosya adını ver.
- Kullanılan ses ID'leri (5809, 6294 vb.) Age of Empires II'nin ses dosyalarıdır.

## Krediler

Ses efektleri, Ensemble Studios/Microsoft yapımı orijinal Age of Empires oyunundan alınmıştır.
