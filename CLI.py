import curses

options = ["Vietnamese (vi)", "Russian (ru)", "English (en)", "Other", "Exit"]

def menu(stdscr, options):
    curses.curs_set(0)  # Ẩn con trỏ
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Màu nổi bật

    stdscr.clear()
    selected = 0
    title = "Choose a language to transcribe:"

    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()

        stdscr.addstr(2, w // 2 - len(title) // 2, title, curses.A_BOLD)

        for i, option in enumerate(options):
            x = w // 2 - len(option) // 2
            y = h // 2 - len(options) // 2 + i

            if i == selected:
                stdscr.attron(curses.color_pair(1))  # Làm nổi bật dòng được chọn
                stdscr.addstr(y, x, option)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, option)

        key = stdscr.getch()

        if (key == curses.KEY_UP or key == curses.KEY_LEFT):
            if selected > 0:
                selected -= 1
            else:
                selected = len(options) - 1
        elif (key == curses.KEY_DOWN or key == curses.KEY_RIGHT or key == curses.KEY_BACKSPACE):
            if selected < len(options) - 1:
                selected += 1
            else: 
                selected = 0
        elif key == ord("\n"):  # Nhấn Enter để chọn
            return options[selected]

def select_language(stdscr):
    if menu(stdscr, options) == "Russian (ru)":
        return "ru"
    elif menu(stdscr, options) == "Vietnamese (vi)":
        return "vi"
    elif menu(stdscr, options) == "English (en)":
        return "en"
    elif menu(stdscr, options) == "Other":
        return "Other"
    elif menu(stdscr, options) == "Exit":
        return "Exit"

def thunghiem():
    curses.wrapper(lambda stdscr: print(f"Bạn đã chọn: {menu(stdscr, options)}"))

if __name__ == "__main__":
    thunghiem()
