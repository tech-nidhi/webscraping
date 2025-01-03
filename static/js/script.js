// Fetch weather data and update the UI
fetch('/weather')
    .then(response => response.json())
    .then(data => {
        const weatherList = document.getElementById('weather-list');
        data.forEach(item => {
            const li = document.createElement('li');
            li.textContent = `Hour: ${item.hour}, Temperature: ${item.temperature}°C`;
            weatherList.appendChild(li);
        });
    })
    .catch(error => console.error('Error fetching weather data:', error));

// Fetch titles data and update the UI
fetch('/titles')
    .then(response => response.json())
    .then(data => {
        const titlesList = document.getElementById('titles-list');
        data.forEach(item => {
            const li = document.createElement('li');
            li.textContent = item.title;  // Adjust key as per data structure
            titlesList.appendChild(li);
        });
    })
    .catch(error => console.error('Error fetching titles data:', error));
