# YouTube Bulk Downloader (No FFmpeg)

This Python script allows you to bulk download YouTube videos by reading URLs from a text file. It is specifically designed to work **without needing FFmpeg**, making it easy to set up. It downloads videos into a dedicated `videos` folder.

## Features
* Bulk downloads from a comma-separated list in `input.txt`.
* Automatically creates a `videos/` directory for all downloads.
* 🚫 **No FFmpeg Required**: Downloads pre-merged MP4 files directly.
* Simple to use and modify.

***
## Requirements
* Python 3.9 or newer.
* The `yt-dlp` Python library.

***
## How to Use

1.  **Install Dependencies**: Open your terminal or Command Prompt and install the required library:
    ```bash
    pip install yt-dlp
    ```

2.  **Create `input.txt`**: In the same directory as the script (`downloader.py`), create a file named `input.txt`. Add the YouTube URLs you want to download, separated by commas.

    **Example `input.txt`:**
    ```text
    [https://www.youtube.com/watch?v=dQw4w9WgXcQ](https://www.youtube.com/watch?v=dQw4w9WgXcQ), [https://www.youtube.com/watch?v=3JZ_D3ELwOQ](https://www.youtube.com/watch?v=3JZ_D3ELwOQ), [https://www.youtube.com/watch?v=C0DPdy98e4c](https://www.youtube.com/watch?v=C0DPdy98e4c)
    ```

3.  **Run the Script**: Execute the script from your terminal:
    ```bash
    python downloader.py
    ```
    The script will create a `videos` folder and save the downloaded files there.

***
## ⚠️ Important Limitations

This script prioritizes convenience over compatibility. Please read these limitations carefully.

* **No Control Over Resolution**
    This script downloads the "best" available pre-merged MP4 file. You **cannot** specify a resolution like 480p or 1080p. You will get whatever quality YouTube provides as a single file.

* **Downloads May Fail**
    The primary limitation is that this script **will fail** if a specific YouTube video does not have a pre-merged MP4 format available. In such cases, `yt-dlp` will report an "unavailable format" error, and the script will move on to the next URL. The only way to reliably download these videos is by using FFmpeg to merge separate video and audio streams.
