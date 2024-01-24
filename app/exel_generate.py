"""This module contains functions for generating exel reports."""

import os

from openpyxl.workbook import Workbook

from app.crud.user import crud_user


def generate_exel_report(db):
    """Generate exel report."""
    wb = Workbook()
    ws = wb.active

    headers = [
        'User ID',
        'Name',
        'Surname',
        'Phone',
        'Email',
        'Role',
        'Message',
        'Message Create',
    ]
    ws.append(headers)

    users = crud_user.get_multi(db)
    for user in users:
        for message in user.messages:
            created_at_local = message.created_at.replace(tzinfo=None)
            row_data = [
                user.id,
                user.name,
                user.surname,
                user.phone,
                user.email,
                user.role.value,
                message.msg,
                created_at_local,
            ]
            ws.append(row_data)

    folder_path = 'user_exel_report'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    filename = 'report.xlsx'
    file_path = os.path.join(folder_path, filename)
    wb.save(file_path)

    return file_path
