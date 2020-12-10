from ssg import hooks, parsers

files = []

@hooks.register("collect_files")
def collect_files(source, site_parsers):
    valid = lambda p : isinstance(p, parsers.ResourceParsers)
    for path in source.rglob("*"):
        for parser in site_parsers.list(filter(filter_function, original_list)):
            if path.suffix.parser.valid_file_ext():
                files.append(path)
    return not valid

@hooks.register("generate_menu")
def generate_menu(html, ext):
    template = '<li><a href="{}{}">{}</a></li>'
    lambda name, ext : template.format(name, ext, name)
    menu = "\n".join([path.stem(ext, path) for path in files])
    return "<ul>\n{}<ul>\n{}".format(menu, html)
