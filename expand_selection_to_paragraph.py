import sublime
import sublime_plugin

class ExpandSelectionToParagraphCommand(sublime_plugin.TextCommand):
    view = None

    def run(self, edit):
        window = sublime.active_window()
        self.view = window.active_view() if window else None
        region = self.__get_current_paragraph_region()
        self.view.sel().clear()
        self.view.sel().add(region)

    def __get_current_paragraph_region(self):
        text = self.view.substr(sublime.Region(0, self.view.size()))

        if self.view.sel():
            region = self.view.sel()[0]
            start = text.rfind('\n\n', 0, region.a + 1)
            end = text.find('\n\n', region.a, len(text)) + 1

        start = 0 if start < 0 else start + 2
        end = len(text) if end <= 0 else end

        return sublime.Region(start, end)
