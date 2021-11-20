from pytube import YouTube
import os, csv, time

url_file = '../file/urls.csv'

def readUrl(path):
    with open(path, 'r') as f:
        reader = csv.reader(f)
        urls = [url for url in reader]
        del urls[0]
    return urls

def clearFile(path):
    with open(path, 'w') as f:
        writer = csv.writer(f)
        writer.writerows([['url']])

def download(url):
    mov = YouTube(url)
    stream = mov.streams.filter(only_audio=True).first()

    if not os.path.isfile(f'../music/{stream.title}.mp3'):
        stream.download('../music')
        os.rename(f'../music/{stream.title}.mp4', f'../music/{stream.title}.mp3')

def main():
    urls = readUrl(url_file)
    for url in urls:
        download(url[0])
        time.sleep(1)
    clearFile(url_file)

if __name__ == '__main__':
    main()