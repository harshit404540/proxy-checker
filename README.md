# 🕵️‍♂️ Proxy Checker

A simple and efficient **multithreaded proxy checker** written in Python.  
This tool verifies if the proxies in your list are working by sending requests to `ipinfo.io`.

---

## 📂 Project Structure

proxy-checker/
│
├── proxy_checker.py
└── proxies.txt

---

## 🚀 Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/proxy-checker.git
   cd proxy-checker
    ```

2. **Install Dependencies**
   ```bash
   pip install requests
   ```

3. **Add your proxies**
    ```bash
    Open proxies.txt
    Add proxies in it line by line
    Example:
        123.45.67.89:8080
        98.76.54.32:3128
    ```

4. **Run the checker**
    ```bash
    python proxy_checker.py
    ```

##  🧠 How It Works

Reads proxies from proxies.txt
Uses Python’s threading and queue modules for parallel processing
Sends a test request to http://ipinfo.io/json

Prints results:

🟢 Working proxies → displayed in green
🔴 Dead proxies → displayed in red

---

## 🧩 Requirements
    
  Python 3.7+
  requests library (pip install requests)

## 📸 Example Output

<img width="1106" height="647" alt="Screenshot (12)" src="https://github.com/user-attachments/assets/c7fb118a-b46a-4d6e-8ed4-6e157ce8cc7c" />
<img width="1111" height="629" alt="Screenshot (13)" src="https://github.com/user-attachments/assets/565f8de2-3d01-4909-9d3a-5e041b6e848b" />
