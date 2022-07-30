import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence, detect_nonsilent

path = "D:\\Video_data\\Grammar\\【文法基礎篇】Eight Parts of Speech｜八大詞類輕鬆學｜Boro English.wav"
write = 'D:\\Video_data\\Grammar\\output.txt'
f = open(write, 'w')


# adjust target amplitude
def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)


# Convert wav to audio_segment
audio_segment = AudioSegment.from_wav(path)

# normalize audio_segment to -20dBFS
normalized_sound = match_target_amplitude(audio_segment, -20.0)
print("音訊長度={} seconds".format(len(normalized_sound) / 1000))
f.write("音訊長度={} seconds".format(len(normalized_sound) / 1000) + "\n")
# Print detected non-silent chunks, which in our case would be spoken words.
nonsilent_data = detect_nonsilent(normalized_sound, min_silence_len=500, silence_thresh=-20, seek_step=1)

# convert ms to seconds


# create a speech recognition object
r = sr.Recognizer()


# a function that splits the audio file into chunks
# and applies speech recognition
def get_large_audio_transcription(path):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    # open the audio file using pydub
    sound = AudioSegment.from_wav(path)
    # split audio sound where silence is 700 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
                              # experiment with this value for your target audio file
                              min_silence_len=200,
                              # adjust this per requirement
                              silence_thresh=sound.dBFS - 10,
                              # keep the silence for 1 second, adjustable as well
                              keep_silence=200,
                              )
    folder_name = "audio-chunks"
    sec = 0
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    # process each chunk
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # try converting it to text
            try:
                text = r.recognize_google(audio_listened, language="zh-TW")
            except sr.UnknownValueError as e:
                text = "can not recognize"
            else:
                text = f"{text.capitalize()}. "
            print([nonsilent_data[sec][0] / 1000, nonsilent_data[sec][1] / 1000], end=" ")
            f.write(str([nonsilent_data[sec][0] / 1000, nonsilent_data[sec][1] / 1000]))
            print(text)
            f.write(text + "\n")
            f.write("\n")
            sec += 1
    f.close
    # return the text for all chunks detected

get_large_audio_transcription(path)