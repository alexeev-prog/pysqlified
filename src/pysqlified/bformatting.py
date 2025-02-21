import shutil
from datetime import datetime
from typing import Optional
from rich.console import Console
from rich.syntax import Syntax

console = Console()


def _get_color_by_message_type(message_type: str) -> str:
	match message_type:
		case 'INFO':
			return 'green'
		case 'WARN':
			return 'yellow'
		case 'ERR':
			return 'red'
		case 'WARNING':
			return 'yellow'
		case 'DEBUG':
			return 'magenta'
		case _:
			return 'blue'


def log(label: str,
	status: Optional[str] = "success",
	comment: Optional[str] = None,
) -> None:
	"""
	Prints a test result.
	
	:param      percent:      The percent
	:type       percent:      str
	:param      label:        The label
	:type       label:        str
	:param      status:       The status
	:type       status:       str
	:param      output:       The output
	:type       output:       Any
	:param      message_type:  The message_type
	:type       message_type:  str
	:param      comment:      The comment
	:type       comment:      str
	"""
	date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
	width = shutil.get_terminal_size().columns - 5 - len(date)

	if comment is not None:
		label = f"[dim]{label}[/dim] [white]{comment}[/white]"
		width += 26

	if status == "success":
		console.print(
			f"[black bold on green]PASS[/black bold on green] {label.ljust(width)}[dim]{date}[/dim]"
		)
	elif status == "error":
		console.print(
			f"[black bold on red]ERR [/black bold on red] {label.ljust(width)}[dim]{date}[/dim]"
		)
	elif status == "warning":
		console.print(
			f"[black bold on yellow]WARN[/black bold on yellow] {label.ljust(width)}[dim]{date}[/dim]"
		)
	elif status == "note":
		console.print(
			f"[black bold on blue]NOTE[/black bold on blue] {label.ljust(width)}[dim]{date}[/dim]"
		)



def print_sql_query(sql_query: str, comment: Optional[str] = 'SQL Query', theme: str = 'monokai') -> None:
	sql_query = f'-- {comment}\n{sql_query.strip()}'

	console.print(Syntax(sql_query, 'sql', theme=theme, line_numbers=True))
