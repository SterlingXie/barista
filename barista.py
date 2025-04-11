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
        num_drinks = 0
        for time in times:
            num_drinks += t // time + 1
        return num_drinks

    # TODO: Your code here.
    min_pos, max_pos = 0, max(times) * K
    while min_pos < max_pos:
        mid = (min_pos + max_pos) // 2
        if finished_drinks(mid) >= K:
            max_pos = mid
        else:
            min_pos = mid + 1
    t_barista_ready = min_pos

    simultaneous_queue = K - finished_drinks(t_barista_ready - 1)

    for i in range(N):
        if t_barista_ready % times[i] == 0:
            simultaneous_queue -= 1
            if simultaneous_queue == 0:
                return i + 1, t_barista_ready + times[i]

    return -1, -1


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
