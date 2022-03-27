from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import database, schemas, oauth2, models

router = APIRouter(prefix="/vote", tags=["Vote"])


@router.post("/{post_id}")
def vote(
    post_id: int,
    db: Session = Depends(database.get_db),
    current_user: dict = Depends(oauth2.get_current_user),
):
    # if post doesn't exist
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )

    # if post already exists
    vote = (
        db.query(models.Vote)
        .filter(models.Vote.post_id == post_id, models.Vote.user_id == current_user.id)
        .first()
    )
    if vote:
        raise HTTPException(
            status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
            detail="User voted on post already",
        )

    new_vote = models.Vote(post_id=post_id, user_id=current_user.id)
    db.add(new_vote)
    db.commit()
    return {"message": f"Post {post_id} upvoted by user {current_user.id}"}
