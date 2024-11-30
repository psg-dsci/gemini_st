**Fake News Detection App Using Gemini API**





**Overview**
The Fake News Detection App is a web-based application that helps users analyze the credibility of news items. By leveraging Google's Gemini Generative AI, the app evaluates the content and provides a classification of whether the news is genuine or fake. If the news is deemed fake, the app generates a plausible true version of the story.

**Features**
News Classification: Determines whether the input news is fake or real.
Content Analysis: Evaluates the news for manipulation, exaggeration, and misinformation.
Context Evaluation: Assesses the credibility of the news in its social, political, and cultural context.
True Story Generation: If the news is found to be fake, the app generates a plausible true version.
**Tech Stack**
Frontend: Streamlit
Backend: Python
AI API: Google Gemini API
Environment Management: python-dotenv
Prerequisites
Python 3.8 or higher installed.
A valid API key for Google Gemini Generative AI.
**Installation Instructions**
1. Clone the Repository
bash
Copy code
git clone https://github.com/psg-dsci/gemini_st.git
cd gemini_st
2. Set Up a Virtual Environment (Optional but Recommended)
bash
Copy code
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Set Up the API Key
Create a .env file in the project directory.
Add your Google Gemini API key:
makefile
Copy code
API_KEY=your_google_gemini_api_key
Running the App
Start the Streamlit application:
bash
Copy code
streamlit run fake_news.py
Open the URL displayed in the terminal (typically http://localhost:8501).
Usage Instructions
Enter a news article or headline in the text area.
Click the "Click to get the Result" button.
View the analysis and results:
Classification of the news (fake or real).
Plausible true version of the news if it's classified as fake.
**File Structure**
bash
Copy code
gemini_st/
│
├── fake_news.py        # Main application file
├── requirements.txt    # Dependencies for the project
├── .env                # API key storage (not included in the repository)
└── README.md           # Project documentation
**Future Enhancements**
Add multilingual support for analyzing news in different languages.
Integrate additional APIs for cross-referencing facts.
Enhance the UI for better user experience.
**License**
This project is licensed under the MIT License.

**Contributing**
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. For major changes, open an issue to discuss your ideas.


Feel free to reach out for any queries or suggestions!
