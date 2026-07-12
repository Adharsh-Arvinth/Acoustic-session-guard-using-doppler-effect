import sounddevice as sd
import numpy as np
import time
import sys

FREQ = 18000
THRESHOLD = 0.5
NOISE_LIMIT = 25.0
LOCK_DELAY = 1
SAMPLE_RATE = 44100
WINDOW_SIZE = 2048
CHANNELS = 2
INPUT_GAIN = 10.0

INPUT_DEVICE = 1
OUTPUT_DEVICE = 3

class SonarStrict:
    def __init__(self):
        self.last_motion_time = time.time()
        self.locked = False
        self.counter = 0
        self.calibrating = True
        self.start_time = time.time()

    def trigger_lock(self):
        print("\n\n" + "!"*45)
        print("   SECURITY ALERT: USER DEPARTED - LOCKING SYSTEM")
        print("!"*45 + "\n")
        self.locked = True

    def audio_callback(self, indata, outdata, frames, time_info, status):
        t = (np.arange(frames) + self.counter) / SAMPLE_RATE
        t = t.reshape(-1, 1)
        outdata[:] = 0.5 * np.sin(2 * np.pi * FREQ * t)
        self.counter += frames

        audio_input = indata[:, 0] * INPUT_GAIN

        fft_data = np.abs(np.fft.rfft(audio_input))
        fft_freqs = np.fft.rfftfreq(len(indata), 1 / SAMPLE_RATE)

        doppler_low = (fft_freqs > (FREQ - 200)) & (fft_freqs < (FREQ - 50))
        doppler_high = (fft_freqs > (FREQ + 50)) & (fft_freqs < (FREQ + 200))
        doppler_energy = np.sum(fft_data[doppler_low]) + np.sum(fft_data[doppler_high])

        noise_band = (fft_freqs > 1000) & (fft_freqs < 5000)
        room_noise = np.mean(fft_data[noise_band]) * 5

        if self.calibrating:
            if time.time() - self.start_time > 3:
                self.calibrating = False
                self.last_motion_time = time.time()
            return

        status_msg = "USER PRESENT"

        if room_noise > NOISE_LIMIT:
            status_msg = "NOISE DETECTED (IGNORED)"
            self.last_motion_time = time.time()
        elif doppler_energy > THRESHOLD:
            self.last_motion_time = time.time()
            status_msg = "DOPPLER MOTION CONFIRMED"
            self.locked = False

        time_idle = time.time() - self.last_motion_time

        bar_dop = "█" * int(doppler_energy * 5)
        bar_noise = "▓" * int(room_noise * 5)
        if len(bar_dop) > 15: bar_dop = bar_dop[:15]
        if len(bar_noise) > 15: bar_noise = bar_noise[:15]

        sys.stdout.write(f"\rDop: {doppler_energy:0.1f} [{bar_dop:<15}] | Noise: {room_noise:0.1f} [{bar_noise:<15}] | Status: {status_msg}   ")
        sys.stdout.flush()

        if time_idle > LOCK_DELAY and not self.locked:
            self.trigger_lock()

if __name__ == "__main__":
    print(f"--- SONAR STRICT MODE ---")
    sonar = SonarStrict()
    try:
        with sd.Stream(device=(INPUT_DEVICE, OUTPUT_DEVICE),
                       channels=CHANNELS,
                       samplerate=SAMPLE_RATE,
                       blocksize=WINDOW_SIZE,
                       callback=sonar.audio_callback):
            while True:
                time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nStopped.")