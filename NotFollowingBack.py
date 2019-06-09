from InstagramAPI import InstagramAPI

def getTotalFollowers(api, user_id):
    """
    Returns the list of followers of the user.
    It should be equivalent of calling api.getTotalFollowers from InstagramAPI
    """

    followers = []
    next_max_id = True
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''

        _ = api.getUserFollowers(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return followers


if __name__ == "__main__":
    
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    api = InstagramAPI(username, password) 
    api.login()
    while hasattr(api, "username_id") == False:
        print ("Sorry you entered something wrong")
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        api = InstagramAPI(username, password) 
        api.login()
    user_id = api.username_id

    followers = api.getTotalFollowers(user_id)

    followings = api.getTotalFollowings(user_id)

    follower_username = []
    following_username = []
    for follower in followers:
        follower_username.append(follower["username"])
    for following in followings:
        following_username.append(following["username"])
     
    for following in following_username:
        if following not in follower_username:
            print (following)


