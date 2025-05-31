from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np
from .job_sources import scrape_remoteok
from .job_sources import scrape_weworkremotely
from .job_fetcher import fetch_cached_jobs

tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

def get_embedding(text):
    tokens = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
    with torch.no_grad():
        output = model(**tokens)
    return output.last_hidden_state.mean(dim=1).squeeze().numpy()


def cosine_similarity(a, b):
    a = a / np.linalg.norm(a)
    b = b / np.linalg.norm(b)
    return np.dot(a, b)


def test_embedding():
    jobs = [{"title": "DevOps Engineer"}, {"title": "Frontend Developer"}, {"title": "Software Engineer"}]
    keywords = ["DevOps", "AWS", "Docker"]
    query = " ".join(keywords)
    query_vector = get_embedding(query)

    for job in jobs:
        job_vector = get_embedding(job["title"])
        score = cosine_similarity(query_vector, job_vector)
        print(job["title"], "->", score)



def find_best_matches(keywords):
    query = " ".join(keywords)
    query_vector = get_embedding(query)

    # jobs = scrape_remoteok()
    jobs = fetch_cached_jobs()
    if not jobs:
        print("No jobs scraped")
        return []
    scored_jobs = []

    for job in jobs:
        # job_vector = get_embedding(job["title"])
        # score = cosine_similarity(query_vector, job_vector)
        # scored_jobs.append((score, job))
        if not isinstance(job, dict):
            print("Skipping non-dict job:", job)
            continue
        title = job.get("title", "")
        job_vector = get_embedding(title)
        score = cosine_similarity(query_vector, job_vector)
        if score > 0.1:
            scored_jobs.append((score, job))

    # scored_jobs.sort(reverse=True, key=lambda x: x[0])
    # return scored_jobs[:5]
    # filtered = [(s, j) for s, j in scored_jobs if s > 0.1]
    # filtered.sort(reverse=True, key=lambda x: x[0])
    # return [j for s, j in filtered[:5]]
    scored_jobs.sort(reverse=True, key=lambda x: x[0])
    return [j for s, j in scored_jobs[:5]]
