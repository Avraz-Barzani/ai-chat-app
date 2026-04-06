# AI Chat Application

This project is a simple AI-powered chat application built using Python and FastAPI.

## Features
- Handles user input and generates responses
- Simulates AI-style responses using backend logic (can be extended to real AI APIs)
- Structured backend for scalability

## Technologies Used
- Python
- FastAPI
- OpenAI API

## Purpose
This project demonstrates how AI models can be integrated into real-world applications.

## How It Works
This application takes user input, sends it to an AI model through an API, and returns a generated response. The backend is built using FastAPI to handle requests and manage the flow of data between the user and the AI model.

## Future Improvements
- Implements REST API endpoints for handling requests and responses
- Add conversation memory
- Deploy application for public access
- Improve UI with a frontend interface

- Built REST API endpoints for handling requests and responses

- ## API Endpoints

### GET /
Returns a simple status message showing the app is running.

### POST /chat
Accepts a JSON message and returns a generated response.

Example request:
```json
{
  "message": "Hello"
}
## Run Locally

1. Install dependencies:
