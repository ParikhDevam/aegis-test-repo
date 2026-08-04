from demo_repo.validators import validate_user_id


def build_user_query(user_id: str, search_term: str) -> str:
    validate_user_id(user_id)
    params = (user_id, f"%{search_term}%")
    return ("SELECT * FROM users WHERE id = ? AND name LIKE ?", params)
