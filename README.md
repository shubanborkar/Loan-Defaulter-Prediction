
# Loan Defaulter Prediction

A Flask-based web application that uses a machine learning model to assess the likelihood of a customer defaulting on a loan. Users provide key financial and credit-related inputs, and the app returns a real-time risk prediction (Low Risk / High Risk).

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Real-Time Prediction:** Assess loan default risk instantly based on user inputs.
- **User-Friendly Interface:** Clean and intuitive web form built with HTML/CSS.
- **ML Integration:** Uses a pre-trained machine learning model (serialized with pickle) for predictions.
- **Flask-Powered:** Back-end powered by Flask, ensuring a lightweight and efficient web application.

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript (optional)
- **Backend:** Python, Flask, Flask-WTF
- **Machine Learning:** Scikit-learn, NumPy, Pandas
- **Deployment:** Ready for cloud deployment (e.g., Render)

## Project Structure

```
Loan-Defaulter-Prediction/
├── Final_predictive_model/
│   └── finalized_model.sav       # Serialized ML model file
├── static/
│   └── styles.css                # CSS styling for the web pages
├── templates/
│   ├── base.html                 # Base HTML template
│   ├── home.html                 # Home page template
│   ├── prediction.html           # Prediction form & result page
│   └── predict.html              # (Optional) Alternative prediction page using Flask-WTF
├── app.py                        # Main Flask application
├── loan.ipynb                    # Jupyter Notebook (data analysis and model training)
├── requirements.txt              # Project dependencies
├── .gitignore                    # Git ignore file
└── README.md                     # This file
```

## Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/shubanborkar/Loan-Defaulter-Prediction.git
   cd Loan-Defaulter-Prediction
   ```

2. **Set Up a Virtual Environment:**
   ```bash
   python -m venv venv
   # On Unix or MacOS:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask App Locally:**
   ```bash
   python app.py
   ```
   Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser to see the application in action.

## Usage

- **Home Page:** Contains general information about the application.
- **Prediction Form:** Navigate to the prediction page, enter the required customer details (e.g., age, dependents, monthly income, etc.), and click **"Calculate Risk"**.
- **Result Display:** The application will display the prediction result (High Risk / Low Risk) based on your input.

## Deployment

This project is ready to be deployed to a cloud hosting platform such as [Render](https://render.com). For Render deployment, ensure you have:
- A `requirements.txt` file with all dependencies.
- Your Flask app exposed as `app` (e.g., using `gunicorn app:app`).

For example, to deploy on Render:
1. Push your project to GitHub.
2. Log in to Render and click **New + > Web Service**.
3. Connect your GitHub account, select the repository, and configure the build and start commands:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
4. Click **Create Web Service** and wait for deployment.

## Contributing

Contributions, suggestions, and improvements are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

**Shuban Borkar**  
Email: [shubanborkar@gmail.com](mailto:shubanborkar@gmail.com)  
LinkedIn: [shuban-borkar](https://www.linkedin.com/in/shuban-borkar)  
GitHub: [shubanborkar](https://github.com/shubanborkar)
