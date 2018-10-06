from arpeggio import Optional, OneOrMore, EOF, RegExMatch


def identifier():
    return RegExMatch(r"[_A-Za-z][A-Za-z0-9_'#]*")


def til_eol():
    return RegExMatch(r".*")


def value():
    return RegExMatch(r"[A-Za-z0-9_]+")


def num():
    return RegExMatch(r"[0-9]+")


def wsl():
    return RegExMatch(r"\s*")


def ws():
    return RegExMatch(r"[\t ]+")


def headerline():
    return Optional(ws), identifier, ":", Optional(ws), til_eol, "\n"


def breakline():
    return "--", RegExMatch(r"-*"), "\n"


def endmarker():
    return [";", "\n"]


def phrase_bit():
    return Optional(wsl), identifier, Optional(ws), Optional(num, Optional(ws)), endmarker


def phrase():
    return (
        "phrase",
        ws,
        identifier,
        wsl,
        "{",
        wsl,
        OneOrMore(phrase_bit),
        Optional(wsl),
        "}"
    )


def section():
    return (
        "section",
        ws,
        identifier,
        wsl,
        "{",
        wsl,
        OneOrMore([identifier_line, phrase_bit]),
        Optional(wsl),
        "}"
    )


def multiplier():
    return Optional(ws), "x", Optional(ws), num


def identifier_line():
    return Optional(wsl), identifier, Optional(multiplier), Optional(ws), endmarker


def song():
    return "song", ws, "{", wsl, OneOrMore([identifier_line]), Optional(wsl), "}"


def bodyset():
    return Optional(wsl), [
        phrase,
        section,
        song,
    ]


def trogfile():
    return Optional(OneOrMore(headerline), breakline), OneOrMore(bodyset), Optional(wsl), EOF
