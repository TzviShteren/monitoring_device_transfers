from neo4j import GraphDatabase

from app.settings.config import *


driver = GraphDatabase.driver(
    NEO4J_URL,
    auth=(NEO4J_USERNAME, NEO4J_PASSWORD),
)
