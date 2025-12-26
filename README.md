# PR-Insight
Problem:

>Open-source maintainers often receive pull requests with poor descriptions, making reviews slow and error-prone.

Solution:

Build a GitHub App that automatically summarizes pull requests and highlights review-critical areas when a PR is opened.

What it does->

>Reads PR metadata and code diff

>Generates a short summary

>Creates a review checklist

>Assigns a risk level (Low / Medium / High)

>Posts this as a PR comment


backend

backend/
│
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── github_webhook.py
│   │   └── health.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── github_client.py
│   │   └── pr_service.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── pr.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── webhook_verify.py
│   │   └── logger.py
│   │
│   └── main.py
│
├── requirements.txt
├── .env.example
└── README.md
