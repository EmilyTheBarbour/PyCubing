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
    def display_start_up(version, puzzles, current_puzzle):
        UI.clear()
        print("PyCubing version", version)
        print(len(puzzles), "puzzle loaded.")
        for i, e in enumerate(puzzles):
            print("-----------------------------------------------------------------")
            print("Puzzle #{}".format(i + 1))
            print("Name:", e.name)
            print("Description:", e.description)
            print("Shuffle count:", len(e.shuffles))
            print("Number of solves:", len(e.overall_solves))
            print("Overall best:", e.overall_best)
            print("Ao3: ", e.overall_average_of_three)
            print("Bo5: ", e.overall_best_of_five)
            print("Bo12:", e.overall_best_of_twelve)

        print("-----------------------------------------------------------------")
        print("default puzzle", current_puzzle.name, "loaded.", '\n')
        print("Press enter to continue.")

    # display to the user that a new personal best was achieved that is x seconds faster
    @staticmethod
    def display_solve_results(solve, solve_results):
        # create a list of just the solve results tags
        solve_results_tags = []
        for e in solve_results:
            solve_results_tags.append(e[0])

        print('\n', solve[Solve.TIME], '\n')

        if SolveResults.NEW_SESSION_BEST in solve_results_tags:
            print("new session best! You beat your previous record by",
                  round(solve_results[solve_results_tags.index(SolveResults.NEW_SESSION_BEST)][1]
                        - solve[Solve.TIME], 2), "seconds!")

        if SolveResults.NEW_OVERALL_BEST in solve_results_tags:
            print("new overall best! You beat your previous record by",
                  round(solve_results[solve_results_tags.index(SolveResults.NEW_OVERALL_BEST)][1]
                        - solve[Solve.TIME], 2), "seconds!")

        print('\n', "Press enter to continue.")

    # display the main page, detailing puzzle, statistics, and solve information
    @staticmethod
    def display_home(current_puzzle, current_solve):
        UI.clear()

        print("Session of", time.strftime("%B %d, %Y", time.localtime()))
        print("-----------------------------------------------------------------")
        print("Puzzle:", current_puzzle.name)
        print("Solves:", current_puzzle.session_solves)
        print("Best:  ", current_puzzle.session_best)
        if current_puzzle.session_solves >= 3: print("Ao3:   ", current_puzzle.session_average_of_three)
        if current_puzzle.session_solves >= 5: print("Bo5:   ", current_puzzle.session_best_of_five)
        if current_puzzle.session_solves >= 12: print("Bo12:  ", current_puzzle.session_best_of_twelve)
        if current_puzzle.session_solves >= 100: print("Bo100: ", current_puzzle.session_best_of_hundred)
        print("-----------------------------------------------------------------")
        print(current_solve[Solve.SHUFFLE], '\n')
        print("Enter to start. 1 for options. 0 for exit.")

    @staticmethod
    def display_options(options_page, current_puzzle, puzzles):
        if options_page == OptionsPage.HOME:
            UI.clear()
            print("1. Puzzle Select")
            print("2. Puzzle Options ({})".format(current_puzzle.name))
            print("3. General Options")
            print("4. Exit")
            print("-----------------------------------------------------------------")
            print("Enter number for page.")

        if options_page == OptionsPage.PUZZLE_SELECT:
            UI.clear()
            for i, e in enumerate(puzzles):
                print("{}. {}".format(i + 1, e.name))
            print("-----------------------------------------------------------------")
            print("Enter number to select cube. enter nothing to return to the last page")

        if options_page == OptionsPage.PUZZLE_OPTIONS:
            UI.clear()
            print("1. Clear Solves and Statistics")
            print("-----------------------------------------------------------------")
            print("Enter number for option.")

        if options_page == OptionsPage.GENERAL_OPTIONS:
            UI.clear()
            print("home")

    @staticmethod
    def display_error(error_code):
        if error_code == 0x000001:
            print("Error: Unknown input, please try again.")
        if error_code == 0x000002:
            print("Error: Expected a number, but you entered something else. please try again.")


# class for readability when designating which option page to navigate to
class OptionsPage:
    HOME = 0
    PUZZLE_SELECT = 1
    PUZZLE_OPTIONS = 2
    GENERAL_OPTIONS = 3
