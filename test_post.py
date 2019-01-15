import mlab
from models.user import User
from models.post import Post

mlab.connect()

# khanh = User.objects(username="doanhtuan").first()
# if khanh is None:
#     print("User not found")
# else:
#     new_post = Post(title="bai viet so 3 cua tuan",
#                     content="tuan day ",
#                     owner=khanh)
# new_post.save()
# print("done saving")

# Post => Owner
# for post in Post.objects():
#     print(post.title,"by",post.owner.username)
    
# OWner => Posts
user = User.objects(username = "admin").first()
posts = Post.objects(owner=user)
for post in posts:
    print(post.title)