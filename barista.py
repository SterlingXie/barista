from typing import List, Tuple


def solve(N: int, K: int, times: List[int]) -> Tuple[int, int]:
    """
    Given the number of baristas, your position in the queue and the time it
    takes each barista to prepare a drink, returns which barista will make your
    drink and when it will be ready.

    Parameters
    ----------
    N : int
        The number of baristas.
    K : int
        Your position in the queue.
    times : List[int]
        A list of the time it takes each barista to prepare a drink.

    Returns
    -------
    Tuple[int, int]
        Two integers, the number of the barista who will prepare your drink and
        the time that it will be ready
    """

    def finished_drinks(t: int) -> int:
        """
        Helper function that given a moment `t` returns the total number of
        drinks all of the baristas have finished by time `t`.

        Parameters
        ----------
        t : int
            Time

        Returns
        -------
        int
            The total number of drinks finished by all the baristas
        """

        # TODO Fill out the helper function

        return 0


    # TODO: Your code here.

    return 0, 0


def read_input():
    N, K = [int(i) for i in input().split()]
    times = [int(i) for i in input().split()]
    return N, K, times


def main():
    N, K, times = read_input()
    barista, T = solve(N, K, times)
    print(barista, T)


if __name__ == '__main__':
    main()
