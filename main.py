from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

# полный адрес видео
video_url = YouTube(input("Введите ссылку на видео: "))

# получение id видео
video_id = (video_url.video_id)

# загрузка видео и получение названия загруженного в папку файла
def video_download():
    get_video = video_url.streams.filter(progressive=True, file_extension='mp4') \
    .desc() \
    .first() \
    .download()
    #получение названия видео без запрещенных символов
    right_title = get_video.split("\\")[-1]
    # получение и сохранение субтитров
    base_lang = 'ru'
    subs = YouTubeTranscriptApi.list_transcripts(video_id)
    base_obj = subs.find_transcript([base_lang])
    base_trans = base_obj.fetch()
    formatted_txt = TextFormatter()
    base_txt = formatted_txt.format_transcript(base_trans)

    with open(f'{right_title}.txt'.format(base_lang), 'w', encoding="utf-8") as f:
        f.write(base_txt)

video_download()

