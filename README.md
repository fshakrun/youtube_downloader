# Загрузчик видео с YouTube

Простая, но быстрая и эффективная программа, позволяющая скачивать с YT видео и переводить его аудиодорожку в текстовой формат за счет преобразования доступных субтитров.

Функционал загрузчика реализован с помощью 2 библиотек: 
1. Pytube — для скачивания видео;
2. youtube_transcript_api — для скачивания и преобразования субтитров.

Достаточно просто ввести ссылку на нужное видео и получить 2 файла: само видео в формате mp4 и максимальным доступным разрешением (до 720 p) и транскрипция в виде файла txt.

Предусмотрен момент с недопустимиыми в Windows для названия файла символами вроде "//", "||" и т.п. — они автоматически удаляются при загрузке.
