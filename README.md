# 🔐 Acoustic Doppler Session Guard

![Patent](https://img.shields.io/badge/Patent-Published-success)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)
![Status](https://img.shields.io/badge/Status-Prototype-brightgreen)
![Research](https://img.shields.io/badge/Research-Cybersecurity-orange)

> 🚀 **Patent Published**
>
> **Acoustic Doppler Session Guard** is a software-defined cybersecurity framework that transforms a laptop's existing speakers and microphone into an acoustic sensing system capable of detecting user presence using the Doppler Effect. The system automatically secures unattended workstations without requiring additional hardware.

---

# 📖 Overview

Acoustic Doppler Session Guard is a **software-only workstation security solution** that leverages ultrasonic acoustic sensing to determine whether a user is physically present near a laptop.

Instead of relying on traditional idle timers, webcams, infrared sensors, or external peripherals, the system emits a low-amplitude **18 kHz ultrasonic signal**, analyzes its Doppler shift using real-time signal processing, and automatically locks the operating system when the user leaves.

The project introduces a **Dual-Band Spectral Veto Algorithm**, enabling reliable user presence detection even in noisy environments by filtering environmental acoustic interference.

---

# ✨ Features

- 🔊 Software-defined ultrasonic sensing
- 🎯 Doppler-based user presence detection
- 🧠 Dual-Band Spectral Veto Algorithm
- 🔒 Automatic workstation locking
- ⚡ Real-time FFT signal processing
- 🔋 Low CPU and battery consumption
- 🔐 Privacy-preserving (No camera, No speech recording)
- 💻 No additional hardware required
- 🌍 Cross-platform architecture

---

# 🚀 Motivation

Traditional workstation security relies on inactivity timers that often leave systems unlocked for several minutes after a user walks away.

This project aims to:

- Reduce workstation exposure time
- Improve cybersecurity against physical access attacks
- Eliminate hardware deployment costs
- Preserve user privacy
- Reduce power consumption compared to vision-based systems

---

# 🏗 System Architecture

```
Laptop Speakers
        │
        ▼
18 kHz Ultrasonic Signal
        │
        ▼
User Motion
        │
        ▼
Microphone Capture
        │
        ▼
FFT Processing
        │
        ▼
Dual-Band Spectral Analysis
        │
        ├───────────────┐
        ▼               ▼
Motion Energy      Noise Energy
        │               │
        └──────┬────────┘
               ▼
      Spectral Veto Logic
               │
               ▼
 Presence Decision
               │
               ▼
 Automatic OS Lock
```

---

# 🧠 Core Innovation

The key innovation is the **Dual-Band Spectral Veto Algorithm**.

Instead of relying solely on motion detection, the system simultaneously analyzes:

- **Ultrasonic Doppler Motion Band (17.8–18.2 kHz)**
- **Audible Noise Band (1–5 kHz)**

If excessive environmental noise is detected, the system temporarily ignores motion measurements, preventing false unlock or lock events.

---

# ⚙ Working Principle

1. Emit an 18 kHz ultrasonic pilot tone.
2. Capture reflected signals using the laptop microphone.
3. Apply a Hanning window.
4. Perform Fast Fourier Transform (FFT).
5. Extract Doppler sideband energy.
6. Measure environmental noise energy.
7. Apply the Spectral Veto Algorithm.
8. Detect user presence or absence.
9. Trigger automatic operating system lock after a configurable delay.

---

# 📊 Signal Processing Pipeline

```
Audio Capture
      │
      ▼
Windowing
      │
      ▼
FFT
      │
      ▼
Doppler Band Extraction
      │
      ▼
Noise Band Extraction
      │
      ▼
Adaptive Thresholding
      │
      ▼
Spectral Veto
      │
      ▼
Presence Classification
      │
      ▼
OS Session Lock
```

---

# 🛡 Security Advantages

- Prevents unattended workstation attacks
- Reduces insider threat risks
- No webcams required
- No infrared sensors
- No Bluetooth devices
- No cloud processing
- Privacy-friendly acoustic sensing
- Local signal processing only

---

# 📈 Experimental Results

Prototype testing demonstrated:

| Metric | Result |
|---------|--------|
| Detection Range | 1.5–2.0 meters |
| Detection Latency | <0.5 seconds |
| Lock Delay | Configurable (~10 seconds) |
| Security Improvement | ~30× faster than traditional idle timers |
| Battery Usage | ~10× lower than camera-based approaches |

---

# 💻 Technology Stack

- Python 3.9+
- NumPy
- PyAudio
- PortAudio
- FFT
- Digital Signal Processing (DSP)
- Windows API (ctypes)

---

# 📂 Project Structure

```
Acoustic-Doppler-Session-Guard/
│
├── src/
│   ├── signal_generator.py
│   ├── audio_capture.py
│   ├── fft_processor.py
│   ├── spectral_veto.py
│   ├── detector.py
│   ├── calibration.py
│   ├── session_lock.py
│   └── main.py
│
├── docs/
│
├── figures/
│
├── requirements.txt
│
├── LICENSE
│
└── README.md
```

---

# 🎯 Applications

- Enterprise cybersecurity
- Corporate IT infrastructure
- Banking and Financial Systems
- Healthcare Workstations
- Government Organizations
- Educational Institutions
- Research Laboratories
- Privacy-sensitive environments

---

# 🔒 Privacy

Unlike camera-based solutions, this system:

- Does **NOT** record speech.
- Does **NOT** store audio.
- Does **NOT** use webcams.
- Does **NOT** transmit data to the cloud.
- Processes all information locally.
- Only analyzes spectral energy around an ultrasonic carrier.

---

# 🔬 Research Areas

- Cybersecurity
- Software-Defined Sensing
- Human-Computer Interaction
- Digital Signal Processing
- Acoustic Signal Processing
- User Presence Detection
- Pervasive Computing

---

# 📌 Project Status

- ✅ Patent Published
- ✅ Experimental Prototype Developed
- ✅ Research Validation Completed
- 🚧 Further Optimization in Progress

---

# 🔮 Future Work

- Linux optimization
- macOS integration
- Embedded implementation
- Machine Learning adaptive thresholds
- Multi-user detection
- Edge AI optimization
- Enterprise deployment tools
- Cloud-based management dashboard

---

# 🤝 Contributing

Contributions are welcome!

Please open an Issue first to discuss major changes before submitting a Pull Request.

---

# 📜 Patent & Intellectual Property

This project and its underlying **Acoustic Doppler Session Guard** architecture are legally protected under a **published patent**.

### 📄 Patent Information

- **Patent Title:** Acoustic Doppler Session Guard
- **Patent Application/Publication Number:** *[Insert Patent Publication Number]*
- **Patent Status:** ✅ Published
- **Technology Domain:** Cybersecurity, Software-Defined Sensing, Human-Computer Interaction (HCI), Digital Signal Processing

---

# 📄 License

## 📝 Usage & Licensing

This repository is provided strictly for **educational, academic, research, and evaluation purposes only**.

The concepts, algorithms, software architecture, signal-processing techniques, and methodologies described in this repository are protected by a **published patent** and remain the intellectual property of the patent owner(s).

### ✅ Permitted Use

- Academic research
- Educational learning
- Non-commercial experimentation
- Personal projects with proper attribution

### ❌ Restricted Use

Without prior written permission from the patent owner(s), the following activities are strictly prohibited:

- Commercial deployment of this technology
- Manufacturing products based on this invention
- Integration into commercial software or hardware
- Reproduction of the patented algorithms
- Redistribution for commercial purposes
- Use in proprietary enterprise or government systems

Commercial implementation of the patented invention may require a separate licensing agreement with the patent owner(s).

---

## © Intellectual Property Notice

**Copyright © 2026 Adharsh Arvinth. All Rights Reserved.**

The invention described in this repository is protected under a **published patent**.

Unauthorized commercial use, duplication, reverse engineering of the patented methods, redistribution, or implementation of the protected intellectual property may violate applicable patent and copyright laws.

---

## 📬 Licensing & Commercial Inquiries

For licensing opportunities, technology transfer, research collaboration, or commercial use, please contact:

**Adharsh Arvinth**

📧 Email:adharsharvinth2108@gmail.com

GitHub: https://github.com/Adharsh-Arvinth

---

## ⚠ Disclaimer

This repository demonstrates the research, implementation, and technical concepts behind the published patent titled **"Acoustic Doppler Session Guard."**

The source code is shared solely to promote academic research, learning, and innovation.

Publication of this repository **does not grant** any patent license, commercial rights, or permission to manufacture, sell, distribute, or otherwise practice the patented invention without explicit authorization from the patent owner(s).

---

# ⭐ Citation

If you use this work in your research, please cite the corresponding published patent and this repository.

```bibtex
@misc{AcousticDopplerSessionGuard2026,
  author = {Adharsh Arvinth},
  title = {Acoustic Doppler Session Guard},
  year = {2026},
  note = {Patent Published},
  url = {https://github.com/your-username/Acoustic-Doppler-Session-Guard}
}
```

---

## ⭐ Star the Repository

If you found this project useful, consider giving it a ⭐ on GitHub to support future research and development.
