

import sublime
import sublime_plugin

import unittest
import textwrap


class OverrideCommitCompletionUnitTests(unittest.TestCase, sublime_plugin.EventListener):
    is_running_unit_tests = False

    @classmethod
    def setUp(self):
        self.maxDiff = None

        # Create a new Sublime Text view to perform the Unit Tests
        self.view = sublime.active_window().new_file()
        self.view.set_syntax_file( "Packages/Text/Plain text.tmLanguage" )

        # make sure we have a window to work with
        self.view.settings().set("close_windows_when_empty", False)

    def tearDown(self):

        if self.view:
            self.view.set_scratch(True)
            self.view.window().focus_view(self.view)
            self.view.window().run_command("close_file")

    def setText(self, text, start_point=0):
        self.view.run_command("append", {"characters": text })

        selections = self.view.sel()
        selections.clear()
        selections.add( sublime.Region( start_point, start_point ) )

        self.view.window().focus_view( self.view )
        self.view.run_command( 'remove_non_ascii_chars_file' )

    def assertEqual(self, expected, *args, **kargs):
        super().assertEqual(expected, self.view.substr( sublime.Region( 0, self.view.size() ) ), *args, **kargs)

    def test_characters_slicing(self):
        self.view.settings().set("file_size_limit", 3)
        self.setText( "1  2  3  4  5  6  7  " )
        self.assertEqual( "1  2  3  4  5  6  7  " )

    def test_accentuation_removal(self):
        self.setText( "á à â ä ñ" )
        self.assertEqual( "a a a a n" )

    def test_alpha_removal(self):
        self.setText( "¡ ¿ ß" )
        self.assertEqual( "  " )

