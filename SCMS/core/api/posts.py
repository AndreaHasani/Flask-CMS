from flask_restful import Resource
from SCMS.core.api.parser import post_mainParser, post_crUpParser
from SCMS.core.users.util import login_required
from SCMS import db
from SCMS.core.models import Posts, Users
from datetime import datetime
from flask_login import current_user


class edit(Resource):
    def post(self):
        args = post_crUpParser.parse_args()

        post = Posts(title=args['title'], content=args['content'],
                     date_posted=datetime.utcnow, user_id=1)
        db.session.add(post)
        db.session.commit()

        return {'id': args['id'], 'title': args['title']}

    def delete(self):
        args = post_mainParser.parse_args()
        Posts.query.filter_by(id=args['id']).delete()
        db.session.commit()
        return {'status': 'succesful', 'id': args['id'],
                'message': "Post %s deleted" % args['id']}

    def put(self):
        post_crUpParser.replace_argument('title', required=False)
        post_crUpParser.replace_argument('content', required=False)
        post_crUpParser.remove_argument('author')
        args = post_crUpParser.parse_args()
        # Posts.query.filter_by(id=args['id']).delete()
        # db.session.commit()
        return {'status': 'succesful'}

