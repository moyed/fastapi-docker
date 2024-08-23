# FastAPI Hello World 🌍

Welcome to the **FastAPI Hello World** project! This repository is a beginner-friendly guide to getting started with FastAPI and Docker. We'll walk you through the basics of setting up a FastAPI application, containerizing it with Docker, and running it locally. 🚀

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Setup Instructions](#setup-instructions)
   - [1. Clone the Repository](#1-clone-the-repository)
   - [2. Build the Docker Image](#2-build-the-docker-image)
   - [3. Run the Docker Container](#3-run-the-docker-container)
4. [Testing the Application](#testing-the-application)
5. [Troubleshooting](#troubleshooting)
6. [Learn More](#learn-more)
7. [Contributing](#contributing)
8. [License](#license)

## Introduction

FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints. This repository contains a simple "Hello World" application to help you get started with FastAPI and Docker.

## Prerequisites

Before you begin, make sure you have the following installed:

- **Docker**: [Get Docker](https://www.docker.com/get-started)
- **Git**: [Get Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Setup Instructions

Follow these simple steps to set up the project on your local machine:

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/moyed/fastapi-docker.git
cd fastapi-docker
```

### 2. Build the Docker Image

Next, build the Docker image for the FastAPI application:

```bash
docker build -t fastapi-hello-world . 
```

### 3. Run the Docker Container

Once the image is built, run the Docker container:
```bash
docker run -d -p 8000:8000 fastapi-hello-world
```

## Testing the Application

Now that your application is running, it’s time to test it! 🎉

Open your web browser and go to:


```bash
http://localhost:8000
```

You should see a “Hello World” message displayed. Congratulations, you’re up and running with FastAPI and Docker! 🎊

## Troubleshooting

If you run into any issues, here are some common troubleshooting steps:

    - Docker Build Issues: Ensure Docker is running and you’re in the correct directory.
    - Port Conflicts: Make sure port 8000 is not being used by another application.
    - Network Issues: Check your Docker network settings if you can’t access the application.

## Learn More
Want to dive deeper into FastAPI and Docker? Check out these resources:
- **Docker**: [Docker Documentation](https://www.docker.com/get-started)
- **FastAPI**: [FastAPI Documentation](https://fastapi.tiangolo.com/)


## Contributing

We welcome contributions! If you have suggestions for improvements, feel free to open an issue or submit a pull request. Let’s make this project even better together! 🤝

## License
This project is licensed under the MIT License - see the LICENSE file for details.




