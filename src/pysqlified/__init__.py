"""
MIT License

Copyright (c) 2025 Alexeev Bronislav

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import requests
from rich import print

__version__ = "0.1.0"


def check_for_update():
	"""
	Check for update in pypi
	"""
	try:
		response = requests.get("https://pypi.org/pypi/pysqlified/json").json()

		latest_version = response["info"]["version"]

		latest_digits = [int(n) for n in latest_version.split(".")]
		current_digits = [int(n) for n in __version__.split(".")]

		if sum(latest_digits) > sum(current_digits):
			message = f"New version of library pysqlified available: {latest_version}"

			print(
				f"[red]{'#' * (len(message) + 4)}\n#[/red][bold yellow] {message} [/bold yellow][red]#\n{'#' * (len(message) + 4)}[/red]\n"
			)
		elif sum(latest_digits) < sum(current_digits):
			print(
				f"[yellow]You use [bold]UNSTABLE[/bold] branch of pysqlified. Stable version: {latest_version}, your version: {__version__}[/yellow]\n"
			)
	except requests.RequestException:
		print(
			f"[dim]Version updates information not available. Your version: {__version__}[/dim]"
		)


check_for_update()

