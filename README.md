# 🏥 FedMed: Privacy-Preserving Medical AI Network

> **Winner of the InnoData Hackathon Challenge** (fingers crossed!)  
> *Training AI on sensitive patient data without ever moving the data.*

![Dashboard Demo](https://github.com/YOUR_USERNAME/YOUR_REPO/blob/main/dashboard_screenshot.png?raw=true)
*(Replace this link with your actual screenshot)*

## 🚨 The Problem
Medical AI research is hitting a wall. To cure rare diseases (like Glioma or Meningioma brain tumors), researchers need massive datasets. However, hospitals **cannot share patient data** due to strict privacy laws (HIPAA/GDPR).
* **Result:** Data remains Siloed. AI remains dumb. Patients suffer.

## 💡 The Solution: FedMed
**FedMed** uses **Federated Learning** to decentralize the training process. Instead of sending X-rays to a central server (risky), we send the AI model to the hospitals (safe).
1.  **Global Model** travels to Hospital A & B.
2.  Trains locally on private patient scans.
3.  Only the **mathematical weights** (patterns) are sent back.
4.  **Zero Data Leakage:** No patient image ever leaves the secure facility.

## 🛠️ Tech Stack
* **Core Logic:** Python 3.9
* **Deep Learning:** PyTorch (CNN Architecture)
* **Federated Infrastructure:** Flower (`flwr`)
* **Visualization:** Streamlit (Real-time Dashboard)
* **Dataset:** Brain Tumor MRI (Glioma, Meningioma, Pituitary)

## ⚡ How It Works (The Architecture)
1.  **Server Initialization:** The central server spins up an empty Global Model.
2.  **Client Connection:** Hospital Nodes (Client 0 & 1) connect via gRPC.
3.  **Local Training:** Each hospital trains the model on its private `Training/` folder.
4.  **Aggregation:** The server averages the weights (FedAvg) to create a smarter global brain.
5.  **Result:** We achieved **91.69% Accuracy** across 2 isolated nodes in just 5 rounds.

## 🚀 How to Run This Project
1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Start the Central Server:**
    ```bash
    python src/server.py
    ```
3.  **Start Hospital A (Terminal 2):**
    ```bash
    python src/client.py 0
    ```
4.  **Start Hospital B (Terminal 3):**
    ```bash
    python src/client.py 1
    ```
5.  **Launch Dashboard:**
    ```bash
    streamlit run src/dashboard.py
    ```