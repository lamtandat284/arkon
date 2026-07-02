content = open('/app/app/services/wiki_service.py', 'r').read()
content = content.replace(
    '''        page = WikiPage(
            slug=INDEX_SLUG,
            title="Wiki Index",
            page_type="index",
            content_md=new_md,''',
    '''        page = WikiPage(
            slug=INDEX_SLUG,
            title="Wiki Index",
            content_md=new_md,'''
)
open('/app/app/services/wiki_service.py', 'w').write(content)
print('Done')
