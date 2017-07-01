from userinterface import UI, OptionsPage


class Options:

    current_puzzle_out = ""
    puzzles_out = ""
    @staticmethod
    def show(current_puzzle, puzzles, option_page=OptionsPage.HOME):
        UI.display_options(option_page, current_puzzle, puzzles)
        input_value = input()

        # Home Page
        if option_page == OptionsPage.HOME:
            if input_value == "1":
                Options.show(current_puzzle, puzzles, OptionsPage.PUZZLE_SELECT)
            elif input_value == "2":
                Options.show(current_puzzle, puzzles, OptionsPage.PUZZLE_OPTIONS)
            elif input_value == "3":
                Options.show(current_puzzle, puzzles, OptionsPage.GENERAL_OPTIONS)
            elif input_value == "0":
                Options.current_puzzle_out = current_puzzle
                Options.puzzles_out = puzzles
                return
            else:
                UI.display_error(0x0000001)
                input()
                Options.show(current_puzzle, puzzles, option_page)

        # Puzzle Select
        elif option_page == OptionsPage.PUZZLE_SELECT:
            try:
                if int(input_value) <= len(puzzles):
                    current_puzzle = puzzles[int(input_value) - 1]
                    Options.show(current_puzzle, puzzles, OptionsPage.HOME)
                else:
                    UI.display_error(0x000003)
                    input()
                    Options.show(current_puzzle, puzzles, option_page)
            except ValueError:
                UI.display_error(0x000002)
                input()
                Options.show(current_puzzle, puzzles, option_page)

        # Puzzle Options
        elif option_page == OptionsPage.PUZZLE_OPTIONS:
            if input_value == "1":
                # statistics related to the current session
                current_puzzle.session_solves = 0
                current_puzzle.session_best = 9999
                current_puzzle.session_average_of_three = 0
                current_puzzle.session_best_of_five = 0
                current_puzzle.session_best_of_twelve = 0
                current_puzzle.session_best_of_hundred = 0

                # statistics related to the overall performance
                current_puzzle.overall_solves = []
                current_puzzle.overall_best = 9999
                current_puzzle.overall_average_of_three = 0
                current_puzzle.overall_best_of_five = 0
                current_puzzle.overall_best_of_twelve = 0
                current_puzzle.overall_best_of_hundred = 0

                Options.show(current_puzzle, puzzles, OptionsPage.HOME)
            elif input_value == "0":
                Options.show(current_puzzle, puzzles, OptionsPage.HOME)
            else:
                UI.display_error(0x0000001)
                input()
                Options.show(current_puzzle, puzzles, option_page)

        # General Options
        elif option_page == OptionsPage.GENERAL_OPTIONS:
            if input_value == "1":
                Options.show(current_puzzle, puzzles, OptionsPage.HOME)
            elif input_value == "2":
                Options.show(current_puzzle, puzzles, OptionsPage.DEFAULT_PUZZLE_SELECT)
            elif input_value == "0":
                Options.show(current_puzzle, puzzles, OptionsPage.HOME)
            else:
                UI.display_error(0x0000001)
                input()
                Options.show(current_puzzle, puzzles, option_page)

        # Default Puzzle Select
        elif option_page == OptionsPage.DEFAULT_PUZZLE_SELECT:
            try:
                if int(input_value) <= len(puzzles):
                    puzzles.default = puzzles[int(input_value) - 1]
                    Options.show(current_puzzle, puzzles, OptionsPage.HOME)
                else:
                    UI.display_error(0x000003)
                    input()
                    Options.show(current_puzzle, puzzles, option_page)
            except ValueError:
                UI.display_error(0x000002)
                input()
                Options.show(current_puzzle, puzzles, option_page)
