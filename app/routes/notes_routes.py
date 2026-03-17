from flask import Blueprint, jsonify, render_template, request, redirect, url_for
from typing import List
from ..models.notes_model import Notes
from ..services.notes_service import NotesService 

notes_bp = Blueprint("notes", __name__)

@notes_bp.route("/")
def home():
    try:
        data = NotesService.get_all_notes()
        return render_template("notes.html", notes=data)
    except Exception as ex:
        print(ex) 
        return "Cannot establish database connection", 500
    
@notes_bp.route("/notes/<int:id>/edit")
def edit_note(id):
    notes = NotesService.get_all_notes()
    return render_template("notes.html", notes=notes, edit_id=id)

@notes_bp.route("/notes/<int:id>/update", methods=["POST"])
def update_note(id):
    try:
        note_text = request.form.get("notes")

        if note_text:
            NotesService.update_note(id, note_text)

        return redirect(url_for("notes.home"))

    except Exception as e:
        print(e)
        return redirect(url_for("notes.home"))


@notes_bp.route("/notes/add", methods=['POST'])
def add_note():
    try:
        if not request.form.get("notes"):
            return redirect(url_for("notes.home"))
        
        body = request.form.get("notes")
        NotesService.add_note(body)
        
        return redirect(url_for("notes.home"))
        
    except Exception as e:
        print(e)
        return render_template("notes.html", notes=NotesService.get_all_notes(), error=str(e))

@notes_bp.route("/notes/<int:id>/delete", methods=['POST'])
def delete_note(id):
    try:
        NotesService.delete_note(id)
        return redirect(url_for("notes.home"))
        
    except Exception as e:
    	print(e)
