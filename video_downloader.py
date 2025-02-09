from pytubefix import YouTube, Playlist
import os

def download_audio(url, destination='.'):
    try:
        yt = YouTube(url)

        audio = yt.streams.filter(only_audio=True).first()
        if audio is None:
            print(f"No audio stream found for {url}")
            return


        song_path = audio.download(output_path=destination)
        
        base, ext = os.path.splitext(song_path)
        new_file = base + '.mp3'
        
        os.rename(song_path, new_file)
        print(f"{yt.title} has been successfully downloaded as {new_file}")
    except Exception as e:
        print(f"An error occurred while downloading {url}: {e}")

def main():
    choice = input("Do you want to download a single video or a playlist? (v/p): ").strip().lower()
    
    destination = input("Enter download destination folder (press Enter for current directory): ").strip() or '.'
    
    if choice == 'v':
        url = input("Enter the URL of the video you want to download:\n>> ").strip()
        download_audio(url, destination)
    
    
    elif choice == 'p':
        playlist_url = input("Enter the URL of the playlist you want to download:\n>> ").strip()
        try:
            playlist = Playlist(playlist_url)
            print(f"Found {len(playlist.video_urls)} videos in the playlist.")
            
            for url in playlist.video_urls:
                print(f"Downloading: {url}")
                download_audio(url, destination)
        except Exception as e:
            print(f"An error occurred while processing the playlist: {e}")
    
    else:
        print("Invalid choice. Please run the script again and select either 'v' for video or 'p' for playlist.")

if __name__ == '__main__':
    main()
