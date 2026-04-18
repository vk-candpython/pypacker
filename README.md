# 🐍 pypacker


<div align="center">

[![Platform](https://img.shields.io/badge/platform-Any-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Language](https://img.shields.io/badge/language-Python%203-3776AB?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Release](https://img.shields.io/badge/release-v1.0.0-brightgreen)](https://github.com/vk-candpython/pypacker/releases/tag/v1.0.0)

*Advanced multi‑layer Python code protection with polymorphic runtime*

</div>

---

## 📖 Table of Contents | Оглавление

- [English](#english)
  - [📋 Overview](#-overview)
  - [✨ Features](#-features)
  - [🔒 Protection Layers](#-protection-layers)
  - [🚀 Quick Start](#-quick-start)
  - [⚙️ How It Works](#️-how-it-works)
  - [📁 Output](#-output)
  - [⚠️ Important Notes](#️-important-notes)
  - [🔧 Troubleshooting](#-troubleshooting)

- [Русский](#русский)
  - [📋 Обзор](#-обзор)
  - [✨ Возможности](#-возможности)
  - [🔒 Уровни защиты](#-уровни-защиты)
  - [🚀 Быстрый старт](#-быстрый-старт)
  - [⚙️ Как это работает](#️-как-это-работает)
  - [📁 Результат](#-результат)
  - [⚠️ Важные замечания](#️-важные-замечания)
  - [🔧 Устранение неполадок](#-устранение-неполадок)

---

# English

## 📋 Overview

**PyPacker** is an advanced Python code protection tool that transforms ordinary scripts into **heavily obfuscated, multi‑layer encrypted, self‑decrypting executables**.

Unlike simple obfuscators, PyPacker implements a **9‑layer protection pipeline**:

1. **XOR Encryption** (16‑bit rolling key)
2. **GZIP Compression** (level 9)
3. **Pickle Serialization** (code object marshaling)
4. **LZMA Compression** (custom 16MB dictionary)
5. **ZLIB Compression** (raw deflate, level 9)
6. **Base85 Encoding** (payload encoding)
7. **UUEncoding** (codecs layer)
8. **Marshal Serialization** (bytecode conversion)
9. **Polymorphic Wrapper** (runtime self‑decryption)

Each layer adds entropy and makes reverse engineering **exponentially more difficult**.

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔐 **9‑Layer Encryption** | XOR → GZIP → Pickle → LZMA → ZLIB → Base85 → UU → Marshal → Polymorphic |
| 🎲 **Polymorphic Code** | Different obfuscation patterns on every build |
| 🔄 **Rolling XOR Key** | 16‑bit key with feedback mechanism |
| 📦 **Triple Compression** | GZIP + LZMA + ZLIB for maximum entropy |
| 🧠 **Marshal Bytecode** | Converts Python source to marshaled code objects |
| 🎭 **Constant Obfuscation** | `True`/`False`/`None`/`...` replaced with complex expressions |
| 🔍 **Anti‑Debugging** | `sys.gettrace()` checks injected |
| 🌍 **Full Unicode Support** | 129‑character alphabet (Latin + Cyrillic + Ukrainian) |
| 🛡️ **No Temp Files** | All decryption happens in memory |
| ⚡ **Self‑Decrypting** | Packed script decrypts itself at runtime |

## 🔒 Protection Layers

### Complete Pipeline

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. XOR Encryption                                               │
│    • 16‑bit random key (token_bytes)                            │
│    • Rolling feedback: f = (f ^ encrypted_byte) & 0xFF          │
│    • Each byte depends on previous state                        │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ 2. GZIP Compression                                             │
│    • Maximum compression level 9                                │
│    • Adds GZIP header/metadata entropy                          │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ 3. Pickle Serialization                                         │
│    • Serializes code objects to byte stream                     │
│    • Preserves Python object structure                          │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ 4. LZMA Compression                                             │
│    • Custom 16 MB dictionary (dict_size = 16_777_216)           │
│    • Filter chain: lc=4, lp=0, pb=2                             │
│    • Raw format (FORMAT_RAW) — no container headers             │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ 5. ZLIB Compression                                             │
│    • Level 9 compression                                        │
│    • wbits=-15 (raw deflate, no zlib header)                    │
│    • Further reduces size and scrambles patterns                │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ 6. Base85 Encoding                                              │
│    • Encodes binary to ASCII‑safe representation                │
│    • Higher density than Base64                                 │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ 7. UUEncoding (codecs)                                          │
│    • Additional encoding layer via codecs.encode(..., 'uu')     │
│    • Legacy format adds another obfuscation barrier             │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ 8. Marshal Serialization                                        │
│    • Converts Python bytecode to marshal format                 │
│    • marshal.dumps() creates platform‑independent bytecode      │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ 9. Polymorphic Wrapper                                          │
│    • Randomized variable names (19‑50 chars)                    │
│    • Injected dead code (NONE/TRUE/ELLIPSIS patterns)           │
│    • Self‑modifying decryption routines                         │
│    • Runtime bytecode execution via exec() + compile()          │
└─────────────────────────────────────────────────────────────────┘
```

### 🎲 Randomization Sources

| Component | Pool Size | Examples |
|-----------|-----------|----------|
| **Variable Names** | 129 chars | Latin + Cyrillic + Ukrainian (`ґєіїҐЄІЇ`) |
| **`None` Patterns** | 20+ | `([].append(0)or(None))`, `((0)if(False)else(None))` |
| **`True` Patterns** | 20+ | `(1<<0==1)`, `(len([0])==1)`, `(not[]==False)` |
| **`...` Patterns** | 20+ | `((lambda x:...)(None))`, `(({}or(...)))` |
| **XOR Key** | 16‑bit | `token_bytes(2)` — 65536 combinations |
| **Char Shift Key** | 8‑bit × 2 | Bit shift + XOR for string obfuscation |
| **Rotation Key** | 8‑bit | `randbelow(255)` for byte rotation |

### 📦 Compression Parameters

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

## ⚙️ How It Works

### Encryption Algorithm (Rolling XOR)

```python
k0, k1 = random_16bit_key
f = k0

for i, byte in enumerate(original_bytes):
    encrypted_byte = byte ^ (((k1 + f) + i) & 0xFF)
    f = (f ^ encrypted_byte) & 0xFF
    output[i] = encrypted_byte
```

**Key properties:**
- Each encrypted byte depends on **position** (`i`), **key** (`k1`), and **previous state** (`f`)
- Changing one byte affects **all subsequent bytes**
- Makes known‑plaintext attacks extremely difficult

### String Obfuscation

Strings are obfuscated using **bit‑shift + XOR**:

```python
shift = random(1-6)
xor_key = random(0-255)

for char in string:
    obfuscated = chr((ord(char) << shift) ^ xor_key)
```

Or via **dynamic chr() generation**:

```python
# Generates: f'%s'*len % (chr(72),chr(101),chr(108),chr(108),chr(111))
"f'{{chr(37)}}{{chr(115)}}'*5%(chr(72),chr(101),chr(108),chr(108),chr(111))"
```

### Marshal Bytecode Conversion

The original Python code is:
1. Compiled to bytecode via `compile(source, '<...>', 'exec')`
2. Serialized via `marshal.dumps(code_object)`
3. Encrypted and embedded in the wrapper

At runtime:
1. Wrapper decrypts the marshal data
2. `marshal.loads()` reconstructs the code object
3. `exec()` executes the bytecode

### Polymorphic Wrapper Structure

```python
# Layer 0: Type creation with __call__
type('...', (object,), {
    '__slots__': (),
    '__or__': lambda _, __: exec(__, globals()),
    '__init__': lambda _, __: ...
})()

# Layer 1: ZLIB decompression
zlib.decompress(packed_1, wbits=-15)

# Layer 2: LZMA decompression
lzma.decompress(packed_2, format=FORMAT_RAW, filters=LZMA_FILTER)

# Layer 3: GZIP decompression
gzip.decompress(encrypted_code)

# Layer 4: XOR decryption (in-memory)
for i, n in enumerate(data):
    x = n ^ (((k1 + f) + i) & 0xFF)
    f = (f ^ x) & 0xFF
```

### Anti‑Debugging

```python
from sys import gettrace

if gettrace() is not None:
    # Debugger detected — exit or behave differently
    exit(0)
```

### Dead Code Injection

Random expressions that **never execute** but appear in source:

```python
((None)and((lambda:None)())and(([]or(None))))
(((0)if(False)else(None))and((lambda x=None:x)()))
((not(not(False)))or(None)and(1>2))
```

These:
- Increase code size
- Confuse static analyzers
- Add no runtime overhead (optimized away)

## 📁 Output

Packer creates a file with `packed-` prefix:

```
original_script.py  →  packed-original_script.py
```

The output is a **valid Python script** containing:
- Polymorphic bootstrap code
- Encrypted payload layers
- Self‑decryption logic
- Original bytecode (marshaled)

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

PyPacker implements **defense in depth**:

| Layer | Purpose |
|-------|---------|
| XOR | First encryption barrier |
| GZIP | Compression + entropy |
| Pickle | Object serialization |
| LZMA | High‑ratio compression |
| ZLIB | Additional scrambling |
| Base85 | ASCII encoding |
| UU | Legacy format obfuscation |
| Marshal | Bytecode conversion |
| Polymorphic | Runtime self‑protection |

**What it protects against:**
- Casual code inspection
- Automated deobfuscators
- Simple `strings` extraction
- Basic static analysis

**What it does NOT protect against:**
- Determined reverse engineer with debugger
- Memory dumping at runtime
- Python bytecode disassemblers

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

**PyPacker** — это продвинутый инструмент защиты Python‑кода, который превращает обычные скрипты в **сильно обфусцированные, многослойно зашифрованные, саморасшифровывающиеся исполняемые файлы**.

В отличие от простых обфускаторов, PyPacker реализует **9‑уровневый конвейер защиты**:

1. **XOR‑шифрование** (16‑битный скользящий ключ)
2. **GZIP‑сжатие** (уровень 9)
3. **Pickle‑сериализация** (маршалинг кодовых объектов)
4. **LZMA‑сжатие** (кастомный словарь 16 МБ)
5. **ZLIB‑сжатие** (raw deflate, уровень 9)
6. **Base85‑кодирование** (кодирование полезной нагрузки)
7. **UU‑кодирование** (слой codecs)
8. **Marshal‑сериализация** (преобразование в байт‑код)
9. **Полиморфная обёртка** (саморасшифровка во время выполнения)

Каждый слой добавляет энтропию и делает обратную разработку **экспоненциально сложнее**.

## ✨ Возможности

| Возможность | Описание |
|-------------|----------|
| 🔐 **9‑уровневое шифрование** | XOR → GZIP → Pickle → LZMA → ZLIB → Base85 → UU → Marshal → Полиморф |
| 🎲 **Полиморфный код** | Разные паттерны обфускации при каждой сборке |
| 🔄 **Скользящий XOR‑ключ** | 16‑битный ключ с механизмом обратной связи |
| 📦 **Тройное сжатие** | GZIP + LZMA + ZLIB для максимальной энтропии |
| 🧠 **Marshal байт‑код** | Преобразование исходников в маршалированные кодовые объекты |
| 🎭 **Обфускация констант** | `True`/`False`/`None`/`...` заменены сложными выражениями |
| 🔍 **Анти‑отладка** | Внедрены проверки `sys.gettrace()` |
| 🌍 **Полная Unicode‑поддержка** | Алфавит из 129 символов (латиница + кириллица + украинские) |
| 🛡️ **Без временных файлов** | Вся расшифровка происходит в памяти |
| ⚡ **Саморасшифровка** | Упакованный скрипт расшифровывает себя при запуске |

## 🔒 Уровни защиты

### Полный конвейер

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. XOR‑шифрование                                               │
│    • 16‑битный случайный ключ (token_bytes)                     │
│    • Скользящая обратная связь: f = (f ^ зашифрованный_байт)    │
│    • Каждый байт зависит от предыдущего состояния               │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ 2. GZIP‑сжатие                                                  │
│    • Максимальный уровень сжатия 9                              │
│    • Добавляет энтропию заголовков GZIP                         │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ 3. Pickle‑сериализация                                          │
│    • Сериализует кодовые объекты в байтовый поток               │
│    • Сохраняет структуру объектов Python                        │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ 4. LZMA‑сжатие                                                  │
│    • Кастомный словарь 16 МБ (dict_size = 16_777_216)           │
│    • Цепочка фильтров: lc=4, lp=0, pb=2                         │
│    • Сырой формат (FORMAT_RAW) — без заголовков контейнера      │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ 5. ZLIB‑сжатие                                                  │
│    • Уровень сжатия 9                                            │
│    • wbits=-15 (raw deflate, без заголовка zlib)                │
│    • Дополнительно уменьшает размер и перемешивает паттерны     │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ 6. Base85‑кодирование                                           │
│    • Кодирует бинарные данные в ASCII‑безопасное представление  │
│    • Более высокая плотность, чем Base64                        │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ 7. UU‑кодирование (codecs)                                      │
│    • Дополнительный слой через codecs.encode(..., 'uu')         │
│    • Устаревший формат добавляет ещё один барьер                │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ 8. Marshal‑сериализация                                         │
│    • Преобразует байт‑код Python в формат marshal               │
│    • marshal.dumps() создаёт платформонезависимый байт‑код      │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│ 9. Полиморфная обёртка                                          │
│    • Рандомизированные имена переменных (19‑50 символов)        │
│    • Впрыск мёртвого кода (паттерны NONE/TRUE/ELLIPSIS)         │
│    • Самомодифицирующиеся рутины расшифровки                    │
│    • Выполнение байт‑кода через exec() + compile()              │
└─────────────────────────────────────────────────────────────────┘
```

### 🎲 Источники рандомизации

| Компонент | Размер пула | Примеры |
|-----------|-------------|---------|
| **Имена переменных** | 129 символов | Латиница + Кириллица + Украинские (`ґєіїҐЄІЇ`) |
| **Паттерны `None`** | 20+ | `([].append(0)or(None))`, `((0)if(False)else(None))` |
| **Паттерны `True`** | 20+ | `(1<<0==1)`, `(len([0])==1)`, `(not[]==False)` |
| **Паттерны `...`** | 20+ | `((lambda x:...)(None))`, `(({}or(...)))` |
| **XOR‑ключ** | 16 бит | `token_bytes(2)` — 65536 комбинаций |
| **Ключ сдвига символов** | 8 бит × 2 | Битовый сдвиг + XOR для обфускации строк |
| **Ключ поворота** | 8 бит | `randbelow(255)` для поворота байтов |

### 📦 Параметры сжатия

| Алгоритм | Настройки |
|----------|-----------|
| **GZIP** | `compresslevel=9` |
| **LZMA** | `dict_size=16MB`, `lc=4`, `lp=0`, `pb=2`, `FORMAT_RAW` |
| **ZLIB** | `level=9`, `wbits=-15` |

## 🚀 Быстрый старт

### 📥 Скачивание

```bash
git clone https://github.com/vk-candpython/pypacker.git
cd pypacker
```

### 🏃 Использование

```bash
python3 pypacker.py <твой_скрипт.py>
```

**Пример:**
```bash
python3 pypacker.py моя_программа.py
```

**Вывод:**
```
packed (моя_программа.py) created (packed-моя_программа.py) [+]
```

### 📦 Запуск упакованного скрипта

```bash
python3 packed-моя_программа.py
```

Упакованный скрипт выполняется идентично оригиналу.

## ⚙️ Как это работает

### Алгоритм шифрования (Скользящий XOR)

```python
k0, k1 = случайный_16битный_ключ
f = k0

for i, byte in enumerate(исходные_байты):
    зашифрованный_байт = byte ^ (((k1 + f) + i) & 0xFF)
    f = (f ^ зашифрованный_байт) & 0xFF
    вывод[i] = зашифрованный_байт
```

**Ключевые свойства:**
- Каждый зашифрованный байт зависит от **позиции** (`i`), **ключа** (`k1`) и **предыдущего состояния** (`f`)
- Изменение одного байта влияет на **все последующие байты**
- Делает атаки с известным открытым текстом крайне сложными

### Обфускация строк

Строки обфусцируются с помощью **битового сдвига + XOR**:

```python
shift = случайный(1-6)
xor_key = случайный(0-255)

for char in string:
    obfuscated = chr((ord(char) << shift) ^ xor_key)
```

Или через **динамическую генерацию chr()**:

```python
# Генерирует: f'%s'*len % (chr(72),chr(101),chr(108),chr(108),chr(111))
"f'{{chr(37)}}{{chr(115)}}'*5%(chr(72),chr(101),chr(108),chr(108),chr(111))"
```

### Marshal‑преобразование байт‑кода

Исходный Python‑код:
1. Компилируется в байт‑код через `compile(source, '<...>', 'exec')`
2. Сериализуется через `marshal.dumps(code_object)`
3. Шифруется и встраивается в обёртку

При запуске:
1. Обёртка расшифровывает marshal‑данные
2. `marshal.loads()` восстанавливает кодовый объект
3. `exec()` выполняет байт‑код

### Структура полиморфной обёртки

```python
# Слой 0: Создание типа с __call__
type('...', (object,), {
    '__slots__': (),
    '__or__': lambda _, __: exec(__, globals()),
    '__init__': lambda _, __: ...
})()

# Слой 1: ZLIB‑распаковка
zlib.decompress(packed_1, wbits=-15)

# Слой 2: LZMA‑распаковка
lzma.decompress(packed_2, format=FORMAT_RAW, filters=LZMA_FILTER)

# Слой 3: GZIP‑распаковка
gzip.decompress(encrypted_code)

# Слой 4: XOR‑расшифровка (в памяти)
for i, n in enumerate(data):
    x = n ^ (((k1 + f) + i) & 0xFF)
    f = (f ^ x) & 0xFF
```

### Анти‑отладка

```python
from sys import gettrace

if gettrace() is not None:
    # Обнаружен отладчик — выход или другое поведение
    exit(0)
```

### Впрыск мёртвого кода

Случайные выражения, которые **никогда не выполняются**, но присутствуют в исходнике:

```python
((None)and((lambda:None)())and(([]or(None))))
(((0)if(False)else(None))and((lambda x=None:x)()))
((not(not(False)))or(None)and(1>2))
```

Они:
- Увеличивают размер кода
- Запутывают статические анализаторы
- Не добавляют накладных расходов (оптимизируются)

## 📁 Результат

Упаковщик создаёт файл с префиксом `packed-`:

```
оригинальный_скрипт.py  →  packed-оригинальный_скрипт.py
```

Выходной файл — **валидный Python‑скрипт**, содержащий:
- Полиморфный код начальной загрузки
- Зашифрованные слои полезной нагрузки
- Логику саморасшифровки
- Исходный байт‑код (маршалированный)

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
| **Накладные расходы для больших скриптов** | Расшифровка добавляет задержку при запуске |
| **Нет поддержки C‑расширений** | Только чистый Python |
| **Ложные срабатывания антивирусов** | Сильно обфусцированный код может вызывать тревоги |

### 🔐 Соображения безопасности

PyPacker реализует **эшелонированную защиту**:

| Слой | Назначение |
|------|------------|
| XOR | Первый барьер шифрования |
| GZIP | Сжатие + энтропия |
| Pickle | Сериализация объектов |
| LZMA | Высокоэффективное сжатие |
| ZLIB | Дополнительное перемешивание |
| Base85 | ASCII‑кодирование |
| UU | Обфускация устаревшим форматом |
| Marshal | Преобразование в байт‑код |
| Полиморф | Самозащита во время выполнения |

**От чего защищает:**
- Поверхностный анализ кода
- Автоматические деобфускаторы
- Простое извлечение `strings`
- Базовый статический анализ

**От чего НЕ защищает:**
- Целеустремлённый реверс‑инженер с отладчиком
- Дамп памяти во время выполнения
- Дизассемблеры байт‑кода Python

> ⚠️ Для критически важной интеллектуальной собственности комбинируй с серверной валидацией, проверками лицензий и юридической защитой.

## 🔧 Устранение неполадок

| Проблема | Решение |
|----------|---------|
| `ModuleNotFoundError` в упакованном скрипте | Сначала установи зависимости на целевой машине |
| `RecursionError` | Исходный скрипт слишком большой — разбей на модули |
| `MemoryError` | Уменьши размер исходного скрипта |
| `SyntaxError` в выводе | Проверь синтаксис исходного скрипта |
| Упакованный скрипт медленнее | Ожидаемо — накладные расходы на многослойную расшифровку |
| Антивирус помечает скрипт | Добавь исключение или используй PyInstaller для дистрибуции |
| Ошибка загрузки `marshal` | Несовпадение версий Python — пакуй и запускай на одной версии |

---

<div align="center">

**[⬆ Back to Top](#-pypacker)**

*9‑Layer Python Protection — Obfuscate, Encrypt, Marshal, Execute*

</div>
