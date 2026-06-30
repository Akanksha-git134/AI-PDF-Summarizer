from flask import Flask, render_template, request
from pypdf import PdfReader
import google.generativeai as genai
from dotenv import load_dotenv
import os

# ==========================================
# LOAD ENVIRONMENT VARIABLES
# ==========================================

load_dotenv()

# ==========================================
# CREATE FLASK APP
# ==========================================

app = Flask(__name__)
import os
os.makedirs("uploads", exist_ok=True)

# ==========================================
# GEMINI API KEYS
# ==========================================

API_KEYS = [
    os.getenv("GEMINI_API_KEY_1"),
    os.getenv("GEMINI_API_KEY_2"),
    os.getenv("GEMINI_API_KEY_3")
]

MAX_PAGES = 200


# ==========================================
# FUNCTION TO TRY MULTIPLE API KEYS
# ==========================================

def generate_summary(prompt):

    last_error = None

    for index, key in enumerate(API_KEYS):

        if not key:
            continue

        try:

            print(f"Trying API Key {index + 1}...")

            genai.configure(api_key=key)

            model = genai.GenerativeModel("gemini-2.5-flash")

            response = model.generate_content(prompt)

            print(f"API Key {index + 1} Worked!")

            return response.text

        except Exception as e:

            print(f"API Key {index + 1} Failed")
            print(e)

            last_error = e

    raise last_error


# ==========================================
# HOME PAGE
# ==========================================

@app.route("/", methods=["GET", "POST"])
def home():

    summary = ""
    error = ""
    page_count = 0
    word_count = 0
    filename = ""

    if request.method == "POST":

        pdf = request.files.get("pdf")

        if not pdf or pdf.filename == "":
            error = "Please upload a PDF file."

            return render_template(
                "index.html",
                summary=summary,
                error=error,
                page_count=page_count,
                word_count=word_count,
                filename=filename
            )

        filename = pdf.filename

        try:

            reader = PdfReader(pdf)

            page_count = len(reader.pages)

            if page_count > MAX_PAGES:

                error = (
                    f"This PDF contains {page_count} pages.\n"
                    f"Maximum allowed pages: {MAX_PAGES}"
                )

                return render_template(
                    "index.html",
                    summary=summary,
                    error=error,
                    page_count=page_count,
                    word_count=word_count,
                    filename=filename
                )

            text = ""

            for page in reader.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

            word_count = len(text.split())

            if len(text.strip()) == 0:

                error = "No readable text was found in this PDF."

            else:

                prompt = f"""You are an expert research assistant.
               Analyze the following document and provide:
              # Executive Summary 
             # Key Points 
             # Important Concepts
            # Conclusion 


Document:

{text[:300000]}
"""

                summary = generate_summary(prompt)

        except Exception as e:

            if "429" in str(e):

                error = (
                    "All Gemini API keys have reached their usage limit. "
                    "Please try again later."
                )

            else:

                error = str(e)

    return render_template(
        "index.html",
        summary=summary,
        error=error,
        page_count=page_count,
        word_count=word_count,
        filename=filename
    )


# ==========================================
# RUN APP
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)