from pytubefix import YouTube, Playlist
import os

def download_audio(url, destination='.'):
    try:
        yt = YouTube(url)
        # Select the first audio-only stream
        audio = yt.streams.filter(only_audio=True).first()
        if audio is None:
            print(f"No audio stream found for {url}")
            return

        # Download the audio file
        song_path = audio.download(output_path=destination)
        
        # Separate the file name and extension
        base, ext = os.path.splitext(song_path)
        new_file = base + '.mp3'
        
        # Rename the file to have an .mp3 extension
        os.rename(song_path, new_file)
        print(f"{yt.title} has been successfully downloaded as {new_file}")
    except Exception as e:
        print(f"An error occurred while downloading {url}: {e}")

def main():
    
    #Ask the user whether to download a single video or a playlist
    choice = input("Do you want to download a single video or a playlist? (v/p): ").strip().lower()
    
    # Ask for the destination folder (default option is the current directory)
    destination = input("Enter download destination folder (press Enter for current directory): ").strip() or '.'
    
    #Singular Video Download option
    if choice == 'v':
        url = input("Enter the URL of the video you want to download:\n>> ").strip()
        download_audio(url, destination)
    
    #Whole Playlist Download option
    elif choice == 'p':
        playlist_url = input("Enter the URL of the playlist you want to download:\n>> ").strip()
        try:
            playlist = Playlist(playlist_url)
            print(f"Found {len(playlist.video_urls)} videos in the playlist.")
            
            # Iterate over all video URLs in the playlist
            for url in playlist.video_urls:
                print(f"Downloading: {url}")
                download_audio(url, destination)
        except Exception as e:
            print(f"An error occurred while processing the playlist: {e}")
    
    else:
        print("Invalid choice. Please run the script again and select either 'v' for video or 'p' for playlist.")

if __name__ == '__main__':
    main()
