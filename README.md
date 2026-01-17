# Pygame Solar System Simulation

A simple yet educational **Python–Pygame based solar system simulation** that visualizes planetary motion around the Sun using real-world inspired data and accelerated time scaling.

This project is designed to demonstrate orbital mechanics in an intuitive and visually engaging way, making it suitable for learning, experimentation, and further extension.

---

## Overview

The simulation models planets revolving around the Sun, similar to the real solar system. Time in the simulation is **fast-forwarded**, allowing long-term planetary motion to be observed quickly.

**Time Scale:**

* **1 second (simulation) = 1 day (real time)**

**Currently Simulated Planets:**

* Mercury
* Venus
* Earth
* Mars

Each planet follows its orbit around the Sun and displays its **real-time distance from the Sun** during the simulation.

---

## Features

* Physics-based planetary motion using Newtonian gravity
* Accelerated simulation time scale (**1 day = 1 second**)
* Four planets currently implemented:

  * Mercury
  * Venus
  * Earth
  * Mars
* Real-time distance display (planet → Sun)
* Orbital trail rendering for each planet
* Smooth 60 FPS animation loop

---

## Technologies Used

* **Python 3**
* **Pygame** (for rendering and animation)
* Basic physics and trigonometry for orbital calculations

---

## How It Works

* The Sun is fixed at the center of the screen and treated as the primary gravitational body.
* Each planet is initialized with real-world inspired values:

  * Distance from the Sun (in Astronomical Units)
  * Mass (in kilograms)
  * Initial orbital velocity (m/s)
* Newton’s Law of Universal Gravitation is used to calculate forces between bodies.
* Planet positions and velocities are updated every frame using a **time step of one real day per second**.
* Orbital paths are stored and rendered to visualize trajectories.
* The real-time distance from each planet to the Sun is calculated and displayed on screen.

---


## Installation & Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/Mayanksharma1s/planets
   ```

3. Install required dependencies:

   ```bash
   pip install pygame
   ```

4. Run the simulation:

   ```bash
   python planet.py
   ```

**Note:** The simulation window is set to `800 × 800` pixels and runs at 60 FPS.

---

## Future Improvements

* Add remaining planets (Jupiter, Saturn, Uranus, Neptune)
* Introduce moons and elliptical orbits
* Zoom and pan functionality
* Toggleable real-world scaling modes
* UI controls for speed adjustment

---

## Educational Purpose

This project is intended for **learning and visualization purposes**. While inspired by real astronomical values, it simplifies certain physics concepts to maintain clarity and performance.

---

## Author

Created by **Basfoot (Mayank Sharma)**
Student Developer | Python & Pygame Enthusiast

---

## License

This project is open-source and free to use for educational purposes. You may modify and extend it as needed.
