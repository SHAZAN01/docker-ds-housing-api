# 🚀 California Housing Price Predictor API

A production-ready, Dockerized machine learning API to predict housing prices in California. Built with FastAPI, Scikit-learn, and Docker.

This project demonstrates a professional end-to-end workflow, separating model training from a scalable inference service.

---

## 🛠️ Tech Stack

* **Python 3.11**
* **Machine Learning**: Scikit-learn, Pandas, Numpy
* **API**: FastAPI
* **Server**: Uvicorn
* **Containerization**: Docker

---

## ✨ Features

* **FastAPI Endpoint**: A `/predict/` endpoint that accepts 8 features and returns a price prediction.
* **Pydantic Validation**: Type-safe data validation for all API inputs.
* **Dockerized**: Fully containerized for easy deployment and reproducible builds.
* **Interactive Docs**: Automatic, interactive API documentation at `/docs`.

---

## 🏁 How to Run Locally

You must have [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/richansar/docker-ds-housing-api.git](https://github.com/richansar/docker-ds-housing-api.git)
    cd docker-ds-housing-api
    ```
    *(Note: Make sure to replace `richansar` with your username if it's different!)*

2.  **Build the Docker image:**
    ```bash
    docker build -t housing-api .
    ```

3.  **Run the container:**
    ```bash
    docker run -d -p 8000:8000 housing-api
    ```

4.  **Test the API!**
    * Open your browser and navigate to **[http://localhost:8000/docs](http://localhost:8000/docs)**.
    * Use the interactive "Try it out" feature to send a test prediction.
