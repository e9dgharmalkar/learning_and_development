
#  Bootstrap Basics — Learning Notes

This document summarizes the basic concepts I’ve learned while starting with **Bootstrap 5**, a front-end framework used to build responsive and mobile-first websites quickly.

---

##  What is Bootstrap?

Bootstrap is a popular open-source CSS framework that provides pre-defined styles, components, and utility classes for building modern and responsive UIs without writing a lot of custom CSS.

---

##  How to Add Bootstrap to a Project

### 1. **Using CDN (Quick Start)**

```html
<!-- Add in your base HTML template (e.g., base.html in Django) -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
```

---

##  Layout: Grid System

Bootstrap uses a **12-column responsive grid** to layout content.

### Example:

```html
<div class="container">
  <div class="row">
    <div class="col-4">Column 1</div>
    <div class="col-4">Column 2</div>
    <div class="col-4">Column 3</div>
  </div>
</div>
```

- `container` creates a fixed-width layout
- `row` creates a horizontal group of columns
- `col-4` means 4 out of 12 columns wide

---

## Utility Classes

Bootstrap provides helper classes for margin, padding, colors, and alignment.

- Margin: `m-2`, `mt-3`, `mb-1`
- Padding: `p-2`, `px-3`, `py-1`
- Text: `text-center`, `text-muted`, `text-danger`
- Background: `bg-primary`, `bg-light`, `bg-success`
- Display: `d-flex`, `d-none`, `d-block`

---

##  Components

Bootstrap includes ready-to-use UI components. A few I learned:

###  Buttons

```html
<button class="btn btn-primary">Primary</button>
<button class="btn btn-outline-success">Success</button>
```

###  Navbar

```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">MySite</a>
</nav>
```

###  Cards

```html
<div class="card" style="width: 18rem;">
  <div class="card-body">
    <h5 class="card-title">Task Title</h5>
    <p class="card-text">Task description goes here.</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>
```

###  Alerts

```html
<div class="alert alert-warning" role="alert">
  This is a warning alert!
</div>
```

---

##  Forms

Bootstrap makes forms clean and user-friendly.

```html
<form>
  <div class="mb-3">
    <label for="taskName" class="form-label">Task Name</label>
    <input type="text" class="form-control" id="taskName">
  </div>
  <button type="submit" class="btn btn-success">Submit</button>
</form>
```

---

##  Responsive Design

Bootstrap includes breakpoints to make layouts adapt to different screen sizes:

- `col-sm-6` — for small devices
- `col-md-4` — for medium devices
- `col-lg-3` — for large devices

You can also use display utilities like:
```html
<div class="d-none d-md-block">Hidden on small, visible on medium+</div>
```

---

## Next Steps

- Learn how to customize Bootstrap (via Sass or custom themes)
- Explore JavaScript plugins (modals, dropdowns, tooltips)

---
