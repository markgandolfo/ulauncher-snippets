import json
import os
from pathlib import Path
from typing import Dict, List

from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction


class SnippetLibraryExtension(Extension):
    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())

    def get_snippets(self) -> List[Dict[str, str]]:
        snippets_path = os.path.expanduser(str(self.preferences.get('snippets_path')))
        path = Path(snippets_path)

        if not path.exists():
            # Create the directory if it doesn't exist
            directory = path.parent
            if not directory.exists():
                directory.mkdir(parents=True, exist_ok=True)

            # Create a simple default snippets file if it doesn't exist
            with open(path, 'w') as f:
                json.dump([
                    {
                        "name": "hello",
                        "description": "A simple greeting",
                        "snippettext": "Hello, world!"
                    }
                ], f, indent=2)

        try:
            with open(path, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            # Return an error snippet if there's a problem with the file
            return [{
                "name": "error",
                "description": f"Error loading snippets: {str(e)}",
                "snippettext": f"Error loading snippets: {str(e)}"
            }]


class KeywordQueryEventListener(EventListener):
    def on_event(self, event: KeywordQueryEvent, extension: Extension) -> RenderResultListAction:
        query = event.get_argument() or ""
        snippets = extension.get_snippets()

        items = []

        # If query is empty, show all snippets
        if not query:
            for snippet in snippets:
                items.append(ExtensionResultItem(
                    icon='images/icon.png',
                    name=snippet['name'],
                    description=snippet['description'],
                    on_enter=CopyToClipboardAction(snippet['snippettext'].replace('\\n', '\n'))
                ))
        else:
            # Filter snippets by name
            for snippet in snippets:
                if query.lower() in snippet['name'].lower():
                    items.append(ExtensionResultItem(
                        icon='images/icon.png',
                        name=snippet['name'],
                        description=snippet['description'],
                        on_enter=CopyToClipboardAction(snippet['snippettext'].replace('\\n', '\n'))
                    ))

        return RenderResultListAction(items)


class ItemEnterEventListener(EventListener):
    def on_event(self, event: ItemEnterEvent, extension: Extension) -> None:
        # This method is required by the API but we don't need to do anything here
        # as we're using CopyToClipboardAction which handles everything for us
        return None


if __name__ == '__main__':
    SnippetLibraryExtension().run()
