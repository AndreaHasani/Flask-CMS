from flask_restful import reqparse


# Main Parser
post_mainParser = reqparse.RequestParser()
post_mainParser.add_argument('id', type=int, help='id for posts')

post_crUpParser = post_mainParser.copy()
post_crUpParser.add_argument('title', type=str,
                             help='Post Title', required=True,
                             case_sensitive=False)
post_crUpParser.add_argument('content', type=str,
                             help='Post Content', required=True,
                             case_sensitive=False)
post_crUpParser.add_argument('author', type=str,
                             help='Content Author', required=True,
                             case_sensitive=False)
