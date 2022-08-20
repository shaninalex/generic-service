from app.db import log, RecordNotFound


class LogsController:
    def __init__(self, connection):
        self.conn = connection

    async def get(self):
        result = await self.conn.execute(
            log.select()
        )
        logs_records = await result.fetchall()
        return [{'id': l[0], 'text': l[1], 'created_at': str(l[2])} for l in logs_records]

    async def get_by_id(self, log_id):
        result = await self.conn.execute(
            log.select()
            .where(log.c.id == log_id))
        question_record = await result.first()

        if not question_record:
            raise RecordNotFound(f"Question with id: {log_id} does not exists")

        return question_record

    async def post_log(self, text):
        ins = log.insert().values(text=text)
        result = await self.conn.execute(ins)
        return result
