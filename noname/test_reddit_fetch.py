from copy import copy
import unittest
import noname

post = {
    u'approved_by': None,
    u'author': u'rya11111',
    u'author_flair_css_class': None,
    u'author_flair_text': None,
    u'banned_by': None,
    u'clicked': False,
    u'created': 1387782629.0,
    u'created_utc': 1387782629.0,
    u'distinguished': None,
    u'domain': u'reddit.com',
    u'downs': 0,
    u'edited': False,
    u'gilded': 0,
    u'hidden': False,
    u'id': u'1tilfi',
    u'is_self': False,
    u'likes': None,
    u'link_flair_css_class': None,
    u'link_flair_text': None,
    u'media': None,
    u'media_embed': {},
    u'name': u't3_1tilfi',
    u'num_comments': 27,
    u'num_reports': None,
    u'over_18': False,
    u'permalink': u'/r/Python/comments/1tilfi/congratulations_rpython_you_are_the_subreddit_of/',
    u'saved': False,
    u'score': 793,
    u'secure_media': None,
    u'secure_media_embed': {},
    u'selftext': u'',
    u'selftext_html': None,
    u'stickied': False,
    u'subreddit': u'Python',
    u'subreddit_id': u't5_2qh0y',
    u'thumbnail': u'',
    u'title': u'Congratulations r/Python! You are the SUBREDDIT OF THE DAY!',
    u'ups': 793,
    u'url': u'http://www.reddit.com/r/subredditoftheday/comments/1tiler/december_23rd_2013_rpython_dont_worry_it_wont/',
    u'visited': False
}


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.post = copy(post)
        self.parsed_post = noname.parse_post(self.post)

    def test_url_post(self):
        assert 'type' in self.parsed_post
        assert self.parsed_post['type'] == 'url'

if __name__ == '__main__':
    unittest.main()
