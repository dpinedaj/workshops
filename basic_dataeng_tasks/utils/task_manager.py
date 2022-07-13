
from utils.sql import session
from sqlalchemy import Column
from sqlalchemy import String, Boolean
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
import uuid

Base = declarative_base()


class TaskManager(Base):

    __tablename__ = 'tasks_manager'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    file_name = Column(String)
    fails = Column(Boolean)
    processing = Column(Boolean)
    error = Column(String)
    host = Column(String)

    @classmethod
    def next(cls, host):
        query = """
            UPDATE %s SET
                processing = true
            WHERE id = (
                SELECT id   
                FROM %s
                WHERE processing = false
                AND 
                (
                    fails = false
                )
                AND (
                    host = '%s'
                )
                FOR UPDATE SKIP LOCKED
                LIMIT 1
            )
            RETURNING *
        """ % (cls.__tablename__,
               cls.__tablename__,
               host)

        try:
            rs = session.execute(query).fetchone()
            session.commit()

            if rs:
                result = session.query(
                    TaskManager).filter_by(id=rs['id']).one()
            else:
                result = None
        except NoResultFound:
            print('No task to update')

        return result

    @classmethod
    def truncate(cls):
        session.execute(f"truncate table {cls.__tablename__}")
        session.commit()

    def destroy(self):
        try:
            self._destroy()
        except Exception as ex:
            print(str(ex))

    def _destroy(self):
        session.delete(self)
        session.commit()

    def failed(self, message):
        self.processing = False
        self.fails = True
        self.error = message

        session.add(self)
        session.commit()

    def __repr__(self):
        return "%s(id=%s, fn=%s, proc=%s, fail=%s, error=%s)" % (
            self.__class__.__name__,
            self.id,
            self.file_name,
            self.processing,
            self.fails,
            self.error
        )
