#!/usr/bin/env python3
"""Simple command-line Russian roulette game."""

from __future__ import annotations

import random

CHAMBERS = 6


def ask_to_play() -> bool:
    """Ask the player whether they want to continue."""
    while True:
        choice = input("Pull the trigger? (y/n): ").strip().lower()
        if choice in {"y", "yes"}:
            return True
        if choice in {"n", "no"}:
            return False
        print("Please answer with 'y' or 'n'.")


def spin_cylinder() -> int:
    """Return the random chamber that contains the bullet."""
    return random.randint(1, CHAMBERS)


def play_round(round_number: int) -> bool:
    """Play one round; return True if the player survives."""
    bullet_chamber = spin_cylinder()
    print(f"\nRound {round_number}: The cylinder spins...")

    for chamber in range(1, CHAMBERS + 1):
        if not ask_to_play():
            print("You chose to walk away. Smart move.")
            return False

        print("*click*" if chamber != bullet_chamber else "*BANG*")

        if chamber == bullet_chamber:
            print("Game over.")
            return False

    print("You survived this round!")
    return True


def main() -> None:
    print("=== Russian Roulette ===")
    print(f"One bullet, {CHAMBERS} chambers.")

    round_number = 1
    while True:
        survived = play_round(round_number)
        if not survived:
            break

        again = input("\nPlay another round? (y/n): ").strip().lower()
        if again not in {"y", "yes"}:
            print("Thanks for playing.")
            break
        round_number += 1


if __name__ == "__main__":
    main()
