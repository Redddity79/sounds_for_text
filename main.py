import json
import urllib.request
from io import BytesIO
from pydub import AudioSegment
import PySimpleGUI as sg
from pydub.playback import _play_with_simpleaudio

class Main:
	def __init__(self):
		sg.theme('Light Brown 7')
		self.Sounds = Sounds().sounds
		self.layout = [[sg.Text('Напиши сюда текст для его трансформации:'), sg.Text(size=(14,1), key='-OUTPUT-')],
						[sg.Input(key='-IN-')],
						[sg.Button('Мелодия'), sg.Button('Пауза'),  sg.Button('Выход')]]
		self.window = sg.Window('Мелодия Слов', self.layout)
		self.song = _play_with_simpleaudio

	def get_word(self, word):
		letters = []
		if word == '': return []
		for i in word:
			letters.append(f'{ord(i)}')
		return letters

	def main(self):
		while True:
			state, values = self.window.read()
			if (state == 'Выход' or state == sg.WIN_CLOSED):
				break
			if (state == 'Пауза' and self.song != None):
				self.song.stop()
				self.song = _play_with_simpleaudio
			if (state == 'Пауза' and self.song == None):
				continue
			if (state == 'Мелодия'):
				letters = self.get_word(values['-IN-'])
				if letters == []:
					sg.Popup('Не забудь ввести что-нибудь!')
					continue
				melodie = AudioSegment.from_wav
				url = urllib.request.urlopen
				bytes = BytesIO
				melodies = []
				if len(letters)%2==0:
					pares = [(bytes(url(self.Sounds[letters[i]]).read()), bytes(url(self.Sounds[letters[i+1]]).read())) for i in range(0,len(letters), 2)]
					for i in pares:
						melodies.append(melodie(i[0]).overlay(melodie(i[-1])))
				else:
					if len(letters) == 1:
						self.song = melodie(bytes(url(self.Sounds[letters[0]]).read()))
						self.song = _play_with_simpleaudio(self.song)
						continue
					pares = [(bytes(url(self.Sounds[letters[:-1][i]]).read()), bytes(url(self.Sounds[letters[:-1][i+1]]).read())) for i in range(0,len(letters[:-1]), 2)]
					pares.append(bytes(url(self.Sounds[letters[-1]]).read()))
					for i in pares[:-1]:
						melodies.append(melodie(i[0]).overlay(melodie(i[-1])))
					melodies.append(melodie(pares[-1]))
				self.song = sum(melodies)
				self.song = _play_with_simpleaudio(self.song)
				self.window['-OUTPUT-'].update(values['-IN-'])
		self.window.close()

class Sounds:
	def __init__(self):
		self.sounds = {'1072': "https://raw.githubusercontent.com/Redddity79/sounds_for_text/main/sound1.wav", 
		'1073': "https://raw.githubusercontent.com/Redddity79/sounds_for_text/main/sound2.wav", 
		'1074': "https://raw.githubusercontent.com/Redddity79/sounds_for_text/main/sound3.wav", 
		'1075': "https://raw.githubusercontent.com/Redddity79/sounds_for_text/main/sound4.wav", 
		'1076': "https://raw.githubusercontent.com/Redddity79/sounds_for_text/main/sound5.wav", 
		'1077': "https://raw.githubusercontent.com/Redddity79/sounds_for_text/main/sound6.wav", 
		'1105': "https://raw.githubusercontent.com/Redddity79/sounds_for_text/main/sound7.wav", 
		'1078': "https://raw.githubusercontent.com/Redddity79/sounds_for_text/main/sound8.wav", 
		'1079': "https://raw.githubusercontent.com/Redddity79/sounds_for_text/main/sound9.wav", 
		'1080': "https://raw.githubusercontent.com/Redddity79/sounds_for_text/main/sound10.wav", 
		'1081': "https://raw.githubusercontent.com/Redddity79/sounds_for_text/main/sound11.wav", 
		'1082': "https://raw.githubusercontent.com/Redddity79/sounds_for_text/main/sound12.wav", 
		'1083': "https://raw.githubusercontent.com/Redddity79/sounds_for_text/main/sound13.wav", 
		'1084': "https://raw.githubusercontent.com/Redddity79/sounds_for_text/main/sound14.wav", 
		'1085': "https://raw.githubusercontent.com/Redddity79/sounds_for_text/main/sound15.wav", 
		'1086': "https://raw.githubusercontent.com/Redddity79/sounds_for_text/main/sound16.wav", 
		'1087': "https://raw.githubusercontent.com/Redddity79/sounds_for_text/main/sound17.wav", 
		'1088': "https://raw.githubusercontent.com/Redddity79/sounds_for_text/main/sound18.wav", 
		'1089': "https://raw.githubusercontent.com/Redddity79/sounds_for_text/main/sound19.wav", 
		'1090': "https://raw.githubusercontent.com/Redddity79/sounds_for_text/main/sound20.wav", 
		'1091': "https://raw.githubusercontent.com/Redddity79/sounds_for_text/main/sound21.wav", 
		'1092': "https://raw.githubusercontent.com/Redddity79/sounds_for_text/main/sound22.wav", 
		'1093': "https://raw.githubusercontent.com/Redddity79/sounds_for_text/main/sound23.wav", 
		'1094': "https://raw.githubusercontent.com/Redddity79/sounds_for_text/main/sound24.wav", 
		'1095': "https://raw.githubusercontent.com/Redddity79/sounds_for_text/main/sound25.wav", 
		'1096': "https://raw.githubusercontent.com/Redddity79/sounds_for_text/main/sound26.wav", 
		'1097': "https://raw.githubusercontent.com/Redddity79/sounds_for_text/main/sound27.wav", 
		'1098': "https://raw.githubusercontent.com/Redddity79/sounds_for_text/main/sound28.wav", 
		'1099': "https://raw.githubusercontent.com/Redddity79/sounds_for_text/main/sound29.wav", 
		'1100': "https://raw.githubusercontent.com/Redddity79/sounds_for_text/main/sound30.wav", 
		'1101': "https://raw.githubusercontent.com/Redddity79/sounds_for_text/main/sound31.wav", 
		'1102': "https://raw.githubusercontent.com/Redddity79/sounds_for_text/main/sound32.wav", 
		'1103': "https://raw.githubusercontent.com/Redddity79/sounds_for_text/main/sound33.wav"}


a = Main()
a.main()


#sg.theme('Light Brown 7')
#
#layout = [[sg.Text('Your typed chars appear here:'), sg.Text(size=(12,1), key='-OUTPUT-')],
#          [sg.Input(key='-IN-')],
#          [sg.Button('Show'), sg.Button('Stop'), sg.Button('Exit')]]
#
#window = sg.Window('Window Title', layout)
#while True:  # Event Loop
#    event, values = window.read(timeout=500)
#    if event == sg.WIN_CLOSED or event in (None,'Exit'):
#        break
#    if event == 'Stop':
#        p.stop()
#    if event == 'Show':
#        self.song = AudioSegment.from_wav('sound2.wav')
#        p = _play_with_simpleaudio(self.song)
#        window['-OUTPUT-'].update(values['-IN-'])
#        #sg.Popup('Not a number')
#
#window.close()











# curl -s -O https://d10e1ba081bf42a78e0f712a5c356e3f716d8bef@raw.githubusercontent.com/Redddity79/paper-cranes-bot/main/cranes.txt

# d10e1ba081bf42a78e0f712a5c356e3f716d8bef




#a = urllib.request.urlopen(Sounds(str(ord('а'))).result).read()
#s = BytesIO(a)
#bang = AudioSegment.from_raw(s, sample_width = 2, frame_rate = 44100, channels = 2)