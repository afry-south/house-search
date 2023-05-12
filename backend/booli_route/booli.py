import requests
import streamlit
from fastapi import APIRouter

from backend.booli_route.booli_api import (
    LISTINGS_URL,
    PropertyResponse,
    Query,
    QueryResponse,
)

router = APIRouter(prefix="/booli_route")


@router.get("/listing/{_id}")
def get_listing(_id: str) -> PropertyResponse:
    r = requests.get(f"{LISTINGS_URL}/{_id}")
    r.raise_for_status()
    response = r.json()
    response = PropertyResponse(**response["listings"][0])
    # TODO wrap and get all listings rather than first [limit]

    return response


@router.post("/query")
def get_listings(query: Query) -> list[PropertyResponse]:
    url = f"{LISTINGS_URL}?{query.build_params()}"
    print(url)
    r = requests.get(url)
    r.raise_for_status()
    r_json = r.json()

    if len(r_json):
        # TODO wrap and get all listings rather than first [limit]
        try:
            response = QueryResponse(**r_json)
        except TypeError:
            streamlit.write("Failed to parse Booli API")
            return []

        return response.listings
    else:
        raise Exception("No listings found")


if __name__ == "__main__":
    print(get_listings(Query(query="malmö")))
