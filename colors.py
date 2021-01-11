def hex2rgb(hex):
    return tuple(int(hex[i:i+2], 16) for i in (1, 3, 5))

LINE = "#ffffff"
BACKGROUND = "#dddddd"
FRAME = "#b9aea1"
FONT_DARK = "#222222"
FONT_LIGHT = "#ffffff"

BLOCKS = {
    0: "#cbc0b9",
    2: "#ede4db",
    4: "#ebe0ca",
    8: "#e8b381",
    16: "#e8996d",
    32: "#e48185",
    64: "#e46a49",
    128: "#e7ce7e",
    256: "#e4c96f",
    512: "#e5c763",
    1024: "#e6c559",
    2048: "#e6c24f"
}
