# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    jarvis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ghorvath <ghorvath@student.hive.fi>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/01/14 10:51:13 by ghorvath          #+#    #+#              #
#    Updated: 2022/01/14 10:54:52 by ghorvath         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import googlesearch

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
	engine.say(text)
	engine.runAndWait()

def take_command():
	try:
		with sr.Microphone() as source:
			print('listening...')
			voice = listener.listen(source)
			command = listener.recognize_google(voice)
			command = command.lower()
			if 'jarvis' in command:
				command = command.replace('jarvis', '')
				print(command)
	except:
		pass
	return command

def wishme():
		hour = int(datetime.datetime.now().hour)
		if hour >= 0 and hour < 12:
			talk('Good Morning Sir!')
		elif hour >= 12 and hour < 18:
			talk('Good Afternoon Sir!')
		else:
			talk('Good evening Sir!')


def run_jarvis():
	command = take_command()
	print(command)
	if 'play' in command:
		song = command.replace('play', '')
		talk('playing' + song)
		pywhatkit.playonyt(song)
	elif 'time' in command:
		time = datetime.datetime.now().strftime('%H:%M %p')
		print(time)
		talk('The current time is' + time)
	elif 'wikipedia' in command:
		person = command.replace('wikipedia', '')
		info = wikipedia.summary(person, 1)
		print(info)
		talk(info)
	elif 'how are you' in command:
		talk('I am pretty fine, living my daily computer life as your personal AI assistant, how about you?')
	elif 'Thank you':
		talk('No problem Sir')
	elif 'joke' in command:
		joking = pyjokes.get_joke()
		talk(joking)
		print(joking)
	elif 'search' in command:
		title = command.replace('search', '')
		talk('searching' + title)
		pywhatkit.search(title)
	elif 'open youtube' in command:
		webbrowser.open('youtube.com')
	else:
		talk('I am not enough intelligent yet to understand that')

#work in progress...

wishme()
talk('How may I help you')
while True:
	run_jarvis()