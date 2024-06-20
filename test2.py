from html_to_json import convert 
from pprint import pprint


html_string = """
                <html lang="en" prop>
                    <head>
                        <title>DOC</title>
                    </head>
                    <body>
                        <div>
                            <h1>ok1</h1>
                        </div>
                        <div>
                            <h2>ok2</h2>
                        </div>
                        <div>
                            <h3>ok3</h3>
                        </div>
                        <div>
                            <h4>ok4</h4>
                        </div>
                        <main>nothing</main>
                        <img src="" alt="">
                    </body>
                </html>
              """


output_json = convert(html_string)

pprint(output_json)


output = {'html': [{'_attributes': {'lang': 'en'},
            'body': [{'div': [{'h1': [{'_value': 'ok1'}]},
                             {'h2': [{'_value': 'ok2'}]},
                             {'h3': [{'_value': 'ok3'}]},
                             {'h4': [{'_value': 'ok4'}]}],
                     'img': [{'_attributes': {'alt': '', 'src': ''}}],
                     'main': [{'_value': 'nothing'}]}],
           'head': [{'title': [{'_value': 'DOC'}]}]}]
        }

output = {'html': [{'_attributes': {'lang': 'en', 'prop': ''},
           'body': [{'div': [{'h1': [{'_value': 'ok1'}]},
                             {'h2': [{'_value': 'ok2'}]},
                             {'h3': [{'_value': 'ok3'}]},
                             {'h4': [{'_value': 'ok4'}]}],
                     'img': [{'_attributes': {'alt': '', 'src': ''}}],
                     'main': [{'_value': 'nothing'}]}],
           'head': [{'title': [{'_value': 'DOC'}]}]}]}