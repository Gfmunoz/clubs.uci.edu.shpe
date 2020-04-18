from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from app.extensions import db, FBUser


def get_all_users() -> [FBUser]:
    users_dict = db.child('users').get().val()
    users = []

    for uid in users_dict:
        user_info = users_dict[uid]
        fb_user = FBUser(uid, user_info)
        users.append(fb_user)

    return users




