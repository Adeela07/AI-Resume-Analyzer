RECOMMENDATIONS = {

    "python": (
        "Practice Python fundamentals, functions, "
        "object-oriented programming, and common libraries."
    ),

    "java": (
        "Learn Java OOP, collections, exception handling, "
        "and basic application development."
    ),

    "sql": (
        "Practice SQL queries, JOINs, GROUP BY, "
        "subqueries, indexes, and database design."
    ),

    "fastapi": (
        "Learn FastAPI routing, request validation, "
        "Pydantic models, and REST API development."
    ),

    "flask": (
        "Learn Flask routing, templates, REST APIs, "
        "and backend application development."
    ),

    "react": (
        "Learn React components, props, state, hooks, "
        "and API integration."
    ),

    "javascript": (
        "Practice JavaScript fundamentals, ES6, DOM "
        "manipulation, asynchronous programming, and APIs."
    ),

    "html": (
        "Learn semantic HTML, forms, tables, "
        "accessibility, and page structure."
    ),

    "css": (
        "Practice CSS layouts, Flexbox, Grid, "
        "responsive design, and styling."
    ),

    "git": (
        "Learn Git commits, branches, merging, "
        "pull requests, and version control workflows."
    ),

    "github": (
        "Practice GitHub repositories, branches, "
        "pull requests, issues, and collaboration."
    ),

    "docker": (
        "Learn Docker images, containers, Dockerfiles, "
        "volumes, networking, and container deployment."
    ),

    "aws": (
        "Learn AWS fundamentals including EC2, S3, "
        "IAM, networking, and basic cloud deployment."
    ),

    "machine learning": (
        "Study supervised and unsupervised learning, "
        "feature preprocessing, model evaluation, "
        "and common ML algorithms."
    ),

    "deep learning": (
        "Learn neural networks, activation functions, "
        "backpropagation, optimization, and CNNs."
    ),

    "pandas": (
        "Practice data loading, cleaning, filtering, "
        "grouping, merging, and analysis with pandas."
    ),

    "numpy": (
        "Learn NumPy arrays, indexing, broadcasting, "
        "vectorized operations, and numerical computation."
    ),

    "scikit-learn": (
        "Practice preprocessing, model training, "
        "evaluation, pipelines, and machine learning algorithms."
    ),

    "tensorflow": (
        "Learn tensors, neural networks, model training, "
        "and deep learning workflows using TensorFlow."
    ),

    "pytorch": (
        "Learn tensors, datasets, neural networks, "
        "training loops, and model evaluation using PyTorch."
    ),

    "rest api": (
        "Learn HTTP methods, status codes, JSON, "
        "REST principles, authentication, and API testing."
    ),

    "linux": (
        "Practice Linux commands, file permissions, "
        "process management, networking, and shell scripting."
    ),

    "mongodb": (
        "Learn MongoDB documents, collections, CRUD "
        "operations, queries, indexes, and aggregation."
    )
}


def get_recommendation(skill):

    return RECOMMENDATIONS.get(
        skill.lower(),
        "Learn the fundamentals of this skill and practice it through a small project."
    )