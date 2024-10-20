from typing import List
from pydantic import BaseModel


class LearningRes(BaseModel):
    id: int
    name: str
    type: str  # Type of resource (e.g., book, online course)
    shortDescription: str
    url: str


learning_resources: List[LearningRes] = [
    LearningRes(
        id=1,
        name="Codecademy",
        type="Online Platform",
        shortDescription="Offers free interactive lessons in various programming languages like Python, JavaScript, "
                         "and HTML/CSS.",
        url="https://www.codecademy.com/"
    ),
    LearningRes(
        id=2,
        name="freeCodeCamp",
        type="Online Platform",
        shortDescription="Provides a full curriculum covering web development, data structures, algorithms, and more.",
        url="https://www.freecodecamp.org/"
    ),
    LearningRes(
        id=3,
        name="Khan Academy",
        type="Online Platform",
        shortDescription="Offers free courses in programming, including JavaScript, SQL, and HTML/CSS.",
        url="https://www.khanacademy.org/computing/computer-programming"
    ),
    LearningRes(
        id=4,
        name="Sololearn",
        type="Online Platform",
        shortDescription="Has free courses in different programming languages like Python, JavaScript, C++, and others.",
        url="https://www.sololearn.com/"
    ),
    LearningRes(
        id=5,
        name="LeetCode",
        type="Interactive Coding Website",
        shortDescription="Offers coding challenges to improve your problem-solving skills, with a focus on algorithms "
                         "and data structures.",
        url="https://leetcode.com/"
    ),
    LearningRes(
        id=6,
        name="HackerRank",
        type="Interactive Coding Website",
        shortDescription="Provides coding challenges in various domains, including algorithms, data structures, "
                         "and artificial intelligence.",
        url="https://www.hackerrank.com/"
    ),
    LearningRes(
        id=7,
        name="Codewars",
        type="Interactive Coding Website",
        shortDescription="Allows you to practice coding through challenges that get progressively harder, helping you "
                         "learn by doing.",
        url="https://www.codewars.com/"
    ),
    LearningRes(
        id=8,
        name="Traversy Media",
        type="YouTube Channel",
        shortDescription="High-quality tutorials on web development and programming.",
        url="https://www.youtube.com/c/TraversyMedia"
    ),
    LearningRes(
        id=9,
        name="Programming with Mosh",
        type="YouTube Channel",
        shortDescription="Covers various programming languages and software development topics.",
        url="https://www.youtube.com/c/programmingwithmosh"
    ),
    LearningRes(
        id=10,
        name="The Net Ninja",
        type="YouTube Channel",
        shortDescription="Provides tutorials on web development, including JavaScript, React, and Node.js.",
        url="https://www.youtube.com/c/TheNetNinja"
    ),
    LearningRes(
        id=11,
        name="CS50 by Harvard University",
        type="Online Course",
        shortDescription="A free introduction to computer science course, also available on YouTube.",
        url="https://cs50.harvard.edu/x/2023/"
    ),
    LearningRes(
        id=12,
        name="Eloquent JavaScript",
        type="Book",
        shortDescription="A free book that covers JavaScript programming and web development fundamentals.",
        url="https://eloquentjavascript.net/"
    ),
    LearningRes(
        id=13,
        name="Automate the Boring Stuff with Python",
        type="Book",
        shortDescription="An excellent resource for learning Python, especially for practical tasks like scripting "
                         "and automation.",
        url="https://automatetheboringstuff.com/"
    ),
    LearningRes(
        id=14,
        name="Learn Python the Hard Way",
        type="Book",
        shortDescription="A great resource for beginners to learn Python step by step.",
        url="https://learnpythonthehardway.org/python3/"
    ),
    LearningRes(
        id=15,
        name="The Odin Project",
        type="Project-Based Course",
        shortDescription="A free and comprehensive web development course that guides you through building real "
                         "projects.",
        url="https://www.theodinproject.com/"
    ),
    LearningRes(
        id=16,
        name="Stack Overflow",
        type="Forum",
        shortDescription="Great for asking questions and getting help from experienced programmers.",
        url="https://stackoverflow.com/"
    ),
    LearningRes(
        id=17,
        name="Reddit - Learn Programming",
        type="Forum",
        shortDescription="The 'Learn Programming' subreddit is an excellent place for beginners to ask questions.",
        url="https://www.reddit.com/r/learnprogramming/"
    ),
    LearningRes(
        id=18,
        name="GitHub",
        type="Project Platform",
        shortDescription="Explore open-source projects, contribute to them, or start your own coding projects.",
        url="https://github.com/"
    ),
    LearningRes(
        id=19,
        name="edX",
        type="Open Online Course",
        shortDescription="Offers free courses from universities like MIT and Harvard, especially in computer science.",
        url="https://www.edx.org/"
    ),
    LearningRes(
        id=20,
        name="Coursera",
        type="Open Online Course",
        shortDescription="Provides free courses from universities and companies; while certificates are paid, "
                         "the course material is often free.",
        url="https://www.coursera.org/"
    ),
    LearningRes(
        id=21,
        name="Udacity",
        type="Open Online Course",
        shortDescription="Some courses are free, especially beginner-level ones in programming.",
        url="https://www.udacity.com/"
    )
]
