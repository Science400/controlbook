from scipy import signal as sg
import numpy as np

class squareWave:
    def __init__(self, frequency=1.0, amplitude=1.0, dutycycle=0.5, phaseshift=0, yoffset = 0) -> None:
        self.frequency  = frequency
        self.amplitude  = amplitude
        self.dutycycle  = dutycycle
        self.phaseshift = phaseshift
        self.yoffset    = yoffset

    def __call__(self, t):
        return self.amplitude*sg.square(2*np.pi*self.frequency*t, duty=self.dutycycle)+self.yoffset

class sawtoothWave:
    def __init__(self, frequency=1.0, amplitude=1.0, width=0.5, phaseshift=0, yoffset = 0) -> None:
        self.frequency  = frequency
        self.amplitude  = amplitude
        self.width      = width
        self.phaseshift = phaseshift
        self.yoffset    = yoffset

    def __call__(self, t):
        return self.amplitude*sg.sawtooth(2*np.pi*self.frequency*t, width=self.width)+self.yoffset

class sineWave:
    def __init__(self, frequency=1.0, amplitude=1.0, phaseshift=0, yoffset = 0) -> None:
        self.frequency  = frequency
        self.amplitude  = amplitude
        self.phaseshift = phaseshift
        self.yoffset    = yoffset

    def __call__(self, t):
        return self.amplitude*np.sin(2*np.pi*self.frequency*t)+self.yoffset

class stepFunction:
    def __init__(self, amplitude=1.0, yoffset = 0) -> None:
        self.amplitude  = amplitude
        self.yoffset    = yoffset

    def __call__(self, t):
        return np.heaviside(t, self.amplitude) + self.yoffset