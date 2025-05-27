# Ulauncher Snippet Library

A simple Ulauncher extension that allows you to quickly access and paste text snippets from a customisable library.

## Features

- Store snippets in a JSON file at `~/.config/snippets/snippets.json`
- Access snippets by typing `s` followed by the snippet name
- Support for multi-line snippets
- Automatic clipboard copying

## Installation

1. Make sure you have [Ulauncher](https://ulauncher.io/) installed
2. Clone this repository to your Ulauncher extensions directory:
   ```
   git clone https://github.com/markgandolfo/ulauncher-snippets ~/.local/share/ulauncher/extensions/ulauncher-snippets
   ```
   or use the extension manager in Ulauncher to install it directly from the Ulauncher extension store.

3. Create the snippets directory if it doesn't exist:
   ```
   mkdir -p ~/.config/snippets
   ```

4. Restart Ulauncher to load the extension

## Usage

1. Type `s` in Ulauncher to see all available snippets
2. Type `s` followed by a snippet name to filter the list
3. Press Enter to copy the selected snippet to your clipboard
4. Paste the snippet anywhere you need it

## Customising Snippets

Edit the `~/.config/snippets/snippets.json` file to add, modify, or remove snippets. The file format is:

```json
[
  {
    "name": "hello",
    "description": "Simple greeting",
    "snippettext": "Hello, World!"
  },
  {
    "name": "email-sig",
    "description": "Email signature",
    "snippettext": "Best regards,\\nYour Name\\nEmail: your.email@example.com\\nPhone: (123) 456-7890"
  }
]
```

Notes:
- Use `\\n` to insert newlines in your snippets
- The extension will create a default snippets file with a sample entry if none exists

## Configuration

In Ulauncher's extension settings, you can configure:
- The keyword to trigger the snippet search (default: `s`)
- The path to your snippets file (default: `~/.config/snippets/snippets.json`)

## Licence

[MIT Licence](LICENSE)
