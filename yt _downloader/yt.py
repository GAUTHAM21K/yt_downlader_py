import yt_dlp
import os

def download_video(url, output_template):

    print(f"\nAttempting to download best available pre-merged MP4: {url}")


    ydl_opts = {
        'format': 'best[ext=mp4]',

        # 2. Ensure no postprocessors are trying to use FFmpeg.
        'postprocessors': [],

        # Set the output path and filename
        'outtmpl': output_template,
    }

    try:
        # Create a YoutubeDL object and download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"✅ Download complete for: {url}")

    except Exception as e:
        print(f"❌ An error occurred while downloading {url}: {e}")

# --- Main part of the program ---
if __name__ == "__main__":
    input_file = 'input.txt'
    output_folder = 'videos'

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created directory: '{output_folder}'")

    if not os.path.exists(input_file):
        print(f"Error: '{input_file}' not found.")
    else:
        with open(input_file, 'r') as f:
            content = f.read()

        urls = [url.strip() for url in content.split(',') if url.strip()]

        if not urls:
            print(f"No valid URLs found in '{input_file}'.")
        else:
            print(f"Found {len(urls)} URLs. Starting downloads...")
            for video_url in urls:
                output_path = os.path.join(output_folder, '%(title)s.%(ext)s')
                download_video(video_url, output_path)

            print("\nAll downloads attempted.")