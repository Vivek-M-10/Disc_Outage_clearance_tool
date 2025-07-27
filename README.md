

---

```markdown
# 🧹 Disc Outage Clearance Tool

A Flask + React-based tool to automatically remove `.log` and `.txt` files older than **7 days** from specified directories. Ideal for automating disk cleanup tasks.

---

## 📁 Project Structure

```

---

<details>
<summary><strong>📁 Disc_outage_clearance/ – Full File Structure</strong></summary>

```
Disc_outage_clearance/
│
├── backend/
│   ├── app.py              # Flask backend with cleanup logic
│   ├── run.sh              # Shell script to start Flask server
│   ├── cleanup.log         # Logs deleted files
│   ├── venv/               # Python virtual environment
│
├── frontend/               # React frontend
│   ├── public/
│   ├── src/
│   │   ├── App.js          # Main UI component
│   │   ├── api.js          # Handles API requests to Flask
│   │   ├── components/
│   │   └── styles/
│   ├── package.json
│   └── .env                # Contains API URL like REACT_APP_API_URL=http://localhost:5000
│
├── logs/
│   ├── app_log/
│   ├── temp_logs/
│   ├── transaction_logs/
```

</details>

---

---

## 🚀 Getting Started

### 1. Backend Setup (Flask)

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install flask
chmod +x run.sh
./run.sh
````

Flask app will start at:
`http://localhost:5000/clean`

### 2. Frontend Setup (React)

```bash
cd ../frontend
npm install
npm start
```

React app will start at:
`http://localhost:3000`

Make sure to create a `.env` file inside `frontend/` with:

```env
REACT_APP_API_URL=http://localhost:5000
```

---

## 🧼 Functionality

* **Flask Backend:** Deletes `.log` and `.txt` files older than 7 days from `TARGET_DIRECTORIES`
* **React Frontend:** One-click cleanup interface + JSON result display
* **Log File:** Maintains cleanup history in `cleanup.log`

---

## 🔗 API

### `GET /clean`

* Triggers the cleanup script
* Returns list of deleted files as JSON:

```json
{
  "deleted": [
    "/logs/app_log/debug.log",
    "/logs/temp_logs/temp.txt"
  ]
}
```

---

## 💻 UI Features (React)

* Button to start cleanup
* Shows loading spinner while backend is processing
* Lists deleted files or shows success/error message

---

## 📄 Dummy Data Setup

To simulate old files for deletion:

```bash
cd logs/app_log
touch dummy.log
touch -t 202401010000 dummy.log
```

---

## 📌 Future Enhancements

* Scheduled job support via CRON or Celery
* Authentication for endpoint
* Multi-user dashboard with historical stats
* File preview/archive before delete

---

## 👨‍💻 Author

**Vivek Mishra**
📬 \[offical.vm81@gmail.com]
🧰 Tech Stack: Flask · React · Bash · Python

---

```

Let me know if you'd like a ready-made React component (`App.js`) or a sample UI to trigger `/clean` and display results.
```
