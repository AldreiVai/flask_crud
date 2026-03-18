from flask import jsonify
from ..extensions import db
from ..models.notes_model import Notes
from typing import List

class NotesService:
    @staticmethod
    def get_all_notes():
        try:
            data: List[Notes] = Notes.query.order_by(Notes.id.desc()).all()
            response = []
            for item in data:
                response.append(item.to_dict())
            return response
        except Exception as ex:
            return {"message":ex}
    
    @staticmethod
    def get_notes_by_id(id:int):
        try:
            data : Notes = Notes.query.get_or_404(id)
            return data
        except Exception as e:
            print(e)

    @staticmethod
    def add_note(note:str):
        try:
           if not note:
               return None

           data = Notes(notes = note)
           db.session.add(data)
           db.session.commit()

           return {"message": "Note Added Successfully"}
        except Exception as e:
            print(e)

    @staticmethod
    def update_note(id, note):
        try:
            if not id and not note:
                return None
            data = Notes.query.get_or_404(id)
          
            data.notes = note
            db.session.commit()
            return {"message": "Note Updated Successfully"}
        except Exception as e:
            print(e)

    @staticmethod
    def delete_note(id:int):
        try:
            data = Notes.query.get_or_404(id)
            db.session.delete(data)
            db.session.commit()

            return {"message": "Note Deleted Successfully"}
        except Exception as e:
            print(e)
    
