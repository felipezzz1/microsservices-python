from fastapi.testclient import TestClient
from main import app
import nltk

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Wikipedia API. Call /search or /wiki or /phrase"
    }


# def test_read_search():
    # this actually will fail
    # every search brings back different results
    # response = client.get("/search/Brazil")
    # assert response.status_code == 200
    # assert response.json() == {
    #     "search": [
    #         "Brazil",
    #         "Brazil national football team",
    #         "Brazilian",
    #         "Municipalities of Brazil",
    #         "Brazilians",
    #         "Brazil (disambiguation)",
    #         "Federative units of Brazil",
    #         "Brazil nut",
    #         "Regions of Brazil",
    #         "Rio de Janeiro",
    #     ]
    # }


def test_read_wiki():
    response = client.get("/wiki/Brazil")
    assert response.status_code == 200
    assert response.json() == {
        "wiki": "Brazil, officially the Federative Republic of Brazil, is the largest and easternmost country in South America and Latin America."
    }


def test_read_phrase():
    nltk.download('punkt_tab')
    response = client.get("/phrase/Brazil")
    assert response.status_code == 200
    assert response.json() == {
        "phrase": [
            "brazil",
            "federative",
            "brazil",
            "easternmost country",
            "america",
            "america",
        ]
    }
