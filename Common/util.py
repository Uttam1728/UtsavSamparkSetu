def is_member(user,groupName):
    return user.groups.filter(name=groupName).exists()