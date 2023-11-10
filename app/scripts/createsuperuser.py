import argparse
import questionary

from app.db.session import SessionLocal
from app.crud.admin import crud_user
from app.schemas.admin import AdminCreate
from app.utils import get_hashed_password
from app.models.admin import UserTypeEnum


def create_superuser(name: str, email: str, password: str):
    db = SessionLocal()
    user = crud_user.get_user_by_email(db, email=email)

    if not user:
        user_in = AdminCreate(
            name=name,
            email=email,
            password=get_hashed_password(password),
            is_superuser=True,
            role=UserTypeEnum.superadmin
        )

        crud_user.create(db, obj_in=user_in)
        print("Superuser created successfully.")
    else:
        print("Superuser with this email already exists.")


def get_user_input():
    name = questionary.text("Enter name (Login) for the superuser: ").ask()
    email = questionary.text("Enter email address for the superuser: ").ask()
    password = questionary.password("Enter password for the superuser: ").ask()
    confirm_password = questionary.password("Enter confirm password for the superuser: ").ask()
    if password == confirm_password:
        return name, email, password
    else:
        raise ValueError("Passwords do not match. Please enter matching passwords.")


def main():
    parser = argparse.ArgumentParser(description='Create a superuser.')
    parser.add_argument('name', nargs='?', type=str, help='Name(Login) for the superuser')
    parser.add_argument('email', nargs='?', type=str, help='Email address for the superuser')
    parser.add_argument('password', nargs='?', type=str, help='Password for the superuser')
    parser.add_argument('confirm password', nargs='?', type=str, help='Confirm password for the superuser')

    args = parser.parse_args()

    if not all([args.name, args.email, args.password]):
        name, email, password = get_user_input()
    else:
        name, email, password = args.name, args.email, args.password

    create_superuser(name, email, password)


if __name__ == "__main__":
    main()
