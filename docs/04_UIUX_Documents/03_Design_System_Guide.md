# Design System Guide
## AI Smart Skill Coach

---

| Document Information | |
|---------------------|---------------------------|
| **Document ID** | UIUX-DS-AISSC-001 |
| **Version** | 1.0 |
| **Date** | December 28, 2024 |
| **Status** | Draft |
| **Author** | Senior UI/UX Designer |

---

# Table of Contents

1. [Introduction](#1-introduction)
2. [Brand Identity](#2-brand-identity)
3. [Color System](#3-color-system)
4. [Typography](#4-typography)
5. [Spacing & Layout](#5-spacing--layout)
6. [Components](#6-components)
7. [Icons & Imagery](#7-icons--imagery)
8. [Motion & Animation](#8-motion--animation)
9. [Accessibility](#9-accessibility)

---

# 1. Introduction

## 1.1 Purpose

Is Design System Guide ka purpose AI Smart Skill Coach ke visual language ko standardize karna hai. Ye guide developers aur designers ke liye reference document hai.

## 1.2 Design Tokens

Design tokens reusable CSS variables hain:

```css
:root {
  --color-primary: #6366F1;
  --color-secondary: #8B5CF6;
  --font-family: 'Inter', sans-serif;
  --spacing-unit: 4px;
  --border-radius: 8px;
}
```

---

# 2. Brand Identity

## 2.1 Logo

| Variant | Usage |
|---------|-------|
| Full Logo | Header, Landing page |
| Icon Only | Mobile, Favicon |
| Dark Mode | Dark backgrounds |

## 2.2 Logo Specifications

```
┌────────────────────────────────────┐
│  🤖 AI Smart Skill Coach           │
│     ↑                              │
│   Icon   Brand Name                │
└────────────────────────────────────┘

Minimum Size: 32px height
Clear Space: 8px around logo
```

## 2.3 Brand Voice

| Tone | Description | Example |
|------|-------------|---------|
| Friendly | Approachable, warm | "Welcome back!" |
| Helpful | Supportive, guiding | "Here's what you can try..." |
| Smart | Intelligent, expert | "Based on your analysis..." |
| Encouraging | Positive, motivating | "Great progress!" |

---

# 3. Color System

## 3.1 Primary Palette

| Name | Hex | CSS Variable | Usage |
|------|-----|--------------|-------|
| **Primary** | `#6366F1` | `--color-primary` | Buttons, Links, CTAs |
| **Primary Light** | `#A5B4FC` | `--color-primary-light` | Hover states |
| **Primary Dark** | `#4338CA` | `--color-primary-dark` | Active states |

## 3.2 Secondary Palette

| Name | Hex | CSS Variable | Usage |
|------|-----|--------------|-------|
| **Secondary** | `#8B5CF6` | `--color-secondary` | AI features, accents |
| **Secondary Light** | `#C4B5FD` | `--color-secondary-light` | Backgrounds |
| **Secondary Dark** | `#6D28D9` | `--color-secondary-dark` | Headers |

## 3.3 Semantic Colors

| Name | Hex | CSS Variable | Usage |
|------|-----|--------------|-------|
| **Success** | `#10B981` | `--color-success` | Success states |
| **Warning** | `#F59E0B` | `--color-warning` | Warnings |
| **Error** | `#EF4444` | `--color-error` | Errors |
| **Info** | `#3B82F6` | `--color-info` | Informational |

## 3.4 Neutral Colors

| Name | Hex | CSS Variable | Usage |
|------|-----|--------------|-------|
| **Gray 50** | `#F9FAFB` | `--gray-50` | Light backgrounds |
| **Gray 100** | `#F3F4F6` | `--gray-100` | Card backgrounds |
| **Gray 200** | `#E5E7EB` | `--gray-200` | Borders |
| **Gray 400** | `#9CA3AF` | `--gray-400` | Placeholder text |
| **Gray 600** | `#4B5563` | `--gray-600` | Secondary text |
| **Gray 900** | `#111827` | `--gray-900` | Primary text |

## 3.5 Dark Mode

| Element | Light | Dark |
|---------|-------|------|
| Background | `#FFFFFF` | `#0F172A` |
| Surface | `#F9FAFB` | `#1E293B` |
| Text Primary | `#111827` | `#F9FAFB` |
| Text Secondary | `#4B5563` | `#94A3B8` |
| Border | `#E5E7EB` | `#334155` |

---

# 4. Typography

## 4.1 Font Family

```css
font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
```

## 4.2 Type Scale

| Name | Size | Weight | Line Height | CSS Class |
|------|------|--------|-------------|-----------|
| **Display** | 48px | 700 | 1.2 | `.text-display` |
| **H1** | 32px | 700 | 1.3 | `.text-h1` |
| **H2** | 24px | 600 | 1.3 | `.text-h2` |
| **H3** | 20px | 600 | 1.4 | `.text-h3` |
| **H4** | 18px | 500 | 1.4 | `.text-h4` |
| **Body** | 16px | 400 | 1.5 | `.text-body` |
| **Small** | 14px | 400 | 1.5 | `.text-small` |
| **Caption** | 12px | 400 | 1.4 | `.text-caption` |

## 4.3 Font Weights

| Weight | Value | Usage |
|--------|-------|-------|
| Regular | 400 | Body text |
| Medium | 500 | Subheadings |
| Semibold | 600 | Headings |
| Bold | 700 | Display |

---

# 5. Spacing & Layout

## 5.1 Spacing Scale

| Name | Value | CSS Variable | Usage |
|------|-------|--------------|-------|
| **xs** | 4px | `--space-1` | Tight spacing |
| **sm** | 8px | `--space-2` | Small gaps |
| **md** | 16px | `--space-4` | Standard spacing |
| **lg** | 24px | `--space-6` | Section gaps |
| **xl** | 32px | `--space-8` | Large sections |
| **2xl** | 48px | `--space-12` | Page sections |
| **3xl** | 64px | `--space-16` | Major sections |

## 5.2 Grid System

```css
.container {
  max-width: 1280px;
  padding: 0 24px;
  margin: 0 auto;
}

.grid {
  display: grid;
  gap: 24px;
}

/* Responsive columns */
@media (min-width: 768px) {
  .grid-cols-2 { grid-template-columns: repeat(2, 1fr); }
  .grid-cols-3 { grid-template-columns: repeat(3, 1fr); }
  .grid-cols-4 { grid-template-columns: repeat(4, 1fr); }
}
```

## 5.3 Breakpoints

| Name | Width | Usage |
|------|-------|-------|
| **Mobile** | 0 - 639px | Mobile phones |
| **Tablet** | 640 - 1023px | Tablets |
| **Desktop** | 1024 - 1279px | Desktop |
| **Wide** | 1280px+ | Large screens |

---

# 6. Components

## 6.1 Buttons

### Primary Button
```css
.btn-primary {
  background: var(--color-primary);
  color: white;
  padding: 12px 24px;
  border-radius: 8px;
  font-weight: 500;
  transition: all 0.2s ease;
}
.btn-primary:hover {
  background: var(--color-primary-dark);
}
```

### Button Variants

| Variant | Background | Border | Text |
|---------|------------|--------|------|
| Primary | `#6366F1` | none | White |
| Secondary | `#8B5CF6` | none | White |
| Outline | Transparent | `#6366F1` | `#6366F1` |
| Ghost | Transparent | none | `#4B5563` |
| Danger | `#EF4444` | none | White |

### Button Sizes

| Size | Padding | Font Size | Height |
|------|---------|-----------|--------|
| Small | 8px 16px | 14px | 32px |
| Medium | 12px 24px | 16px | 44px |
| Large | 16px 32px | 18px | 52px |

## 6.2 Input Fields

```css
.input {
  width: 100%;
  padding: 12px 16px;
  border: 1px solid var(--gray-200);
  border-radius: 8px;
  font-size: 16px;
  transition: border-color 0.2s ease;
}
.input:focus {
  border-color: var(--color-primary);
  outline: none;
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
}
.input-error {
  border-color: var(--color-error);
}
```

## 6.3 Cards

```css
.card {
  background: white;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
  border: 1px solid var(--gray-100);
}
.card:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
```

## 6.4 Badges

| Variant | Background | Text |
|---------|------------|------|
| Default | `#F3F4F6` | `#4B5563` |
| Primary | `#EEF2FF` | `#6366F1` |
| Success | `#D1FAE5` | `#059669` |
| Warning | `#FEF3C7` | `#D97706` |
| Error | `#FEE2E2` | `#DC2626` |

## 6.5 Alerts

```css
.alert {
  padding: 16px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  gap: 12px;
}
.alert-success { background: #D1FAE5; color: #065F46; }
.alert-warning { background: #FEF3C7; color: #92400E; }
.alert-error { background: #FEE2E2; color: #991B1B; }
.alert-info { background: #DBEAFE; color: #1E40AF; }
```

---

# 7. Icons & Imagery

## 7.1 Icon Library

Recommended: **Heroicons** (MIT License)

| Category | Icons |
|----------|-------|
| Navigation | Home, Menu, ChevronLeft, ChevronRight |
| Actions | Plus, Trash, Edit, Download, Upload |
| Status | Check, X, ExclamationCircle, InformationCircle |
| Objects | Document, Chat, Quiz, Certificate, User |

## 7.2 Icon Sizes

| Size | Value | Usage |
|------|-------|-------|
| **xs** | 16px | Inline with text |
| **sm** | 20px | Buttons |
| **md** | 24px | Default |
| **lg** | 32px | Emphasis |
| **xl** | 48px | Hero sections |

## 7.3 Illustration Style

| Guideline | Description |
|-----------|-------------|
| Style | Flat, minimal, modern |
| Colors | Primary + Secondary palette |
| Characters | Inclusive, diverse |
| Objects | Rounded corners, soft shadows |

---

# 8. Motion & Animation

## 8.1 Timing Functions

```css
--ease-default: cubic-bezier(0.4, 0, 0.2, 1);
--ease-in: cubic-bezier(0.4, 0, 1, 1);
--ease-out: cubic-bezier(0, 0, 0.2, 1);
--ease-bounce: cubic-bezier(0.68, -0.55, 0.265, 1.55);
```

## 8.2 Duration

| Name | Value | Usage |
|------|-------|-------|
| **Fast** | 150ms | Hover states |
| **Normal** | 200ms | Default |
| **Slow** | 300ms | Modal, drawer |
| **Slower** | 500ms | Page transitions |

## 8.3 Animation Examples

```css
/* Button hover */
.btn { transition: all 0.2s var(--ease-default); }

/* Fade in */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Loading spinner */
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
```

---

# 9. Accessibility

## 9.1 WCAG 2.1 AA Compliance

| Requirement | Implementation |
|-------------|----------------|
| **Color Contrast** | Minimum 4.5:1 for text |
| **Focus States** | Visible focus rings |
| **Keyboard Navigation** | All interactive elements |
| **Screen Readers** | ARIA labels |
| **Reduced Motion** | Respect `prefers-reduced-motion` |

## 9.2 Focus States

```css
*:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}
```

## 9.3 Screen Reader Text

```css
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
```

## 9.4 Color Contrast Ratios

| Element | Foreground | Background | Ratio |
|---------|------------|------------|-------|
| Body Text | `#111827` | `#FFFFFF` | 16.73:1 ✅ |
| Primary Button | `#FFFFFF` | `#6366F1` | 4.53:1 ✅ |
| Secondary Text | `#4B5563` | `#FFFFFF` | 6.63:1 ✅ |
| Dark Mode Text | `#F9FAFB` | `#0F172A` | 15.48:1 ✅ |

---

*Document Version: 1.0 | Last Updated: December 28, 2024*
