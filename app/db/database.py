import redis

from neo4j import GraphDatabase

from app.settings.config import *


redis_client = redis.Redis(host='localhost', port=6379, db=0)


driver = GraphDatabase.driver(
    NEO4J_URL,
    auth=(NEO4J_USERNAME, NEO4J_PASSWORD),
)
