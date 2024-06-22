# https://shallowsky.com/blog/programming/python-play-chords.html

import pygame, pygame.sndarray
pygame.mixer.init(channels=1)

def play_for(sample_wave, ms):
    """Play the given NumPy array, as a sound, for ms milliseconds."""
    sound = pygame.sndarray.make_sound(sample_wave)
    sound.play(-1)
    pygame.time.delay(ms)
    sound.stop()

import numpy
import scipy.signal

sample_rate = 44100

def sine_wave(hz, peak, n_samples=sample_rate):
    """Compute N samples of a sine wave with given frequency and peak amplitude.
       Defaults to one second.
    """
    length = sample_rate / float(hz)
    omega = numpy.pi * 2 / length
    xvalues = numpy.arange(int(length)) * omega
    onecycle = peak * numpy.sin(xvalues)
    return numpy.resize(onecycle, (n_samples,)).astype(numpy.int16)

# Play A (440Hz) for 1 second as a sine wave:
#play_for(sine_wave(440, 4096), 1000)

# Chords
#play_for(sum([sine_wave(440, 4096), sine_wave(880, 4096)]), 1000)

# Label the three octaves around middle C:
note_names = ["C0", ["CS0", "DF0"], "D0", ["DS0", "EF0"], "E0", "F0", ["FS0", "GF0"], "G0", ["GS0", "AF0"], "A0", ["AS0", "BF0"], "B0",
              "C1", ["CS1", "DF1"], "D1", ["DS1", "EF1"], "E1", "F1", ["FS1", "GF1"], "G1", ["GS1", "AF1"], "A1", ["AS1", "BF1"], "B1",
              "C2", ["CS2", "DF2"], "D2", ["DS2", "EF2"], "E2", "F2", ["FS2", "GF2"], "G2", ["GS2", "AF2"], "A2", ["AS2", "BF2"], "B2",
              "C3"]
global notes
note2freq = {}

def setup_notes():
    global note2freq
    c0 = 130.81
    n = 0
    for note_name in note_names:
        f = c0*(2**(n/12))
        if (isinstance(note_name, str)):
            note2freq[note_name]=f
        else:
            note2freq[note_name[0]]=f
            note2freq[note_name[1]]=f
        n = n + 1
    
setup_notes()
print(note2freq)

def play_tune(notes,ms=1000):
    global note2freq
    for note in notes:
        play_for(sine_wave(note2freq[note], 4096),ms)

play_tune(["C2","C2","D2","C2","F2","E2","C2","C2","D2","C2","G2","F2"],300)

# Play a chord by note name
play_for(sum([sine_wave(note2freq[note], 4096) for note in ["C1","E1","G1"]]), 1000) # C Major
play_for(sum([sine_wave(note2freq[note], 4096) for note in ["C1","EF1","G1"]]), 1000) # C Minor

# Something's wrong with the below. Need to debug at some point.  It
# came from the original web site (as at top) but seems to be broken.

def make_chord(hz, ratios):
    """Make a chord based on a list of frequency ratios."""
    sampling = 4096
    chord = waveform(hz, sampling)
    for r in ratios[1:]:
        chord = sum([chord, sine_wave(hz * r / ratios[0], sampling)])
    return chord

#play_for(make_chord(440,[1,2,3])

def major_triad(hz):
    return make_chord(hz, [4, 5, 6])

#play_for(major_triad(440), length)

def make_chord(hz, ratios, waveform=None):
    """Make a chord based on a list of frequency ratios
       using a given waveform (defaults to a sine wave).
    """
    sampling = 4096
    if not waveform:
        waveform = sine_wave
    chord = waveform(hz, sampling)
    for r in ratios[1:]:
        chord = sum([chord, waveform(hz * r / ratios[0], sampling)])
    return chord

def major_triad(hz, waveform=None):
    return make_chord(hz, [4, 5, 6], waveform)

#play_for(major_triad(440, square_wave), length)
