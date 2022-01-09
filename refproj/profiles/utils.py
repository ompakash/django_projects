import uuid

def generate_ref_code():
    code = str(uuid.uuid4()).replace("-", "new")[:12]
    return code