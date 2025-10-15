#!/usr/bin/env python3
"""
Simple Movie Chatbot - Assignment 3 Part 2 (Simple Solution)

"""

import random
from typing import List, Tuple
import sys

# import movie_db from movies.py
try:
    from movies import movie_db
except Exception as e:
    print("ERROR: Unable to import movie_db from movies.py:", e)
    sys.exit(1)

def format_movie(m: Tuple[str, str, int, List[str]]) -> str:
    title, director, year, actors = m
    actors_str = ", ".join(actors) if actors else "N/A"
    return f"{title} ({year}) | Director: {director} | Actors: {actors_str}"

# --- Search functions ---

def search_by_title(substring: str):
    s = substring.lower()
    return [m for m in movie_db if s in m[0].lower()]

def search_by_director(name: str):
    s = name.lower()
    return [m for m in movie_db if s in m[1].lower()]

def search_by_year(year: int):
    return [m for m in movie_db if m[2] == year]

def search_by_actor(name: str):
    s = name.lower()
    return [m for m in movie_db if any(s in actor.lower() for actor in m[3])]

def search_by_exact_title(title: str):
    t = title.lower().strip()
    return [m for m in movie_db if m[0].lower().strip() == t]

# New action function: random recommendation
def get_random_movie():
    return random.choice(movie_db)

# Extra utility: count movies
def count_movies():
    return len(movie_db)

# --- Chatbot CLI ---
def print_help():
    print("\nAvailable commands:")
    print("  title     - search by (part of) movie title")
    print("  exact     - search by exact movie title")
    print("  director  - search by director name")
    print("  year      - search by release year")
    print("  actor     - search by actor/actress name")
    print("  random    - get a random movie recommendation (new action)")
    print("  count     - show how many movies are in the database")
    print("  help      - show this help text")
    print("  quit      - exit the chatbot\n")

def chatbot_loop():
    print("🎬 Simple Movie Chatbot (Simple Solution)")
    print("Uses the movie_db from movies.py\n")
    print_help()

    pa_list = ["title", "exact", "director", "year", "actor", "random", "count", "help", "quit"]

    while True:
        cmd = input("Enter command (type 'help' for options): ").strip().lower()
        if not cmd:
            continue

        if cmd == "quit":
            print("Goodbye! 👋")
            break
        elif cmd == "help":
            print_help()
            continue
        elif cmd == "count":
            print(f"There are {count_movies()} movies in the database.")
            continue
        elif cmd == "random":
            m = get_random_movie()
            print("\nRandom recommendation:\n" + format_movie(m) + "\n")
            continue
        elif cmd == "title":
            q = input("Enter part of the movie title to search for: ").strip()
            results = search_by_title(q)
        elif cmd == "exact":
            q = input("Enter the exact movie title to search for: ").strip()
            results = search_by_exact_title(q)
        elif cmd == "director":
            q = input("Enter director name (or part of it): ").strip()
            results = search_by_director(q)
        elif cmd == "year":
            q = input("Enter release year (e.g., 1994): ").strip()
            try:
                y = int(q)
                results = search_by_year(y)
            except ValueError:
                print("Please enter a valid year (integer).")
                continue
        elif cmd == "actor":
            q = input("Enter actor/actress name (or part of it): ").strip()
            results = search_by_actor(q)
        else:
            print("Unknown command. Type 'help' for available options.")
            continue

        # Display results
        if results:
            print(f"\nFound {len(results)} result(s):")
            for m in results:
                print(" - " + format_movie(m))
            print()
        else:
            print("No results found.\n")

if __name__ == '__main__':
    chatbot_loop()
