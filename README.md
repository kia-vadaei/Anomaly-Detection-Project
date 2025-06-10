# 📘 Anomaly Detection Project

This report outlines the technical requirements and implementation details for a project in anomaly detection using classical machine learning and LLM-based reasoning. The purpose is to help students gain practical experience with AI techniques in a structured and guided environment. Students are 

---

## 📁 Project Structure

You are provided with the following files:

* `server.py` — Handles communication. **You are not required to modify this file.** It continuously sends a stream of data (mostly normal, some anomalous) to the client.
* `client.py` — This is where you will implement anomaly detection logic. You will load a trained model and trigger an LLM-based alert when an anomaly is detected.
* `train_model.ipynb` — This notebook is where you will generate data, train an anomaly detection model, and save it for use in `client.py`.

---

## 🎯 Project Objectives

The complete project is graded out of **100 points**. You are required to complete the core tasks and optionally implement bonus features for extra credit.

### 🔧 Step-by-Step Breakdown

#### Step 1: Complete `train_model.ipynb` (**30 points**)

You must:

* Generate synthetic **normal** sensor data.
* Use the **Isolation Forest** algorithm for training an anomaly detection model.
* Save the trained model to a file (e.g., using `joblib`).

#### 🔍 Isolation Forest Explanation

* Isolation Forest is an unsupervised learning method.
* It isolates anomalies by randomly selecting a feature and then randomly selecting a split value.
* Anomalies are detected because they are more susceptible to isolation.

```python
from sklearn.ensemble import IsolationForest
model = IsolationForest()
model.fit(normal_data)
```

#### Step 2: Update `client.py` to Detect Anomalies (**40 points**)

In this file, you will:

* Load your trained model.
* Receive streaming data from the server.
* For each incoming data point:

  * Use the model to **predict if it is an anomaly**.
  * If an anomaly is detected:

    * Call the Together AI API (DeepSeek LLaMA3 70B model).
    * Send a prompt asking the LLM to label the anomaly and describe it.

#### Together API Integration

Use the [Together AI API](https://api.together.xyz/) to access the LLaMA3 70B model.

##### 📨 Step 1: Create the Message Payload

Construct your request with a system and user message:

```python
messages = [
  {"role": "system", "content": "You are a helpful assistant that labels sensor anomalies."},
  {"role": "user", "content": "Sensor reading: {data}
Describe the type of anomaly and suggest a possible cause."}
]
```

##### 🔁 Step 2: Send the Request

Use the Together client to send the request:

```python
response = self.__client.chat.completions.create(
    model=self.__model_name,
    messages=messages,
    stream=False,
)
```

⚠️ **Important:** This is a sample prompt format. You must **not copy or reuse this prompt exactly**. Adapt it responsibly for your implementation.

Use a readable alert format like:

```python
print("\n🚨 Anomaly Detected!\nLabel: {label}\nReason: {reason}\n")
```

#### Step 3: Final Submission (**30 points**)

* All TODOs in the notebook and client script must be completed.
* Ensure code is clean and runs end-to-end.
* Include comments and variable names that are readable.

---

## 🧩 Bonus Tasks (Up to 10 points)

You can earn additional credit by completing any of the following:

* 📊 **Visualize** normal vs anomaly points using matplotlib/seaborn. (**+10 pts**)
* 💾 **Log detected anomalies** to a `.csv` file. (**+10 pts**)
* 🧪 Add a **confidence score** to model predictions. (**+10 pts**)
* 🧠 Use multiple LLM prompt templates and compare results. (**+10 pts**)
* 🗂️ Use more complex synthetic features/patterns. (**+10 pts**)

---

## ✅ Summary

| Task                                                     | Points  |
| -------------------------------------------------------- | ------- |
| Complete `train_model.ipynb`                             | 30      |
| Implement anomaly detection and LLM alert in `client.py` | 40      |
| Final Integration and Completion                         | 30      |
| **Total**                                                | **100** |
| **Bonus (Optional)**                                     | **+50** |

This report defines the scope and grading criteria. All students are expected to follow the instructions precisely and submit clean, working code.
