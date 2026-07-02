content = open('/app/app/services/wiki_service.py', 'r').read()
content = content.replace(
    '            page_type="log",\n            content_md=f"# Wiki Log',
    '            content_md=f"# Wiki Log'
).replace(
    'slug=slug, title=title, page_type=page_type,\n            content_md=final_content',
    'slug=slug, title=title,\n            content_md=final_content'
)
open('/app/app/services/wiki_service.py', 'w').write(content)
print('Done')
