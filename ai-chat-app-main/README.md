# AI Chat Application

This project is a full-stack AI-powered chat application built using Python, FastAPI, OpenAI API, and a simple frontend with HTML, CSS, and JavaScript. It allows users to send messages through a browser-based chat interface and receive real-time AI-generated responses.

## Features
- Handles user input and generates real-time AI responses
- Integrates with the OpenAI API for natural language processing
- Uses a FastAPI backend with REST API endpoints
- Includes a simple frontend chat interface built with HTML, CSS, and JavaScript
- Supports structured request and response handling with JSON
- Uses CORS middleware to allow frontend-to-backend communication
- Designed with a modular backend structure for scalability and future improvements

## Technologies Used
- Python
- FastAPI
- OpenAI API
- Pydantic
- Uvicorn
- HTML
- CSS
- JavaScript

## Purpose
This project demonstrates how AI models can be integrated into real-world applications through a backend API and connected to a browser-based frontend. It also shows how modern AI applications handle user requests, send them to a language model, and return generated responses in real time.

## How It Works
The application uses a frontend chat interface where the user types a message. That message is sent to the FastAPI backend through a POST request. The backend processes the request, sends the prompt to the OpenAI API, receives the generated response, and returns it to the frontend. The frontend then displays the AI response in the chat window.

## Project Structure
- `main.py` — FastAPI backend application
- `index.html` — Frontend chat interface
- `requirements.txt` — Project dependencies
- `README.md` — Project documentation
- `.gitignore` — Files and folders excluded from Git tracking

## API Endpoints

### GET /
Returns a simple status message showing the backend is running.

Example response:

```json
{
  "message": "AI Chat App is running"
}

```
### POST /chat
Accepts a JSON message from the user and returns an AI-generated response.

Example request:

```json
{
  "message": "Hello"
}

{
  "response": "Hello! How can I help you todayssss?"
}

---
