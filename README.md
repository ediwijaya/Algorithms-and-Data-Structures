# Algorithms-and-Data-Structures

This is my public repository for MicroMaster of Algorithms and Data Structures from edX.
It will show my progress for each courses which I took in my sparetime.

I allow public to use my work as inspiration for the education as long as it does not violate the purpose of education: "Developing your knowledge and skill."
So, please don't plagiarize it and make sure when use my work as the inspiration, code the solution in your own way.

## DSA practice setup

Open this folder in VS Code or use
`Algorithms-and-Data-Structures.code-workspace`. Project settings in
`.vscode/settings.json` disable automatic inline ghost text, Copilot completions
and next edit suggestions, and Gemini automatic suggestions and edit predictions.
Normal IntelliSense, syntax help, and diagnostics remain available.

AI assistance follows `AGENTS.md`: one small hint at a time by default, with more
direct help when I am stuck, explicitly request a solution, or want another
perspective on a solution I have completed. Exercise code should only be edited
when I explicitly request implementation changes.

These are project settings and agent guidance, not a hard block on every AI
extension or manually invoked generation command.

## Fresh practice branch

`practice/refresh` is a new practice round. The existing starter subfolders and
their Python contents are preserved. Previous implementations directly under
the week folders have been removed from this branch's tracked files.

Start with [PROGRESS.md](PROGRESS.md), which links to all 63 course exercises.
For example, the reachability starter is at
`graph_algorithms/week1_decomposition1_starters/1_reachability/reachability.py`.
Keep your new attempts in those starter files. PDFs and test fixtures retain
their original locations. Week numbers follow the course; weeks with only
lecture materials are not assigned invented exercises.

Mark an exercise as Attempting when you begin, Solved after checking your work,
or Revisit when it needs another pass. Commit progress as you complete exercises.
AI help remains hints first under `AGENTS.md`.

The `main` branch retains the previous layout and implementations. This branch
also has local backup copies of the 60 removed implementations under
`.practice-archive/`; that folder is ignored by Git and hidden in VS Code.
Ask explicitly before using either archive to compare solutions.

The development interpreter is Python 3.15, selected by `.python-version`.
Use `.venv/bin/python` in VS Code. Project metadata retains Python 3.14 as the
compatibility minimum.
