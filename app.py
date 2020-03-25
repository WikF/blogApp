from database.database import Database
from models.blog import Blog

__author__ = "wiktor"

Database.initialize()

blog = Blog(author = "ka",
            title = "O mnie",
            description = "tea",
            id = "a")

blog.new_post()

blog.save_to_mongo()

from_database = Blog.from_mongo(blog.id)

print(blog.get_posts())