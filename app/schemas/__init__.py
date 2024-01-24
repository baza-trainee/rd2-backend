"""Package containing schemas for various data structures."""
from .admin import AdminCreate, AdminLogin, AdminUpdate, BaseAdmin, ChangePassword, ForgotPassword, ResetPassword
from .contact import ContactBase, ContactEmail, ContactPhone, EmailCreate, PhoneCreate, UpdateContact
from .logos import BaseLogo, LogoList, LogoUpload
from .message import ResponseMessage
from .reports import BaseFile, ReportDetail, ReportResponse
from .token import RefreshToken, Token
from .user import BaseUser, CreateUser, ListUser, MessageSchema
