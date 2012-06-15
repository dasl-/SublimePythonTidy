import sublime
import sublime_plugin
import PythonTidy
import re
import StringIO

s = sublime.load_settings('PythonTidy.sublime-settings')


class SublimePythonTidyCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        selection = []
        nwsOffset = self.prev_non_whitespace()

        # do formatting and replacement

        replaceRegion = None
        formatSelection = False
        replaceRegion = sublime.Region(0, self.view.size())

        file_in = StringIO.StringIO()
        file_in.write(self.view.substr(replaceRegion))
        file_in.seek(0)
        file_out = StringIO.StringIO()

        PythonTidy.tidy_up(file_in, file_out)

        file_out.seek(0)
        res = file_out.read()

        self.view.replace(edit, replaceRegion, res)

        # re-place cursor

        offset = self.get_nws_offset(nwsOffset,
                self.view.substr(sublime.Region(0, self.view.size())))
        rc = self.view.rowcol(offset)
        pt = self.view.text_point(rc[0], rc[1])
        sel = self.view.sel()
        sel.clear()
        self.view.sel().add(sublime.Region(pt))

        self.view.show_at_center(pt)

    def prev_non_whitespace(self):
        pos = self.view.sel()[0].a
        preTxt = self.view.substr(sublime.Region(0, pos))
        return len(re.findall('\S', preTxt))

    def get_nws_offset(self, nonWsChars, buff):
        nonWsSeen = 0
        offset = 0
        for i in range(0, len(buff)):
            offset += 1
            if not buff[i].isspace():
                nonWsSeen += 1

            if nonWsSeen == nonWsChars:
                break

        return offset


