---
version: alpha
name: Developers
description: |
  The OpenAI Developers platform embodies a clean, technical minimalism grounded
  in trust and clarity. The design prioritizes developer usability through a
  monochromatic foundation, generous whitespace, and a deliberate absence of
  decorative flourish. The palette is anchored in near-black neutrals with a
  single clean white canvas, creating high contrast for code readability.
  Typography is precise and generous, with tight letter-spacing on display sizes
  reinforcing a contemporary, engineered aesthetic. The system favors subtle
  borders and minimal shadows—elevation is communicated primarily through
  surface colour rather than depth effects—resulting in a calm, focused
  experience suited to technical documentation.
source:
  url: "https://developers.openai.com/api/docs"
  pagesAnalyzed: 1
  extractedAt: 2026-10-24
  tokensMeasured: true
colors:
  primary: "#181818"
  canvas: "#FFFFFF"
  on-primary: "#FFFFFF"
  ink: "#0D0D0D"
  body: "#181818"
  muted: "#282828"
  faint: "#5D5D5D"
typography:
  display:
    fontFamily: "OpenAI Sans"
    fontSize: 80px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: -1.6px
  heading-lg:
    fontFamily: "OpenAI Sans"
    fontSize: 30px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: -0.6px
  heading-md:
    fontFamily: "OpenAI Sans"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: -0.52px
  heading-sm:
    fontFamily: "OpenAI Sans"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.61
    letterSpacing: -0.18px
  heading-xs:
    fontFamily: "OpenAI Sans"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: -0.16px
  body-md:
    fontFamily: "OpenAI Sans"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: -0.16px
  body-sm:
    fontFamily: "OpenAI Sans"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: -0.14px
  body-sm-tight:
    fontFamily: "OpenAI Sans"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: -0.16px
  body-sm-loose:
    fontFamily: "OpenAI Sans"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.71
    letterSpacing: -0.14px
  body-sm-strong:
    fontFamily: "OpenAI Sans"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: -0.16px
  body-sm-2:
    fontFamily: "OpenAI Sans"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: -0.14px
  button-sm:
    fontFamily: "OpenAI Sans"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: -0.14px
  button-sm-tight:
    fontFamily: "OpenAI Sans"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.71
    letterSpacing: -0.16px
  code-md:
    fontFamily: "SF Mono"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: -0.16px
  code-sm:
    fontFamily: "SF Mono"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: -0.16px
rounded:
  none: 0px
  xs: 12px
  full: 9999px
spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 20px
  xl: 24px
  xxl: 32px
  xxxl: 40px
  section: 64px
  band: 96px
borderWidths:
  thin: 1px
shadows:
  sm: "oklab(0 0 0 / 0.05) 0px 0px 0px 1px, rgba(0, 0, 0, 0.08) 0px 2px 4px -1px"
  md: "oklab(0 0 0 / 0.1) 0px 0px 0px 1px, rgba(15, 23, 42, 0.55) 0px 36px 120px -48px"
  lg: "rgba(15, 23, 42, 0.45) 0px 16px 48px -18px"
elevationStrategy: layered-micro
themes:
  derived: dark   # the other theme is the site's measured palette
  light:
    bg: "#FFFFFF"
    surface: "#F7F7F7"
    surfaceRaised: "#EEEEEE"
    text: "#0D0D0D"
    textMuted: "#181818"
    border: "#E2E2E2"
    accent: "#181818"
    accentFg: "#FFFFFF"
    focusRing: "#181818"
    elevation: shadow
  dark:
    bg: "#0F0F10"
    surface: "#1D1D1E"
    surfaceRaised: "#29292A"
    text: "#F6F6F6"
    textMuted: "#9E9E9F"
    border: "#353536"
    accent: "#7E7E7E"
    accentFg: "#0B0B0C"
    focusRing: "#5F5F5F"
    elevation: "border+surface"
gradients:
  - context: section
    kind: linear
    value: "linear-gradient(rgba(0, 0, 0, 0), rgba(0, 0, 0, 0)), linear-gradient(90deg, rgb(228, 246, 235), rgb(234, 242, 255) 65%, rgb(238, 234, 255))"
components:
  button-filled:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    height: 28px
    padding: "4px 10px 4px 10px"
    rounded: 8px
    backgroundColor: "rgb(237, 237, 237)"
  button-icon:
    typography: "{typography.body-md}"
    textColor: "{colors.faint}"
    height: 44px
    rounded: "{rounded.full}"
  button-icon-sm:
    typography: "{typography.body-md}"
    textColor: "{colors.faint}"
    height: 16px
  card:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
    padding: "16px 16px 16px 16px"
    rounded: "{rounded.xs}"
  navigation:
    typography: "{typography.body-md}"
    textColor: "oklab(0 0 0 / 0.9)"
    height: 28px
  link:
    typography: "{typography.heading-xs}"
    textColor: "oklab(0 0 0 / 0.9)"
  link-sm:
    typography: "{typography.body-sm-strong}"
    textColor: "{colors.on-primary}"
    padding: "0px 16px 0px 16px"
    rounded: "{rounded.full}"
states:
  other-hover:
    target: other
    state: hover
    opacity: 1
    transform: "translate(0px)"
  other-active:
    target: other
    state: active
    transform: "scale(0.96)"
  other-focus:
    target: other
    state: focus
    outline: none
  button-active:
    target: button
    state: active
    opacity: 1
  other-focus-visible:
    target: other
    state: focus-visible
    opacity: 1
breakpoints:
  - width: 375
    containerWidth: 365
    gridColumns: 2
    navLinksVisible: 0
    menuToggleVisible: true
    headingPx: 30
    bodyPx: 16
    sectionPaddingX: 16
  - width: 768
    containerWidth: 758
    gridColumns: 4
    navLinksVisible: 0
    menuToggleVisible: true
    headingPx: 30
    bodyPx: 16
    sectionPaddingX: 48
  - width: 1024
    containerWidth: 1014
    gridColumns: 2
    navLinksVisible: 51
    menuToggleVisible: true
    headingPx: 30
    bodyPx: 16
    sectionPaddingX: 48
  - width: 1280
    containerWidth: 1270
    gridColumns: 2
    navLinksVisible: 51
    menuToggleVisible: true
    headingPx: 30
    bodyPx: 16
    sectionPaddingX: 16
  - width: 1440
    containerWidth: 1430
    gridColumns: 2
    navLinksVisible: 51
    menuToggleVisible: true
    headingPx: 30
    bodyPx: 16
    sectionPaddingX: 16
coverage:
  statesFound: 61
  gradientsFound: 1
  rolesUnassigned: 0
  archetypesUnnamed: 0
  archetypesDetected: 0
  responsiveMeasured: true
  stylesheetsBlocked: false
  semanticRampDeclared: false
---

# Design System Inspired by OpenAI

## 1. Visual Theme & Atmosphere

The OpenAI Developers platform embodies a clean, technical minimalism grounded in trust and clarity. The design prioritizes developer usability through a monochromatic foundation, generous whitespace, and a deliberate absence of decorative flourish. The palette is anchored in near-black neutrals with a single clean white canvas, creating high contrast for code readability. Typography is precise and generous, with tight letter-spacing on display sizes reinforcing a contemporary, engineered aesthetic. The system favors subtle borders and minimal shadows—elevation is communicated primarily through surface colour rather than depth effects—resulting in a calm, focused experience suited to technical documentation.

**Key Characteristics**
- Monochromatic palette centred on `{colors.primary}` (`#181818`) and neutral gray ramps
- Generous whitespace and breathing room throughout
- Pixel-precise typography with tight, negative letter-spacing on large sizes
- Minimal elevation; colour blocking preferred over shadows
- High contrast for readability of code and documentation
- Pill-shaped interactive controls (`{rounded.full}` — `9999px`)
- Soft, rounded card containers (`{rounded.xs}` — `12px`)
- Functional, no ornament

## 2. Color Palette & Roles

### Primary
- **Primary / Brand** (`{colors.primary}` — `#181818`): Primary CTA fills, brand accent, active states, body copy, and heading emphasis. Dark near-black used for text and button backgrounds.

### Neutral Scale
- **Canvas** (`{colors.canvas}` — `#FFFFFF`): Default page background and surfaces. Label and accent text on dark backgrounds.
- **Ink** (`{colors.ink}` — `#0D0D0D`): Primary heading and high-emphasis text. Darkest text colour for maximum contrast.
- **Muted** (`{colors.muted}` — `#282828`): Secondary text, captions, and visual hierarchy reduction.
- **Faint** (`{colors.faint}` — `#5D5D5D`): Tertiary text, placeholder copy, and de-emphasized content.

### Surface & Decorative
- **Gradient (Section Background)**: `linear-gradient(rgba(0, 0, 0, 0), rgba(0, 0, 0, 0)), linear-gradient(90deg, rgb(228, 246, 235), rgb(234, 242, 255) 65%, rgb(238, 234, 255))` — Subtle pastel blend across hero or featured sections, adding visual warmth without breaking the monochromatic core.

## 3. Typography Rules

### Font Family
- **Primary**: OpenAI Sans (all text, headings, body, buttons)
- **Code**: SF Mono (code blocks, technical content)
- Fallback stack (for OpenAI Sans): `-apple-system, BlinkMacSystemFont, "Segoe UI", "Helvetica Neue", sans-serif`
- Fallback stack (for SF Mono): `"SF Mono", Monaco, "Cascadia Code", "Courier New", monospace`

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|---|---|---|---|---|---|---|
| Display | OpenAI Sans | 80px | 600 | 1.0 | -1.6px | Hero / ultra-large showcase text |
| Heading Large | OpenAI Sans | 30px | 600 | 1.4 | -0.6px | Page titles, major sections |
| Heading Medium | OpenAI Sans | 26px | 600 | 1.5 | -0.52px | Section headers |
| Heading Small | OpenAI Sans | 18px | 600 | 1.61 | -0.18px | Subsection titles |
| Heading XS | OpenAI Sans | 16px | 600 | 1.5 | -0.16px | Card titles, component labels |
| Body Medium | OpenAI Sans | 16px | 400 | 1.5 | -0.16px | General content, descriptions |
| Body Small | OpenAI Sans | 14px | 400 | 1.43 | -0.14px | Body copy, list items |
| Body Small (Loose) | OpenAI Sans | 14px | 400 | 1.71 | -0.14px | Relaxed line spacing variant |
| Body Small (Tight) | OpenAI Sans | 14px | 400 | 1.43 | -0.16px | Condensed variant |
| Button Small | OpenAI Sans | 14px | 500 | 1.43 | -0.14px | Button labels, CTAs |
| Button Small (Tight) | OpenAI Sans | 14px | 500 | 1.71 | -0.16px | Button variant with looser line height |
| Body Strong | OpenAI Sans | 14px | 600 | 1.43 | -0.14px | Emphasis within body text |
| Code Small | SF Mono | 14px | 400 | 1.43 | -0.16px | Inline code, technical snippets |
| Code Medium | SF Mono | 16px | 400 | 1.5 | -0.16px | Code blocks |

### Principles
- Tight, negative letter-spacing on all sizes drives a contemporary, engineered feel
- Display and heading sizes use aggressive letter-spacing compression (`-1.6px` to `-0.18px`) for visual impact
- Line height increases with text size for comfortable reading
- Body text is generous at `14px` to `16px`, supporting long-form documentation
- Weights are minimal: 400 (regular), 500 (button/emphasis), 600 (headings/strong)
- Code uses fixed-width SF Mono at matching baseline sizes for alignment

## 4. Component Stylings

### Buttons

#### Filled Button
- **Background**: `{colors.primary}` (`#181818`)
- **Text Color**: `{colors.muted}` (`#282828`)
- **Padding**: `{spacing.xs}` `{spacing.sm}` `{spacing.xs}` `{spacing.sm}` (4px 12px 4px 12px)
- **Font**: `{typography.button-sm}` (14px, weight 500)
- **Border Radius**: `{rounded.full}` (`9999px`) — pill shape
- **Border**: None
- **Box Shadow**: None
- **Hover State**: `background-color: var(--button-background-color-hover)`, `transform: scale(1)`
- **Active State**: `background-color: var(--button-background-color-active)`, `transform: scale(var(--scale))`
- **Focus Visible**: `outline: 2px solid var(--color-ring)`

#### Icon Button
- **Background**: Transparent
- **Text Color**: `{colors.faint}` (`#5D5D5D`)
- **Padding**: `0`
- **Width**: 44px
- **Height**: 44px
- **Font**: `{typography.body-md}` (16px, weight 400)
- **Border Radius**: `{rounded.full}` (`9999px`)
- **Border**: None
- **Box Shadow**: None
- **Hover State**: `opacity: 1`, `transform: scale(1)`
- **Focus Visible**: `outline: 2px solid var(--avatar-ring-color)`

#### Icon Button Small
- **Background**: Transparent
- **Text Color**: `{colors.faint}` (`#5D5D5D`)
- **Padding**: `0`
- **Width**: 16px
- **Height**: 16px
- **Font**: `{typography.body-md}` (16px, weight 400)
- **Border Radius**: `{rounded.none}` (`0px`)
- **Border**: None
- **Box Shadow**: None

### Cards & Containers

#### Default Card
- **Background**: `{colors.canvas}` (`#FFFFFF`)
- **Text Color**: `{colors.ink}` (`#0D0D0D`)
- **Padding**: `{spacing.md}` (`16px`) all sides
- **Font**: `{typography.body-md}` (16px, weight 400)
- **Border Radius**: `{rounded.xs}` (`12px`)
- **Border**: 1px solid transparent
- **Box Shadow**: None
- **Hover State**: `border-color: var(--gray-300)` or `var(--gray-600)`, background holds

### Navigation

#### Default Navigation Link
- **Background**: Transparent
- **Text Color**: `oklab(0 0 0 / 0.9)` — near-black with alpha
- **Padding**: `0`
- **Font**: `{typography.body-md}` (16px, weight 400)
- **Border Radius**: `{rounded.none}` (`0px`)
- **Border**: None
- **Box Shadow**: None
- **Hover State**: `color: var(--color-text-emphasis)`, `text-decoration: underline`
- **Focus Visible**: `outline: 2px solid var(--color-ring)`

### Inputs & Forms

#### Text Input
- **Background**: `{colors.canvas}` (`#FFFFFF`)
- **Text Color**: `{colors.ink}` (`#0D0D0D`)
- **Border**: 1px solid `rgba(0, 0, 0, 0.05)` (hairline)
- **Border Radius**: `{rounded.xs}` (`12px`)
- **Hover State**: `border-color: var(--gray-300)` or `var(--gray-600)`
- **Focus State**: `box-shadow: var(--shadow-hairline), 0 2px 12px 0 #0000000a`
- **Focus Visible**: `outline: 2px solid var(--color-ring)` inset

#### Radio & Select
- **Hover State**: `box-shadow: 0 0 0 1px var(--radio-group-indicator-border-color-hover) inset`
- **Focus State**: `box-shadow: inset 0 0 0 2px var(--slider-range-color)` (for range inputs)

### Links

#### Primary Link
- **Background**: Transparent
- **Text Color**: `oklab(0 0 0 / 0.9)`
- **Font**: `{typography.heading-xs}` (16px, weight 600)
- **Border Radius**: `{rounded.none}` (`0px`)
- **Border**: None
- **Hover State**: `color: var(--link-primary-text-color-hover)`, `text-decoration: underline`
- **Focus Visible**: `outline: 2px solid var(--color-ring)`, `color: var(--color-text-emphasis)`

#### Secondary Link (Small)
- **Background**: Transparent
- **Text Color**: `{colors.canvas}` (`#FFFFFF`) on dark backgrounds
- **Padding**: `0` `{spacing.md}` (`0 16px`)
- **Font**: `{typography.button-sm}` (14px, weight 500)
- **Border Radius**: `{rounded.full}` (`9999px`)
- **Border**: None
- **Hover State**: `color: var(--button-text-color-hover)`
- **Focus Visible**: `outline: 2px solid var(--color-ring)`

## 5. Layout Principles

### Spacing System
Base unit: `{spacing.xxs}` — `4px`. Scale follows an 8px rhythm with selective multiples for larger gaps:
- `{spacing.xxs}` = 4px — micro-adjustments, icon padding
- `{spacing.xs}` = 8px — tight component gaps
- `{spacing.sm}` = 12px — small padding, list item spacing
- `{spacing.md}` = 16px — standard component padding, body content gutters
- `{spacing.lg}` = 20px — moderate gaps between elements
- `{spacing.xl}` = 24px — card internal spacing
- `{spacing.xxl}` = 32px — section breaks
- `{spacing.xxxl}` = 40px — large content blocks
- `{spacing.section}` = 64px — major section padding vertical
- `{spacing.band}` = 96px — full-width hero/featured section padding

### Grid & Container
- **Max Content Width**: 1430px (measured at 1440px viewport)
- **Flexible Content Column**: Content scales with viewport, maintaining `{spacing.lg}` gutters:
  - 375px: 365px (full width − 10px each side)
  - 768px: 758px (full width − 10px each side)
  - 1024px+: 1014px–1430px
- **Grid Columns**: Layout is primarily 2-column at larger breakpoints; mobile collapses to single column
- **Section Patterns**: Full-width sections with centered content, nested padding of `{spacing.section}` vertically and `{spacing.lg}` to `{spacing.xxxl}` horizontally depending on viewport

### Whitespace Philosophy
Whitespace is functional and generous, supporting rapid scanning and reducing cognitive load. Large sections breathe with `{spacing.section}` (`64px`) and `{spacing.band}` (`96px`) gaps. Component internal padding uses `{spacing.md}` as default. Negation of ornament (no background textures, minimal shadows) allows semantic whitespace to emerge naturally, guiding focus to content and CTAs.

### Border Radius Scale
- `{rounded.none}` = `0px` — sharp corners on images, input text fields, and fine-grained UI
- `{rounded.xs}` = `12px` — cards, small containers, moderate softness
- `{rounded.full}` = `9999px` — buttons, icon buttons, pill-shaped interactive elements

### Border Widths
- **Thin**: `1px` — hairline borders on buttons, inputs, and cards for definition without weight

## 6. Depth & Elevation

| Level | Treatment | Use |
|---|---|---|
| Flat | No shadow, colour blocking only | Default cards, text layers, backgrounds |
| Micro Lift | `rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, oklab(0 0 0 / 0.05) 0px 0px 0px 1px, rgba(0, 0, 0, 0.08) 0px 2px 4px -1px` | Subtle container lift, custom component surfaces (md elevation) |
| Raised | `rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, oklab(0 0 0 / 0.1) 0px 0px 0px 1px, rgba(15, 23, 42, 0.55) 0px 36px 120px -48px` | Elevated custom surfaces (lg elevation) |
| Deep | `rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(15, 23, 42, 0.45) 0px 16px 48px -18px` | Deep shadows on modals, overlays (xl elevation) |

**Shadow Philosophy**: This system employs a layered-micro elevation strategy. Rather than bold, obvious shadows, depth emerges from a stack of near-transparent layers: a hairline colour border (critical for button focus rings and input definition) plus two opacity-modulated drop shadows. This creates barely-there lift suitable for a technical product where shadows might distract from content. Buttons carry no shadow (`sm` level), while custom surfaces use measured micro-shadows only when a container must float above the background.

### Opacity Levels
- **50%** (`0.50`) — Intermediate hover or semi-active states
- **75%** (`0.75`) — Slightly transparent overlays or emphasis reduction

### Z-index / Layering
- **10**: Dropdown menus, initial popover level
- **20**: Secondary dropdowns or nested overlays
- **40**: Modals, major dialogs
- **50**: High-priority alerts or tooltips
- **60**: Critical overlays, top-level notifications
- **80**: Sticky headers, permanently elevated UI

## 7. Do's and Don'ts

### Do
- Use pill-shaped buttons (`{rounded.full}`) for all primary CTAs and interactive controls.
- Maintain high contrast between text and backgrounds; rely on the `{colors.primary}` (`#181818`) and `{colors.canvas}` (`#FFFFFF`) pair.
- Apply negative letter-spacing consistently on display and heading sizes for visual compression and technical polish.
- Space sections with `{spacing.section}` (`64px`) and major features with `{spacing.band}` (`96px`) for breathing room.
- Use `{spacing.md}` (`16px`) as the default component padding; scale up or down by multiples of 4px as needed.
- Embed colour blocking (surface colour changes) instead of heavy shadows to communicate depth.
- Keep buttons and interactive elements focusable with `2px solid` outline in the system's ring colour.
- Use the gradient background sparingly for hero or featured sections; do not overuse across the entire page.

### Don't
- Do not add decorative elements, gradients, or background patterns outside the defined section gradient.
- Do not use rounded corners smaller than `{rounded.xs}` (`12px`) on containers; keep them soft but intentional.
- Do not introduce new font sizes or weights beyond the documented hierarchy; use existing sizes and scale them contextually.
- Do not apply shadows to buttons; they are flat and interactive through colour and scale.
- Do not use border-radius on images; keep them `{rounded.none}` (`0px`) for crispness.
- Do not reduce line height below the specified ratios; readability is paramount in technical documentation.
- Do not apply opacity to text directly for emphasis; use colour or weight changes instead.
- Do not mix semantic status colours (error, success, warning) with the primary palette; this system does not define them.

## 8. Responsive Behavior

### Breakpoints

| Breakpoint | Width | Grid Columns | Nav Links Visible | Section Padding X | Largest Heading | Body Size |
|---|---|---|---|---|---|---|
| Mobile | 375px | 1 | 0 (hidden, menu toggle shown) | `{spacing.md}` (16px) | 30px | 16px |
| Tablet | 768px | 2–4 | 0 (hidden, menu toggle shown) | `{spacing.xxxl}` (48px) | 30px | 16px |
| Desktop | 1024px | 2 | 51px visible | `{spacing.xxxl}` (48px) | 30px | 16px |
| Large Desktop | 1280px+ | 2 | 51px visible | `{spacing.md}` (16px) | 30px | 16px |

**Collapse Point**: Navigation menu collapses and shows toggle at or below `1024px` viewport width. Above `1024px`, horizontal nav links are displayed inline.

### Touch Targets
- Minimum interactive target size: `44px` × `44px` (measured on icon buttons)
- Small icon targets: `16px` × `16px` (decorative or supplementary only, not primary interaction)
- Button minimum height: `36px` (measured on secondary links)

### Collapsing Strategy
- **Mobile (375px)**: Single-column layout, full-width content, section padding reduces to `{spacing.md}` horizontally. Navigation menu hidden behind toggle. Display and heading sizes remain at `30px` to prioritize readable hierarchy.
- **Tablet (768px)**: Content widens, section padding increases to `{spacing.xxxl}` (`48px`). Grid begins supporting 2–4 columns for content cards. Navigation remains toggled.
- **Desktop (1024px+)**: Full horizontal navigation visible. Multi-column layouts and sidebar patterns possible. Section padding stabilizes at `{spacing.xxxl}` (`48px`) or reduces to `{spacing.md}` depending on viewport width.
- **Heading Consistency**: Largest heading (`{typography.heading-lg}` — `30px`) stays constant across all breakpoints; body text remains `16px` for consistency and readability.

## 9. Agent Prompt Guide

### Quick Color Reference
- **Primary CTA / Brand Accent**: Primary (`#181818`)
- **Canvas / Page Background**: Canvas (`#FFFFFF`)
- **Heading Text**: Ink (`#0D0D0D`)
- **Body / Secondary Text**: Muted (`#282828`) for captions; Faint (`#5D5D5D`) for tertiary
- **Borders / Hairlines**: `rgba(0, 0, 0, 0.05)` or alpha-adjusted grays

### Iteration Guide
1. All interactive elements (buttons, icon buttons, form inputs) use `{rounded.full}` (`9999px`) unless they are images or fine-grained UI (then `{rounded.none}`). Cards and containers use `{rounded.xs}` (`12px`).
2. Typography is always from the documented hierarchy (`{typography.display}`, `{typography.heading-lg}`, `{typography.body-md}`, etc.). Do not invent sizes; scale existing ones by adjusting weight or colour.
3. Buttons have no shadow (`sm` level: all transparent layers). Elevation on custom surfaces uses `md` or `lg` shadows only when a container must visually float; default is flat.
4. Spacing follows the scale: start with `{spacing.md}` (`16px`) for component padding and gutters. Use `{spacing.section}` (`64px`) between major sections, `{spacing.band}` (`96px`) for hero or featured bands.
5. Letter-spacing is tight and negative on all sizes; apply the exact value from the hierarchy table. Do not round to zero on any heading or display.
6. Focus states always use a `2px solid` outline in the system's ring colour (or `--color-ring` CSS variable). Do not omit focus visible states on interactive elements.
7. Colours are semantic: `{colors.primary}` is brand/emphasis, `{colors.canvas}` is background, `{colors.ink}` is primary text, `{colors.muted}` is secondary, `{colors.faint}` is tertiary. Do not repurpose them as semantic status colours.
8. Breakpoint collapse is at `1024px`: navigation goes hidden/toggled below this, inline above. Section padding and content width shift at `768px` (tablet) and `1280px` (large desktop).
9. Opacity levels are `0.50` and `0.75` for interactive states; do not invent intermediate values.
10. Z-index ladder: `10` (dropdown), `20` (nested overlay), `40` (modal), `50` (alert), `60` (critical), `80` (sticky header).

## 10. Known Gaps

- **Semantic Status Colours**: The site does not declare or expose error, success, warning, or info colours in its markup. No semantic colour ramp exists; the extraction found only a monochromatic core. If status indication is needed, it must be added and documented separately.
- **Interaction States Not Observed**: Explicit hover, active, and disabled states for form fields, links, and buttons are defined in the CSS codebase but were not exhaustively captured in component screenshots. Implementation should reference the state rules provided in token data.
- **Dark Mode / Theme Variants**: The extraction analysed a single light theme. No dark mode or theme switching mechanics were observed or measured on the page.
- **Authentication Surfaces**: Content and UI behind login or restricted access were not visited during extraction.
- **Micro-Animations & Transitions**: CSS transitions, animation timings, and keyframes were not extracted. Interaction polish (e.g. button scale, opacity fade) is noted in state rules but not quantified as duration.
- **Icon Library**: No icon set, naming convention, or SVG asset details were provided. Component examples show generic icon placeholders.
- **Component Coverage**: Extraction analysed visible page elements only. Advanced components (tabs, accordions, complex forms, date pickers, modals) may exist elsewhere on the site but were not sampled.
- **Accessibility Roles & ARIA**: Form labels, ARIA attributes, and semantic HTML structure were not extensively documented; implementation should follow WCAG 2.1 AA standards independently.
- **Print Styles**: No print media queries or print-specific styling rules were extracted.