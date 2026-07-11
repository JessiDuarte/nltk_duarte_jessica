
import os
os.system("cls") 

from youtube_comment_downloader import YoutubeCommentDownloader, SORT_BY_POPULAR

VIDEO_URL = "https://www.youtube.com/watch?v=0BstRqp6Svg&t=6s"

downloader = YoutubeCommentDownloader()

comentarios = downloader.get_comments_from_url(

   VIDEO_URL,
   sort_by=SORT_BY_POPULAR

)

with open("comentarios_youtube.txt", "w", encoding="utf-8") as archivo:

   for i, comentario in enumerate(comentarios):

       if i >= 100:
           break

       archivo.write(comentario["text"] + "\n")

print("Comentarios descargados correctamente.")
import os
os.system("cls") 

from youtube_comment_downloader import YoutubeCommentDownloader, SORT_BY_POPULAR

VIDEO_URL = "https://www.youtube.com/watch?v=0BstRqp6Svg&t=6s"

downloader = YoutubeCommentDownloader()

comentarios = downloader.get_comments_from_url(

   VIDEO_URL,
   sort_by=SORT_BY_POPULAR

)

with open("comentarios_youtube.txt", "w", encoding="utf-8") as archivo:

   for i, comentario in enumerate(comentarios):

       if i >= 100:
           break

       archivo.write(comentario["text"] + "\n")

print("Comentarios descargados correctamente.")