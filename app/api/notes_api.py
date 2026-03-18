from flask import Flask, Blueprint, jsonify, request
from ..services.notes_service import NotesService
from typing import List
from ..models.notes_model import Notes

notes_api_bp = Blueprint("notes_api", __name__, url_prefix="/api")

@notes_api_bp.route("/notes/get-all", methods=["GET"])
def get_all_notes():
    try:
        data : List[Notes] = NotesService.get_all_notes()
        return data , 200
    except Exception as ex:
        print(ex) 
        return jsonify({"error": "Cannot establish database connection"}), 500
    
@notes_api_bp.route("/notes/<int:id>", methods=["GET"])
def get_note_by_id(id):
    try:
        data = NotesService.get_notes_by_id(id)
        return data.to_dict(), 200
    except Exception as ex:
        print(ex) 
        return jsonify({"error": "Cannot establish database connection"}), 500
    
@notes_api_bp.route("/notes/add", methods=["POST"])
def add_note():
    try:
        data = request.get_json()
        note_text = data.get("notes")

        if not note_text:
            return jsonify({"error": "Note text is required"}), 400

        new_note = NotesService.add_note(note_text)
        return jsonify(new_note), 200

    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500
    
@notes_api_bp.route("/notes/<int:id>", methods=["PUT"])
def update_note(id):
    try:
        data = request.get_json()
        note_text = data.get("notes")

        if not note_text:
            return jsonify({"error": "Note text is required"}), 400

        updated_note = NotesService.update_note(id, note_text)
        if updated_note:
            return jsonify(updated_note), 200
        else:
            return jsonify({"error": "Note not found"}), 404

    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500

@notes_api_bp.route("/notes/<int:id>", methods=["DELETE"])
def delete_note(id):
    try:
        result = NotesService.delete_note(id)
        if result:
            return jsonify({"message": "Note deleted successfully"}), 200
        else:
            return jsonify({"error": "Note not found"}), 404

    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500