import urwid

def show_or_exit(key):
    if key in ('q', 'Q', 'esc'):
		#Exit loop better than SIGint
        raise urwid.ExitMainLoop()
	#For printing var
    txt.set_text(repr(key))


txt = urwid.Text(u"Hello World")
fill = urwid.Filler(txt, 'bottom')
loop = urwid.MainLoop(fill, unhandled_input=show_or_exit)
loop.run()