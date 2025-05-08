"""
handling "main" app views
"""

from django.shortcuts import render

programing_items = {
    "Python": "python",
    "Django": "django",
    "Tailwind CSS": "tailwindcss",
    "JavaScript": "javascript",
    "Svelte": "svelte",
    "Postgres": "postgresql",
    "Langage C": "c",
    "Bash Scripting": "bash",
}
tool_items = {
    "Linux": "linux",
    "Git": "git",
    "Docker": "docker",
    "Poetry": "poetry",
    "Figma": "figma",
}


def home(request):
    """
    rendering homepage
    uses home.html that extends base.html
    """
    return render(
        request,
        "home.html",
        {
            "programing_items": programing_items,
            "tool_items": tool_items,
        },
    )
