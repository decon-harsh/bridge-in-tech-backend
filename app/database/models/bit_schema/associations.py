from app.database.sqlalchemy_extension import db
from sqlalchemy.exc import IntegrityError

class MembersAssocaitionModel(db.Model):
    __tablename__ = "member_model"
    __table_args__ = {"schema": "bitschema", "extend_existing": True}

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('public.users.id'))
    organization_id = db.Column(db.Integer,db.ForeignKey('bitschema.organizations.id'))

    
    def __init__(self, user_id, organization_id):
        """Initialises OrganizationModel class."""
        ## required fields

        self.user_id = user_id
        self.organization_id = organization_id

    def __repr__(self):
        """Returns the organization."""
        return (
            f"Association id : {self.id}\n"
            f"User Id : {self.user_id}\n"
            f"Organization Id : {self.organization_id}\n"
        )

    def save_to_db(self) -> None:
        """Adds an organization to the database. """
        try:
            db.session.add(self)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return "Session Rollbacked"

    def delete_from_db(self) -> None:
        """Deletes an organization from the database. """
        db.session.delete(self)
        db.session.commit()
