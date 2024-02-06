😄 Emotion

## Usage

### Setup emoji font
You can use your favorite emoji font. 
command `\emotionsetup`
accept one parameter(font name), which you have installed in your
computer

```latex
\emotionsetup{Twemoji Mozilla}
```

### Use emoji symbol

Command `\emotion` accept one parameter.
the parameter can be emoji symbol or the defined emoji id

```latex
\emotion{☘}
\emotion{🥵}
\emotion{emotion}
```

### Custom emoji alias

Command `\emotiondef` need two parameters, 
one is the emoji id, the other is emoji value(emoji symbol or unicode value)

```latex
\emotiondef{apple}{🍎}
\emotiondef{tea}{🍵}
\emotiondef{A}{^^^^^^01f1e6}
```

```latex
\emotion{apple}
\emotion{tea}
\emotion{A}
```