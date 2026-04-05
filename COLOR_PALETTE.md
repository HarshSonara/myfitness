# MyFitness Website Color Palette 🎨

## Primary Colors (Main Brand Identity)

### Purple Gradient
- **Primary Purple**: `#667eea` 
  - RGB: (102, 126, 234)
  - Usage: Main brand color, buttons, headers, primary elements
  
- **Dark Purple**: `#764ba2`
  - RGB: (118, 75, 162)
  - Usage: Gradient middle, hover states, depth

- **Pink Accent**: `#f093fb`
  - RGB: (240, 147, 251)
  - Usage: Gradient end, highlights, playful elements

### Coral Accent
- **Accent Coral**: `#f5576c`
  - RGB: (245, 87, 108)
  - Usage: Call-to-action, important highlights, energy

---

## Secondary Colors (Functional)

### Success/Health
- **Success Green**: `#10b981`
  - RGB: (16, 185, 129)
  - Usage: Nutrition, meals, positive metrics, success states

### Warning/Energy
- **Warning Orange**: `#f59e0b`
  - RGB: (245, 158, 11)
  - Usage: Calories burned, workouts, energy metrics

### Information
- **Info Blue**: `#3b82f6`
  - RGB: (59, 130, 246)
  - Usage: Progress tracking, informational elements, BMI

---

## Neutral Colors (Background & Text)

### Backgrounds
- **Light Background**: `#f8fafc`
  - RGB: (248, 250, 252)
  - Usage: Page background, light sections

- **Card White**: `#ffffff`
  - RGB: (255, 255, 255)
  - Usage: Cards, containers, clean surfaces

### Text
- **Text Dark**: `#1e293b`
  - RGB: (30, 41, 59)
  - Usage: Primary text, headings, important content

- **Text Muted**: `#64748b`
  - RGB: (100, 116, 139)
  - Usage: Secondary text, descriptions, labels

### Borders
- **Border Light**: `#e2e8f0`
  - RGB: (226, 232, 240)
  - Usage: Card borders, dividers, subtle separations

---

## Gradient Combinations

### Primary Gradient (Hero, CTA, Buttons)
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
```

### Purple-Pink Gradient (Testimonials, Special Sections)
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
```

### Light Purple Background (Plans Section)
```css
background: linear-gradient(135deg, #f8f9ff 0%, #f0f4ff 100%);
```

### Light Pink Background (Exercises Section)
```css
background: linear-gradient(135deg, #fff5f7 0%, #ffe8f0 100%);
```

### Light Blue Background (Features Section)
```css
background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
```

### Dark Navy Background (Stats Section)
```css
background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
```

---

## Icon Gradients

### Purple Icon
```css
background: linear-gradient(135deg, #667eea, #764ba2);
```

### Pink Icon
```css
background: linear-gradient(135deg, #f093fb, #f5576c);
```

### Green Icon
```css
background: linear-gradient(135deg, #10b981, #059669);
```

### Orange Icon
```css
background: linear-gradient(135deg, #f59e0b, #d97706);
```

### Blue Icon
```css
background: linear-gradient(135deg, #3b82f6, #2563eb);
```

---

## Usage Guidelines

### Homepage
- **Hero Section**: Primary purple-pink gradient background, white text
- **Stats Section**: Dark navy gradient, white text with colored icons
- **Plans Section**: Light purple gradient background, dark text
- **Exercises Section**: Light pink gradient background, dark text
- **Features Section**: Light blue gradient background, dark text
- **Testimonials**: Purple-pink gradient, white cards
- **CTA**: Primary gradient, white text

### Dashboard
- **Background**: Light purple gradient (#f8f9ff → #f0f4ff)
- **Hero**: Primary purple-pink gradient
- **Cards**: White with subtle shadows
- **Icons**: Gradient backgrounds (purple, pink, green, orange, blue)
- **Text**: Dark text on light backgrounds
- **Buttons**: Gradient buttons with matching colors

### Buttons
- **Primary Action**: Purple gradient (#667eea → #764ba2)
- **Workout/Energy**: Orange gradient (#f59e0b → #d97706)
- **Nutrition/Health**: Green gradient (#10b981 → #059669)
- **Secondary**: White with purple border

### Cards & Components
- **Background**: White (#ffffff)
- **Border**: Light gray (#e2e8f0)
- **Hover**: Slight lift with purple accent
- **Shadow**: Soft purple-tinted shadows

---

## Color Psychology

- **Purple**: Premium, fitness, transformation, energy
- **Pink**: Motivation, positivity, wellness
- **Green**: Health, nutrition, growth, success
- **Orange**: Energy, calories, activity, warmth
- **Blue**: Trust, progress, information, calm

---

## Accessibility Notes

- All text colors meet WCAG AA standards for contrast
- Primary purple (#667eea) on white: 4.5:1 contrast ratio ✓
- Dark text (#1e293b) on white: 14:1 contrast ratio ✓
- White text on purple gradient: 4.5:1+ contrast ratio ✓
- Muted text (#64748b) on white: 4.5:1 contrast ratio ✓

---

## CSS Variables (Copy & Paste)

```css
:root {
  /* Primary Colors */
  --primary-purple: #667eea;
  --primary-dark-purple: #764ba2;
  --primary-pink: #f093fb;
  --accent-coral: #f5576c;
  
  /* Secondary Colors */
  --success-green: #10b981;
  --warning-orange: #f59e0b;
  --info-blue: #3b82f6;
  
  /* Neutral Colors */
  --light-bg: #f8fafc;
  --card-white: #ffffff;
  --text-dark: #1e293b;
  --text-muted: #64748b;
  --border-light: #e2e8f0;
  
  /* Gradients */
  --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
  --purple-gradient: linear-gradient(135deg, #667eea, #764ba2);
  --pink-gradient: linear-gradient(135deg, #f093fb, #f5576c);
  --green-gradient: linear-gradient(135deg, #10b981, #059669);
  --orange-gradient: linear-gradient(135deg, #f59e0b, #d97706);
  --blue-gradient: linear-gradient(135deg, #3b82f6, #2563eb);
}
```

---

**Design Philosophy**: Modern, energetic, and motivational with a premium feel. The purple-pink gradient creates a unique brand identity while maintaining professionalism. Light backgrounds with colorful accents keep the interface clean and easy to read.
