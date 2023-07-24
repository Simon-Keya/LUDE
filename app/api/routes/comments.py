from fastapi import APIRouter

router = APIRouter(tags=['comments']
)


@router.get("/")
def get_comments():
    # Implementation for getting all comments
    return "Get all comments"


@router.post("/")
def create_comment():
    # Implementation for creating a new comment
    return "Create a new comment"


@router.get("/{comment_id}")
def get_comment(comment_id: int):
    # Implementation for getting a specific comment by ID
    return f"Get comment with ID: {comment_id}"


@router.put("/{comment_id}")
def update_comment(comment_id: int):
    # Implementation for updating a comment by ID
    return f"Update comment with ID: {comment_id}"


@router.delete("/{comment_id}")
def delete_comment(comment_id: int):
    # Implementation for deleting a comment by ID
    return f"Delete comment with ID: {comment_id}"
