from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star


class EchoPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @filter.command("echo")
    async def echo(self, event: AstrMessageEvent, message: str = ""):
        """原样返回用户文字消息"""

        if message:
            yield event.plain_result(message)
        else:
            yield event.plain_result("PONG")
