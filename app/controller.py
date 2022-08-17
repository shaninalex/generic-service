from app.db import log, RecordNotFound


async def get_question(conn, question_id):
    result = await conn.execute(
        log.select()
        .where(log.c.id == question_id))
    question_record = await result.first()

    if not question_record:
        msg = "Question with id: {} does not exists"
        raise RecordNotFound(msg.format(question_id))

    return question_record


async def controller_get_logs(conn):
    result = await conn.execute(
        log.select()
    )
    logs_records = await result.fetchall()
    return logs_records
