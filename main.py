import wave

# copy_wav.py
# with wave.open("in.wav", "rb") as src:
#     params = src.getparams()
#     frames = src.readframes(src.getnframes())

# with wave.open("out.wav", "wb") as dst:
#     dst.setparams(params)
#     dst.writeframes(frames)

# print("Copied to out.wav")







# # count_frames.py

# with wave.open("in.wav", "rb") as w:
#     print(w.getnframes())
    
    
    
    
    
    
    
# # half_sound.py


# with wave.open("in.wav", "rb") as src:
#     params = src.getparams()
#     n = src.getnframes() // 2
#     frames = src.readframes(n)

# with wave.open("out.wav", "wb") as dst:
#     dst.setparams(params)
#     dst.writeframes(frames)

# print("Wrote first half to out.wav")







# # reverse_sound.py

# with wave.open("in.wav", "rb") as src:
#     params = src.getparams()
#     nframes = src.getnframes()
#     sampwidth = src.getsampwidth()
#     nchannels = src.getnchannels()
#     frame_size = sampwidth * nchannels
#     raw = src.readframes(nframes)

# # split into frames and reverse
# frames = [raw[i:i+frame_size] for i in range(0, len(raw), frame_size)]
# rev = b"".join(reversed(frames))

# with wave.open("out.wav", "wb") as dst:
#     dst.setparams(params)
#     dst.writeframes(rev)

# print("Reversed written to out.wav")







# # speed_up.py

# with wave.open("in.wav", "rb") as src:
#     params = list(src.getparams())
#     frames = src.readframes(src.getnframes())

# # params is a tuple-like: (nchannels, sampwidth, framerate, nframes, comptype, compname)
# params[2] = int(params[2] * 2)  # double framerate

# with wave.open("out.wav", "wb") as dst:
#     dst.setparams(tuple(params))
#     dst.writeframes(frames)

# print("Sped up 2x -> out.wav (framerate doubled)")







# # slow_down.py

with wave.open("in.wav", "rb") as src:
    params = list(src.getparams())
    frames = src.readframes(src.getnframes())

new_rate = max(1, int(params[2] // 2))
params[2] = new_rate

with wave.open("out.wav", "wb") as dst:
    dst.setparams(tuple(params))
    dst.writeframes(frames)

print(f"Slowed down 2x -> out.wav (framerate set to {new_rate})")