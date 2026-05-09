# 🚀 João's Programming Projects

Welcome to my programming portfolio! This repository contains multiple exciting projects that showcase my skills in web development, Python programming, and interactive applications.

## 📁 Projects Overview

### 🌤️ [Flask Weather App](./weather_app/)
A modern, responsive web application that provides real-time weather information for any city worldwide.

**Features:**
- 🌡️ Real-time temperature, humidity, wind speed, and pressure
- 🌍 Global city coverage using Open-Meteo API
- 📱 Responsive design (works on desktop, tablet, and mobile)
- 🎨 Beautiful gradient UI with smooth animations
- ⚡ No API keys required - uses free weather data

**Tech Stack:** Python, Flask, HTML, CSS, JavaScript

**Live Demo:** Run `python app.py` in the weather_app directory and visit `http://localhost:5000`

---

### 👕 [Clothes Decider App](./clothes_decider/)
A friendly Flask web app that helps you randomly choose what clothes to take by entering options line by line.

**Features:**
- 🎲 Randomly selects one clothing item from your list
- 📝 Keeps your entered options visible after submission
- ⚠️ Handles empty input with a clear message
- 🎨 Simple, responsive UI with clean styling

**Tech Stack:** Python, Flask, HTML, CSS

**Usage:**
```bash
cd clothes_decider
python app.py
```

Then open `http://localhost:5000` in your browser.

---

### 🎡 [Spin Wheel App](./spin_wheel.html)
An interactive web app where you can create a custom spinning wheel with any names you want and spin to find a winner!

**Features:**
- 🎯 Add custom names to the wheel
- 🎨 Automatic colorful segments for each entry
- 🎪 Smooth spinning animation with deceleration
- 🎉 Confetti celebration and trumpet sound when a winner is chosen
- ➡️ Visual arrow pointer pointing to the winner
- 📱 Fully responsive design
- ✨ No dependencies - pure HTML, CSS, and JavaScript

**Tech Stack:** HTML, CSS, JavaScript (Canvas API, Web Audio API)

**How to Use:** Simply open `spin_wheel.html` in your web browser and start adding names!

---

### 🔢 [Simple Calculator](./Calculator.py)
A command-line calculator application with basic arithmetic operations.

**Features:**
- ➕ Addition, subtraction, multiplication, division
- 🔄 Continuous calculations in a loop
- 🛡️ Error handling for invalid inputs
- 📝 Clean, user-friendly interface

**Tech Stack:** Python

**Usage:**
```bash
python Calculator.py
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.13+ installed
- Git for version control
- Modern web browser (for web apps)

### Weather App Setup
```bash
cd weather_app
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
python app.py
```

Then open `http://localhost:5000` in your browser!

### Clothes Decider Setup
```bash
cd clothes_decider
python app.py
```

Then open `http://localhost:5000` in your browser!

### Spin Wheel App Setup
Simply open `spin_wheel.html` in your web browser - no installation needed!

### Calculator Setup
```bash
python Calculator.py
```

## 📊 Project Structure

```
Ficheiros de Programação/
├── Calculator.py              # Command-line calculator
├── spin_wheel.html            # Interactive spin wheel app
├── clothes_decider/           # Flask clothes decider application
│   ├── app.py                # Main Flask application
│   ├── requirements.txt      # Python dependencies
│   ├── static/
│   │   └── style.css        # CSS styling
│   └── templates/
│       └── index.html       # HTML template
├── weather_app/               # Flask weather application
│   ├── app.py                # Main Flask application
│   ├── requirements.txt      # Python dependencies
│   ├── README.md            # Weather app documentation
│   ├── templates/
│   │   └── index.html       # HTML template
│   └── static/
│       └── style.css        # CSS styling
└── README.md                # This file
```

## 🎯 Learning Outcomes

Through these projects, I've demonstrated:

- **Web Development:** Building RESTful APIs with Flask and creating interactive web applications
- **Frontend Design:** Creating responsive, modern user interfaces with smooth animations
- **Canvas API:** Drawing and animating graphics with HTML5 Canvas
- **Web Audio API:** Generating sound effects programmatically
- **API Integration:** Working with external weather APIs
- **Version Control:** Using Git and GitHub for project management
- **Python Programming:** Clean code, functions, and user input handling
- **JavaScript ES6+:** Modern JavaScript features for interactive applications
- **Problem Solving:** Implementing mathematical operations, animations, and user interactions

## 🚀 Future Enhancements

### Weather App
- [ ] 7-day weather forecast
- [ ] Weather alerts and notifications
- [ ] Location-based weather detection
- [ ] Multiple language support
- [ ] Weather history and trends

### Spin Wheel App
- [ ] Save wheel configurations
- [ ] Sound effect options
- [ ] Custom wheel colors
- [ ] Share wheel via URL

### Calculator
- [ ] Scientific calculator functions (sin, cos, tan, etc.)
- [ ] GUI interface using Tkinter
- [ ] Memory functions
- [ ] Unit conversions
- [ ] Calculation history

## 📞 Contact

**João**
- 📧 Email: joaopedroafonso23@gmail.com
- 💼 GitHub: [joaopedroafonso23-cmd](https://github.com/joaopedroafonso23-cmd)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

⭐ **Feel free to star this repository if you find it helpful!**

*Built with ❤️ using Python and modern web technologies*
