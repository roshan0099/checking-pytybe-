from pytube import YouTube
import time

def complete():
	success = "- - - S U C C E S S - - -"
	print("\n")
	for x in success :
		print(x, end = "", flush = True)
		time.sleep(0.1)

def home():
	
	url = input("Enter the url : ")
	yt = YouTube(url)
	print(yt.title, end = "\n")

	names = yt.streams.filter(type = "audio")

	for x in names :
		print(x)

	tag = input("\nwhich one you wanna download ? mention the tag : ")
	print(yt.streams.get_by_itag(tag))
	confirm = input("\n -- sure ? [y/n] : ")

	if confirm == 'y' :

		print("\nWait a min !!!!!.......")
		video = yt.streams.get_by_itag(tag)
		# print(round(video.filesize/1024000,2), "MB")


		video.download()
		complete()

if __name__ == '__main__':
	home()
            

