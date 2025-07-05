# Example main.py for testing RPS player
from RPS import player
from RPS_game import play, quincy, abbey, kris, mrugesh

if __name__ == "__main__":
    print("Testing against quincy:")
    play(player, quincy, 1000, verbose=False)
    print("Testing against abbey:")
    play(player, abbey, 1000, verbose=False)
    print("Testing against kris:")
    play(player, kris, 1000, verbose=False)
    print("Testing against mrugesh:")
    play(player, mrugesh, 1000, verbose=False)

    # Uncomment the next lines if you want to run the unit tests (if available)
    # import test_module
    # test_module.test_player()
