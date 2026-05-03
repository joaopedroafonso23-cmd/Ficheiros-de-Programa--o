# Flask Weather App

A modern, responsive weather application built with Flask that displays real-time weather information.

## Features

✨ **Real-time Weather Data**: Get current temperature, humidity, wind speed, and pressure  
🌍 **Global Coverage**: Search weather for any city worldwide  
📱 **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices  
🎨 **Beautiful UI**: Modern gradient design with smooth animations  
⚡ **Fast Performance**: Uses Open-Meteo API (no API key required)  
🔍 **Easy Search**: Simply enter a city name to get weather information  

## Weather Information Displayed

- 🌡️ **Temperature** (in Celsius)
- 💧 **Humidity** (percentage)
- 💨 **Wind Speed** (km/h)
- 🔽 **Pressure** (hPa)
- 📝 **Weather Description** (Clear, Rainy, Cloudy, etc.)
- 🕐 **Last Updated Time**

## Installation

### 1. Clone or Navigate to the Project
```bash
cd weather_app
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment
**On Windows:**
```bash
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

## Running the Application

1. Make sure your virtual environment is activated
2. Run the application:
```bash
python app.py
```

3. Open your web browser and go to:
```
http://localhost:5000
```

4. Enter a city name and click Search to get weather information

## API Used

This app uses the **Open-Meteo API**, which is:
- ✅ Free to use
- ✅ No API key required
- ✅ No rate limiting
- ✅ Accurate weather data
- 📍 Visit: https://open-meteo.com/

## Project Structure

```
weather_app/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # HTML template
└── static/
    └── style.css         # Styling
```

## How It Works

1. **Frontend**: User enters a city name in the search box
2. **API Call**: Frontend sends POST request to `/api/weather` endpoint
3. **Geocoding**: Backend converts city name to coordinates using Open-Meteo Geocoding API
4. **Weather Data**: Backend fetches weather data using those coordinates
5. **Response**: Weather information is sent back and displayed beautifully

## Features Explained

### Temperature Display
Shows the current temperature in Celsius with large, easy-to-read format.

### Weather Description
Provides detailed description of current weather conditions (e.g., "Light rain", "Clear sky", "Thunderstorm").

### Detailed Metrics
- **Humidity**: Percentage of moisture in the air
- **Wind Speed**: Current wind speed in km/h
- **Pressure**: Atmospheric pressure in hectoPascals

### Responsive Design
The app automatically adapts to different screen sizes:
- Desktop: Multi-column layout
- Tablet: Flexible grid
- Mobile: Single-column layout

## Customization

### Change Default City
Edit line in `index.html`:
```javascript
value="London"  // Change to your preferred city
```

### Modify Colors
Edit `static/style.css`:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Add More Weather Details
Edit `app.py` to include additional parameters in the API request.

## Troubleshooting

**Port Already in Use**
If port 5000 is already in use, modify in `app.py`:
```python
app.run(debug=True, port=5001)  # Change to another port
```

**City Not Found**
Make sure the city name is spelled correctly. Try entering just the main city name (e.g., "London" instead of "Greater London").

**No Internet Connection**
The app requires internet to fetch weather data. Check your connection and try again.

## Future Enhancements

- 📅 7-day forecast
- 🌙 Sunrise/Sunset times
- 🗺️ Location detection (geolocation)
- 📊 Temperature history
- 🔔 Weather alerts
- 🌍 Multiple language support

## License

Free to use and modify!

## Support

For issues or questions, refer to:
- Flask Documentation: https://flask.palletsprojects.com/
- Open-Meteo API: https://open-meteo.com/

Enjoy your Weather App! 🌤️
