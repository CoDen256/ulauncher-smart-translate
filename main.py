from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.search.apps.AppDb import AppDb
import logging
from multitran import Mutltitran

from ulauncher.utils.desktop.reader import find_apps_cached

logger = logging.getLogger(__name__)


mt = Mutltitran()

class DemoExtension(Extension):

    def __init__(self):
        super(DemoExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []
        query = event.get_argument()

        keyword = event.get_keyword()
        # Find the keyword id using the keyword (since the keyword can be changed by users)
        keyword_id = None
        for kw_id, kw in list(extension.preferences.items()):
            if kw == keyword:
                keyword_id = kw_id

        if keyword_id == "multitran_de_ru":
            response = mt.get_translations("DE", "RU", query.strip())
            for t in response['translations']:
                translation = t['translation']
            items.append(
                ExtensionResultItem(
                    icon='images/icon.png',
                    name=translation,
                    on_enter=response['url']))
        return RenderResultListAction(items)

if __name__ == '__main__':
    logger.info("HELO ITS ME MARIO")
    DemoExtension().run()