from returns.maybe import Maybe
import toolz as t
from operator import itemgetter
from app.db.database import driver


def pip_return(res, node: str):
    return t.pipe(
        res,
        t.partial(t.pluck, node),
        list
    )


def for_single(res, node: str):
    return (Maybe.from_optional(res)
            .map(itemgetter(node))
            .map(lambda x: dict(x))
            .value_or(None))


@t.curry
def read_generic(n_type, filters=None):
    filter_query = " AND ".join([f"n.{key} = ${key}" for key in filters]) if filters else "1=1"
    query = f"""
            MATCH (n:{n_type})
            WHERE {filter_query}
            RETURN n
        """
    with driver.session() as session:
        result = session.run(query, filters or {}).data()
        return pip_return(result, 'n')
