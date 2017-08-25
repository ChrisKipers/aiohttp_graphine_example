from collections import defaultdict

from aiodataloader import DataLoader
from . import models


def get_table_data_loader(table, key_property, db, multiple):
    async def batch_load_fn(keys):
        async with db.acquire() as conn:
            results =  \
                await conn.execute(
                    table.select().where(key_property.in_(keys)))

            if not multiple:
                results_by_id = {r[key_property.name]: r for r in results}
            else:
                results_by_id = defaultdict(list)
                for r in results:
                    results_by_id[r[key_property.name]].append(r)
            return [results_by_id.get(key) for key in keys]

    return DataLoader(batch_load_fn)


def get_question_loader(db):
    return get_table_data_loader(models.question, models.question.c.id, db, multiple=False)


def get_choice_loader(db):
    return get_table_data_loader(models.choice, models.choice.c.question_id, db, multiple=True)
