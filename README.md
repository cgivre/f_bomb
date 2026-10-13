[![Pylint](https://github.com/cgivre/f_bomb/actions/workflows/pylint.yml/badge.svg)](https://github.com/cgivre/f_bomb/actions/workflows/pylint.yml)
[![Tests](https://github.com/cgivre/f_bomb/actions/workflows/tests.yml/badge.svg)](https://github.com/cgivre/f_bomb/actions/workflows/tests.yml)

# F Bomb
If you've ever need to drop an F bomb in your code, we've got you covered. Drop a blunt, multilingual "F-bomb" in your Python code.

## Installation
```bash
pip install f_bomb
```

## Quick start
```python
from f_bomb import F_Bomb

bomb = F_Bomb()
print(str(bomb))          # FUCK!
print(bomb.drop("fr"))    # PUTAIN!
```

## Usage

### Choose a default language

```python
from f_bomb import F_Bomb

bomb = F_Bomb("de")
print(bomb.drop())        # SCHEISSE!
```

### Drop once in a specific language

```python
from f_bomb import F_Bomb

bomb = F_Bomb()
print(bomb.drop("it"))    # CAZZO!
```

### Carpet bomb (intentionally noisy)

```python
from f_bomb import F_Bomb

bomb = F_Bomb("en")
print(bomb.carpet_bomb(3))  # FUCK!\nFUCK!\nFUCK!
```

### More ordnance

```python
from f_bomb import F_Bomb

bomb = F_Bomb()
print(bomb.defuse())        # F**K!
print(bomb.dud())           # fudge.
print(bomb.countdown())     # 3... 2... 1... FUCK!
print(bomb.grawlix())       # e.g. #@$%&!
print(bomb.roulette())      # one drop in a random language
print(bomb.cluster_bomb())  # 5 drops in different random languages
print(bomb.nuke())          # every supported language at once
```

### Drop one when your code blows up

```python
from f_bomb import F_Bomb

@F_Bomb.on_error
def deploy():
    raise RuntimeError("prod is down")

deploy()  # prints FUCK! to stderr, then re-raises the RuntimeError
```

## API

### `F_Bomb(language: str = "en")`
Creates a new bomb with a default language code.

### `drop(language: str | None = None) -> str`
Returns the uppercase expletive for the provided language code, or the default.

### `carpet_bomb(number: int = 100, language: str | None = None) -> str`
Returns `number` drops, one per line.

### `defuse(language: str | None = None) -> str`
Returns a work-safe drop with the middle letters starred out.

### `dud() -> str`
Returns `fudge.`

### `countdown(seconds: int = 3, language: str | None = None) -> str`
Counts down from `seconds`, then drops.

### `grawlix(length: int = 5) -> str`
Returns `length` random cartoon swear symbols followed by `!`.

### `roulette() -> str`
Drops in a random supported language.

### `cluster_bomb(number: int = 5) -> str`
Drops in `number` different random languages, one per line. Raises `ValueError` if `number` exceeds the supported languages.

### `nuke() -> str`
Drops in every supported language, one per line.

### `@F_Bomb.on_error`
Decorator that prints an English drop to stderr when the wrapped function raises, then re-raises.

## Supported language codes

The library ships with a list of language codes mapped to strong profanities.
Examples: `en`, `es`, `fr`, `de`, `it`, `pt`, `ru`, `ja`, `ko`, `zh`.

## Notes

- Language codes are lowercased internally.
- Unknown language codes raise `KeyError`.

