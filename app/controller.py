from sqlalchemy import update, insert, delete, select
from app.db import log, RecordNotFound


class LogsController:
    def __init__(self, connection):
        self.conn = connection

    async def list(self):
        q = select(log)
        result = await self.conn.execute(q)
        logs_records = await result.fetchall()
        return [{'id': l[0], 'text': l[1], 'created_at': str(l[2])} for l in logs_records]

    async def get(self, log_id):
        q = select(log).where(log.c.id == log_id)
        result = await self.conn.execute(q)
        log_record = await result.first()
        if not log_record:
            raise RecordNotFound(f"Log with id: {log_id} does not exists")
        return {'id': log_record[0], 'text': log_record[1], 'created_at': str(log_record[2])}

    async def create(self, text):
        ins = insert(log).values(text=text)
        result = await self.conn.execute(ins)
        print(ins)
        print(result)
        return result

    async def delete(self, log_id):
        q = delete(log).where(log.c.id == log_id)
        await self.conn.execute(q)
        return None

    async def update(self, log_id, text):
        u = update(log).where(log.c.id == log_id)
        u = u.values(text=text)
        await self.conn.execute(u)
        return await self.get(log_id)
