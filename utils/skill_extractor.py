SKILLS = [
    "python",
    "java",
    "c++",
    "c",
    "sql",
    "mysql",
    "postgresql",
    "fastapi",
    "flask",
    "streamlit",
    "react",
    "javascript",
    "html",
    "css",
    "git",
    "github",
    "docker",
    "aws",
    "azure",
    "machine learning",
    "deep learning",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "rest api",
    "rest",
    "api",
    "linux",
    "mongodb",
    "firebase"
]


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        if skill in text:
            found_skills.append(skill)

    return found_skills