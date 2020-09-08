def setup(app):
    import os.path
    theme_path = os.path.join(os.path.dirname(__file__), 'themes')
    app.add_html_theme('yeen', os.path.join(theme_path, 'yeen'))
