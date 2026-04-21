from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response
from fastapi import status
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.core.db import get_db
from backend.modules.projects.models import Project
from backend.modules.projects.schemas import ProjectCreate
from backend.modules.projects.schemas import ProjectRead
from backend.modules.projects.schemas import ProjectUpdate
from backend.modules.users.models import User


router = APIRouter(prefix="/users/{user_id}/projects", tags=["projects"])


DbSession = Annotated[Session, Depends(get_db)]


@router.post("/", response_model=ProjectRead, status_code=status.HTTP_201_CREATED)
def create_project(user_id: int, payload: ProjectCreate, db: DbSession) -> Project:
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found."
        )

    project = Project(
        name=payload.name,
        description=payload.description,
        user_id=user_id,
    )
    
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


@router.get("/", response_model=list[ProjectRead])
def list_projects(user_id: int, db: DbSession) -> list[Project]:
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found."
        )

    statement = select(Project).where(Project.user_id == user_id).order_by(Project.id)
    return list(db.scalars(statement).all())


@router.get("/{project_id}", response_model=ProjectRead)
def get_project(user_id: int, project_id: int, db: DbSession) -> Project:
    project = db.scalar(
        select(Project).where(Project.id == project_id, Project.user_id == user_id)
    )
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Project not found."
        )
    return project


@router.patch("/{project_id}", response_model=ProjectRead)
def update_project(
    user_id: int, project_id: int, payload: ProjectUpdate, db: DbSession
) -> Project:
    project = db.scalar(
        select(Project).where(Project.id == project_id, Project.user_id == user_id)
    )
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Project not found."
        )

    updates = payload.model_dump(exclude_unset=True)

    if "name" in updates:
        project.name = updates["name"]
    if "description" in updates:
        project.description = updates["description"]

    db.commit()
    db.refresh(project)
    return project


@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(user_id: int, project_id: int, db: DbSession) -> Response:
    project = db.scalar(
        select(Project).where(Project.id == project_id, Project.user_id == user_id)
    )
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Project not found."
        )

    db.delete(project)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
