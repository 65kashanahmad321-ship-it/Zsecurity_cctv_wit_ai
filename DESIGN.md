---
name: Aegis Nexus
colors:
  surface: '#0b1326'
  surface-dim: '#0b1326'
  surface-bright: '#31394d'
  surface-container-lowest: '#060e20'
  surface-container-low: '#131b2e'
  surface-container: '#171f33'
  surface-container-high: '#222a3d'
  surface-container-highest: '#2d3449'
  on-surface: '#dae2fd'
  on-surface-variant: '#b9cacb'
  inverse-surface: '#dae2fd'
  inverse-on-surface: '#283044'
  outline: '#849495'
  outline-variant: '#3a494b'
  surface-tint: '#00dbe7'
  primary: '#e1fdff'
  on-primary: '#00363a'
  primary-container: '#00f2ff'
  on-primary-container: '#006a71'
  inverse-primary: '#00696f'
  secondary: '#f5fff3'
  on-secondary: '#003919'
  secondary-container: '#34ff8d'
  on-secondary-container: '#007239'
  tertiary: '#fff6e4'
  on-tertiary: '#3b2f00'
  tertiary-container: '#fed83a'
  on-tertiary-container: '#725e00'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#74f5ff'
  primary-fixed-dim: '#00dbe7'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f54'
  secondary-fixed: '#60ff99'
  secondary-fixed-dim: '#00e479'
  on-secondary-fixed: '#00210c'
  on-secondary-fixed-variant: '#005228'
  tertiary-fixed: '#ffe173'
  tertiary-fixed-dim: '#e8c423'
  on-tertiary-fixed: '#221b00'
  on-tertiary-fixed-variant: '#554500'
  background: '#0b1326'
  on-background: '#dae2fd'
  surface-variant: '#2d3449'
typography:
  display-lg:
    fontFamily: Montserrat
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Montserrat
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Montserrat
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Roboto Flex
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Roboto Flex
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin-desktop: 80px
  margin-mobile: 20px
  container-max: 1440px
---

## Brand & Style
The design system embodies a high-end, cinematic aesthetic tailored for the elite AI security sector. It targets enterprise decision-makers who require the psychological assurance of impenetrable defense combined with cutting-edge technological superiority.

The visual style is a fusion of **Glassmorphism** and **High-Tech Futurism**. It utilizes deep, atmospheric depth, photorealistic lighting, and ultra-fine details to evoke the feeling of a premium command center. Interfaces should feel like "8K resolution" digital surfaces—crisp, translucent, and alive with subtle energy. The emotional response is one of absolute control, silent vigilance, and professional sophistication.

## Colors
The palette is rooted in the "Deep Space" spectrum, utilizing a base of **Deep Slate (#0f172a)** and **True Black (#020617)** to establish a cinematic foundation. 

- **Neon Blue (#00f2ff)**: Used for primary actions, data visualization, and "active" security states. It represents intelligence and connectivity.
- **Futuristic Green (#00ff88)**: Reserved for "secure" status indicators, success states, and secondary highlights. It represents safety and system health.
- **Accents**: Subtle gradients between the two accents are used for high-importance "glow" effects and progress indicators.

## Typography
The typography strategy balances the authoritative, geometric presence of **Montserrat** for headings with the systematic, highly legible nature of **Roboto Flex** for body copy. 

A third tier using **JetBrains Mono** is introduced for technical labels, data readouts, and security timestamps to reinforce the "AI/Code" nature of the product. Display headings should use tight letter-spacing to appear more cinematic and "locked-in."

## Layout & Spacing
The design system employs a **Fluid Grid** model with high internal margins to allow the cinematic background visuals to breathe. 

- **Desktop**: 12-column grid with generous 24px gutters. Content should be centered with an 80px side margin to create a "widescreen" cinematic feel.
- **Mobile**: 4-column grid with 16px gutters and 20px margins. 
- **Rhythm**: All spacing is derived from a 4px base unit. Component internal padding should be generous (e.g., 32px for cards) to maintain a premium, spacious atmosphere.

## Elevation & Depth
Depth is the core differentiator of this design system. It is achieved through **Glassmorphism** and atmospheric lighting rather than traditional shadows.

1.  **Backdrop Blur**: Surfaces use a heavy `20px` to `40px` blur to create a frosted glass effect over background imagery.
2.  **Inner Glows**: Elements are defined by a `1px` semi-transparent white border on the top and left edges to simulate light hitting a glass edge.
3.  **Neon Bloom**: High-elevation components (like active alerts) emit a soft `0 0 20px` glow using the primary Neon Blue color.
4.  **Z-Axis**: Layering is strictly enforced. The "HUD" (Head-Up Display) layer sits on top with the highest transparency, while content cards sit mid-depth.

## Shapes
The shape language is **Soft (0.25rem)** but precise. While corners are slightly rounded to avoid the harshness of brutalism, they remain sharp enough to feel engineered and professional. 

Interactive elements like buttons use slightly higher rounding (0.5rem) to signify touchability. "Glass" panels should always have a subtle, high-contrast stroke to define their silhouette against the dark backgrounds.

## Components
- **Frosted Glass Cards**: Built with `backdrop-filter: blur(30px)`, a `1px` border of `rgba(255,255,255,0.1)`, and a dark gradient fill.
- **Action Buttons**: Primary buttons use a solid Neon Blue fill with a `0 0 15px` outer glow on hover. Secondary buttons use a ghost style with a Blue stroke.
- **System Transitions**: All interactions must run at a locked **60FPS**. Use `cubic-bezier(0.22, 1, 0.36, 1)` for all transitions (the "Expo-Out" feel) with a standard duration of `300ms`.
- **Status Chips**: Small, high-contrast pills with a "pulsing" dot indicator for real-time security monitoring.
- **Input Fields**: Dark, inset backgrounds with a Neon Blue focus ring that glows when active.
- **HUD Overlays**: Ultra-thin lines and monospaced data points that appear to "scan" in using a clip-path animation upon page load.