#!/usr/bin/env python3
import random

import atheris
import sys
import fuzz_helpers
import random

with atheris.instrument_imports(include=["pretty_midi"]):
    import pretty_midi

from mido import KeySignatureError
def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    try:
        with fdp.ConsumeMemoryFile(all_data=True, as_bytes=True) as f:
            midi_data = pretty_midi.PrettyMIDI(f)
            midi_data.estimate_tempo()
            midi_data.get_chroma()
    except (EOFError, OSError, ValueError, KeySignatureError):
        return -1
    #except IndexError:
     #   if random.random() > .9:
      #      raise
       # return -1
def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
