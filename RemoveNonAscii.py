import sublime
import sublime_plugin

# https://stackoverflow.com/questions/4324790/removing-control-characters-from-a-string-in-python
from unicodedata import category

VIEW_SIZE_LIMIT = 4194304


def remove_control(view, view_region, edit, file_size_limit):
    walked_size = 0
    region_size = view_region.b - view_region.a
    # print('view_region.a', view_region.a, 'view_region.b', view_region.b)

    while region_size > 0:
        region_size -= file_size_limit
        if region_size < 0: region_size = 0

        _remove_control( view, sublime.Region( view_region.a + region_size, view_region.b - walked_size ), edit )
        walked_size += file_size_limit


def _remove_control(view, view_region, edit):
    view_text = view.substr(view_region)
    # print('view_text', view_text, 'view_region.a', view_region.a, 'view_region.b', view_region.b)

    ascii_only = "".join(character for character in view_text if category( character )[0] != "C" or character == '\n' )
    view.replace(edit, view_region, ascii_only)


class RemoveNonAsciiCharsFileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file_size_limit = self.view.settings().get( 'file_size_limit', VIEW_SIZE_LIMIT )
        view_region = sublime.Region(0, self.view.size())
        remove_control(self.view, view_region, edit, file_size_limit)


class RemoveNonAsciiCharsSelecCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file_size_limit = self.view.settings().get( 'file_size_limit', VIEW_SIZE_LIMIT )

        sel_view = self.view.sel()
        for view_region in sel_view:
            if not view_region.empty():
                # Get the selected text
                remove_control(self.view, view_region, edit, file_size_limit)

