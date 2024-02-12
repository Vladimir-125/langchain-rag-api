# Langchain RAG API

Welcome to the Langchain RAG API, a cutting-edge solution leveraging the power of Retrieval-Augmented Generation (RAG) to enhance query responses. Built with FastAPI, integrated with Langchain, and utilizing the Chroma database, this project showcases the capabilities of RAG in processing and augmenting queries with unparalleled precision.

## Overview

The Langchain RAG API dynamically processes textual data, offering an innovative approach to information retrieval. Embedding documents from the `data` folder into the Chroma database ensures efficient data storage and retrieval. This technology is particularly suited for applications requiring enhanced query responses through the augmentation of similar documents.

## Features

- **FastAPI for rapid development and performance**
- **Langchain integration for advanced data processing**
- **Chroma database for efficient data embedding and retrieval**

## Getting Started

Follow these instructions to set up the Langchain RAG API on your local machine.

### Prerequisites

- Python 3.10 or higher
- Poetry for dependency management

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone git@github.com:Vladimir-125/langchain-rag-api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd langchain-rag-api
   ```

3. Install the required dependencies using Poetry:

   ```bash
   poetry install
   ```

### Running the Application

1. Move to the `app` directory:

   ```bash
   cd app
   ```

   You can also use `make` command and skip step 2
   ```bash
   make dev
   ```

2. Start the FastAPI application:

   ```bash
   poetry run uvicorn main:app --reload
   ```


3. Access the API documentation and try out endpoints:

   - Visit `http://localhost:8000/docs` in your browser for the Swagger UI.
   - Explore the API endpoints and test them directly from the UI.

## Usage

To query the API:

1. Send a GET request to `/ask` with a query parameter:

   ```bash
   curl -X 'GET' \
     'http://localhost:8000/ask?query=your_question_here' \
     -H 'accept: application/json'
   ```

2. Review the returned response augmented with the most relevant information extracted from the documents.

## Contributing

We welcome contributions from the community! Please see our `CONTRIBUTING.md` file for guidelines on how to make contributions to this project.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Support

For support, questions, or feedback, please open an issue in the GitHub issue tracker.

Thank you for exploring the Langchain RAG API!