from jinja2 import Template

template_src = ''
with open('template.html') as f:
	template_src = f.read()

# print(template_src)

template = Template(template_src)

properties = [
			  {'title': 'A house',
			   'address': 'A lovely address',
			   'description': 'This is a lovely house',
			   'price': 'A lot.',
			   'images': ['title1.jpg', 'title2.jpg']
				},

			   {'title': 'Another house',
			   'address': 'Somewhere in dublin',
			   'description': 'Buy me',
			   'price': '100,000',
			   'images': ['title1.jpg', 'title2.jpg']
			   }
			  ]

html = template.render(properties=properties)

print(html)

# http://jinja.pocoo.org/docs/2.9/intro/