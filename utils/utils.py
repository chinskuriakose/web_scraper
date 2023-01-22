from itertools import cycle


class YamlCleanup:
    def __init__(self, html):
        self.split_char_cycle = cycle(["<a", ">", "</a>"])
        self.props = []
        self.html = html
        self.get_yaml_elements()

    def get_cleaned_html(self):
        while True:
            start = self.html.find("<code ")
            end = self.html.find("</code>")
            if start != -1:
                self.html = self.html[:start + 1] + self.html[end + 7:]
            else:
                break

    def split_props(self):
        for split_char in self.split_char_cycle:
            if len(self.html.split(split_char)) > 1:
                if split_char == "</a>":
                    self.props.append(self.html.split(split_char)[0].strip())
                self.html = self.html.split(split_char, 1)[1]
            else:
                break

    def get_yaml_elements(self):
        self.html = self.html.split("\n", 2)[2]
        self.get_cleaned_html()
        self.split_props()

    def get_props(self):
        return self.props
