# sine_wave_model.py

import numpy as np
import matplotlib.pyplot as plt

def generate_sine_wave(frequency, amplitude, duration, sample_rate):
    """
    Generates a sine wave with the given parameters.

    Parameters:
        frequency (float): Frequency of the sine wave in Hz.
        amplitude (float): Amplitude of the sine wave.
        duration (float): Duration of the sine wave in seconds.
        sample_rate (int): Number of samples per second.

    Returns:
        t (numpy.ndarray): Array of time values.
        y (numpy.ndarray): Array of sine wave values.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    y = amplitude * np.sin(2 * np.pi * frequency * t)
    return t, y

def plot_sine_wave(t, y, title="Sine Wave"):
    """
    Plots a sine wave.

    Parameters:
        t (numpy.ndarray): Array of time values.
        y (numpy.ndarray): Array of sine wave values.
        title (str): Title of the plot.
    """
    plt.figure(figsize=(10, 4))
    plt.plot(t, y, label="Sine Wave")
    plt.title(title)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Example usage
    frequency = 440  # A4 note frequency in Hz
    amplitude = 1.0  # Maximum amplitude
    duration = 2.0   # 2 seconds
    sample_rate = 44100  # Standard audio sample rate

    t, y = generate_sine_wave(frequency, amplitude, duration, sample_rate)
    plot_sine_wave(t, y, title=f"Sine Wave - {frequency} Hz")
