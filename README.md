# Flask Screen Recorder

An advanced screen recording app for hackers and programmers, built with Flask.

## Features

- Screen recording with start/stop controls
- Downloadable recordings in MP4 format
- Dark theme hacker aesthetic

## Usage

```bash 
git clone https://github.com/SleepTheGod/flask_screen_recorder
cd flask_screen_recorder
pip install -r requirements.txt
python main.py
```
1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the app:

    ```bash
    python main.py
    ```

3. Visit `http://127.0.0.1:5000/` to start using the app.

## Docker

Build and run using Docker:

```bash
docker build -t flask_screen_recorder .
docker run -p 5000:5000 flask_screen_recorder
