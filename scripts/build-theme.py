# -*- coding: utf-8 -*-
"""Build the Coastal Cream Light / Dark color themes from one palette table.

    py -3 scripts/build-theme.py
"""

import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
THEMES = BASE / "themes"
NAME = "coastal-cream-theme"
SLUG = "coastal-cream"
DISPLAY = "Coastal Cream Theme"
VERSION = "1.0.0"
REPO = "https://github.com/vaxicy/coastal-cream-theme"

UI = {
    "foreground": ("#3A4650", "#E7EEF3"),
    "editor.foreground": ("#3A4650", "#E7EEF3"),
    "terminal.foreground": ("#3A4650", "#E7EEF3"),
    "input.foreground": ("#2C3A44", "#F1F7FA"),
    "dropdown.foreground": ("#2C3A44", "#F1F7FA"),
    "quickInput.foreground": ("#2C3A44", "#F1F7FA"),
    "editorWidget.foreground": ("#2C3A44", "#F1F7FA"),
    "editorHoverWidget.foreground": ("#2C3A44", "#F1F7FA"),
    "editorSuggestWidget.foreground": ("#2C3A44", "#F1F7FA"),
    "notifications.foreground": ("#2C3A44", "#F1F7FA"),
    "descriptionForeground": ("#7C8A94", "#93A2AC"),
    "input.placeholderForeground": ("#7C8A94", "#93A2AC"),
    "focusBorder": ("#5E9BC0", "#8CC5E8"),
    "inputOption.activeBorder": ("#4E86A8", "#A9D3EE"),
    "input.border": ("#DCE4E9", "#3E4A54"),
    "dropdown.border": ("#DCE4E9", "#3E4A54"),
    "editor.background": ("#FDF9F7", "#1F252B"),
    "tab.activeBackground": ("#FDF9F7", "#1F252B"),
    "titleBar.activeBackground": ("#FBF1E2", "#191E23"),
    "titleBar.activeForeground": ("#4A5560", "#CFDCE4"),
    "titleBar.inactiveBackground": ("#FBF5EC", "#1C2227"),
    "titleBar.inactiveForeground": ("#8C959B", "#7E8C96"),
    "activityBar.background": ("#EAF3F9", "#171C21"),
    "activityBar.foreground": ("#4E86A8", "#A9C4D3"),
    "activityBar.activeBorder": ("#4E86A8", "#8CC5E8"),
    "activityBar.inactiveForeground": ("#94A8B4", "#66757F"),
    "sideBar.background": ("#F3F8FB", "#1C2228"),
    "sideBar.foreground": ("#43505A", "#C6D4DD"),
    "sideBarSectionHeader.background": ("#E7F1F7", "#242C33"),
    "sideBarSectionHeader.foreground": ("#4C5A64", "#D2DEE6"),
    "panel.background": ("#FBF6F2", "#1B2127"),
    "terminal.background": ("#FBF6F2", "#1B2127"),
    "panel.border": ("#E3E8EA", "#333D46"),
    "editorGroup.border": ("#E3E8EA", "#333D46"),
    "tab.border": ("#E3E8EA", "#333D46"),
    "sideBar.border": ("#E3E8EA", "#333D46"),
    "titleBar.border": ("#E3E8EA", "#333D46"),
    "statusBar.background": ("#4E86A8", "#3A5568"),
    "statusBar.noFolderBackground": ("#4E86A8", "#3A5568"),
    "statusBar.foreground": ("#FDF9F7", "#EAF2F7"),
    "statusBar.noFolderForeground": ("#FDF9F7", "#EAF2F7"),
    "statusBarItem.hoverBackground": ("#3F7392", "#47647A"),
    "statusBar.debuggingBackground": ("#B06A3E", "#8A5A38"),
    "statusBar.debuggingForeground": ("#FFFAF4", "#F7EFE6"),
    "editorGroupHeader.tabsBackground": ("#EFECE6", "#1B2127"),
    "tab.inactiveBackground": ("#EFECE6", "#1B2127"),
    "tab.activeForeground": ("#33414B", "#F3F8FB"),
    "tab.activeBorderTop": ("#8CC5E8", "#8CC5E8"),
    "tab.inactiveForeground": ("#7C8A93", "#8595A0"),
    "tab.hoverBackground": ("#E9E5DE", "#242C33"),
    "tab.activeModifiedBorder": ("#A8802E", "#E2C384"),
    "tab.inactiveModifiedBorder": ("#A8802E", "#E2C384"),
    "list.hoverBackground": ("#F2EEE8", "#252D34"),
    "list.activeSelectionBackground": ("#CFE8F7", "#2F4657"),
    "editorSuggestWidget.selectedBackground": ("#CFE8F7", "#2F4657"),
    "list.activeSelectionForeground": ("#2C3A44", "#EAF2F7"),
    "list.inactiveSelectionForeground": ("#2C3A44", "#EAF2F7"),
    "editorSuggestWidget.selectedForeground": ("#2C3A44", "#EAF2F7"),
    "list.inactiveSelectionBackground": ("#E1EFF7", "#293744"),
    "list.highlightForeground": ("#2F6B93", "#8CC5E8"),
    "list.focusHighlightForeground": ("#2F6B93", "#8CC5E8"),
    "tree.indentGuidesStroke": ("#DDE6EB", "#333D46"),
    "editorLineNumber.foreground": ("#A9B6BE", "#66757F"),
    "editorLineNumber.activeForeground": ("#4E86A8", "#8CC5E8"),
    "editor.lineHighlightBackground": ("#FBF5EE", "#262E35"),
    "editor.lineHighlightBorder": ("#F3E7D8", "#2F3A43"),
    "editorCursor.foreground": ("#4E86A8", "#8CC5E8"),
    "selection.background": ("#CFE8F7", "#2F4657"),
    "editor.selectionBackground": ("#CFE8F7", "#2F4657"),
    "terminal.selectionBackground": ("#CFE8F7", "#2F4657"),
    "editor.inactiveSelectionBackground": ("#E1EFF7", "#293744"),
    "editor.wordHighlightBackground": ("#CFE8F780", "#3C556880"),
    "editor.wordHighlightStrongBackground": ("#CFE8F780", "#3C556880"),
    "editor.selectionHighlightBackground": ("#CFE8F766", "#3C556866"),
    "editor.findMatchHighlightBackground": ("#FEE6BB", "#4A6072"),
    "editor.findMatchBackground": ("#F7D89A", "#5B7488"),
    "editor.findMatchBorder": ("#B06A3E", "#FEE6BB"),
    "editorBracketMatch.background": ("#E1F0F8", "#2A3843"),
    "editorBracketMatch.border": ("#8CC5E8", "#8CC5E8"),
    "editorIndentGuide.background1": ("#E5EDF1", "#2E373F"),
    "editorIndentGuide.activeBackground1": ("#A9C4D3", "#55697A"),
    "editorWhitespace.foreground": ("#DDE6EB", "#333D46"),
    "editorRuler.foreground": ("#EAEFF2", "#2E373F"),
    "textLink.foreground": ("#2F6B93", "#8CC5E8"),
    "textLink.activeForeground": ("#245B80", "#A9D3EE"),
    "editorLink.activeForeground": ("#245B80", "#A9D3EE"),
    "quickInput.background": ("#FEFBF8", "#242B32"),
    "editorHoverWidget.background": ("#FEFBF8", "#242B32"),
    "notifications.background": ("#FEFBF8", "#242B32"),
    "input.background": ("#FFFDFB", "#1C2228"),
    "dropdown.background": ("#FFFDFB", "#1C2228"),
    "editorWidget.background": ("#FEFBF8", "#242B32"),
    "editorSuggestWidget.background": ("#FEFBF8", "#242B32"),
    "editorWidget.border": ("#E3E8EA", "#39434C"),
    "editorHoverWidget.border": ("#E3E8EA", "#39434C"),
    "editorSuggestWidget.border": ("#E3E8EA", "#39434C"),
    "notifications.border": ("#E3E8EA", "#39434C"),
    "button.background": ("#8CC5E8", "#8CC5E8"),
    "button.foreground": ("#213038", "#1F252B"),
    "button.hoverBackground": ("#6FAFD8", "#A9D3EE"),
    "button.secondaryBackground": ("#EFEAE4", "#2F3A43"),
    "button.secondaryForeground": ("#3A4650", "#DCE8F0"),
    "button.secondaryHoverBackground": ("#E4DED6", "#39454F"),
    "badge.background": ("#4E86A8", "#8CC5E8"),
    "activityBarBadge.background": ("#4E86A8", "#8CC5E8"),
    "badge.foreground": ("#FFFFFF", "#1F252B"),
    "activityBarBadge.foreground": ("#FFFFFF", "#1F252B"),
    "scrollbarSlider.background": ("#8FA4B066", "#7E8C9688"),
    "scrollbarSlider.hoverBackground": ("#7C929E88", "#93A2AC99"),
    "scrollbarSlider.activeBackground": ("#5E768399", "#A9C4D399"),
    "errorForeground": ("#B85C5C", "#E39A9A"),
    "editorError.foreground": ("#B85C5C", "#E39A9A"),
    "problemsErrorIcon.foreground": ("#B85C5C", "#E39A9A"),
    "gitDecoration.deletedResourceForeground": ("#B85C5C", "#E39A9A"),
    "editorGutter.deletedBackground": ("#B85C5C", "#E39A9A"),
    "editorWarning.foreground": ("#A8802E", "#E2C384"),
    "problemsWarningIcon.foreground": ("#A8802E", "#E2C384"),
    "editorInfo.foreground": ("#4E86A8", "#8CC5E8"),
    "problemsInfoIcon.foreground": ("#4E86A8", "#8CC5E8"),
    "gitDecoration.addedResourceForeground": ("#4E8A5E", "#8FC9A0"),
    "gitDecoration.untrackedResourceForeground": ("#4E8A5E", "#8FC9A0"),
    "editorGutter.addedBackground": ("#4E8A5E", "#8FC9A0"),
    "gitDecoration.modifiedResourceForeground": ("#A8802E", "#E2C384"),
    "editorGutter.modifiedBackground": ("#A8802E", "#E2C384"),
    "diffEditor.insertedTextBackground": ("#D8EBDCAA", "#2F465766"),
    "diffEditor.removedTextBackground": ("#F2D9D6AA", "#5B383866"),
    "diffEditor.insertedLineBackground": ("#D8EBDC66", "#2F465744"),
    "diffEditor.removedLineBackground": ("#F2D9D666", "#5B383844"),
    "terminal.ansiBlack": ("#3A4650", "#2A3238"),
    "terminal.ansiRed": ("#B85C5C", "#E39A9A"),
    "terminal.ansiGreen": ("#4E8A5E", "#8FC9A0"),
    "terminal.ansiYellow": ("#A8802E", "#E2C384"),
    "terminal.ansiBlue": ("#2F6B93", "#8CC5E8"),
    "terminal.ansiMagenta": ("#8A6B8E", "#CBB0CE"),
    "terminal.ansiCyan": ("#1F7A8C", "#8FD9C8"),
    "terminal.ansiWhite": ("#8A9AA4", "#C6D4DD"),
    "terminal.ansiBrightBlack": ("#6B7C88", "#7E8C96"),
    "terminal.ansiBrightRed": ("#CC7070", "#F0B4B4"),
    "terminal.ansiBrightGreen": ("#5E9E6E", "#A9DDB8"),
    "terminal.ansiBrightYellow": ("#BC9438", "#F0D6A2"),
    "terminal.ansiBrightBlue": ("#3E7FA8", "#A9D3EE"),
    "terminal.ansiBrightMagenta": ("#9E7EA2", "#DDC6DF"),
    "terminal.ansiBrightCyan": ("#2A8FA0", "#A8E5D8"),
    "terminal.ansiBrightWhite": ("#2C3A44", "#EAF2F7"),
}

TOKENS = [
    ("comment", ("#8A9AA4", "#7E8F9A"), "italic"),
    (("keyword", "storage"), ("#2F6B93", "#8CC5E8"), None),
    ("string", ("#8A6B2E", "#FEE6BB"), None),
    (("entity.name.function", "support.function"), ("#1F7A8C", "#8FD9C8"), None),
    (("entity.name.type", "support.type", "support.class"), ("#4A6B8A", "#B7C9E8"), None),
    (("constant.numeric", "constant.language", "variable.other.constant"), ("#B06A3E", "#E8B98A"), None),
    ("variable", ("#3A4650", "#E7EEF3"), None),
    ("variable.parameter", ("#5D6E78", "#B9C8D2"), None),
    (("variable.other.property", "support.variable.property"), ("#2F7A8C", "#8FD9C8"), None),
    ("keyword.operator", ("#6B7C88", "#A9B8C2"), None),
    ("punctuation", ("#8A9AA4", "#8595A0"), None),
    ("entity.name.tag", ("#2F6B93", "#8CC5E8"), None),
    ("entity.other.attribute-name", ("#A8802E", "#E2C384"), None),
    ("string.regexp", ("#8A6B2E", "#D9C48A"), None),
    ("constant.character.escape", ("#A8802E", "#FEE6BB"), None),
    ("markup.heading", ("#22303A", "#F3F8FB"), "bold"),
    ("markup.bold", ("#22303A", "#F3F8FB"), "bold"),
    ("markup.italic", ("#22303A", "#F3F8FB"), "italic"),
    ("invalid", ("#B85C5C", "#E39A9A"), None),
]

SEMANTIC = {
    "variable": "#3A4650|#E7EEF3",
    "parameter": "#5D6E78|#B9C8D2",
    "property": "#2F7A8C|#8FD9C8",
    "function": "#1F7A8C|#8FD9C8",
    "method": "#1F7A8C|#8FD9C8",
    "type": "#4A6B8A|#B7C9E8",
    "class": "#4A6B8A|#B7C9E8",
    "interface": "#4A6B8A|#B7C9E8",
    "variable.readonly": "#B06A3E|#E8B98A",
}

PACKAGE = {
    "name": NAME,
    "displayName": DISPLAY,
    "description": "Creamy coastal palette: warm sand and sea blue in the light variant, a neutral graphite coast at night in the dark one.",
    "version": VERSION,
    "publisher": "lilinhuang",
    "engines": {"vscode": "^1.80.0"},
    "categories": ["Themes"],
    "keywords": ["theme", "light", "dark", "coastal", "cream", "blue", "sand", "pastel"],
    "icon": "assets/icon.png",
    "license": "SEE LICENSE IN LICENSE",
    "galleryBanner": {"color": "#1F252B", "theme": "dark"},
    "repository": {"type": "git", "url": REPO},
    "contributes": {
        "themes": [
            {"label": f"{DISPLAY} Light", "uiTheme": "vs",
             "path": f"./themes/{SLUG}-light-color-theme.json"},
            {"label": f"{DISPLAY} Dark", "uiTheme": "vs-dark",
             "path": f"./themes/{SLUG}-dark-color-theme.json"},
        ]
    },
}


def build(variant, index):
    colors = {key: pair[index] for key, pair in UI.items()}
    tokens = []
    for scope, pair, style in TOKENS:
        settings = {"foreground": pair[index]}
        if style:
            settings["fontStyle"] = style
        tokens.append({"scope": [scope] if isinstance(scope, str) else list(scope),
                       "settings": settings})
    theme = {
        "name": f"{DISPLAY} {variant.title()}",
        "type": variant,
        "colors": colors,
        "semanticHighlighting": True,
        "semanticTokenColors": {k: v.split("|")[index] for k, v in SEMANTIC.items()},
        "tokenColors": tokens,
    }
    out = THEMES / f"{SLUG}-{variant}-color-theme.json"
    out.write_text(json.dumps(theme, indent=2) + "\n", encoding="utf-8")
    print("wrote", out.relative_to(BASE), len(colors), "UI colors")


def main():
    THEMES.mkdir(exist_ok=True)
    for index, variant in enumerate(("light", "dark")):
        build(variant, index)
    (BASE / "package.json").write_text(json.dumps(PACKAGE, indent=2) + "\n", encoding="utf-8")
    print("wrote package.json")


if __name__ == "__main__":
    main()
