# HTTP Response Inspector
Back-end sample that inspects an HTTP GET response for a public website.

# Instructions (Windows)
1. Terminal 1: Build the Docker container: `docker build -t py-http-response .`
2. Terminal 1: Run the application (port 5000 by default): `docker run --rm -p 5000:5000 py-http-response`
3. Terminal 2: Request a website in the GET parameter `url`: 
    - Windows Powershell: `Invoke-WebRequest -UseBasicParsing "http://127.0.0.1:5000/inspect?url=https://www.ek.dk"`
    - Mac/Linux/Windows CLI: `curl -i "http://127.0.0.1:5000/inspect?url=https://www.ek.dk"` 
4. Check the output in both terminals

# Tools
Flask / Python

# Author
ChatGPT 5.1/5.2, prompted by Arturo Mora-Rioja