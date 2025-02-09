# YouTube Audio Downloader 🎵

A simple Python project that allows you to download the audio from either a single YouTube video or an entire playlist. This project is perfect for users who want a quick and easy way to save their favorite tracks or podcasts from YouTube.

---

## Features 🚀

- **Single Video Download:** Input a YouTube video URL and download its audio.
- **Playlist Download:** Download audio from every video in a YouTube playlist in one go.
- **User-Friendly Interface:** A simple, command-line interface that guides you through every step.
- **Customizable Download Destination:** Choose your preferred location to save downloaded files.
- **Custom Chrome Extension** A more user friendly method for downloading songs.

---

## Installation 🔧

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/YourUsername/YourRepo.git
   cd YourRepo
    ```
2. **Install Dependencies:**

  This project uses a requirements.txt file to manage its dependencies. Make sure you have Python 3 installed on your system, then run:
  ```bash
  pip install -r requirements.txt
  ```
---
## Usage 💡
To run the downloader, simply execute the Python script:
```bash
python video_downloader.py
```
You will be prompted to choose whether you want to download a single video or an entire playlist. Follow the on-screen instructions to enter the URL and specify your download destination.

---

## Running the Extension and Server 🌐

### 1. Run the Python Server

**Start the Server:**
   - Open a terminal and navigate to your project directory.
   - Run the Flask server with:
     ```bash
     python server.py
     ```
   - The server should now be running at `http://localhost:5000`.

### 2. Load the Chrome Extension

1. **Open Chrome Extensions Page:**
   - Open Google Chrome and go to:  
     ```
     chrome://extensions/
     ```

2. **Enable Developer Mode:**
   - Toggle the **Developer mode** switch in the top-right corner of the page.

3. **Load Unpacked Extension:**
   - Click the **Load unpacked** button.
   - In the file dialog, select the folder that contains your extension files (`manifest.json`, `popup.html`, `popup.js`).

4. **Verify the Extension:**
   - The extension should now appear in your list of installed extensions. Its icon will appear in the Chrome toolbar.

### 3. Using the Extension

1. **Navigate to a YouTube Video:**
   - Open a new tab and navigate to any YouTube video page.

2. **Activate the Extension:**
   - Click on the extension’s icon in the Chrome toolbar.

3. **Download Audio:**
   - Click the **Download Audio** button.
   - The extension will send the active tab's URL to your Python server.
   - Check the status message in the popup and your terminal for download progress and any potential errors.
