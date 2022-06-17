import models, schemas, utils, oauth2
from fastapi import FastAPI ,Response ,status ,HTTPException, Depends ,APIRouter
from sqlalchemy import func
from sqlalchemy.orm import Session
from database import engine, get_db
import psycopg2
from psycopg2.extras import RealDictCursor
from typing import Optional, List

router = APIRouter(prefix="/posts",tags=['Posts'])




@router.get("/",response_model=List[schemas.PostOut])
def posts(db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    #cursor.execute("""SELECT * FROM products """)
    #post = cursor.fetchall()
    #To behave like job portal application ,we can retrieve only specific id posts
    #posts = db.query(models.Pomst).filter(models.Pomst.owner_id == user_id.id).all()
    #posts = db.query(models.Pomst).all()
    #To limit posts w.r.t number , to skip posts used in pagination i.e page 3 == skip first 40 ,
    #posts = db.query(models.Pomst).filter(models.Pomst.title.contains(search)).limit(limit).offset(skip).all()
    results = db.query(models.Pomst, func.count(models.Votes.post_id).label("votes")).join(models.Votes, models.Votes.post_id == models.Pomst.id, isouter=True).group_by(models.Pomst.id).filter(models.Pomst.title.contains(search)).limit(limit).offset(skip).all()
    return results

#Taking data from body converting it into dictionary and saving it in payload
#Body -> dict type -> payload(variable)

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_posts(post:schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):


    new_post = models.Pomst(owner_id= current_user.id, **post.dict())
    #add -> add to database
    db.add(new_post)
    #commit to database
    db.commit()
    #retrieve new post just like returning in sql and storing back to new_post
    db.refresh(new_post)

    return new_post

# I want my title and content to be in the form of only string so applying validation
#hi in this case is a pydantic dict

@router.post("/createposts_with_pydantic",status_code=status.HTTP_201_CREATED)
def createposts(hi: schemas.PostCreate):
    #this sql query is not prone to sql injections
    cursor.execute("""INSERT INTO socialm(title,content,published) VALUES(%s,%s,%s) RETURNING *""",
                   (hi.title,hi.content,hi.published))
    new_posts = cursor.fetchone()
    conn.commit()
    return {"message":new_posts}

@router.get("/{id}",response_model=schemas.PostOut)
def get_post(id: int,db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    #cursor.execute(""" SELECT * FROM socialm WHERE "id " = %s """,(str(id)))
    #post = cursor.fetchone()
    #post = db.query(models.Pomst).filter(models.Pomst.id == id).first()
    post = db.query(models.Pomst, func.count(models.Votes.post_id).label("votes")).join(models.Votes,
                                                                                           models.Votes.post_id == models.Pomst.id,
                                                                                           isouter=True).group_by(
        models.Pomst.id).filter(models.Pomst.id == id).first()
    print(current_user.email)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id : {id} was not found")

    return post

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    #cursor.execute(""" DELETE FROM socialm WHERE "id " = %s returning *""",(str(id)))
    #deleted_post = cursor.fetchone()
    #deleting post
    #find the index in array that has required ID
    # my_posts.pop(index)
    #conn.commit()
    post = db.query(models.Pomst).filter(models.Pomst.id == id)

    check_for_owner = post.first()


    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with {id} is not found")
    #No response for delete function

    if check_for_owner.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not allowed to commit requested action")

    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}",response_model=schemas.Post)
def update_post(id: int,updated_post: schemas.PostCreate,db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    #cursor.execute(""" UPDATE socialm SET title = %s , content = %s , published = %s WHERE "id "= %s RETURNING *""",(post.title,post.content
                                                                                                     #,post.published,str(id)))
    #update_post = cursor.fetchone()

    #conn.commit()

    post_query = db.query(models.Pomst).filter(models.Pomst.id == id)

    post = post_query.first()




    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with {id} is not found")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not allowed to commit requested action")

    post_query.update(updated_post.dict(),synchronize_session=False)
    # commit to database
    db.commit()
    return post