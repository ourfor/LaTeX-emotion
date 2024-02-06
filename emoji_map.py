from fontTools.ttLib import TTFont
from os import path

def make_emoji_map():
    user_home = path.expanduser("~")
    font_path = path.join(user_home, "Library/Fonts/Twemoji.Mozilla.ttf")
    font = TTFont(font_path)

    cmap = font.getBestCmap()
    exps = []
    for char_code in cmap:
        char = chr(char_code)
        unicode_value = '^^^^^^' + format(char_code, '06x')
        exp = f"\\tl_const:cn{'{'}const_emoji_ {char}{'}'}{'{'}{unicode_value}{'}'}"
        exps.append(exp)

    content = '\n'.join(exps)
    with open("emoji_map.def", "w", encoding="utf-8") as file:
        content = r"""\ProvidesExplFile{emoji_map.def}
    {2024/02/06}{0.1}{LaTeX emoji}
""" + content
        file.write(content)

def make_test_tex():
    user_home = path.expanduser("~")
    print(f"User Home: {user_home}")
    font_path = path.join(user_home, "Library/Fonts/Twemoji.Mozilla.ttf")
    print(f"Font Path: {font_path}")
    font = TTFont(font_path)

    cmap = font.getBestCmap()
    exps = []
    for char_code in cmap:
        char = chr(char_code)
        exp = f"\myemoji{'{'}{char}{'}'} & \myemoji{'{'}{char}{'}'} \\\\"
        exps.append(exp)
        content = '\n'.join(exps)

    with open("main.tex", "w", encoding="utf-8") as file:
        content = r"""\documentclass{article}
\usepackage{myemoji}
\begin{document}
\begin{table}
\begin{tabular}{cc}
""" + content + r"""
\end{tabular}
\end{table}
\end{document}
        """
        file.write(content)
    

if __name__ == "__main__":
    # make_emoji_map()
    make_test_tex()