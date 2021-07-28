# This file represents the work done to use the text to speech feature using IBM service
# The main code belongs to Nicholas Renotte



# This is the text to speech code, starts by defining API key variable and URL variable taken from IBM service credentials section

apikey='e5LJDKtAfNK8hENIbH9Z__gpHN9hEpNxOtSwY-c8EAYl'
url= 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/f72a3d91-e33f-42d2-a757-d12412786f0a'


# This parts includes the needed imports from ibm_watson module and ibm_cloud_sdk_core module 

from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# Defining the authenticator and setting the service URL : 

authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)


# Using the file created from the speech to text feature named (user_speech) and modifying it (removing \n )

with open('user_speech.txt', 'r') as f:
    text = f.readlines()
text = [line.replace('\n','') for line in text]
text = ''.join(str(line) for line in text)


# Creating an mp3 file to save the speech and determining the voice 

with open('user_speech.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice='en-GB_KateVoice').get_result()
    audio_file.write(res.content)