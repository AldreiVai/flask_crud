from ..extensions import db
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from datetime import date

class Notes(db.Model):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True)
    notes = Column(Text, nullable=False)
    created_at = Column(DateTime, default=func.now())

    def to_dict(self):
        return {
            "id": self.id,
            "notes": self.notes,
            "created_at": self.created_at,
        }