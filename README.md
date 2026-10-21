<p align="center">
  <img src="https://raw.githubusercontent.com/vaxicy/coastal-cream-theme/main/assets/icon.png" alt="Coastal Cream Theme logo" width="128">
</p>

<h1 align="center">Coastal Cream Theme</h1>

<p align="center">
  <a href="https://marketplace.visualstudio.com/items?itemName=lilinhuang.coastal-cream-theme"><img src="https://img.shields.io/badge/VS%20Code-Theme-4E86A8?logo=visual-studio-code" alt="VS Code Theme"></a>
  <img src="https://img.shields.io/badge/version-1.0.0-8CC5E8?logo=visual-studio-code" alt="version 1.0.0">
  <img src="https://img.shields.io/badge/Variants-Light%20%26%20Dark-A6D3EF?logo=visual-studio-code" alt="Light and Dark variants">
  <a href="https://github.com/vaxicy/coastal-cream-theme/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-Non--Commercial-lightgrey" alt="License: Non-Commercial"></a>
</p>

A soft coastal theme: **creamy paper** with sea blue and warm sand in the light variant, and a **neutral graphite coast at night** in the dark one. Both variants share one palette, so switching changes the hour, not the place.

一套柔和的海岸色主题：浅色版是**奶油纸白**配海蓝与暖沙，深色版是**夜色里的石墨海岸**。明暗两版共用同一套色板，切换时变的是时辰，不是地点。

## Preview / 预览

| Light 浅色 | Dark 深色 |
| --- | --- |
| ![Coastal Cream Theme Light](https://raw.githubusercontent.com/vaxicy/coastal-cream-theme/main/store-assets/screenshots/en/screenshot-light.png) | ![Coastal Cream Theme Dark](https://raw.githubusercontent.com/vaxicy/coastal-cream-theme/main/store-assets/screenshots/en/screenshot-dark.png) |

> Both previews are captured from a real VS Code window running the theme — no mockups.
>
> 上方预览图取自真实运行该主题的 VS Code 窗口截图，非模拟图。

## Palette / 色板

| Role | Light | Dark |
| --- | --- | --- |
| Editor background | `#FDF9F7` creamy paper | `#1F252B` graphite coast |
| Foreground | `#3A4650` deep sea ink | `#E7EEF3` sea mist |
| Muted text / placeholders | `#7C8A94` | `#93A2AC` |
| Side bar | `#F3F8FB` with `#43505A` text | `#1C2228` with `#C6D4DD` text |
| Panel / terminal | `#FBF6F2` | `#1B2127` |
| Title bar | `#FBF1E2` with `#4A5560` text | `#191E23` with `#CFDCE4` text |
| Tab bar / inactive tab | `#EFECE6` | `#1B2127` |
| Active tab / indicator | `#33414B` text, `#8CC5E8` top border | `#F3F8FB` text, `#8CC5E8` top border |
| Activity bar | `#EAF3F9` with `#4E86A8` icons | `#171C21` with `#A9C4D3` icons |
| Status bar | `#4E86A8` with `#FDF9F7` text | `#3A5568` with `#EAF2F7` text |
| Selection | `#CFE8F7` shallow water | `#2F4657` evening tide |
| Current line | `#FBF5EE` | `#262E35` |
| Borders | `#E3E8EA` | `#333D46` |
| Indent guides | `#E5EDF1` | `#2E373F` |
| Button | `#8CC5E8` with `#213038` text (hover `#6FAFD8`) | `#8CC5E8` with `#1F252B` text (hover `#A9D3EE`) |
| Badge | `#4E86A8` with white text | `#8CC5E8` with `#1F252B` text |
| Cursor | `#4E86A8` | `#8CC5E8` |
| Links | `#2F6B93` | `#8CC5E8` |
| Errors / warnings | `#B85C5C` / `#A8802E` | `#E39A9A` / `#E2C384` |
| Git added / modified / deleted | `#4E8A5E` / `#A8802E` / `#B85C5C` | `#8FC9A0` / `#E2C384` / `#E39A9A` |

Cream `#FDF9F7`, sky `#A6D3EF`, sea `#4E86A8`, sand `#FEE6BB` and mint `#CEE2D0` carry both variants, so a file still reads as "coastal cream" after switching.

奶白 `#FDF9F7`、天蓝 `#A6D3EF`、海蓝 `#4E86A8`、沙黄 `#FEE6BB` 与薄荷 `#CEE2D0` 贯穿明暗两版，切换后整个文件还是同一片海岸。

## Syntax mapping / 语法映射

| Syntax | Light | Dark |
| --- | --- | --- |
| Comments | `#8A9AA4` | `#7E8F9A` |
| Keywords / storage | `#2F6B93` | `#8CC5E8` |
| Strings | `#8A6B2E` | `#FEE6BB` |
| Functions / methods | `#1F7A8C` | `#8FD9C8` |
| Types / classes | `#4A6B8A` | `#B7C9E8` |
| Numbers / constants | `#B06A3E` | `#E8B98A` |
| Variables | `#3A4650` | `#E7EEF3` |
| Parameters | `#5D6E78` | `#B9C8D2` |
| Properties | `#2F7A8C` | `#8FD9C8` |
| Operators | `#6B7C88` | `#A9B8C2` |
| Punctuation | `#8A9AA4` | `#8595A0` |
| HTML tags | `#2F6B93` | `#8CC5E8` |
| Attribute names | `#A8802E` | `#E2C384` |
| Regex | `#8A6B2E` | `#D9C48A` |
| Escape characters | `#A8802E` | `#FEE6BB` |

Semantic highlighting is enabled, so variables, parameters, properties, functions and types follow the same mapping in TypeScript, JavaScript, Go, Rust and Python.

已开启语义高亮，TypeScript、JavaScript、Go、Rust 与 Python 里的变量、参数、属性、函数与类型都会落到同一套配色。

## Install / 安装

Search **Coastal Cream Theme** in the Extensions view, then pick `Coastal Cream Theme Light` or `Coastal Cream Theme Dark` from the theme picker (`Ctrl+K Ctrl+T`).

在扩展面板搜索 **Coastal Cream Theme**，安装后用 `Ctrl+K Ctrl+T` 在 `Coastal Cream Theme Light` 与 `Coastal Cream Theme Dark` 之间选择。

```bash
code --install-extension lilinhuang.coastal-cream-theme
```

## Build from source / 本地构建

```bash
py -3 scripts/build-theme.py       # regenerate both theme JSON files
py -3 scripts/generate-icon.py     # export assets/icon.png from the selected logo
py -3 scripts/capture-real-screenshots.py   # real VS Code screenshots
```

## License / 许可证

Non-Commercial License — free for personal, educational and non-commercial use. See [LICENSE](https://github.com/vaxicy/coastal-cream-theme/blob/main/LICENSE).

非商业许可证：个人、教育与非商业用途免费使用，详见 LICENSE。
