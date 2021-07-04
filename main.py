import pytube
from pytube import YouTube

link = input("Digite o link do video:")
yt = YouTube(link)

print("Titulo: ",yt.title)
print("Visualizações: ",yt.views)
print("Comprimento do video: ",yt.length,"seconds")
print("Descrição: ",yt.description)
print("Ratings: ",yt.rating)

video = yt.streams.first()

download = input("Deseja fazer download do video? (sim/nao)")

if download == "sim":
    video.download()
elif download == "não":
    yt = null
    video = null
else:
    print("Resposta invalida, tente novamente")

