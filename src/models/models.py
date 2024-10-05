from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from src.utils.DB.database import Base

class Users(Base):
   __tablename__ = "users"

   id = Column(Integer, autoincrement=True, primary_key=True)
   email = Column(String(length=30), nullable= False, unique=True)
   password = Column(String(length=255), nullable=False)
   nickname = Column(String(length=10), nullable=False, unique=True)
   isOpen = Column(Boolean, default=True)
   image = Column(String(length=255), nullable=True)
   createdAt = Column(DateTime, default= datetime.now)
   updatedAt = Column(DateTime, default= datetime.now, onupdate=datetime.now)
   deletedAt = Column(DateTime, nullable= True)

   roles = relationship("Roles", back_populates="users", cascade="all, delete")

class Roles(Base):
   __tablename__ = "roles"

   id = Column(Integer, autoincrement=True, primary_key=True)
   role = Column(Enum("admin", "user", "guest"), default= "user")
   createdAt = Column(DateTime, default= datetime.now)
   updatedAt = Column(DateTime, default=datetime.now, onupdate=datetime.now)
   deletedAt = Column(DateTime, nullable= True)
   userId = Column(Integer, ForeignKey("users.id"), name="userId")

   users = relationship("Users", back_populates="roles")
   
class Posts(Base):
   __tablename__ = "posts"
   id = Column(Integer, autoincrement=True, primary_key=True)
   title = Column(String(length=15), nullable=False)
   context = Column(String(length=255), nullable=True)
   category = Column(Enum("music", "today", "blog"))
   isOpen = Column(Boolean, default=True)
   image = Column(String(length=255), default=None)
   createdAt = Column(DateTime, default=datetime.now)
   updatedAt = Column(DateTime, default=datetime.now, onupdate=datetime.now)
   deletedAt = Column(DateTime, nullable= True)