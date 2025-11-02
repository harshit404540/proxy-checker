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

<img width="1366" height="768" alt="Screenshot (12)" src="https://github.com/user-attachments/assets/581818ec-61ea-498a-b606-55194d923a97" />
<img width="1366" height="768" alt="Screenshot (13)" src="https://github.com/user-attachments/assets/cdc891c3-62b5-4f87-aa6f-3338c40802fb" />


