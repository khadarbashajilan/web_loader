from chatbot import handle_command
from cli import console


console.print(
    """
[bold cyan]
Web Research Assistant
[/bold cyan]

Type /help
"""
)

while True:

    try:

        user_input = console.input(
            "\n[bold green]> [/bold green]"
        ).strip()

        if not user_input:
            continue

        if not handle_command(user_input):
            break

    except KeyboardInterrupt:
        break

console.print(
    "\n[green]Goodbye![/green]"
)
