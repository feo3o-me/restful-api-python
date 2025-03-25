from flask import Blueprint, request
from authentication import require_auth

blueprint = Blueprint("acc", __name__)

users = [
    {"email": "usr1@gmail.com", "name": "user1", "password": "1234"}
]

@blueprint.route("/test")
def ping_accounts_service():
    return "OK", 200

@blueprint.route("/email/<name>")
@require_auth
def get_user_by_email(name):
    for user in users:
        if user["name"] == name:
            return {"email": user["email"]}, 200
        return {"error": "User not found"}, 404
    
@blueprint.route("/search")
@require_auth
def search_user_by_domain():
    email_domain = request.args.get('email_domain')
    if not email_domain:
        return {"error": "No email domain provided"}, 400
    matched_users = [u for u in users if u["email"].endswith(email_domain)]
    return {"users": matched_users}, 200   

@blueprint.route("/user", methods=["POST"])
@require_auth
def add_user():
    for fld in ['email', 'name', 'password']:
        if fld not in request.json:
            return {"error": "Bad request"}, 400
        
    for user in users:
        if user["email"] == request.json['email']:
            return {"error": "User already exists"}, 400
            
    new_user = {
        "email": request.json['email'],
        "name": request.json['name'],
        "password": request.json['password']
    }  

    users.append(new_user)
    return new_user, 201  
