import time
from puzzle import Solve, SolveResults


class UI:
    # place holder clear functionality
    # TODO: find better clear implementation
    @staticmethod
    def clear():
        print('\n' * 50)
        # os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def center_string(string, width, siding=0):
        side_len = (width - len(string)) // 2
        if siding == 0:
            return ''.join((' ' * side_len, string, ' ' * side_len))
        else:
            temp = ''.join(("||", ' ' * (side_len - 2), string, ' ' * (side_len - 2), "||"))
            if len(temp) == width:
                return temp
            else:
                temp = temp[:len(temp) - 2]
                temp = ''.join((temp, " ||"))
                return temp

    @staticmethod
    def display_start_up(version, puzzles, current_puzzle):
        UI.clear()
        print("PyCubing version", version)
        print(len(puzzles), "puzzle loaded.")
        for i, e in enumerate(puzzles):
            print("--------------------------------------------------------")
            print("Puzzle #{}".format(i + 1))
            print("Name:", e.name)
            print("Description:", e.description)
            print("Shuffle count:", len(e.shuffles))
            print("Number of solves:", len(e.overall_solves))
            print("Overall best:", e.overall_best)
            print("Ao3: ", e.overall_average_of_three)
            print("Bo5: ", e.overall_best_of_five)
            print("Bo12:", e.overall_best_of_twelve)

        print("--------------------------------------------------------")
        print("default puzzle", current_puzzle.name, "loaded.", '\n')
        print("Press enter to continue.")

    # display to the user that a new personal best was achieved that is x seconds faster
    @staticmethod
    def display_solve_results(solve, solve_results):
        UI.clear()
        # create a list of just the solve results tags
        solve_results_tags = []
        for e in solve_results:
            solve_results_tags.append(e[0])

        print('\n', solve[Solve.TIME], '\n')

        if SolveResults.NEW_SESSION_BEST in solve_results_tags:
            if solve_results[solve_results_tags.index(SolveResults.NEW_SESSION_BEST)][1] != 0:
                print("New session best! You beat your previous record by",
                      round(solve_results[solve_results_tags.index(SolveResults.NEW_SESSION_BEST)][1]
                            , 2), "seconds!")
            else:
                print("New session best!")

        if SolveResults.NEW_OVERALL_BEST in solve_results_tags:
            if solve_results[solve_results_tags.index(SolveResults.NEW_OVERALL_BEST)][1] != 0:
                print("New overall best! You beat your previous record by",
                      round(solve_results[solve_results_tags.index(SolveResults.NEW_OVERALL_BEST)][1]
                            , 2), "seconds!")
            else:
                print("New overall best!")
        print()

        input("Press enter to continue.")

    # display the main page, detailing puzzle, statistics, and solve information
    @staticmethod
    def display_home(current_puzzle, current_solve):
        UI.clear()

        print("||------------------------------------------------------------||")
        print(UI.center_string("Session of {}".format(time.strftime("%B %d, %Y", time.localtime())), 64, 1))
        print("||-----------------------------||-----------------------------||")
        print("||---------- Session ----------||---------- Overall ----------||")
        print("||-----------------------------||-----------------------------||")

        print_list = []
        print_list.append("|| Puzzle: {}".format(current_puzzle.name))
        print_list.append("|| Solves: {}".format(current_puzzle.session_solves))
        if current_puzzle.session_best == 9999:
            print_list.append("|| Best:  N/A")
        else:
            print_list.append("|| Best:  {}".format(current_puzzle.session_best))

        if current_puzzle.session_solves >= 3:
            print_list.append("|| Ao3:   {}".format(current_puzzle.session_average_of_three))
        else:
            print_list.append("|| Ao3:   N/A")
        if current_puzzle.session_solves >= 5:
            print_list.append("|| Bo5:   {}".format(current_puzzle.session_best_of_five))
        else:
            print_list.append("|| Bo5:   N/A")
        if current_puzzle.session_solves >= 12:
            print_list.append("|| Bo12:  {}".format(current_puzzle.session_best_of_twelve))
        else:
            print_list.append("|| Bo12:  N/A")
        if current_puzzle.session_solves >= 100:
            print_list.append("|| Bo100: {}".format(current_puzzle.session_best_of_hundred))
        else:
            print_list.append("|| Bo100: N/A")

        i = 0
        for e in print_list:
            place_holder_string = ''.join((e, ' ' * (31 - len(e)), "||"))
            print_list[i] = place_holder_string
            i += 1

        print_list[1] = ' '.join((print_list[1], "Solves: {}".format(len(current_puzzle.overall_solves))))
        if current_puzzle.overall_best == 9999:
            print_list[2] = ' '.join((print_list[2], "Best:  N/A"))
        else:
            print_list[2] = ' '.join((print_list[2], "Best:  {}".format(current_puzzle.overall_best)))

        if len(current_puzzle.overall_solves) >= 3:
            print_list[3] = ' '.join((print_list[3], "Ao3:   {}".format(current_puzzle.overall_average_of_three)))
        else:
            print_list[3] = ' '.join((print_list[3], "Ao3:   N/A"))
        if len(current_puzzle.overall_solves) >= 5:
            print_list[4] = ' '.join((print_list[4], "Bo5:   {}".format(current_puzzle.overall_best_of_five)))
        else:
            print_list[4] = ' '.join((print_list[4], "Bo5:   N/A"))
        if len(current_puzzle.overall_solves) >= 12:
            print_list[5] = ' '.join((print_list[5], "Bo12:  {}".format(current_puzzle.overall_best_of_twelve)))
        else:
            print_list[5] = ' '.join((print_list[5], "Bo12:  N/A"))
        if len(current_puzzle.overall_solves) >= 100:
            print_list[6] = ' '.join((print_list[6], "Bo100: {}".format(current_puzzle.overall_best_of_hundred)))
        else:
            print_list[6] = ' '.join((print_list[6], "Bo100: N/A"))

        for e in print_list:
            place_holder_string = ''.join((e, ' ' * (29 - (len(e) - 33)), "||"))
            print(place_holder_string)

        print("||-----------------------------||-----------------------------||")
        print(UI.center_string(current_solve[Solve.SHUFFLE], 64, 1))
        print("||-----------------------------||-----------------------------||", '\n')
        print("Enter to start. 1 for options. 0 for exit.")

    @staticmethod
    def display_options(options_page, current_puzzle, puzzles):
        if options_page == OptionsPage.HOME:
            UI.clear()
            print("1. Puzzle Select")
            print("2. Puzzle Options ({})".format(current_puzzle.name))
            print("3. General Options")
            print("0. Exit")
            print("--------------------------------------------------------")
            print("Enter number for page.")

        if options_page == OptionsPage.PUZZLE_SELECT or options_page == OptionsPage.DEFAULT_PUZZLE_SELECT:
            UI.clear()
            for i, e in enumerate(puzzles):
                print("{}. {}".format(i + 1, e.name))
            print("--------------------------------------------------------")
            print("Enter number to select cube")

        if options_page == OptionsPage.PUZZLE_OPTIONS:
            UI.clear()
            print("1. Clear Solves and Statistics")
            print("2. Rebuild shuffle database from file")
            print("0. Return")
            print("--------------------------------------------------------")
            print("Enter number for option.")

        if options_page == OptionsPage.GENERAL_OPTIONS:
            UI.clear()
            print("1. Statistics...")
            print("2. Set default puzzle ({})".format(puzzles.default.name))
            print("0. Return")
            print("--------------------------------------------------------")
            print("Enter number for option.")

    @staticmethod
    def display_error(error_code):
        if error_code == 0x000001:
            print("Error: Unknown input, please try again.")
        if error_code == 0x000002:
            print("Error: Expected a number, but you entered something else. please try again.")
        if error_code == 0x000003:
            print("Error: Number you input is out of range. please try again.")


# class for readability when designating which option page to navigate to
class OptionsPage:
    HOME = 0
    PUZZLE_SELECT = 1
    PUZZLE_OPTIONS = 2
    GENERAL_OPTIONS = 3
    DEFAULT_PUZZLE_SELECT = 4
