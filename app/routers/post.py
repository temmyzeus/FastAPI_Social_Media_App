from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas, oauth2
from ..database import get_db

router = APIRouter(prefix="/post", tags=["User"])


@router.get("/", response_model=list[schemas.GetPostResponse])
def get_posts(db: Session = Depends(get_db)):
    """Get a post with specified ID from DataBase"""
    posts = db.query(models.Post).all()
    return posts


@router.get("/{id}", response_model=schemas.GetPostResponse)
def get_post(id: int, db: Session = Depends(get_db)):
    """Get all Posts from DataBase"""
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if post:
        return post
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post ID: {id} not found in database!",
        )


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=schemas.CreatePostResponse
)
def create_post(
    post: schemas.Post,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    """Create post"""
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.put("/{id}", status_code=status.HTTP_201_CREATED)
def update_post(
    id: int,
    post: schemas.UpdatePost,
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user),
):
    """Update Post in DataBase"""
    post_update_query = db.query(models.Post).filter(models.Post.id == id)
    post_to_be_updated = post_update_query.first()

    merged_post_with_changes = {
        key: (value if (value is not None) else post_to_be_updated.__dict__[key])
        for key, value in post.dict().items()
    }

    if post_to_be_updated:
        post_update_query.update(merged_post_with_changes, synchronize_session=False)
        db.commit()
        return merged_post_with_changes
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Post {id} not found!"
        )


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(
    id: int,
    db: Session = Depends(get_db),
    current_user=Depends(oauth2.get_current_user),
):
    """Delete Post from DataBase"""
    post_deletion_query = db.query(models.Post).filter(models.Post.id == id)

    if post_deletion_query.first():
        post_deletion_query.delete(synchronize_session=False)
        db.commit()
        return {"detail": f"Post {id} deleted from DataBase!"}
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post {id} not found in database",
        )
