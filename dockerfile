# Use a base Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies for Ollama
RUN apt-get update && \
    apt-get install -y curl git libssl-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Ollama (for Linux)
RUN curl -fsSL https://ollama.com/install.sh | bash

# Add ollama binary to PATH if needed
ENV PATH="/root/.ollama/bin:$PATH"

# Copy your project files
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Download the model (optional: llama3, phi3, etc)
RUN ollama pull llama3

# Expose the Streamlit default port
EXPOSE 8501

# Start Ollama in background and launch Streamlit
CMD bash -c "ollama serve & streamlit run app.py --server.port=8501 --server.enableCORS=false --server.enableXsrfProtection=false"
