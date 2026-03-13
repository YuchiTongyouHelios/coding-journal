Day 26: Started My AI Violin Coach – Finished Phase 1!

## What I Built Today
Started building an AI Violin Coach web app! Today I finished Phase 1 – a pitch detection tool that lets users upload a recording of a single violin note and tells them if it's in tune. The app shows the detected note, how many cents sharp or flat it is, and even draws a graph of the pitch over time.

## What I Learned
Terminal coding – I created and edited files entirely in the terminal using nano. Never used it before today!
Virtual environments – Learned to create isolated Python environments with venv so packages don't conflict
SSL certificate issues on Mac – Discovered that Python can have certificate problems, and how to work around them with --trusted-host flags
Python version matters – Found out that some packages (like llvmlite) don't have pre-built wheels for newer Python versions yet
Pre-release packages – Learned how to install release candidates like llvmlite==0.44.0rc2 to get Python 3.13 support
Full stack basics – Saw how Flask (backend) and HTML/JavaScript (frontend) work together

## One Thing I Struggled With
Python version compatibility! I spent hours fighting with llvmlite not installing on Python 3.13. The error messages were confusing at first – first an SSL certificate problem, then a build error, then a missing CMake error. Finally got it working by using pre-release package versions specifically built for Python 3.13. Also had to learn to use --trusted-host flags to bypass SSL issues. The terminal felt intimidating at first, but by the end I was navigating and editing files like a pro.

## My Code (End of Day 26)
```python
# Key function from my AI Violin Coach – detects pitch from uploaded audio
def analyze_pitch(file_path):
    y, sr = librosa.load(file_path, sr=None, mono=True)
    f0, voiced_flag, voiced_probs = librosa.pyin(y, fmin=65, fmax=2093, sr=sr)
    f0_clean = f0[~np.isnan(f0)]
    median_pitch = np.median(f0_clean)
    confidence = np.mean(voiced_probs[voiced_flag]) if any(voiced_flag) else 0
    return float(median_pitch), float(confidence)

def pitch_to_note(pitch):
    A4 = 440.0
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    midi = 12 * np.log2(pitch / A4) + 69
    midi_rounded = int(round(midi))
    cents = int(100 * (midi - midi_rounded))
    note_name = notes[midi_rounded % 12] + str((midi_rounded // 12) - 1)
    return note_name, cents
```
## What Clicked Today
The terminal isn't that scaryas i thought it would be! I always used graphical code editors, but today I created files, edited them, ran servers, and debugged problems all from the command line. Also clicked how Python packages depend on each other – librosa needs numba, which needs llvmlite, which needs the right Python version. Understanding that chain helped me troubleshoot.

## Still Fuzzy?
How exactly SSL certificates work and why they break
What CMake actually does and why some packages need it
The difference between release candidates, pre-releases, and stable versions

##  What I DON'T Understand Yet (But Will Learn)
- How logarithms convert frequency to pitch
- What NumPy arrays are and why [~np.isnan()] works
- How MIDI numbers map to note names
