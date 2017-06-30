import time
from puzzle import Solve


class UI:

    # place holder clear functionality
    # TODO: find better clear implementation
    @staticmethod
    def clear():
        print('\n' * 50)
        # os.system('cls' if os.name == 'nt' else 'clear')

    # display the main page, detailing puzzle, statistics, and solve information
    @staticmethod
    def display_home(current_puzzle, current_solve):
        UI.clear()

        print("Session of", time.strftime("%B %d, %Y", time.localtime()))
        print(len(current_puzzle.shuffles), "Shuffles loaded.")
        print("-----------------------------------------------------------------")
        print("Puzzle:", current_puzzle.name)
        print("Solves:", current_puzzle.session_solves)
        print("Best:  ", current_puzzle.overall_best)
        if current_puzzle.session_solves >= 3: print("Ao3:   ", current_puzzle.session_average_of_three)
        if current_puzzle.session_solves >= 5: print("Bo5:   ", current_puzzle.session_best_of_five)
        if current_puzzle.session_solves >= 12: print("Bo12:  ", current_puzzle.session_best_of_twelve)
        if current_puzzle.session_solves >= 100: print("Bo100: ", current_puzzle.session_best_of_hundred)
        print("-----------------------------------------------------------------")
        print(current_solve[Solve.SHUFFLE], '\n')
        print("Enter to start. 1 for options. 0 for exit.")

    @staticmethod
    def display_options(options_page):
        print("To be implemented.")


# class for readability when designating which option page to navigate to
class OptionsPage:
    HOME = 0
