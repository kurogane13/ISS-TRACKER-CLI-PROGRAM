# ISS-Tracker-Program
This program is an api-client that trackes the ISS (International space spation).

It trackes the ISS from a public API, and displays its actual coordinates in the console.
You can pre-select the iterations(How many times to show snapshots and coordinates), and refresh intervals(Amount of seconds to show coordinates). 
It will open Google Maps with firerox(using selenium, and show the ISS coordinates as they change, 
taking snapshots of every location to store them in a folder by date. It also has a log file, 
where it appends the raw data in txt format.
