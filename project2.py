import requests
from bs4 import BeautifulSoup
from pytube import YouTube

def extract_video_urls_from_playlist(playlist_url):
    response = requests.get(playlist_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    video_urls = []

    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if '/watch?v=' in href and 'list=' in href:
            full_url = 'https://www.youtube.com' + href.split('&')[0]
            if full_url not in video_urls:
                video_urls.append(full_url)
    return video_urls

def download_playlist(playlist_url):
    try:
        print("Fetching playlist URLs...")
        video_urls = extract_video_urls_from_playlist(playlist_url)
        print(f"Found {len(video_urls)} videos.")

        for url in video_urls:
            try:
                yt = YouTube(url)
                print(f'Downloading: {yt.title}')
                yt.streams.get_highest_resolution().download()
            except Exception as e:
                print(f"Error downloading {url}: {e}")

        print('All downloads completed.')
    except Exception as e:
        print(f"An error occurred: {e}")

playlist_url = input('Enter the YouTube Playlist URL: ')
download_playlist(playlist_url)
