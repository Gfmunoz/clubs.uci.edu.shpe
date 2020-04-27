from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from app.extensions import db, FBUser


def get_all_users() -> [dict]:
    users_dict = db.child('users').get().val()
    users = []

    for uid in users_dict:
        user_info = users_dict[uid]
        fb_user = FBUser(uid, user_info)
        user_dict = fb_user.get_dict()
        users.append(user_dict)
        # users.append(fb_user)

    return users

def get_user(username: str) -> FBUser:
	users_dict = db.child('users').get().val()
	fb_user = None
	for uid in users_dict:
		if (users_dict[uid]['email'] == username+"@uci.edu"):

			user_info = users_dict[uid]
			fb_user = FBUser(uid, user_info)
	print(type(fb_user))
	return fb_user





