# Spam Classifier

This project contains a Streamlit application that classifies messages as spam or not spam.

## Requirements

- Python 3.7+
- Streamlit
- NLTK
- scikit-learn
- Other dependencies as needed

## Setup Instructions

1. **Clone the Repository**  
   Open your terminal and run:
   ```bash
   git clone <your-github-repo-url>
   ```

2. **Navigate to the Project Directory**  
   ```bash
   cd /home/ansingh0305/Desktop/mlProjects
   ```

3. **(Optional) Create and Activate a Virtual Environment**  
   ```bash
   python -m venv env
   source env/bin/activate   # on Unix/macOS
   env\Scripts\activate      # on Windows
   ```

4. **Install Dependencies**  
   If you have a `requirements.txt` file, run:
   ```bash
   pip install -r requirements.txt
   ```
   If not, install the required packages manually:
   ```bash
   pip install streamlit nltk scikit-learn
   ```

5. **Download Required NLTK Data**  
   Open a Python shell or include these lines in a script and run them:
   ```python
   import nltk
   nltk.download('stopwords')
   nltk.download('punkt')
   nltk.download('punkt_tab')
   ```

6. **Ensure Necessary Pickle Files Are in Place**  
   Make sure you have:
   - `vectorizer.pkl`
   - `model.pkl`  
   These files should be located in the project root.

7. **Run the Application**  
   In your terminal, run:
   ```bash
   streamlit run spam.py
   ```
   This will open the app in your web browser.

## Usage

- Enter your message in the text area.
- Click on the **Predict** button.
- The application will display **Spam** if the message is classified as spam, or **Not Spam** otherwise.

Happy classifying!
