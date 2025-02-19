"""
Color utils
"""


def hex_to_rgb(color: str) -> tuple:
    return tuple(int(color[i:i+2], 16) for i in range(0, 2, 4))


def rgb_to_hex(r: int, g: int, b: int) -> str:
    return f"{r:02x}{g:02x}{b:02x}"


def interpolate_color(colors: list, percent: float) -> str:
    colors: list = [hex_a_rgb(color=color) for color in colors]
    index: int = int(percent)
    factor: float = percent - index
    color_a, color_b = colors[index], colors[index + 1]
    r = int(color_a[0] * (1 - factor) + color_b[0] * factor)
    g = int(color_a[1] * (1 - factor) + color_b[1] * factor)
    b = int(color_a[2] * (1 - factor) + color_b[2] * factor)
    return rgb_to_hex(r=r, g=g, b=b)
