"""PyAudio example: Record a few seconds of audio and save to a WAVE file."""

import pyaudio
import httplib
import urllib
import audioop
import wave
import json
from base64 import b64decode

import ledm

def outputWave(name, lpcm, rate):
    wf = wave.open(name, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(pyaudio.PyAudio().get_sample_size(pyaudio.paInt16))
    wf.setframerate(rate)
    wf.writeframes(lpcm)
    wf.close()

def take_action(data_json):
    if data_json.has_key("light"):
        color = data_json["light"]
        ledm.set_color(color[0], color[1], color[2])
    print "finish taking action"

def getResponse(lpcm, index):
    httpServ = httplib.HTTPConnection("40.117.226.250", 8000)
    httpServ.connect()

    params = urllib.urlencode({'@index': "%d"%index, '@lpcm': "%s"%lpcm})
    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Accept": "text/plain"}

    httpServ.request('POST', "/dm.py", params, headers)
    print "Sending request"
    response = httpServ.getresponse()

    if response.status == httplib.OK:
        s = response.read()
        print(s)
        data = json.loads(s)
        print(data)
        take_action(data)
        #backlpcm = b64decode(data['@lpcm'])
    else:
        print(response.status)


def listen():
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 48000
    CHUNK = RATE/10
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    # Threshold params to trigger voice
    expand = 2
    threshold = 250

    frames = []
    left = expand
    index = 1
    print("* recording")
    while (1>0):
        data = '\x00'*CHUNK
        try:
            data = stream.read(CHUNK)
            data = audioop.ratecv(data, 2, 1, 48000, 16000, None)[0]
        except IOError as ex:
            if ex[1] != pyaudio.paInputOverflowed:
                raise
        print(audioop.rms(data, 2))
        frames.append(data)
        if (audioop.rms(data, 2) > threshold):
            left = 3
        else:
            left -= 1
            '''at least have 2 frame excced threshold'''
            if (left <= 0 and len(frames) > 2*expand+2):
                index += 1
                print("get sentence", index)
                # outputWave("history_audios/"+str(index)+".wav", b''.join(frames), 16000)
                getResponse(b''.join(frames), index)
                frames = []
                left = expand
            elif left < 0:
                frames = frames[0:expand]


if __name__ == "__main__":
    ledm.init()
    listen()

    frames = getRecord(6)
    open("test_lpcm", "wb").write(b''.join(frames))
    for frame in frames:
        print(audioop.rms(frame,2))
    #getResponse(frames)

