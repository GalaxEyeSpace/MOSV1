# Mission Operation Software (MOS)

Mission Operation Software is a rapidly developed project built from scratch in 10 days using a lean approach.

## Overview

This project is being developed with a lean approach. For more details, see the [requirements](#).

## Architecture

### Lean Approach

![Lean Approach][./Media/UntitledDiagram.drawio.png]

### System Architecture

![System Architecture][def]

### Detailed Architecture

![Detailed Architecture][def]

## Backend

The backend is built using Django and consists of three servers:

- **MOS**: Main Mission Operation Software server.
- **TM Simulator**: Connects via WebSocket.
- **Astro Server**: Provides REST connections.

## Frontend

The frontend is a single project consisting of 6-7 dashboards developed using React.

## Getting Started

1. **Clone the repository.**
2. **Install dependencies** for both backend and frontend.
3. **Run the Django servers** (MOS, TM Simulator, Astro Server).
4. **Start the React application.**

Happy coding!

[def]: attach_photo
