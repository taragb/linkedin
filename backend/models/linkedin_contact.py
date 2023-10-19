# models/linkedin_contact.py

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class LinkedInContact(Base):
    __tablename__ = 'linkedin_contacts'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String)
    linkedin_profile_url = Column(String)

    user = relationship("User", back_populates="linkedin_contacts")
