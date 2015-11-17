"""PyAudio example: Record a few seconds of audio and save to a WAVE file."""

import pyaudio
import httplib
import urllib
import audioop

def getRecord(seconds):
    CHUNK = 1600
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []
    for i in range(0, int(RATE / CHUNK * seconds)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    return frames

def getResponse(lpcm, index):
    httpServ = httplib.HTTPConnection("192.168.1.2", 8000)
    httpServ.connect()

    params = urllib.urlencode({'@index': "%d"%index, '@lpcm': "%s"%lpcm})
    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Accept": "text/plain"}

    httpServ.request('POST', "/test_cgi.py", params, headers)
    response = httpServ.getresponse()

    response.
    if response.status == httplib.OK:
        print(response.read())
    else:
        print(response.status)


def listen():
    CHUNK = 1600
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    # Threshold params to trigger voice
    expand = 2
    threshold = 700

    frames = []
    left = expand
    index = 1
    print("* recording")
    while (1>0):
        data = stream.read(CHUNK)
        if (audioop.rms(data, 2) > threshold):
            frames.append(data)
            left = expand
        else:
            left -= 1
            if (left <= 0 and len(frames) > 2*expand):
                index += 1
                print("get sentence", index)
                open("test.lpcm", "wb").write(b''.join(frames))
                getResponse(b''.join(frames), index)
                frames = []
            elif left < 0:
                frames = frames[0:expand]


if __name__ == "__main__":

    listen()

    frames = getRecord(6)
    open("test_lpcm", "wb").write(b''.join(frames))
    for frame in frames:
        print(audioop.rms(frame,2))
    #getResponse(frames)



