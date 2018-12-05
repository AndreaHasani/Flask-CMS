from faker import Faker
from random import choice

fake = Faker()


def fakePosts(db, Posts):
    for i in range(50):
        title = fake.sentence(
            nb_words=9, variable_nb_words=True, ext_word_list=None)
        content = "<p>{}</p><p>{}</p>".format(''.join(fake.paragraphs(nb=2, ext_word_list=None)),
                                              ''.join(fake.paragraphs(nb=2, ext_word_list=None)))
        excerpt = ''.join(fake.paragraphs(nb=2, ext_word_list=None))
        date_posted = fake.date_time().strftime("%Y-%m-%d %H:%M:%S")
        user_id = 1
        status = choice(
            ['published', 'draft', 'future', 'pending', 'private', 'trash'])
        post = Posts(title=title, content=content,
                     date_posted=date_posted, user_id=user_id,
                     excerpt=excerpt, status=status
                     )
        db.session.add(post)
        db.session.commit()
