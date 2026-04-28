# 🐍 pypacker


<div align="center">

[![Platform](https://img.shields.io/badge/platform-Any-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Language](https://img.shields.io/badge/language-Python%203-3776AB?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

*Advanced multi‑layer Python code protection with polymorphic runtime*

</div>

---

> [!WARNING]
> This tool is for educational purposes and authorized security auditing only. The author is not responsible for any misuse.

---

## 📖 Table of Contents | Оглавление

- [English](#english)
  - [📋 Overview](#-overview)
  - [✨ Features](#-features)
  - [🔒 Protection Layers](#-protection-layers)
  - [🚀 Quick Start](#-quick-start)
  - [⚙️ Deep Technical Analysis](#️-deep-technical-analysis)
  - [📁 Output](#-output)
  - [⚠️ Important Notes](#️-important-notes)
  - [🔧 Troubleshooting](#-troubleshooting)

- [Русский](#русский)
  - [📋 Обзор](#-обзор)
  - [✨ Возможности](#-возможности)
  - [🔒 Уровни защиты](#-уровни-защиты)
  - [🚀 Быстрый старт](#-быстрый-старт)
  - [⚙️ Глубокий технический анализ](#️-глубокий-технический-анализ)
  - [📁 Результат](#-результат)
  - [⚠️ Важные замечания](#️-важные-замечания)
  - [🔧 Устранение неполадок](#-устранение-неполадок)

---

# English

## 📋 Overview

**PyPacker** is an advanced Python code protection tool that transforms ordinary scripts into heavily obfuscated, multi‑layer encrypted, self‑decrypting executables.

### What makes it unique?

| Component | Implementation |
|-----------|----------------|
| **9‑Layer Encryption Pipeline** | XOR → GZIP → Pickle → LZMA → ZLIB → Base85 → UU → Marshal → Polymorphic |
| **Rolling XOR Cipher** | 16‑bit key with feedback — each encrypted byte depends on all previous |
| **Triple Compression** | GZIP + LZMA (16MB dictionary) + ZLIB (raw deflate) for maximum entropy |
| **Polymorphic Wrapper** | 100% unique per build — random identifiers from 129-char alphabet |
| **Constant Obfuscation** | `True`/`False`/`None`/`...` replaced with 60+ complex expressions |
| **Marshal Bytecode** | Converts Python source to marshaled code objects |
| **Dead Code Injection** | Random expressions that never execute but confuse static analyzers |
| **Anti‑Debugging** | `sys.gettrace()` checks injected |
| **No Temp Files** | All decryption happens in memory |

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔐 **9‑Layer Encryption** | XOR → GZIP → Pickle → LZMA → ZLIB → Base85 → UU → Marshal → Polymorphic |
| 🎲 **Polymorphic Code** | Different obfuscation patterns on every build |
| 🔄 **Rolling XOR Key** | 16‑bit key with feedback mechanism — each byte depends on previous state |
| 📦 **Triple Compression** | GZIP + LZMA + ZLIB for maximum entropy |
| 🧠 **Marshal Bytecode** | Converts Python source to marshaled code objects via `marshal.dumps()` |
| 🎭 **Constant Obfuscation** | `True`/`False`/`None`/`...` replaced with 60+ complex expressions |
| 🔍 **Anti‑Debugging** | `sys.gettrace()` checks injected into bootstrap |
| 🌍 **Full Unicode Support** | 129‑character alphabet (Latin + Cyrillic + Ukrainian: `ґєіїҐЄІЇ`) |
| 🛡️ **No Temp Files** | All decryption happens in memory via `BytesIO` and `memoryview` |
| ⚡ **Self‑Decrypting** | Packed script decrypts itself at runtime — zero external dependencies |

## 🔒 Protection Layers

### Complete Pipeline

```
PHASE 1: XOR ENCRYPTION
├── 16‑bit random key (token_bytes)
├── Rolling feedback: f = (f ^ encrypted_byte) & 0xFF
└── Each byte depends on position, key, and previous state

PHASE 2: GZIP COMPRESSION
├── Maximum compression level 9
└── Adds GZIP header/metadata entropy

PHASE 3: PICKLE SERIALIZATION
├── Serializes code objects to byte stream
└── Preserves Python object structure

PHASE 4: LZMA COMPRESSION
├── Custom 16 MB dictionary (dict_size = 16_777_216)
├── Filter chain: lc=4, lp=0, pb=2
└── Raw format (FORMAT_RAW) — no container headers

PHASE 5: ZLIB COMPRESSION
├── Level 9 compression
├── wbits=-15 (raw deflate, no zlib header)
└── Further reduces size and scrambles patterns

PHASE 6: BASE85 ENCODING
├── Encodes binary to ASCII‑safe representation
└── Higher density than Base64

PHASE 7: UUENCODING (codecs)
├── Additional encoding layer via codecs.encode(..., 'uu')
└── Legacy format adds another obfuscation barrier

PHASE 8: MARSHAL SERIALIZATION
├── Converts Python bytecode to marshal format
└── marshal.dumps() creates platform‑independent bytecode

PHASE 9: POLYMORPHIC WRAPPER
├── Randomized variable names (19‑50 chars, 129-char alphabet)
├── 60+ dead code patterns (NONE/TRUE/ELLIPSIS)
├── Self‑modifying decryption routines
└── Runtime bytecode execution via exec() + compile()
```

### Randomization Sources

| Component | Pool Size | Examples |
|-----------|-----------|----------|
| **Variable Names** | 129 chars | Latin + Cyrillic + Ukrainian (`ґєіїҐЄІЇ`) |
| **`None` Patterns** | 20+ | `([].append(0)or(None))`, `((0)if(False)else(None))` |
| **`True` Patterns** | 20+ | `(1<<0==1)`, `(len([0])==1)`, `(not[]==False)` |
| **`...` Patterns** | 20+ | `((lambda x:...)(None))`, `(({}or(...)))` |
| **XOR Key** | 16‑bit | `token_bytes(2)` — 65536 combinations |
| **Char Shift Key** | 8‑bit × 2 | Bit shift (1-6) + XOR (0-255) for string obfuscation |
| **Rotation Key** | 8‑bit | `randbelow(255)` for byte rotation |

### Compression Parameters

| Algorithm | Settings |
|-----------|----------|
| **GZIP** | `compresslevel=9` |
| **LZMA** | `dict_size=16MB`, `lc=4`, `lp=0`, `pb=2`, `FORMAT_RAW` |
| **ZLIB** | `level=9`, `wbits=-15` |

## 🚀 Quick Start

### 📥 Download

```bash
git clone https://github.com/vk-candpython/pypacker.git
cd pypacker
```

### 🏃 Usage

```bash
python3 pypacker.py <your_script.py>
```

**Example:**
```bash
python3 pypacker.py my_program.py
```

**Output:**
```
packed (my_program.py) created (packed-my_program.py) [+]
```

### 📦 Running the Packed Script

```bash
python3 packed-my_program.py
```

The packed script executes identically to the original.

## ⚙️ Deep Technical Analysis

### Encryption Algorithm (Rolling XOR)

The XOR cipher uses a 16‑bit key with a rolling feedback mechanism. The first key byte initializes the feedback state. Each original byte is XORed with a derived value that depends on the second key byte, the current feedback state, and the position index. After encrypting each byte, the feedback state is updated by XORing with the ciphertext byte — creating a chain where every output byte depends on all previous bytes.

### String Obfuscation

Strings are obfuscated using bit‑shift + XOR. Each character is shifted left by a random amount (1-6 bits) and XORed with a random 8‑bit key. Alternatively, strings can be generated dynamically at runtime using `chr()` calls with randomized bases (binary, octal, decimal, hexadecimal) for each character code.

### Marshal Bytecode Conversion

The original Python code is compiled to bytecode via `compile(source, '<...>', 'exec')`, serialized via `marshal.dumps()`, encrypted, and embedded in the polymorphic wrapper. At runtime, the wrapper decrypts the marshal data, `marshal.loads()` reconstructs the code object, and `exec()` executes it.

### Polymorphic Wrapper Structure

The wrapper creates a custom type via `type()` with operator overloading (`__or__`, `__add__`, `__lshift__`, etc.) to chain the decryption layers. Each layer is decompressed in reverse order: type creation → ZLIB decompress → LZMA decompress → GZIP decompress → XOR decrypt → exec().

### Anti‑Debugging

A `sys.gettrace()` check is injected into the bootstrap code. If a debugger is attached, the script can exit or behave differently.

### Dead Code Injection

Random boolean expressions that always evaluate to a constant are peppered throughout the generated code. They increase code size, confuse static analyzers, but add zero runtime overhead as Python's optimizer eliminates them.

## 📁 Output

Packer creates a file with `packed-` prefix:

```
original_script.py  →  packed-original_script.py
```

The output is a valid Python script containing the polymorphic bootstrap code, all encrypted payload layers, self‑decryption logic, and the original bytecode in marshaled form.

## ⚠️ Important Notes

### ✅ Works Best For

- Single‑file Python scripts
- Python 3.6+ compatible code
- Scripts without native C extensions

### ❌ Limitations

| Limitation | Explanation |
|------------|-------------|
| **Requires Python Interpreter** | Output is still `.py` — needs Python 3.x |
| **Not Native Executable** | Use PyInstaller for `.exe` distribution |
| **Large Script Overhead** | Decryption adds startup latency |
| **No C Extension Support** | Pure Python only |
| **AV False Positives** | Heavily obfuscated code may trigger alerts |

### 🔐 Security Considerations

PyPacker implements defense in depth across 9 layers. Each layer adds entropy and makes reverse engineering exponentially more difficult. The combination of encryption (XOR), triple compression (GZIP+LZMA+ZLIB), dual encoding (Base85+UU), and marshal bytecode conversion means an attacker must peel through all 9 layers to recover the original source.

**What it protects against:** casual code inspection, automated deobfuscators, simple `strings` extraction, basic static analysis.

**What it does NOT protect against:** determined reverse engineer with debugger, memory dumping at runtime, Python bytecode disassemblers.

> ⚠️ For mission‑critical IP, combine with server‑side validation, license checks, and legal protections.

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` in packed script | Install dependencies on target machine first |
| `RecursionError` | Original script too large — split into modules |
| `MemoryError` | Reduce original script size |
| `SyntaxError` in output | Check original script syntax |
| Packed script slower | Expected — multi‑layer decryption overhead |
| AV flags packed script | Add exception or use PyInstaller for distribution |
| `marshal` load error | Python version mismatch — pack and run on same version |

---

# Русский

## 📋 Обзор

**PyPacker** — продвинутый инструмент защиты Python‑кода, который превращает обычные скрипты в сильно обфусцированные, многослойно зашифрованные, саморасшифровывающиеся исполняемые файлы.

### Что делает его уникальным?

| Компонент | Реализация |
|-----------|------------|
| **9‑уровневый конвейер** | XOR → GZIP → Pickle → LZMA → ZLIB → Base85 → UU → Marshal → Полиморф |
| **Скользящий XOR‑шифр** | 16‑битный ключ с обратной связью — каждый байт зависит от предыдущих |
| **Тройное сжатие** | GZIP + LZMA (словарь 16 МБ) + ZLIB (raw deflate) для максимальной энтропии |
| **Полиморфная обёртка** | 100% уникальна для каждой сборки — имена из 129-символьного алфавита |
| **Обфускация констант** | `True`/`False`/`None`/`...` заменены 60+ сложными выражениями |
| **Marshal байт‑код** | Преобразование исходников в маршалированные кодовые объекты |
| **Впрыск мёртвого кода** | Случайные выражения, которые никогда не выполняются |
| **Анти‑отладка** | Внедрены проверки `sys.gettrace()` |
| **Без временных файлов** | Вся расшифровка происходит в памяти |

## ✨ Возможности

| Возможность | Описание |
|-------------|----------|
| 🔐 **9‑уровневое шифрование** | XOR → GZIP → Pickle → LZMA → ZLIB → Base85 → UU → Marshal → Полиморф |
| 🎲 **Полиморфный код** | Разные паттерны обфускации при каждой сборке |
| 🔄 **Скользящий XOR‑ключ** | 16‑битный ключ с обратной связью — каждый байт зависит от предыдущего состояния |
| 📦 **Тройное сжатие** | GZIP + LZMA + ZLIB для максимальной энтропии |
| 🧠 **Marshal байт‑код** | Преобразование в маршалированные кодовые объекты через `marshal.dumps()` |
| 🎭 **Обфускация констант** | `True`/`False`/`None`/`...` заменены 60+ сложными выражениями |
| 🔍 **Анти‑отладка** | Проверки `sys.gettrace()` в коде начальной загрузки |
| 🌍 **Полная Unicode‑поддержка** | Алфавит из 129 символов (латиница + кириллица + украинские: `ґєіїҐЄІЇ`) |
| 🛡️ **Без временных файлов** | Расшифровка через `BytesIO` и `memoryview` |
| ⚡ **Саморасшифровка** | Упакованный скрипт расшифровывает себя при запуске |

## 🔒 Уровни защиты

*(См. английскую версию для подробной диаграммы)*

## 🚀 Быстрый старт

```bash
git clone https://github.com/vk-candpython/pypacker.git
cd pypacker
python3 pypacker.py моя_программа.py
python3 packed-моя_программа.py
```

## ⚙️ Глубокий технический анализ

### Алгоритм шифрования (Скользящий XOR)

XOR‑шифр использует 16‑битный ключ с механизмом скользящей обратной связи. Первый байт ключа инициализирует состояние обратной связи. Каждый исходный байт XOR'ится с производным значением, зависящим от второго байта ключа, текущего состояния и позиции. После шифрования каждого байта состояние обновляется XOR'ом с шифротекстом — создаётся цепочка, где каждый выходной байт зависит от всех предыдущих.

### Обфускация строк

Строки обфусцируются через битовый сдвиг + XOR: каждый символ сдвигается влево на случайную величину (1-6 бит) и XOR'ится со случайным 8‑битным ключом. Альтернативно, строки генерируются динамически через вызовы `chr()` со случайными основаниями систем счисления для каждого кода символа.

### Marshal‑преобразование байт‑кода

Исходный код компилируется в байт‑код через `compile()`, сериализуется через `marshal.dumps()`, шифруется и встраивается в полиморфную обёртку. При запуске обёртка расшифровывает marshal‑данные, `marshal.loads()` восстанавливает кодовый объект, и `exec()` выполняет его.

### Структура полиморфной обёртки

Создаётся кастомный тип через `type()` с перегрузкой операторов для цепочки расшифровки: создание типа → ZLIB → LZMA → GZIP → XOR → exec().

### Анти‑отладка

В код начальной загрузки внедрена проверка `sys.gettrace()`. Если отладчик обнаружен, скрипт может завершиться или изменить поведение.

### Впрыск мёртвого кода

Случайные булевы выражения, всегда вычисляющиеся в константу, щедро разбросаны по генерируемому коду. Они увеличивают размер, запутывают анализаторы, но не добавляют накладных расходов — оптимизатор Python их устраняет.

## 📁 Результат

```
оригинальный_скрипт.py  →  packed-оригинальный_скрипт.py
```

## ⚠️ Важные замечания

### ✅ Лучше всего подходит для

- Однофайловых Python‑скриптов
- Кода, совместимого с Python 3.6+
- Скриптов без нативных C‑расширений

### ❌ Ограничения

| Ограничение | Пояснение |
|-------------|-----------|
| **Требуется интерпретатор Python** | На выходе `.py` — нужен Python 3.x |
| **Не нативный исполняемый файл** | Используй PyInstaller для `.exe` |
| **Накладные расходы** | Расшифровка добавляет задержку при запуске |
| **Нет поддержки C‑расширений** | Только чистый Python |
| **Ложные срабатывания антивирусов** | Сильно обфусцированный код может вызывать тревоги |

## 🔧 Устранение неполадок

| Проблема | Решение |
|----------|---------|
| `ModuleNotFoundError` | Установи зависимости на целевой машине |
| `RecursionError` | Разбей скрипт на модули |
| `MemoryError` | Уменьши размер исходного скрипта |
| `SyntaxError` в выводе | Проверь синтаксис исходного скрипта |
| Упакованный скрипт медленнее | Ожидаемо — многослойная расшифровка |
| Антивирус помечает скрипт | Добавь исключение или используй PyInstaller |
| Ошибка загрузки `marshal` | Пакуй и запускай на одной версии Python |

---

<div align="center">

**[⬆ Back to Top](#-pypacker)**

*9‑Layer Python Protection — Obfuscate, Encrypt, Marshal, Execute*

</div>
