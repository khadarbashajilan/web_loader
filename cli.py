from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

console = Console()


def show_banner():
    console.print(
        Panel.fit(
            "[bold cyan]Web Research Assistant[/bold cyan]",
            border_style="cyan",
        )
    )


def show_summary(summary: str):
    console.print(
        Panel(
            Markdown(summary),
            title="[bold green]Summary[/bold green]",
            border_style="green",
        )
    )


def show_ai_message(content: str):
    console.print(
        Panel(
            Markdown(content),
            title="[bold cyan]AI[/bold cyan]",
            border_style="cyan",
        )
    )


def show_info(msg: str):
    console.print(
        Panel(
            msg,
            title="Info",
            border_style="blue",
        )
    )


def show_error(msg: str):
    console.print(f"[red]{msg}[/red]")
