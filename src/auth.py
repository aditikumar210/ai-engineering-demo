
def is_valid_token(token):
    if token == "valid-token":
        return True

    return False


def get_user_role(token):
    if is_valid_token(token):
        return "user"

    return None
