import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaduio.paInt16
CHANNELS = 1 
RATE = 44100
RECORD_SECONDS = 5

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT, channels=CHANNELS, rate = RATE, input=True, frames_per_buffer=CHUNK)
print("* recording")

for i in range(0, int(RATE/CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print("done")
stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open("new_test", "wb")
wf.setnchannels(1)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
