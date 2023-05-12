import streamlit as st

from backend.booli_route import booli
from backend.booli_route.booli_api import Query

BASE_URL = "http://localhost:8000"


def get_booli_listings(_query: Query):
    return booli.get_listings(_query)
