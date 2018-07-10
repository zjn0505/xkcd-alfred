# encoding: utf-8

import sys
from workflow import Workflow, ICON_WEB, web

query = ""

def get_suggestions():
    global query
    if query == None or query == "":
        url = 'https://api.jienan.xyz/xkcd/xkcd-top?sortby=thumb-up'
    else:
        url = 'https://api.jienan.xyz/xkcd/xkcd-suggest?q=' + query
    params = dict(count=20, format='json')
    r = web.get(url, params)

    # throw an error if request failed
    # Workflow will catch this and show it to the user
    r.raise_for_status()

    # Parse the JSON returned by pinboard and extract the posts
    return r.json()

def main(wf):
    global query

    if len(wf.args):
        query = wf.args[0]
    else:
        query = None
    # Retrieve posts from cache if available and no more than 3600
    # seconds old

    posts = wf.cached_data('comics-'+query, get_suggestions, 3600)
    
    # Loop through the returned posts and add an item for each to
    # the list of results for Alfred
    for post in posts:
        wf.add_item(title=("%d - %s" % (post['num'], post['title'])),
                subtitle=post['alt'],
                arg="https://xkcd.com/%d" % post['num'],
                valid=True,
                quicklookurl=post['img'],
                icon=ICON_WEB)

    # Send the results to Alfred as XML
    wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
